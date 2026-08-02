#!/usr/bin/env python3
"""Regression tests for the Seedance 2.5 mode-aware prompt validator."""

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("validate_prompt", SCRIPT_DIR / "validate_prompt.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def codes(findings, level=None):
    return {
        item["code"] for item in findings
        if level is None or item["level"] == level
    }


def add_case(cls, name, function):
    function.__name__ = name
    setattr(cls, name, function)


class TestModeNormalization(unittest.TestCase):
    def test_unknown_mode_rejected(self):
        with self.assertRaises(ValueError):
            validator.normalize_mode("imaginary")


MODE_CASES = {
    "standard": "standard", "generation": "standard", "all_reference": "standard",
    "first_last": "standard", "全能参考": "standard", "首尾帧": "standard",
    "ultra_long": "ultra_long", "ultra-long": "ultra_long", "超长视频": "ultra_long",
    "extension": "extension", "extend": "extension", "视频延长": "extension",
    "smart_edit": "smart_edit", "edit": "smart_edit", "智能编辑": "smart_edit",
    "advanced_edit": "advanced_edit", "高级编辑": "advanced_edit", "视频编辑": "advanced_edit",
    "viewpoint": "viewpoint", "空间视角修改": "viewpoint",
    "bgm": "bgm", "audio_edit": "bgm", "音轨编辑": "bgm",
    "creative_transfer": "creative_transfer", "迁移创意": "creative_transfer",
    "green_screen": "green_screen", "绿幕编辑": "green_screen",
    "rough_white_model": "rough_white_model", "粗颗粒白模": "rough_white_model",
    "fine_white_model": "fine_white_model", "细颗粒白模": "fine_white_model",
    "seamless_transition": "seamless_transition", "视频无缝转场": "seamless_transition",
    "storyboard": "storyboard", "多宫格分镜": "storyboard",
}

for index, (raw, expected) in enumerate(MODE_CASES.items()):
    def make_test(value=raw, target=expected):
        def test(self):
            self.assertEqual(validator.normalize_mode(value), target)
        return test
    add_case(TestModeNormalization, f"test_alias_{index:02d}_{expected}", make_test())


class TestDurationMatrix(unittest.TestCase):
    pass


DURATION_CASES = [
    ("standard", 4, None, True, "DURATION_OK"),
    ("standard", 30, None, True, "DURATION_OK"),
    ("standard", 3.9, None, False, "STANDARD_DURATION_OUT_OF_RANGE"),
    ("standard", 30.1, None, False, "STANDARD_DURATION_OUT_OF_RANGE"),
    ("ultra_long", 30, None, True, "DURATION_OK"),
    ("ultra_long", 180, None, True, "DURATION_OK"),
    ("ultra_long", 29.9, None, False, "ULTRA_LONG_DURATION_OUT_OF_RANGE"),
    ("ultra_long", 180.1, None, False, "ULTRA_LONG_DURATION_OUT_OF_RANGE"),
    ("extension", 4, 20, True, "DURATION_OK"),
    ("extension", 30, 30, True, "DURATION_OK"),
    ("extension", 3.9, 20, False, "EXTENSION_ADDED_DURATION_OUT_OF_RANGE"),
    ("extension", 30.1, 20, False, "EXTENSION_ADDED_DURATION_OUT_OF_RANGE"),
    ("extension", 20, 30.1, False, "EXTENSION_SOURCE_DURATION_OUT_OF_RANGE"),
    ("extension", 30, 30.1, False, "EXTENSION_FINAL_DURATION_EXCEEDED"),
    ("extension", 20, None, True, "SOURCE_DURATION_MISSING"),
    ("smart_edit", 12, 20, True, "DURATION_OK"),
    ("smart_edit", 25, 25, True, "EDIT_SOURCE_STABILITY_BAND"),
    ("smart_edit", 25, 31, False, "EDIT_SOURCE_DURATION_OUT_OF_RANGE"),
    ("green_screen", 4, None, True, "DURATION_OK"),
    ("storyboard", 30, None, True, "DURATION_OK"),
    ("seamless_transition", 6, None, True, "DURATION_OK"),
    ("creative_transfer", 31, None, False, "STANDARD_DURATION_OUT_OF_RANGE"),
    ("standard", None, None, False, "DURATION_MISSING"),
    ("bgm", None, None, True, "DURATION_MISSING"),
]

for index, (mode, duration, source_duration, no_error, expected_code) in enumerate(DURATION_CASES):
    def make_test(m=mode, d=duration, s=source_duration, ok=no_error, expected=expected_code):
        def test(self):
            result = validator.check_duration(m, d, s)
            self.assertIn(expected, codes(result))
            self.assertEqual(not any(item["level"] == "error" for item in result), ok)
        return test
    add_case(TestDurationMatrix, f"test_duration_{index:02d}_{mode}", make_test())


class TestResolutionMatrix(unittest.TestCase):
    pass


RESOLUTION_CASES = [
    ("480p", "pass", "RESOLUTION_OK"),
    ("720p", "pass", "RESOLUTION_OK"),
    ("720P", "pass", "RESOLUTION_OK"),
    ("720P+", "warning", "RESOLUTION_UI_LABEL"),
    ("1080p", "error", "RESOLUTION_UNDOCUMENTED"),
    ("4k", "error", "RESOLUTION_UNDOCUMENTED"),
    (None, "info", "RESOLUTION_NOT_SUPPLIED"),
]

for index, (value, level, expected) in enumerate(RESOLUTION_CASES):
    def make_test(raw=value, target_level=level, code=expected):
        def test(self):
            findings = validator.check_resolution(raw)
            self.assertIn(code, codes(findings, target_level))
        return test
    add_case(TestResolutionMatrix, f"test_resolution_{index:02d}", make_test())


class TestLanguageDetection(unittest.TestCase):
    pass


LANGUAGE_CASES = [
    ("一个女孩在雨中奔跑，镜头跟拍。", "zh"),
    ("A woman runs through rain while the camera follows.", "en"),
    ("少女が雨の中を走り、カメラが追う。", "ja"),
    ("여자가 빗속을 달리고 카메라가 따라간다.", "ko"),
    ("ตัวละครเดินผ่านสายฝนอย่างช้าๆ", "th"),
    ("تتحرك الشخصية ببطء أمام الكاميرا", "ar"),
    ("El personaje entra en la escena con una cámara lenta.", "es"),
    ("Uma personagem entra em cena e a câmera acompanha.", "pt"),
    ("Karakter yang berjalan dengan kamera mengikuti adegan.", "id"),
    ("Nhân vật bước vào cảnh, video không có phụ đề.", "vi"),
]

for index, (text, expected) in enumerate(LANGUAGE_CASES):
    def make_test(value=text, target=expected):
        def test(self):
            self.assertEqual(validator.detect_language(value), target)
        return test
    add_case(TestLanguageDetection, f"test_language_{index:02d}_{expected}", make_test())


class TestAssetLimits(unittest.TestCase):
    def test_no_combined_twelve_file_cap(self):
        text = " ".join([f"@图片{i}" for i in range(1, 11)] + [f"@视频{i}" for i in range(1, 6)])
        findings = validator.check_asset_refs(text)
        self.assertNotIn("TOTAL_REF_EXCEEDED", codes(findings))
        self.assertFalse(any(item["level"] == "error" for item in findings))

    def test_audio_only_allowed(self):
        findings = validator.check_asset_refs("只参考@音频1生成抽象影像。", audio_durations=[30])
        self.assertIn("ASSET_LIMITS_OK", codes(findings, "pass"))


ASSET_CASES = [
    (" ".join(f"@图片{i}" for i in range(1, 31)), {}, True, "ASSET_LIMITS_OK"),
    ("@图片31", {}, False, "IMAGE_TOKEN_OUT_OF_RANGE"),
    ("", {"image_count": 31}, False, "IMAGE_COUNT_EXCEEDED"),
    (" ".join(f"@视频{i}" for i in range(1, 11)), {}, True, "ASSET_LIMITS_OK"),
    ("@视频11", {}, False, "VIDEO_TOKEN_OUT_OF_RANGE"),
    ("", {"video_durations": [2] * 11}, False, "VIDEO_COUNT_EXCEEDED"),
    (" ".join(f"@音频{i}" for i in range(1, 11)), {}, True, "ASSET_LIMITS_OK"),
    ("@音频11", {}, False, "AUDIO_TOKEN_OUT_OF_RANGE"),
    ("", {"audio_durations": [2] * 11}, False, "AUDIO_COUNT_EXCEEDED"),
    ("@视频1", {"video_durations": [1.8]}, True, "ASSET_LIMITS_OK"),
    ("@视频1", {"video_durations": [30.2]}, True, "ASSET_LIMITS_OK"),
    ("@视频1", {"video_durations": [1.7]}, False, "VIDEO_DURATION_OUT_OF_RANGE"),
    ("@视频1", {"video_durations": [30.3]}, False, "VIDEO_DURATION_OUT_OF_RANGE"),
    ("@视频1 @视频2", {"video_durations": [15.1, 15.1]}, True, "ASSET_LIMITS_OK"),
    ("@视频1 @视频2", {"video_durations": [15.2, 15.1]}, False, "VIDEO_TOTAL_DURATION_EXCEEDED"),
    ("@音频1", {"audio_durations": [30]}, True, "ASSET_LIMITS_OK"),
    ("@音频1", {"audio_durations": [30.1]}, False, "AUDIO_DURATION_OUT_OF_RANGE"),
    ("@音频1 @音频2", {"audio_durations": [15, 15.1]}, False, "AUDIO_TOTAL_DURATION_EXCEEDED"),
    ("@Image1 @image1 @图片1", {}, True, "ASSET_LIMITS_OK"),
    ("@Video10 @Audio10 @Image30", {}, True, "ASSET_LIMITS_OK"),
]

for index, (text, kwargs, no_error, expected) in enumerate(ASSET_CASES):
    def make_test(value=text, options=kwargs, ok=no_error, code=expected):
        def test(self):
            findings = validator.check_asset_refs(value, **options)
            self.assertIn(code, codes(findings))
            self.assertEqual(not any(item["level"] == "error" for item in findings), ok)
        return test
    add_case(TestAssetLimits, f"test_asset_{index:02d}", make_test())


class TestTimelineParsing(unittest.TestCase):
    def test_mixed_formats_sorted(self):
        text = "[00:10-00:20] B；0-5秒：A；第120-240帧：C"
        slices = validator.parse_time_slices(text, fps=24)
        self.assertEqual([(item["start"], item["end"]) for item in slices], [(0, 5), (5, 10), (10, 20)])

    def test_frame_fps_override(self):
        slices = validator.parse_time_slices("第60-120帧", fps=30)
        self.assertEqual((slices[0]["start"], slices[0]["end"]), (2, 4))


TIMELINE_CASES = [
    ("0-5秒：A；5-10秒：B", 10, "standard", "TIMELINE_OK", False),
    ("[0-5s] A [5-10s] B", 10, "standard", "TIMELINE_OK", False),
    ("[00:00-00:20] A [00:20-01:00] B", 60, "ultra_long", "TIMELINE_OK", False),
    ("第0-120帧：A；第120-240帧：B", 10, "standard", "TIMELINE_OK", False),
    ("0-6秒：A；5-10秒：B", 10, "standard", "TIMELINE_OVERLAP", True),
    ("5-0秒：A", 5, "standard", "TIMELINE_REVERSED", True),
    ("0-4秒：A；5-10秒：B", 10, "standard", "TIMELINE_GAP", False),
    ("1-5秒：A；5-10秒：B", 10, "standard", "TIMELINE_NOT_FROM_ZERO", False),
    ("0-5秒：A", 10, "standard", "TIMELINE_DURATION_MISMATCH", False),
    ("单一动作，固定机位。", 4, "standard", "TIMELINE_OPTIONAL", False),
    ("单一动作，固定机位。", 10, "standard", "TIMELINE_OPTIONAL", False),
    ("连续剧情，跟拍。", 11, "standard", "TIMELINE_REQUIRED", True),
    ("连续剧情，跟拍。", 30, "standard", "TIMELINE_REQUIRED", True),
    ("连续剧情，跟拍。", 30, "ultra_long", "TIMELINE_REQUIRED", True),
    ("编辑@视频1，全片替换杯子，保持人物不变。", 12, "smart_edit", "TIMELINE_MISSING", False),
    ("编辑@视频1，0-3秒替换，3-6秒保持。", 6, "smart_edit", "TIMELINE_OK", False),
    ("0.0-2.5秒：A；2.5-5.0秒：B", 5, "standard", "TIMELINE_OK", False),
    ("0–5秒：A；5—10秒：B", 10, "standard", "TIMELINE_OK", False),
]

for index, (text, duration, mode, expected, has_error) in enumerate(TIMELINE_CASES):
    def make_test(value=text, seconds=duration, route=mode, code=expected, error=has_error):
        def test(self):
            findings = validator.check_time_slices(value, seconds, route)
            self.assertIn(code, codes(findings))
            self.assertEqual(any(item["level"] == "error" for item in findings), error)
        return test
    add_case(TestTimelineParsing, f"test_timeline_{index:02d}_{mode}", make_test())


class TestModeContracts(unittest.TestCase):
    def assertContractPasses(self, text, mode):
        findings = validator.check_mode_contract(text, mode)
        self.assertFalse(any(item["level"] == "error" for item in findings), findings)

    def test_ultra_long_complete(self):
        self.assertContractPasses("【角色 Bible】一致。【故事概述】开端发展。【结尾】收束。", "ultra_long")

    def test_ultra_long_missing_bible(self):
        self.assertIn("LONGFORM_BIBLE_MISSING", codes(validator.check_mode_contract("故事概述，结尾收束", "ultra_long"), "error"))

    def test_extension_complete(self):
        self.assertContractPasses("参考@视频1向后延长20秒，新增部分从尾帧交接状态开始，原视频保持不变。", "extension")

    def test_extension_missing_direction(self):
        self.assertIn("EXTENSION_DIRECTION_MISSING", codes(validator.check_mode_contract("@视频1延长10秒", "extension"), "error"))

    def test_smart_edit_complete(self):
        self.assertContractPasses("编辑@视频1，全片将白杯替换为玻璃杯，人物、镜头保持不变。", "smart_edit")

    def test_advanced_edit_needs_annotation(self):
        findings = validator.check_mode_contract("编辑@视频1，全片移除杯子，人物保持不变。", "advanced_edit")
        self.assertIn("ANNOTATION_LOCATOR_MISSING", codes(findings, "error"))

    def test_advanced_edit_complete(self):
        self.assertContractPasses("编辑@视频1，全片移除红框内杯子，红框外人物、镜头保持不变。", "advanced_edit")

    def test_viewpoint_complete(self):
        self.assertContractPasses("将@视频1机位改为右后方视角，保持房间空间布局、比例和动作不变。", "viewpoint")

    def test_bgm_complete(self):
        self.assertContractPasses("编辑@视频1：移除BGM，保留对白和环境音，画面保持不变。", "bgm")

    def test_creative_transfer_complete(self):
        self.assertContractPasses("参考@视频1的运镜轨迹和节奏，不要迁移原人物、背景和音轨。", "creative_transfer")

    def test_green_screen_complete(self):
        self.assertContractPasses("将@视频1绿幕前景合成到@图片1，去除绿色溢色，匹配透视、光线和接触阴影。", "green_screen")

    def test_rough_white_model_complete(self):
        self.assertContractPasses("@视频1是粗颗粒白模，将蓝色人形映射为@图片1，去除轨迹线和灰色材质。", "rough_white_model")

    def test_fine_white_model_complete(self):
        self.assertContractPasses("将@视频1细颗粒白模render为成片，人物对应@图片1，不要保留相机锥体。", "fine_white_model")

    def test_transition_complete(self):
        self.assertContractPasses("不修改@视频1和@视频2，@视频1尾帧红伞遮挡并匹配@视频2首帧红幕作为锚点。", "seamless_transition")

    def test_storyboard_complete(self):
        self.assertContractPasses("@图片1为六宫格，顺序左上到右下，镜头1开始，保持人物和场景连续一致。", "storyboard")


class TestConflictsAndQuality(unittest.TestCase):
    def test_audio_contradiction_is_error(self):
        findings = validator.check_conflict("全片无声音，同时保留对白。")
        self.assertIn("AUDIO_CONTRADICTION", codes(findings, "error"))

    def test_motion_conflict_is_warning(self):
        self.assertIn("MOTION_CONFLICT", codes(validator.check_conflict("0-5秒：快速又缓慢推进。"), "warning"))

    def test_vague_quality_is_warning(self):
        self.assertIn("VAGUE_QUALITY_LANGUAGE", codes(validator.check_cgi_words("杰作，高画质。"), "warning"))

    def test_no_universal_length_error(self):
        findings = validator.check_length("光" * 5000, "zh")
        self.assertEqual(codes(findings), {"PROMPT_SIZE_REPORTED"})
        self.assertFalse(any(item["level"] == "error" for item in findings))

    def test_bare_camera_term_warns(self):
        self.assertIn("AMBIGUOUS_CAMERA_TERM", codes(validator.check_ambiguous_terms("Use Dolly then stop."), "warning"))

    def test_full_camera_phrase_passes(self):
        self.assertIn("NO_AMBIGUOUS_CAMERA_TERMS", codes(validator.check_ambiguous_terms("Use a dolly tracking shot."), "pass"))


class TestEndToEnd(unittest.TestCase):
    def test_standard_thirty_seconds(self):
        prompt = """30秒现实主义短片，720p。镜头缓慢跟拍。
0-10秒：女孩进入车站。10-20秒：她发现车票。20-30秒：特写车票后收束。"""
        result = validator.validate_prompt(prompt, mode="standard", duration=30, resolution="720p")
        self.assertTrue(result["passed"], result)

    def test_ultra_long_ninety_seconds(self):
        prompt = """全片时长90秒，720p。【角色 Bible】面孔服装连续。【故事概述】寻找失踪列车。
【连续性】车票始终在右手。00:00-00:30 第一幕，跟拍进入。00:30-01:10 转折。01:10-01:30 结尾收束。"""
        result = validator.validate_prompt(prompt, mode="ultra_long", duration=90, resolution="720p")
        self.assertTrue(result["passed"], result)

    def test_extension_valid_final_forty_five(self):
        prompt = """参考@视频1向后延长20秒，新增部分从尾帧交接状态开始，原视频保持不变。
0-10秒：跟拍延续奔跑。10-20秒：人物停下并收束。"""
        result = validator.validate_prompt(prompt, mode="extension", duration=20, source_duration=25)
        self.assertTrue(result["passed"], result)

    def test_extension_invalid_final_sixty_one(self):
        result = validator.validate_prompt(
            "参考@视频1向后延长30秒，新增部分从尾帧开始，原视频保持不变。0-30秒：镜头跟拍。",
            mode="extension", duration=30, source_duration=31,
        )
        self.assertFalse(result["passed"])
        self.assertIn("EXTENSION_SOURCE_DURATION_OUT_OF_RANGE", codes(result["results"], "error"))

    def test_bgm_edit_does_not_require_camera(self):
        prompt = "编辑@视频1：移除背景音乐，保留对白和环境音，画面保持不变。"
        result = validator.validate_prompt(prompt, mode="bgm", duration=12, source_duration=12)
        self.assertTrue(result["passed"], result)
        self.assertIn("CAMERA_NOT_REQUIRED", codes(result["results"], "info"))

    def test_empty_prompt_fails(self):
        result = validator.validate_prompt("", mode="standard", duration=10)
        self.assertFalse(result["passed"])
        self.assertIn("PROMPT_EMPTY", codes(result["results"], "error"))

    def test_duration_inferred_from_prompt(self):
        prompt = "时长：8秒，固定机位，一个玻璃球缓慢滚动。"
        result = validator.validate_prompt(prompt, mode="standard")
        self.assertEqual(result["duration"], 8)
        self.assertTrue(result["passed"], result)

    def test_frame_timeline_end_to_end(self):
        prompt = "时长10秒，跟拍。第0-120帧：人物走近；第120-240帧：人物停下。"
        result = validator.validate_prompt(prompt, mode="standard", fps=24)
        self.assertTrue(result["passed"], result)

    def test_legacy_1080p_claim_rejected(self):
        result = validator.validate_prompt("时长8秒，固定机位。", mode="standard", resolution="1080p")
        self.assertFalse(result["passed"])
        self.assertIn("RESOLUTION_UNDOCUMENTED", codes(result["results"], "error"))

    def test_native_japanese_not_forced_to_english(self):
        result = validator.validate_prompt("8秒。固定カメラで少女が窓を開ける。", mode="standard", duration=8)
        self.assertEqual(result["language"], "ja")


class TestCLI(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT_DIR / "validate_prompt.py"), *args],
            text=True, capture_output=True, check=False,
        )

    def test_json_success_exit_zero(self):
        completed = self.run_cli("--mode", "standard", "--duration", "8", "--prompt", "固定机位，玻璃球缓慢滚动。", "--json")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertTrue(json.loads(completed.stdout)["passed"])

    def test_json_failure_exit_one(self):
        completed = self.run_cli("--mode", "standard", "--duration", "31", "--prompt", "固定机位。", "--json")
        self.assertEqual(completed.returncode, 1)
        self.assertFalse(json.loads(completed.stdout)["passed"])

    def test_unknown_mode_exit_two(self):
        completed = self.run_cli("--mode", "unknown", "--duration", "8", "--prompt", "固定机位。")
        self.assertEqual(completed.returncode, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
