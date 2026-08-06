# Seedance 2.5 Failure Diagnosis Guide

Use this reference when generated output does not match the prompt intent. Diagnose the failure category first, then apply the targeted fix. Blind re-rolling wastes compute; structured diagnosis improves acceptance rate.

## Contents

- Diagnosis workflow
- Failure mode catalog
- Complexity-to-success guidance

## Diagnosis workflow

1. **Identify the symptom** — watch the output and match it to one of the failure modes below.
2. **Trace the root cause** — check which part of the prompt is likely responsible.
3. **Apply the targeted fix** — modify only the relevant prompt section.
4. **Consider an alternate route** — if the fix does not resolve the issue after two iterations, switch to a different approach.

Do not change the entire prompt at once. Isolate the failing dimension and test one fix per iteration.

---

## Failure mode catalog

### 1. Character drift (角色漂移)

**Symptom:** The character's face, hair, body proportions, or clothing change between shots or within a long-form generation. The person in shot 5 looks noticeably different from shot 1.

**Root causes:**
- Identity reference is described only in text without a visual anchor image.
- Identity attributes are scattered across the prompt rather than consolidated.
- A video or creative-transfer reference is contaminating the character's appearance.
- Long-form prompt does not restate character invariants at act boundaries.

**Fixes:**
- Provide a clear, well-lit, front-facing identity reference image and bind it with an explicit scope: `@图片1 → 角色A的面孔、发型、体型 → 全片`.
- Add 2–3 unique physical identity anchors that persist across every shot: a specific scar, accessory, tattoo, or clothing detail. List these in the continuity bible.
- In long-form prompts, restate character identity at the start of each act rather than only in the bible header.
- If using a video reference, explicitly exclude its character identity: `不要迁移@视频1中的人物外貌`.

**Alternate route:** Use the keyframe-first two-stage contract. Lock identity in a T2I hero frame first, then use it as `@图片1` for I2V, reducing drift.

---

### 2. Limb deformation (肢体变形)

**Symptom:** Hands have too many or too few fingers. Arms bend unnaturally. Limbs merge with objects or other body parts. Proportions shift mid-action.

**Root causes:**
- Action description is too vague — the model fills in ambiguous motion with artifacts.
- Requested action exceeds physical plausibility at the given timescale.
- Multiple overlapping actions are described simultaneously.

**Fixes:**
- Describe the action causally and sequentially: `右手从口袋中缓慢抽出信封 → 五指握住信封上缘 → 手臂向前平伸递出`. Avoid `拿出信封` alone.
- Reduce the number of simultaneous limb actions. One primary action with one supporting action is generally safe; three concurrent actions increase deformation risk.
- Specify which hand (left/right) and which fingers when precision matters.
- Add a negative constraint when hand clarity is critical: `双手始终保持自然的五指结构`.

**Alternate route:** For complex hand/body interactions, use a rough white-model previs to lock the motion skeleton first, then render with the white-model pipeline.

---

### 3. Motion mush (糊动 / 运动模糊)

**Symptom:** Action has insufficient amplitude or unclear direction. The character appears to "shift" rather than perform a distinct movement. Camera motion is present but generic and directionless.

**Root causes:**
- Action description lacks intensity modifiers and direction specifics.
- Camera instruction is generic (`镜头跟随`) rather than physically defined.
- Too many micro-actions are packed into a short time window.

**Fixes:**
- Add intensity modifiers to every action: `猛然起身` not `起身`, `explosive stride` not `moves forward`. See the motion intensity chart in `cinematography.md`.
- Specify direction, speed, and distance: `向画面左侧大步迈出三步` rather than `走过去`.
- For camera motion, use Level 1 + Level 2 modifiers: `快速手持跟拍` rather than `镜头跟随`.
- Reduce action density — allow at least 2–3 seconds per distinct physical action.

**Alternate route:** If a complex action sequence keeps producing mush, split it into two shorter clips and join them with a seamless transition.

---

### 4. Lighting / style discontinuity (光线/风格断裂)

**Symptom:** Lighting direction, color temperature, or visual style changes abruptly between shots or within a single generation. A warm golden-hour shot suddenly becomes cold and blue.

**Root causes:**
- Lighting parameters are embedded in the motion layer instead of being locked in the visual anchor.
- Camera movement prompt inadvertently redefines the light source.
- Different shots use inconsistent quality anchors or film stock references.

**Fixes:**
- In multi-shot projects, use the keyframe-first contract: put all lighting in Stage 1 (T2I) and exclude it from Stage 2 (I2V).
- In the continuity bible, state the light source position and color as invariants: `主光始终来自画面左上方30°、色温5600K暖白`.
- Use a consistent film stock or rendering engine across all shots: pick one and note it in the bible.
- Add an explicit constraint: `运镜不改变光源方向或色调基准`.

**Alternate route:** Generate a single hero frame that defines the lighting, then use it as the first-frame reference for all shots in the sequence.

---

### 5. Camera instruction ignored (镜头指令失效)

