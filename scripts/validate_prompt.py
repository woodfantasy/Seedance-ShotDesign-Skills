#!/usr/bin/env python3
"""Mode-aware validator for Seedance 2.5 shot-design prompts.

The validator distinguishes documented platform limits from stability guidance.
It never enforces the legacy 15-second, 9/3/3/12-file, 1080p, or universal
prompt-length rules.

Examples:
    python3 scripts/validate_prompt.py --mode standard --duration 30 \
        --prompt-file prompt.txt
    python3 scripts/validate_prompt.py --mode extension --duration 20 \
        --source-duration 25 --prompt "参考@视频1，向后延长20秒……"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


MODE_ALIASES = {
    "standard": "standard",
    "generation": "standard",
    "all_reference": "standard",
    "first_last": "standard",
    "全能参考": "standard",
    "首尾帧": "standard",
    "ultra_long": "ultra_long",
    "ultra-long": "ultra_long",
    "超长视频": "ultra_long",
    "extension": "extension",
    "extend": "extension",
    "视频延长": "extension",
    "smart_edit": "smart_edit",
    "smart-edit": "smart_edit",
    "edit": "smart_edit",
    "智能编辑": "smart_edit",
    "advanced_edit": "advanced_edit",
    "advanced-edit": "advanced_edit",
    "高级编辑": "advanced_edit",
    "视频编辑": "advanced_edit",
    "viewpoint": "viewpoint",
    "空间视角修改": "viewpoint",
    "bgm": "bgm",
    "audio_edit": "bgm",
    "音轨编辑": "bgm",
    "creative_transfer": "creative_transfer",
    "creative-transfer": "creative_transfer",
    "迁移创意": "creative_transfer",
    "green_screen": "green_screen",
    "green-screen": "green_screen",
    "绿幕编辑": "green_screen",
    "rough_white_model": "rough_white_model",
    "rough-white-model": "rough_white_model",
    "粗颗粒白模": "rough_white_model",
    "fine_white_model": "fine_white_model",
    "fine-white-model": "fine_white_model",
    "细颗粒白模": "fine_white_model",
    "seamless_transition": "seamless_transition",
    "seamless-transition": "seamless_transition",
    "视频无缝转场": "seamless_transition",
    "storyboard": "storyboard",
    "multi_panel": "storyboard",
    "多宫格分镜": "storyboard",
}

GENERATION_MODES = {
    "standard", "ultra_long", "extension", "creative_transfer",
    "green_screen", "rough_white_model", "fine_white_model", "storyboard",
}
EDIT_MODES = {"smart_edit", "advanced_edit", "viewpoint", "bgm"}
STANDARD_WINDOW_MODES = {
    "standard", "creative_transfer", "green_screen", "rough_white_model",
    "fine_white_model", "seamless_transition", "storyboard",
}

ASSET_RE = re.compile(
    r"@(图片|视频|音频|image|video|audio)\s*(\d+)", re.IGNORECASE
)


def finding(level: str, code: str, message: str, **values):
    item = {"level": level, "code": code, "message": message}
    item.update(values)
    return item


def normalize_mode(mode: str | None) -> str:
    if not mode:
        return "standard"
    key = mode.strip().lower().replace(" ", "_")
    if key not in MODE_ALIASES:
        raise ValueError(
            f"Unsupported mode '{mode}'. Choose one of: "
            + ", ".join(sorted(set(MODE_ALIASES.values())))
        )
    return MODE_ALIASES[key]


def detect_language(text: str) -> str:
    """Return a useful language hint without forcing non-Chinese text to English."""
    if re.search(r"[\u3040-\u30ff]", text):
        return "ja"
    if re.search(r"[\uac00-\ud7af]", text):
        return "ko"
    if re.search(r"[\u0e00-\u0e7f]", text):
        return "th"
    if re.search(r"[\u0600-\u06ff]", text):
        return "ar"
    cjk = len(re.findall(r"[\u3400-\u9fff]", text))
    letters = len(re.findall(r"[^\W\d_]", text, re.UNICODE))
    if cjk and cjk / max(letters, 1) >= 0.25:
        return "zh"
    lower = f" {text.lower()} "
    lexical = {
        "es": [" el ", " la ", " una ", " vídeo ", " personaje "],
        "pt": [" uma ", " vídeo ", " personagem ", " câmera ", " não "],
        "id": [" yang ", " dengan ", " video ", " adegan "],
        "ms": [" yang ", " dengan ", " video ", " babak "],
        "vi": [" video ", " nhân vật ", " cảnh ", " không "],
    }
    scores = {lang: sum(token in lower for token in tokens) for lang, tokens in lexical.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] >= 2 else "en"


def _clock_to_seconds(minutes: str, seconds: str) -> float:
    return int(minutes) * 60 + float(seconds)


def parse_time_slices(text: str, fps: float = 24.0) -> list[dict]:
    """Parse seconds, mm:ss, and frame-range timestamps."""
    slices = []
    occupied = []

    clock_pattern = re.compile(
        r"(?<!\d)(\d{1,2}):(\d{2}(?:\.\d+)?)\s*[-–—~至]\s*"
        r"(\d{1,2}):(\d{2}(?:\.\d+)?)(?!\d)"
    )
    for match in clock_pattern.finditer(text):
        start = _clock_to_seconds(match.group(1), match.group(2))
        end = _clock_to_seconds(match.group(3), match.group(4))
        slices.append({"start": start, "end": end, "kind": "clock", "raw": match.group(0)})
        occupied.append(match.span())

    second_pattern = re.compile(
        r"(?<![:\d])(\d+(?:\.\d+)?)\s*[-–—~至]\s*"
        r"(\d+(?:\.\d+)?)\s*(?:秒|s(?:ec(?:onds?)?)?)(?![A-Za-z])",
        re.IGNORECASE,
    )
    for match in second_pattern.finditer(text):
        if any(match.start() >= a and match.end() <= b for a, b in occupied):
            continue
        slices.append({
            "start": float(match.group(1)), "end": float(match.group(2)),
            "kind": "seconds", "raw": match.group(0),
        })

    frame_pattern = re.compile(
        r"(?:第\s*)?(\d+)\s*[-–—~至]\s*(\d+)\s*帧"
    )
    if fps > 0:
        for match in frame_pattern.finditer(text):
            slices.append({
                "start": int(match.group(1)) / fps,
                "end": int(match.group(2)) / fps,
                "kind": "frames", "raw": match.group(0),
            })

    unique = {}
    for item in slices:
        key = (round(item["start"], 3), round(item["end"], 3))
        unique[key] = item
    return sorted(unique.values(), key=lambda item: (item["start"], item["end"]))


def _detect_declared_duration(text: str) -> float | None:
    head = text[:300]
    patterns = [
        r"(?:全片|目标|视频|新增|生成|added\s+)?(?:时长|duration|length)\s*[：:=]?\s*(\d+(?:\.\d+)?)\s*(秒|s|分钟|min(?:utes?)?)",
        r"^\s*(\d+(?:\.\d+)?)\s*(秒|s|分钟|min(?:utes?)?)(?=\s|[，,。:：\[【])",
    ]
    for pattern in patterns:
        match = re.search(pattern, head, re.IGNORECASE | re.MULTILINE)
        if match:
            value = float(match.group(1))
            return value * 60 if match.group(2).lower().startswith(("分", "min")) else value
    return None


def check_length(text: str, lang: str | None = None) -> list[dict]:
    """Report length as information; the 2.5 manual gives no prompt ceiling."""
    words = len(re.findall(r"\S+", text))
    return [finding(
        "info", "PROMPT_SIZE_REPORTED",
        f"Prompt size: {len(text)} characters / {words} whitespace-delimited words. "
        "Seedance 2.5's manual states no universal prompt-length ceiling.",
        characters=len(text), words=words,
    )]


def check_duration(mode: str, duration: float | None, source_duration: float | None = None) -> list[dict]:
    results = []
    if duration is None:
        level = "error" if mode in GENERATION_MODES or mode == "ultra_long" else "warning"
        return [finding(level, "DURATION_MISSING", "Declare the output or added duration for mode-aware validation.")]

    if mode in STANDARD_WINDOW_MODES and not 4 <= duration <= 30:
        results.append(finding(
            "error", "STANDARD_DURATION_OUT_OF_RANGE",
            f"{mode} duration is {duration:g}s; documented standard generation range is 4–30s.",
            value=duration, minimum=4, maximum=30,
        ))
    elif mode == "ultra_long" and not 30 <= duration <= 180:
        results.append(finding(
            "error", "ULTRA_LONG_DURATION_OUT_OF_RANGE",
            f"Ultra-long duration is {duration:g}s; documented range is 30–180s.",
            value=duration, minimum=30, maximum=180,
        ))
    elif mode == "extension":
        if not 4 <= duration <= 30:
            results.append(finding(
                "error", "EXTENSION_ADDED_DURATION_OUT_OF_RANGE",
                f"Added duration is {duration:g}s; each extension adds 4–30s.",
                value=duration, minimum=4, maximum=30,
            ))
        if source_duration is None:
            results.append(finding(
                "warning", "SOURCE_DURATION_MISSING",
                "Provide the source-video duration to verify the 30s source and 60s final limits.",
            ))
        else:
            if source_duration <= 0 or source_duration > 30:
                results.append(finding(
                    "error", "EXTENSION_SOURCE_DURATION_OUT_OF_RANGE",
                    f"Source duration is {source_duration:g}s; an extension source must be no longer than 30s.",
                ))
            if source_duration + duration > 60:
                results.append(finding(
                    "error", "EXTENSION_FINAL_DURATION_EXCEEDED",
                    f"Source {source_duration:g}s + added {duration:g}s = {source_duration + duration:g}s; final video must not exceed 60s.",
                ))
    elif mode in EDIT_MODES and source_duration is not None:
        if source_duration <= 0 or source_duration > 30.2:
            results.append(finding(
                "error", "EDIT_SOURCE_DURATION_OUT_OF_RANGE",
                f"Source duration is {source_duration:g}s; referenced video tolerance is about 1.8–30.2s.",
            ))
        elif source_duration > 20:
            results.append(finding(
                "warning", "EDIT_SOURCE_STABILITY_BAND",
                f"Source duration is {source_duration:g}s; editing sources of 20s or less are recommended for stability.",
            ))

    if not results:
        results.append(finding("pass", "DURATION_OK", f"Duration {duration:g}s is valid for {mode}."))
    return results


def check_resolution(resolution: str | None) -> list[dict]:
    if not resolution:
        return [finding("info", "RESOLUTION_NOT_SUPPLIED", "Resolution was not supplied to the validator.")]
    normalized = resolution.strip().lower().replace(" ", "")
    if normalized in {"480p", "720p"}:
        return [finding("pass", "RESOLUTION_OK", f"Documented output resolution selected: {normalized}.")]
    if normalized == "720p+":
        return [finding(
            "warning", "RESOLUTION_UI_LABEL",
            "720P+ appears as a UI label in the manual, not as a separately documented output parameter.",
        )]
    return [finding(
        "error", "RESOLUTION_UNDOCUMENTED",
        f"'{resolution}' is not a documented Seedance 2.5 output resolution in the supplied manual; use 480p or 720p, or verify the current UI.",
    )]


def _asset_inventory(text: str) -> dict[str, list[int]]:
    inventory = {"image": [], "video": [], "audio": []}
    type_map = {"图片": "image", "image": "image", "视频": "video", "video": "video", "音频": "audio", "audio": "audio"}
    for type_name, index in ASSET_RE.findall(text):
        inventory[type_map[type_name.lower()]].append(int(index))
    return {name: sorted(set(indices)) for name, indices in inventory.items()}


def check_asset_refs(
    text: str,
    image_count: int | None = None,
    video_durations: list[float] | None = None,
    audio_durations: list[float] | None = None,
) -> list[dict]:
    inventory = _asset_inventory(text)
    inferred = {name: len(indices) for name, indices in inventory.items()}
    counts = {
        "image": image_count if image_count is not None else inferred["image"],
        "video": len(video_durations) if video_durations is not None else inferred["video"],
        "audio": len(audio_durations) if audio_durations is not None else inferred["audio"],
    }
    limits = {"image": 30, "video": 10, "audio": 10}
    results = []
    labels = {"image": "Image", "video": "Video", "audio": "Audio"}
    for asset_type, limit in limits.items():
        if counts[asset_type] > limit:
            results.append(finding(
                "error", f"{asset_type.upper()}_COUNT_EXCEEDED",
                f"{labels[asset_type]} count is {counts[asset_type]}; documented limit is {limit}.",
            ))
        if inventory[asset_type] and max(inventory[asset_type]) > limit:
            results.append(finding(
                "error", f"{asset_type.upper()}_TOKEN_OUT_OF_RANGE",
                f"Highest {asset_type} token is {max(inventory[asset_type])}; documented maximum index is {limit}.",
            ))

    if video_durations is not None:
        for index, value in enumerate(video_durations, 1):
            if not 1.8 <= value <= 30.2:
                results.append(finding(
                    "error", "VIDEO_DURATION_OUT_OF_RANGE",
                    f"Video {index} duration is {value:g}s; accepted tolerance is about 1.8–30.2s.",
                ))
        if sum(video_durations) > 30.2:
            results.append(finding(
                "error", "VIDEO_TOTAL_DURATION_EXCEEDED",
                f"Aggregate referenced-video duration is {sum(video_durations):g}s; maximum tolerance is about 30.2s.",
            ))

    if audio_durations is not None:
        for index, value in enumerate(audio_durations, 1):
            if value <= 0 or value > 30:
                results.append(finding(
                    "error", "AUDIO_DURATION_OUT_OF_RANGE",
                    f"Audio {index} duration is {value:g}s; each audio must be no longer than 30s.",
                ))
        if sum(audio_durations) > 30:
            results.append(finding(
                "error", "AUDIO_TOTAL_DURATION_EXCEEDED",
                f"Aggregate audio duration is {sum(audio_durations):g}s; maximum is 30s.",
            ))

    if not results:
        results.append(finding(
            "pass", "ASSET_LIMITS_OK",
            f"Asset limits pass: {counts['image']} images, {counts['video']} videos, {counts['audio']} audios. No undocumented mixed-total cap applied.",
            **counts,
        ))
    return results


def check_time_slices(
    text: str,
    duration: float | None = None,
    mode: str = "standard",
    fps: float = 24.0,
) -> list[dict]:
    slices = parse_time_slices(text, fps=fps)
    results = []
    timeline_required = mode == "ultra_long" or (
        mode in {"standard", "extension", "creative_transfer", "storyboard"}
        and duration is not None and duration > 10
    )
    if not slices:
        if timeline_required:
            return [finding(
                "error", "TIMELINE_REQUIRED",
                f"{mode} at {duration:g}s requires timestamped beats for temporal control.",
            )]
        return [finding(
            "pass" if duration is not None and duration <= 10 else "warning",
            "TIMELINE_OPTIONAL" if duration is not None and duration <= 10 else "TIMELINE_MISSING",
            "No timeline found; this is acceptable for one simple action up to 10s." if duration is not None and duration <= 10
            else "No timeline found; add an effective edit window or timestamped beats if timing matters.",
        )]

    for item in slices:
        if item["end"] <= item["start"]:
            results.append(finding(
                "error", "TIMELINE_REVERSED",
                f"Timestamp '{item['raw']}' ends before or at its start.",
            ))
    for previous, current in zip(slices, slices[1:]):
        if current["start"] < previous["end"] - 0.01:
            results.append(finding(
                "error", "TIMELINE_OVERLAP",
                f"'{previous['raw']}' overlaps '{current['raw']}'.",
            ))
        elif current["start"] > previous["end"] + 0.5:
            results.append(finding(
                "warning", "TIMELINE_GAP",
                f"Gap from {previous['end']:g}s to {current['start']:g}s is not directed.",
            ))

    if mode not in EDIT_MODES and mode not in {"viewpoint", "bgm", "seamless_transition"}:
        if slices[0]["start"] > 0.1:
            results.append(finding(
                "warning", "TIMELINE_NOT_FROM_ZERO",
                f"Timeline starts at {slices[0]['start']:g}s instead of 0s.",
            ))
        if duration is not None and abs(slices[-1]["end"] - duration) > 0.5:
            results.append(finding(
                "warning", "TIMELINE_DURATION_MISMATCH",
                f"Timeline ends at {slices[-1]['end']:g}s but target duration is {duration:g}s.",
            ))

    if not results:
        results.append(finding(
            "pass", "TIMELINE_OK",
            f"Parsed {len(slices)} ordered time ranges using seconds, clock time, or {fps:g}fps frames.",
        ))
    return results


def check_camera_language(text: str, mode: str = "standard") -> list[dict]:
    if mode in EDIT_MODES or mode in {"bgm", "seamless_transition"}:
        return [finding("info", "CAMERA_NOT_REQUIRED", "This mode does not require adding camera direction.")]
    terms = [
        "特写", "近景", "中景", "远景", "全景", "跟拍", "推近", "拉远", "摇摄", "环绕",
        "航拍", "俯拍", "仰拍", "手持", "固定机位", "一镜到底", "浅景深", "镜头",
        "close-up", "wide shot", "tracking shot", "dolly", "pan shot", "tilt shot", "orbit",
        "aerial shot", "pov", "handheld", "locked-off", "camera", "lens",
    ]
    found = [term for term in terms if term in text.lower()]
    if not found:
        return [finding(
            "warning", "CAMERA_LANGUAGE_MISSING",
            "No concrete shot size, viewpoint, or camera behavior found; add one when it serves the story.",
        )]
    return [finding("pass", "CAMERA_LANGUAGE_OK", f"Camera direction found: {', '.join(found[:5])}.")]


def check_cgi_words(text: str) -> list[dict]:
    vague = [
        word for word in ("超清晰", "杰作", "高画质", "超高画质", "完美画质", "masterpiece", "best quality", "ultra hd")
        if word.lower() in text.lower()
    ]
    if vague:
        return [finding(
            "warning", "VAGUE_QUALITY_LANGUAGE",
            f"Vague quality language found ({', '.join(vague)}); prefer concrete light, material, texture, and motion behavior.",
        )]
    return [finding("pass", "QUALITY_LANGUAGE_OK", "No vague quality-booster language found.")]


def _segments_for_conflict(text: str, fps: float = 24.0) -> list[str]:
    ranges = list(re.finditer(
        r"(?:\d{1,2}:\d{2}(?:\.\d+)?|\d+(?:\.\d+)?)\s*[-–—~至]\s*"
        r"(?:\d{1,2}:\d{2}(?:\.\d+)?|\d+(?:\.\d+)?)\s*(?:秒|s)?",
        text, re.IGNORECASE,
    ))
    if not ranges:
        return [text]
    return [text[m.end(): ranges[i + 1].start() if i + 1 < len(ranges) else len(text)] for i, m in enumerate(ranges)]


def check_conflict(text: str) -> list[dict]:
    results = []
    pairs = [
        (("快速", "高速", "fast", "rapid"), ("缓慢", "慢动作", "slow motion"), "simultaneous fast and slow motion"),
        (("推进", "推近", "push in", "dolly in"), ("拉远", "pull out", "dolly out"), "simultaneous push-in and pull-out"),
    ]
    for segment in _segments_for_conflict(text):
        lower = segment.lower()
        for left, right, description in pairs:
            if any(term in lower for term in left) and any(term in lower for term in right):
                results.append(finding(
                    "warning", "MOTION_CONFLICT",
                    f"A single time range contains {description}; clarify sequence or intent.",
                ))

    lower = text.lower()
    if any(term in lower for term in ("14mm", "超广角", "ultra-wide")) and any(
        term in lower for term in ("强烈背景虚化", "creamy bokeh", "极浅景深")
    ):
        results.append(finding(
            "warning", "OPTICAL_TRADEOFF",
            "Extreme wide-angle optics and extremely shallow background blur are in tension; clarify whether this is a stylized effect.",
        ))
    if ("无声音" in text or "total silence" in lower) and any(
        term in lower for term in ("保留对白", "保留环境音", "keep dialogue", "keep ambience")
    ):
        results.append(finding(
            "error", "AUDIO_CONTRADICTION",
            "The prompt requests total silence while also preserving audio stems.",
        ))
    if not results:
        results.append(finding("pass", "NO_CONFLICT", "No direct timing, optical, or audio contradiction detected."))
    return results


def check_ambiguous_terms(text: str, lang: str | None = None) -> list[dict]:
    risky = {
        "Dolly": "dolly tracking shot", "Aerial": "aerial drone shot", "Crane": "crane shot",
        "Pan": "pan shot", "Arc": "arc shot", "Dutch": "dutch angle shot",
    }
    found = []
    for word, alternative in risky.items():
        for match in re.finditer(rf"(?<![A-Za-z]){word}(?![A-Za-z])", text, re.IGNORECASE):
            tail = text[match.end():match.end() + 18].strip().lower()
            if not any(tail.startswith(suffix) for suffix in ("shot", "camera", "tracking", "in", "out", "left", "right", "angle", "drone")):
                found.append(f"{word}→{alternative}")
                break
    if found:
        return [finding(
            "warning", "AMBIGUOUS_CAMERA_TERM",
            "Bare English camera terms may be ambiguous; use full phrases: " + "; ".join(found),
        )]
    return [finding("pass", "NO_AMBIGUOUS_CAMERA_TERMS", "No bare ambiguous English camera term found.")]


def _contains(text: str, terms: tuple[str, ...] | list[str]) -> bool:
    lower = text.lower()
    return any(term.lower() in lower for term in terms)


def check_mode_contract(text: str, mode: str) -> list[dict]:
    results = []

    def require(condition: bool, code: str, message: str, level: str = "error"):
        if not condition:
            results.append(finding(level, code, message))

    video_tokens = _asset_inventory(text)["video"]
    image_tokens = _asset_inventory(text)["image"]

    if mode == "ultra_long":
        require(_contains(text, ("bible", "连续性", "continuity")), "LONGFORM_BIBLE_MISSING", "Ultra-long prompts need a continuity/character bible.")
        require(_contains(text, ("故事概述", "story overview", "开端", "第一幕", "act 1")), "LONGFORM_STORY_MISSING", "Ultra-long prompts need a story overview or act structure.")
        require(_contains(text, ("结尾", "收束", "resolution", "ending", "尾声")), "LONGFORM_ENDING_MISSING", "Ultra-long prompts need an explicit ending or resolution.")
    elif mode == "extension":
        require(bool(video_tokens), "EXTENSION_SOURCE_MISSING", "Extension requires a source-video token such as @视频1.")
        require(_contains(text, ("向后", "向前", "forward", "backward", "extend after", "extend before")), "EXTENSION_DIRECTION_MISSING", "State forward/backward extension direction.")
        require(_contains(text, ("延长", "新增", "added", "extend")), "EXTENSION_ADDED_SCOPE_MISSING", "State that the duration applies to the added portion.")
        require(_contains(text, ("交接状态", "首帧", "尾帧", "boundary state", "last frame", "first frame")), "EXTENSION_BOUNDARY_MISSING", "Describe the source boundary state.", "warning")
        require(_contains(text, ("原视频保持不变", "原视频不变", "source unchanged", "original unchanged")), "EXTENSION_PRESERVE_MISSING", "State that the original source portion remains unchanged.", "warning")
    elif mode in {"smart_edit", "advanced_edit"}:
        require(bool(video_tokens), "EDIT_SOURCE_MISSING", "Video editing requires a source-video token.")
        require(_contains(text, ("替换", "移除", "删除", "添加", "改为", "修改", "→", "replace", "remove", "add", "change", "recolor")), "EDIT_CHANGE_MISSING", "State the A→B change or removal/addition.")
        require(_contains(text, ("保持", "保留", "不变", "preserve", "keep", "unchanged")), "EDIT_PRESERVE_LIST_MISSING", "List the content that must remain unchanged.")
        require(bool(parse_time_slices(text)) or _contains(text, ("全片", "throughout", "entire video", "从第", "起")), "EDIT_TIME_SCOPE_MISSING", "State the effective edit time or 'entire video'.", "warning")
        if mode == "advanced_edit":
            require(_contains(text, ("红框", "箭头", "地标", "红线", "框内", "左侧", "右侧", "box", "arrow", "landmark", "line")), "ANNOTATION_LOCATOR_MISSING", "Advanced editing needs the annotation and intended side/region.")
    elif mode == "viewpoint":
        require(bool(video_tokens), "VIEWPOINT_SOURCE_MISSING", "Viewpoint modification requires a source-video token.")
        require(_contains(text, ("机位", "视角", "pov", "viewpoint", "angle", "camera")), "VIEWPOINT_TARGET_MISSING", "Specify the target viewpoint, height, angle, or camera path.")
        require(_contains(text, ("空间", "布局", "比例", "几何", "geometry", "layout", "scale")), "VIEWPOINT_GEOMETRY_MISSING", "State which spatial geometry must remain coherent.", "warning")
    elif mode == "bgm":
        require(bool(video_tokens), "BGM_SOURCE_MISSING", "BGM separation requires a source-video token.")
        require(_contains(text, ("移除背景音乐", "移除bgm", "remove background music", "remove bgm")), "BGM_REMOVAL_MISSING", "Explicitly request removal of BGM/background music.")
        require(_contains(text, ("保留对白", "保留人声", "保留环境音", "keep dialogue", "keep speech", "keep ambience")), "BGM_STEMS_MISSING", "State which speech, ambience, or foley stems remain.")
        require(_contains(text, ("画面", "visual", "video")) and _contains(text, ("不变", "保持", "unchanged", "preserve")), "BGM_VISUAL_PRESERVE_MISSING", "State that requested visual content remains unchanged.")
    elif mode == "creative_transfer":
        require(bool(video_tokens), "TRANSFER_SOURCE_MISSING", "Creative transfer needs a source-video reference.")
        require(_contains(text, ("运镜", "节奏", "情绪", "机制", "轨迹", "创意", "camera", "rhythm", "emotion", "mechanism", "form")), "TRANSFER_ATTRIBUTE_MISSING", "Name the abstract form to transfer.")
        require(_contains(text, ("不要迁移", "不参考", "exclude", "do not transfer", "不带入")), "TRANSFER_EXCLUSION_MISSING", "Exclude unwanted source identity, scene, brand, text, or audio.", "warning")
    elif mode == "green_screen":
        require(bool(video_tokens), "GREEN_FOREGROUND_MISSING", "Green-screen editing needs a foreground video.")
        require(bool(image_tokens) or len(video_tokens) >= 2, "GREEN_BACKGROUND_MISSING", "Bind an image or second video as the background.")
        require(_contains(text, ("绿幕", "绿色背景", "green screen", "green spill", "绿色溢色")), "GREEN_KEYING_MISSING", "Request green-background and spill removal.")
        require(_contains(text, ("透视", "光线", "接触阴影", "perspective", "lighting", "contact shadow")), "GREEN_INTEGRATION_MISSING", "Match perspective, lighting, and contact shadow.", "warning")
    elif mode in {"rough_white_model", "fine_white_model"}:
        require(bool(video_tokens), "WHITE_MODEL_SOURCE_MISSING", "White-model rendering needs a source video.")
        require(_contains(text, ("白模", "blockout", "previs", "proxy")), "WHITE_MODEL_TYPE_MISSING", "Identify the source as a white model/blockout/previs.")
        require(_contains(text, ("映射", "对应", "map", "render")), "WHITE_MODEL_MAPPING_MISSING", "Map proxies to final characters, props, or materials.")
        require(_contains(text, ("去除", "不要保留", "remove", "轨迹线", "相机锥体", "helper", "debug")), "WHITE_MODEL_HELPERS_MISSING", "Remove gray materials and production helper geometry.", "warning")
    elif mode == "seamless_transition":
        require(len(video_tokens) >= 2, "TRANSITION_TWO_SOURCES_REQUIRED", "Seamless transition requires two source-video tokens.")
        require(_contains(text, ("不修改", "保持原视频", "unchanged", "do not modify")), "TRANSITION_SOURCE_PRESERVE_MISSING", "State that both source clips remain unchanged.")
        require(_contains(text, ("尾帧", "首帧", "锚点", "遮挡", "match", "anchor", "last frame", "first frame")), "TRANSITION_BRIDGE_MISSING", "Define the A→bridge→B anchor or mechanism.")
    elif mode == "storyboard":
        require(bool(image_tokens), "STORYBOARD_IMAGE_MISSING", "Multi-panel storyboard generation needs an image token.")
        require(_contains(text, ("顺序", "左上", "右上", "panel", "reading order", "镜头1")), "STORYBOARD_ORDER_MISSING", "Declare panel reading order and shot mapping.")
        require(_contains(text, ("保持", "连续", "一致", "continuity", "consistent")), "STORYBOARD_CONTINUITY_MISSING", "State identity and scene continuity across panels.", "warning")

    if not results:
        results.append(finding("pass", "MODE_CONTRACT_OK", f"Required {mode} prompt contract fields are present."))
    return results


def validate_prompt(
    text: str,
    lang: str | None = None,
    mode: str = "standard",
    duration: float | None = None,
    source_duration: float | None = None,
    resolution: str | None = None,
    image_count: int | None = None,
    video_durations: list[float] | None = None,
    audio_durations: list[float] | None = None,
    fps: float = 24.0,
) -> dict:
    """Run Seedance 2.5 hard-limit, timeline, contract, and conflict checks."""
    if not text or not text.strip():
        result = finding("error", "PROMPT_EMPTY", "Prompt is empty.")
        return {
            "version": "2.5", "mode": normalize_mode(mode), "language": lang or "unknown",
            "duration": duration, "passed": False,
            "summary": {"errors": 1, "warnings": 0, "passed": 0, "infos": 0},
            "results": [result],
        }

    normalized_mode = normalize_mode(mode)
    language = lang or detect_language(text)
    declared = _detect_declared_duration(text)
    effective_duration = duration if duration is not None else declared

    results = []
    results.extend(check_length(text, language))
    results.extend(check_duration(normalized_mode, effective_duration, source_duration))
    results.extend(check_resolution(resolution))
    results.extend(check_asset_refs(text, image_count, video_durations, audio_durations))
    results.extend(check_time_slices(text, effective_duration, normalized_mode, fps))
    results.extend(check_mode_contract(text, normalized_mode))
    results.extend(check_camera_language(text, normalized_mode))
    results.extend(check_cgi_words(text))
    results.extend(check_conflict(text))
    results.extend(check_ambiguous_terms(text, language))

    summary = {
        "errors": sum(item["level"] == "error" for item in results),
        "warnings": sum(item["level"] == "warning" for item in results),
        "passed": sum(item["level"] == "pass" for item in results),
        "infos": sum(item["level"] == "info" for item in results),
    }
    return {
        "version": "2.5", "mode": normalized_mode, "language": language,
        "duration": effective_duration, "source_duration": source_duration,
        "resolution": resolution, "passed": summary["errors"] == 0,
        "summary": summary, "results": results,
    }


def validate_multi_segment(segments: list[str], lang: str | None = None) -> dict:
    """Validate deliberately segmented projects, normally for >180s or episodic work."""
    if not segments:
        return {"passed": False, "error": "No prompt segments supplied."}
    segment_results = [validate_prompt(segment, lang=lang, mode="standard") for segment in segments]
    cross = []
    for label, terms, code in (
        ("continuity", ("连续性", "continuity", "bible"), "CROSS_CONTINUITY_MISSING"),
        ("handoff", ("交接", "尾帧", "首帧", "handoff", "boundary"), "CROSS_HANDOFF_MISSING"),
    ):
        if not all(_contains(segment, terms) for segment in segments):
            cross.append(finding(
                "warning", code,
                f"Not every deliberate segment declares its {label} state.",
            ))
    if not cross:
        cross.append(finding("pass", "CROSS_SEGMENT_OK", "Continuity and handoff language appears in every segment."))
    return {
        "version": "2.5", "segment_count": len(segments),
        "passed": all(item["passed"] for item in segment_results) and not any(item["level"] == "error" for item in cross),
        "per_segment": segment_results, "cross_segment": cross,
    }


def format_report(validation: dict) -> str:
    icons = {"error": "❌", "warning": "⚠️", "pass": "✅", "info": "ℹ️"}
    lines = [
        "", "=" * 58, "Seedance 2.5 prompt validation report", "=" * 58,
        f"Mode: {validation.get('mode', 'n/a')} | Language: {validation.get('language', 'n/a')} | Duration: {validation.get('duration', 'n/a')}", "",
    ]
    for item in validation.get("results", []):
        lines.append(f"{icons.get(item['level'], '•')} [{item['code']}] {item['message']}")
    summary = validation.get("summary", {})
    lines.extend([
        "", "-" * 58,
        ("PASS" if validation.get("passed") else "FAIL")
        + f" — {summary.get('errors', 0)} errors, {summary.get('warnings', 0)} warnings",
    ])
    return "\n".join(lines)


def _float_list(value: str | None) -> list[float] | None:
    if value is None:
        return None
    if not value.strip():
        return []
    return [float(part.strip()) for part in value.split(",")]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a Seedance 2.5 shot-design prompt.")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--prompt", help="Prompt text.")
    source.add_argument("--prompt-file", type=Path, help="UTF-8 prompt file.")
    parser.add_argument("--mode", default="standard", help="Seedance route/mode.")
    parser.add_argument("--duration", type=float, help="Output duration; for extension, added duration.")
    parser.add_argument("--source-duration", type=float, help="Source-video duration in seconds.")
    parser.add_argument("--resolution", help="Requested output resolution (480p or 720p).")
    parser.add_argument("--image-count", type=int, help="Uploaded image count if not inferable from tokens.")
    parser.add_argument("--video-durations", help="Comma-separated referenced-video durations.")
    parser.add_argument("--audio-durations", help="Comma-separated referenced-audio durations.")
    parser.add_argument("--fps", type=float, default=24.0, help="FPS for frame anchors; default 24.")
    parser.add_argument("--lang", help="Override detected language code.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of a human report.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.prompt_file:
        text = args.prompt_file.read_text(encoding="utf-8")
    elif args.prompt is not None:
        text = args.prompt
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        parser.error("provide --prompt, --prompt-file, or pipe prompt text on stdin")

    try:
        result = validate_prompt(
            text, lang=args.lang, mode=args.mode, duration=args.duration,
            source_duration=args.source_duration, resolution=args.resolution,
            image_count=args.image_count,
            video_durations=_float_list(args.video_durations),
            audio_durations=_float_list(args.audio_durations), fps=args.fps,
        )
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else format_report(result))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
