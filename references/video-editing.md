# Seedance 2.5 Video Editing

Use this guide for smart editing, advanced annotation-based editing, local replacement/removal, spatial viewpoint modification, BGM separation, and edits that must preserve everything outside a narrow target.

## Contents

- Select the editing mode
- Use the edit contract
- Locate the target
- Describe A→B transformation
- Build the preserve list
- Remove and inpaint
- Add or replace elements
- Modify viewpoint
- Separate BGM
- Combine edits safely
- Validate the edit

## Select the editing mode

| Intent | Route | Core control |
|---|---|---|
| Replace, add, remove, restyle, or rewrite a clear object/region | 智能编辑 | Object + change + time + preserve list |
| Use red boxes, arrows, landmarks, or boundary lines | 高级编辑 / 视频编辑 | Annotation side/region + edit contract |
| Reconstruct camera position or POV | 空间视角修改 | Target viewpoint + spatial invariants |
| Remove music but retain speech and visuals | 音轨编辑 | Audio stem preserve/remove list |

For editing stability, source videos of 20 seconds or less are recommended. Image references used for editing are most stable at 1–5; 6–8 may reduce stability. These are guidance bands, not hard platform rejection limits.

## Use the edit contract

Every edit must state:

```text
编辑对象：什么对象、人物、区域或音轨。
定位方式：时间 + 空间/标注位置。
变化：原状态A → 目标状态B。
生效范围：全片、渐变区间或精确时间段。
保持不变：所有未授权修改的内容。
补全规则：删除区域、遮挡关系、光线、透视、材质或声音如何恢复。
```

Weak: `把杯子换掉。`

Strong:

```text
编辑@视频1。将桌面右侧、人物右手旁的白色陶瓷杯从00:04起替换为透明矮玻璃杯；杯子位置、尺寸和运动轨迹保持一致，匹配窗外左侧来光和桌面接触阴影。人物、手指遮挡关系、桌面、镜头、对白与其余画面不变。
```

## Locate the target

Use at least two of these when ambiguity is possible:

- semantic identity: `穿蓝夹克的男子`;
- spatial relation: `画面右下、木桌上`;
- temporal range: `00:06–00:11`;
- interaction: `被女主左手拿起的`;
- annotation: `红框内`, `蓝色箭头指向`, `地标点处`, `红线左侧`.

For annotations, always name the intended side or enclosed region. A line alone does not tell the model which side to modify.

```text
只修改红线左侧的天空区域；红线右侧城市、人物、道路和车辆全部保持不变。
```

## Describe A→B transformation

State both origin and destination. This reduces accidental reinterpretation.

```text
灰色阴天 → 夕阳后的深蓝暮色
完整路牌 → 移除路牌并补全被遮挡的砖墙
红色棉质外套 → 深绿色防水风衣，剪裁与褶皱运动保持一致
固定正面机位 → 角色右后方低机位跟拍
有BGM的混合音轨 → 仅保留对白、呼吸和现场环境音
```

If change is gradual, define its onset, progression, and completed state.

## Build the preserve list

The preserve list is the editing equivalent of continuity direction. List only relevant invariants, but be explicit.

Categories:

- subject: identity, face, hair, body, costume outside edited area;
- performance: action timing, gaze, lip sync, hand-object contact;
- world: background, geometry, weather, lighting direction;
- image: composition, camera motion, frame rate feel, depth of field, color;
- audio: dialogue, voice timbre, ambience, foley, music;
- graphics: subtitles, logos, or text that must remain—or must be removed.

Do not write `其他不变` as the only preservation instruction for a high-risk edit.

## Remove and inpaint

Removal requires a reconstruction rule:

```text
移除00:03–00:09画面左侧墙上的海报，并根据周围旧砖墙的砖缝、风化纹理、透视和右上方暖光自然补全。人物经过时保持其身体轮廓和遮挡关系，不出现模糊补丁、纹理重复、边缘闪烁或残留文字。
```

For moving objects, specify whether shadows, reflections, footprints, or sounds caused by the object should also be removed.

## Add or replace elements

New elements must inherit scene physics:

- perspective and scale;
- contact point and shadow;
- light direction, softness, color temperature;
- occlusion and reflection;
- motion path, acceleration, and interaction timing;
- matching grain, sharpness, depth of field, and color grade.

For replacement using an image, name which attributes to take from it and what not to import.

```text
将@视频1中的背包替换为@图片1的棕色帆布包，只参考包的外形、材质和肩带结构，不带入@图片1的手、背景和光线。
```

## Modify viewpoint

Viewpoint modification reconstructs unseen space; it is not a simple crop.

```text
将@视频1的正面固定机位改为人物右后方45度、腰部高度的缓慢跟拍。保持人物身份、原动作时序、房间布局、门窗相对位置、物体比例和左侧窗光方向不变。根据原空间关系自然补全新视角看见的桌后区域，不新增无关家具，不改变人物路线和接触事件。
```

Define target angle, height, distance, lens feel, movement path, and invariants. If the requested viewpoint contradicts known geometry, flag the tradeoff instead of promising exact preservation.

## Separate BGM

Treat audio as stems:

```text
移除：全部背景音乐，包括片头淡入与片尾残响。
保留：人物对白、笑声、呼吸、脚步、衣料摩擦、室内空调底噪。
禁止：改变人声音色、语气、声场、口型同步；添加新音乐、新音效或降噪水波感。
画面：人物、动作、字幕、构图、画质和色调完全不变。
```

If the user asks for silent output, clarify whether all stems—including dialogue and ambience—must be removed. Do not infer total silence from `去掉音乐`.

## Combine edits safely

Compound edits are allowed when their targets do not conflict. Number them and give each its own scope.

```text
编辑1（00:02–00:08，红框内）：移除广告牌并补全砖墙。
编辑2（全片，音轨）：移除BGM，保留对白和环境音。
全局保持：人物、动作、镜头、字幕、砖墙以外背景和色调不变。
```

Split into separate passes when:

- two edits require incompatible preservation rules;
- viewpoint reconstruction and fine local inpainting compete for geometry;
- the result of the first edit is needed as the stable source for the second;
- the user needs independent approval or rollback.

## Validate the edit

- The primary mode matches the requested change.
- Source token and effective time range are present.
- Target has semantic, spatial, temporal, or annotated localization.
- Original A and desired B are both explicit.
- Preserve list covers likely collateral damage.
- Removal includes reconstruction of texture, geometry, shadow, reflection, and sound where relevant.
- Addition/replacement matches perspective, lighting, occlusion, material, and motion.
- Viewpoint modification preserves action timing and coherent scene geometry.
- BGM removal distinguishes music from speech, ambience, and foley.
- Compound edits have non-conflicting scopes or are intentionally staged.