**Symptom:** The requested camera movement does not appear in the output. A `dolly zoom` produces a static shot. An `orbit` becomes a simple pan. The camera drifts in an unintended direction.

**Root causes:**
- English camera terms triggered a content-safety false positive (e.g., bare `Dolly`, `Crane`, `Aerial` misread as names/brands).
- Camera instruction is buried deep in a long prompt and loses attention weight.
- Camera movement conflicts with the described action or scene geometry.

**Fixes:**
- Use Seedance-safe phrasings from `cinematography.md`: `推轨推进` / `dolly tracking shot` instead of bare `Dolly`.
- Move camera instructions to a prominent position — either immediately after the one-line concept or as the first element of each timestamp beat.
- Ensure the camera path is physically possible in the described space. A 360° orbit requires enough room around the subject.
- Reduce prompt length if it exceeds the model's effective attention window. Consolidate redundant descriptions.

**Alternate route:** Provide a video reference that demonstrates the desired camera movement and bind it with `@视频N仅参考运镜轨迹`.

---

### 6. Timeline compression (时间线压缩)

**Symptom:** Events that should take 15 seconds are crammed into 5 seconds. Actions feel rushed and incomplete. Some described events are skipped entirely.

**Root causes:**
- Too many events are packed into the available duration.
- Time allocation does not match the physical reality of the described actions.
- Timestamps are present but intervals are unrealistically short for the described content.

**Fixes:**
- Apply the time-budget method from `long-form-storytelling.md`: establishment 10–15%, development 25–35%, turn 10–20%, climax 20–30%, resolution 10–20%.
- Count the number of distinct actions per timestamp beat. More than 2–3 actions in a 5-second window risks compression.
- Extend the total duration or reduce the number of events to fit the time budget.
- For critical moments (emotional turns, reveals), allocate at least 3–5 seconds of dedicated screen time.

**Alternate route:** Split the narrative into two generations with a planned handoff point, rather than forcing everything into one prompt.

---

### 7. Reference contamination (素材污染)

**Symptom:** Unwanted attributes from a reference asset bleed into the output. A video reference's background replaces the intended scene. A voice reference's content overrides the scripted dialogue. A character reference's clothing appears on the wrong character.

**Root causes:**
- The reference binding lacks explicit exclusions.
- `完全参考@视频1` gives the model no signal about what to ignore.
- Two references provide conflicting attributes for the same dimension (e.g., two different scene backgrounds).

**Fixes:**
- Every reference must have the three-field binding from `multimodal-references.md`: what transfers, where it applies, and what does not transfer.
- Replace vague bindings: `参考@视频1` → `参考@视频1的手部拉花动作（08–14秒）；不迁移人物外貌、背景、音轨和字幕`.
- When two references conflict, declare explicit priority: `场景以@图片2为准；发生冲突时@图片2优先`.
- For voice references, always separate role: `@音频1仅参考声线，不作为BGM`.

**Alternate route:** Reduce the number of references. If contamination persists with 5+ references, simplify to 2–3 essential references and describe the rest in text.

---

### 8. Looping / freezing (循环 / 静止)

**Symptom:** The character repeats the same 2–3 second motion on a loop. Or the character freezes entirely while the camera continues to move. The video feels stuck.

**Root causes:**
- The prompt describes a static state without any progression or causality.
- Action description is a single pose rather than a sequence with beginning, middle, and end.
- Duration is too long for the amount of described content, leaving the model with nothing to generate.

**Fixes:**
- Ensure every beat has a state change: something must be different between the first and last frame.
- Describe actions as processes, not states: `她的手从桌面缓慢滑向信封边缘，指尖停在封口处` instead of `她的手放在桌上`.
- For long holds or contemplative moments, add micro-actions: breathing rhythm, subtle eye movement, wind in hair, environmental motion.
- Match content density to duration: at least one new action or change per 3–5 seconds.

**Alternate route:** Shorten the generation to match the content density, then use video extension to add more content in a second pass.

---

## Complexity-to-success guidance

Not all shots are created equal. The following rough hierarchy reflects typical first-generation success rates, from highest to lowest:

| Complexity tier | Example | Relative success rate | Recommendation |
|---|---|---|---|
| Tier 1: Static environment | Landscape, architectural interior, product hero | Highest | Reliable for single-pass generation |
| Tier 2: Single subject, simple action | One person walking, turning, sitting | High | Standard prompt usually sufficient |
| Tier 3: Single subject, complex action | Dance, martial arts, detailed hand work | Medium | Use intensity modifiers and causal chains |
| Tier 4: Multi-subject, simple interaction | Two people talking, walking together | Medium | Use role ledger and position tracking |
| Tier 5: Multi-subject, complex interaction | Fight, ensemble dance, crowd | Lower | Consider keyframe-first or white-model pipeline |
| Tier 6: Extreme physics | Explosions, fluid, destruction, fast vehicles | Lowest | Use VFX anchors and test with short clips first |

**For long-form projects:** Start with a simplified test prompt (fewer actions, shorter duration) to validate the baseline before adding complexity. This avoids wasting compute on an elaborate prompt that fails due to a fundamental constraint.
