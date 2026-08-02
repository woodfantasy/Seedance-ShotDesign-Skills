# Seedance 2.5 官方平台规范

> Source of truth: `【即梦】Seedance 2.5 使用手册.md`, reviewed 2026-08-02. Use this file for platform limits. Distinguish hard limits from quality guidance and unresolved UI details.

## Contents

- Hard platform limits
- Input file requirements
- Stability guidance
- Supported modes and language behavior
- Prompt and timestamp behavior
- Unverified or ambiguous items

## Hard platform limits

### Output duration

| Mode | Duration | Notes |
|---|---:|---|
| Standard generation | 4–30s | `duration=-1` may represent platform auto duration; do not assume it when the user requests an exact length |
| Ultra-long video | 30–180s | Dedicated 超长视频 mode; one generation rather than mandatory 15s splitting |
| Video extension source | ≤30s | Only a source/current result no longer than 30s can be extended |
| Added extension | 4–30s | UI duration means the added interval, not the final total |
| Extension result | ≤60s | Maximum example: 30s source + 30s extension |

Standard generation uses 97–721 frames for 4–30 seconds. The official examples use 24fps frame anchors, e.g. 720 frames for 30 seconds.

### Output resolution

- Supported API/manual values: **480p** and **720p**.
- Do not claim official 1080p support from this manual.
- The UI walkthrough mentions a `720P+` label. Treat it as a UI label, not a documented 1080p parameter.

### Images

- Maximum per request: **30 images**.
- Supported formats listed in the manual's unchanged input specification: jpeg, png, webp, bmp, tiff, gif, heic, heif.
- Single image: under 30MB.
- Width/height ratio: 0.4–2.5.
- Width and height: 300–6000px.
- Prefer images within 4K for the 30-image workflow.

### Videos

- Maximum per request: **10 videos**.
- Single reference duration: nominally 2–30s; accepted tolerance shown as 1.8–30.2s.
- Total duration of all reference videos: nominally ≤30s; accepted tolerance shown as ≤30.2s.
- Formats: mp4, mov.
- Resolution: 480p–4K.
- Aspect ratio: 0.4–2.5.
- Width and height: 300–6000px.
- Total pixel range: 409,600–8,295,044.
- Single video size: ≤200MB.
- Frame rate: 24–60fps.

### Audio

- Maximum per request: **10 audio clips**.
- Single reference duration: ≤30s.
- Total duration of all reference audio: ≤30s.
- Formats: wav, mp3.
- Single audio size: ≤15MB.
- Audio-only multimodal generation is supported; an image or video is no longer mandatory.

### Mixed inputs

The Seedance 2.5 manual does **not** state a combined 12-file cap. Validate the documented per-type limits rather than reusing the Seedance 2.0 mixed-total rule.

## Stability guidance

These are quality recommendations, not upload rejection limits.

| Scenario | Stable range | Higher-risk range |
|---|---|---|
| Distinct subjects from video/audio | 1–5 | 6–10 may require more attempts |
| Subject video/audio duration | 5–10s | Longer references may reduce stability |
| Distinct subjects from images | 1–8 | 9–12 may require more attempts |
| Video used for editing | ≤20s | Longer clips may reduce edit preservation |
| Reference images for video editing | 1–5 | 6–8 may reduce stability |

For more than five subjects, separate multi-angle views into multiple images. Multiple images containing one view each are more stable than one collage containing many views.

## Supported modes

- 全能参考
- 智能编辑
- 超长视频
- 首尾帧
- 视频延长
- 高级编辑 for locally uploaded video
- 视频编辑 for an already generated result
- Spatial viewpoint modification
- BGM separation/removal
- Creative transfer
- Multi-character reference
- Voice-timbre reference
- Green-screen editing
- Rough/fine white-model control
- Seamless transition between two source clips
- Multi-panel storyboard input

## Prompt structure

Official common formula:

```text
Material description
+ one-sentence overview
+ detailed story/timestamp description
+ global supplement at the end
```

Within a segment, include positive instructions for image, camera, action, dialogue, and sound, plus contextual negative instructions for unwanted content. Repeat only global constraints that genuinely need persistence.

For a complex 30s video, use:

```text
Multimodal reference layer
+ global world/visual/camera/character/performance setup
+ timestamped script with physical action and optional directing subtext
+ global continuity and negative constraints
```

For an ultra-long video, the manual explicitly permits restating duration and aspect ratio at the beginning.

## Timestamp behavior

- Native second-level interval control is supported.
- Use ordered ranges such as `[00.0-05.0s]`, `0-5秒`, or `0:30-0:45`.
- Frame anchors are supported in official examples. Assume 24fps only when the prompt or production brief establishes it.
- Attach actions, dialogue, sound effects, transitions, or edit windows to explicit time ranges when timing matters.

## Language behavior

- Priority optimization: Chinese, English, Spanish, Indonesian, Malay.
- Supported coverage: Thai, Arabic, Portuguese, Vietnamese, Japanese, Korean.
- Native-language directing prompts are supported.
- Exact target-language dialogue and subtitles should be written explicitly, with speaker binding and pronunciation/delivery intent.

## Asset tokens

Use the exact token inserted by the platform UI. Typical Chinese-interface tokens are:

```text
@图片1   @视频1   @音频1
```

Do not infer that token numbering must stop at the old 9/3/3 limits.

## Content and identity safety

The provided capability manual demonstrates photorealistic human generation but does not define every identity-binding or moderation rule. Distinguish generated fictional humans from real-person likeness use. Require authorization for recognizable real people and follow current platform policy for public figures, copyrighted characters, brands, violence, sexual content, and other sensitive material.

## Unverified or ambiguous items

- No official prompt character/word ceiling is stated in this manual. Do not enforce the legacy 500-character/1000-word limit.
- `720P+` appears in a UI example, while the parameter table states 480p/720p. Use the parameter table until separately verified.
- The manual links a Maya/Blender white-model plugin guide but does not document CLI commands or model channel names. Do not publish old CLI commands as 2.5 facts without current official verification.
- Per-file image/audio requirements appear in the unchanged specification column. Treat them as current operational limits while marking future changes through a source update rather than silently guessing.
