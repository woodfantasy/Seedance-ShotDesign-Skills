# Seedance 2.5 Multimodal Reference Design

Use this guide when a prompt combines images, video, audio, multiple characters, voice references, audio-only input, or creative transfer. The goal is explicit attribute binding with minimal cross-contamination.

## Contents

- Inventory and hard limits
- Assign one primary job per asset
- Set scope and exclusions
- Bind characters and voices
- Manage dense image sets
- Use video references selectively
- Use audio and audio-only references
- Transfer creative form safely
- Resolve conflicting references
- Validate the reference graph

## Inventory and hard limits

Before writing, list every uploaded source using the exact interface token.

| Type | Documented limit | Key constraints |
|---|---:|---|
| Images | 30 | png/jpeg/webp/bmp/tiff/gif; each no larger than 30MB |
| Videos | 10 | mp4/mov; each nominally 2–30s; aggregate duration no more than about 30s; each no larger than 200MB |
| Audios | 10 | wav/mp3; each and aggregate duration no more than 30s; each no larger than 15MB |

There is no documented combined 12-file cap in the Seedance 2.5 manual. Video and audio can be used without an image. For exact tolerance and resolution/fps requirements, see `seedance-specs.md`.

## Assign one primary job per asset

Create a binding map before the final prompt.

```text
@图片1 → 女主身份、发型与服装 → 全片
@图片2 → 咖啡馆空间、色彩和材质 → 全片；不要迁移图片中的顾客
@视频1 → 手部拉花动作力学 → 08–14秒；不要迁移人物外貌和背景
@视频2 → 镜头环绕轨迹 → 18–24秒；不要迁移动作和音轨
@音频1 → 女主说话音色 → 两句台词；不是BGM
@音频2 → 结尾音乐节奏 → 22–30秒
```

One asset may supply multiple attributes only when they are enumerated. Avoid `完全参考@视频1` because the engine cannot know whether identity, scene, motion, camera, rhythm, or audio is intended.

## Set scope and exclusions

Every binding has three fields:

1. **what** transfers: identity, costume, scene, motion, camera, voice, music, rhythm;
2. **where/when** it applies: full video, a character, or a timestamp range;
3. **what does not transfer**: source person, background, watermark, brand, original sound, helper geometry.

Use positive preservation before negative exclusions:

```text
参考@视频1的运镜速度与绕行轨迹，应用于18–24秒；主体始终使用@图片1的外形，场景始终使用@图片2。不要迁移@视频1中的人物、室内背景、字幕和原音轨。
```

## Bind characters and voices

For multi-person work, use a role ledger:

| Role | Visual identity | Costume/prop | Start position | Voice/dialogue |
|---|---|---|---|---|
| A / 林澈 | @图片1 | blue coat, silver ring | frame left | @音频1; Mandarin |
| B / 米娅 | @图片2 | red scarf, black notebook | frame right | no voice ref; Spanish |

Then bind every dialogue line:

```text
林澈（@图片1，普通话，低声克制）说：“别回头。”
米娅（@图片2，西班牙语，急促）说：“Sigue caminando.”
无字幕。
```

Keep each person's face, hair, costume, body scale, props, screen position, and voice stable. If characters swap positions, describe the crossing action and resulting positions.

Video/audio subject counts of 1–5 are the most stable; 6–10 may reduce stability. Image subjects of 1–8 are most stable; 9–12 may reduce stability. These are warnings, not platform rejection limits.

## Manage dense image sets

The engine may accept up to 30 images, but uploading more images is not automatically better.

- With more than five important subjects, prefer separate single-view identity images instead of dense group sheets.
- Label a multi-panel sheet's panel order and map each panel explicitly.
- Do not assign two conflicting identity references to the same person without stating which attribute comes from which.
- Rank reference priority when multiple images cover the same attribute.
- Use first/last-frame images only for boundary composition; do not assume they also define all intermediate action.

```text
身份优先级：@图片1的面孔和发型最高；@图片2只参考夹克版型；@图片3只参考银色徽章，不参考人物。
```

## Use video references selectively

Video references can provide:

- body mechanics and action timing;
- camera path and acceleration;
- edit rhythm or transition logic;
- emotion/performance pattern;
- scene or lighting behavior;
- sound or voice, when explicitly selected.

Subject-reference clips of about 5–10 seconds are generally more stable than needlessly long clips. For source editing, source videos of 20 seconds or less are recommended for stability even though the platform may accept longer valid files.

When copying motion across bodies with different proportions, describe intent and contact points rather than demanding frame-perfect pose copying. Preserve gravity, weight transfer, reach, and collision response.

## Use audio and audio-only references

An audio source can serve as voice timbre, dialogue performance, BGM, beat/rhythm, ambience, or sound effect. Name exactly one or more roles.

```text
@音频1仅参考男主的声线、年龄感和克制语气；台词使用下方准确中文，不复制参考音频里的原句和背景噪声。
@音频2作为全片BGM，从00:18开始进入；不要把@音频1混入音乐层。
```

For audio-only generation, describe the visual response to audio structure:

```text
以@音频1为唯一参考。按鼓点和段落能量生成30秒抽象舞蹈影像：0–8秒低能量建立，8–22秒动作密度递增，22–30秒在最后一次重拍后定格。不要生成对白或额外音乐。
```

Do not say `无声音` when voice or foley must remain. Distinguish BGM, dialogue, ambience, and action sounds.

## Transfer creative form safely

Creative transfer should separate abstract form from source content.

Transferable form:

- camera trajectory and reveal order;
- comic timing or suspense rhythm;
- movement energy and performance arc;
- match-cut or transition mechanism;
- editing cadence and audio-visual synchronization.

Usually exclude:

- source identity and distinctive costume;
- source background and unrelated props;
- brands, watermarks, subtitles, and copyrighted character design;
- source dialogue or music unless deliberately authorized and requested.

```text
参考@视频1的“一次误会、两次升级、第三次反转”喜剧节奏，以及三次快速推近；重新设计为原创机器人在温室追逐一只蝴蝶。不要迁移原人物、原场景、原台词、品牌和音轨。
```

## Resolve conflicting references

Use explicit priority and attribute partitioning:

```text
人物身份以@图片1为准；动作以@视频1为准；镜头以@视频2为准；场景和光线以@图片2为准；发生冲突时保持人物身份和场景地理优先。
```

If two assets demand incompatible camera paths, scene geometry, or lighting, choose one or split their scopes by time. Never hide a real conflict inside `融合两者风格`.

## Validate the reference graph

- Every uploaded token appears once in the inventory and at least once in the prompt.
- Every token has a transfer role, scope, and contamination exclusion when needed.
- No asset counts or durations exceed documented limits.
- Character identity, voice, dialogue, and screen position are unambiguous.
- Audio roles distinguish dialogue, BGM, ambience, and effects.
- Multi-panel and multi-view images have a declared reading order.
- Conflicting references have a priority or non-overlapping time scopes.
- Creative transfer takes form without accidentally copying source identities or protected content.
