# Seedance 2.5 Industrial Workflows

Use this guide for white-model pipelines, green-screen compositing, seamless video transitions, and multi-panel storyboard animation. These modes translate production artifacts into finished video while preserving structure.

## Contents

- Route the industrial task
- Rough white-model pipeline
- Fine white-model pipeline
- Green-screen compositing
- Seamless transitions
- Multi-panel storyboards
- Handoff and versioning
- Validate the result

## Route the industrial task

| Source artifact | Route | What should survive |
|---|---|---|
| Simple blockout / proxy animation | 粗颗粒白模 | Motion skeleton, path, staging, camera, basic occlusion |
| Detailed previs / rendered gray model | 细颗粒白模 | Geometry, animation timing, camera, light-change structure |
| Foreground on green background | 绿幕编辑 | Foreground identity, action, timing, clean edges |
| Two approved finished clips | 视频无缝转场 | Both clips unchanged; only bridge is designed |
| Storyboard sheet or comic panels | 多宫格分镜 | Panel order, composition, identity, narrative continuity |

Do not confuse a rough white model with a fine one. Rough mode reconstructs performance and appearance from a motion skeleton. Fine mode renders a more complete previs while removing production helpers.

## Rough white-model pipeline

### Extract the skeleton

Read the proxy as production data:

- character count and role mapping;
- start/end position, facing, and body path;
- complete limb actions and contact events;
- object ownership and handoffs;
- camera position, path, speed, and cut points;
- foreground/background occlusion;
- broad light or shadow changes.

### Map every proxy

```text
白模中的蓝色人形 → @图片1的女主，保持完整动作、站位和左手持物关系。
白模中的橙色人形 → @图片2的男主。
白模中的灰色立方体 → @图片3的旧木箱。
白模背景只提供空间尺度；最终场景使用@图片4。
```

### Rebuild appearance

Supply final identity, costume, prop, environment, material, lighting, atmosphere, and sound. Explicitly discard proxy artifacts:

```text
不要保留白模材质、纯灰背景、颜色编码、骨骼线、轨迹线、网格、相机锥体或未映射代理物。
```

If a proxy action is physically incomplete, fill preparation, contact, reaction, and recovery while preserving its timing and intent.

## Fine white-model pipeline

A fine white model usually contains reliable geometry and timing. Preserve:

- mesh silhouette and relative scale;
- camera and cut timing;
- animation and collision timing;
- scene layout and major shadows;
- planned VFX onset and transition points.

Add:

- final material assignments;
- texture scale and wear;
- environmental detail;
- light color, softness, volumetrics, and reflections;
- atmospheric and VFX finishing;
- final sound design.

```text
将@视频1的细颗粒白模渲染为写实科幻机库。几何结构、人物动画、机位和切镜时序不变。金属墙面为拉丝铝材，地面有轻微磨损和冷色反射；00:08警报灯由白转红，00:11蒸汽从右侧阀门喷出。去除全部坐标线、轨迹线、相机锥体、视口网格和调试文字。
```

State whether any material changes over time. Avoid accidental gray materials or viewport helpers in the final image.

## Green-screen compositing

### Bind layers

```text
前景：@视频1中的舞者，保留身份、服装、动作和时序。
背景：@视频2的夜间屋顶，只参考环境与镜头运动，不保留原人物。
```

### Match the composite

Control:

- perspective, camera height, horizon, and parallax;
- scale, ground plane, foot contact, and contact shadow;
- light direction, color temperature, softness, and exposure;
- foreground edge detail, motion blur, depth of field, and grain;
- environmental reflection, atmospheric integration, and spill removal.

```text
完全移除绿色背景、绿色溢色和半透明绿边；头发丝、纱料和快速运动边缘保持自然。根据背景左上方霓虹主光给前景添加同方向冷紫轮廓光，脚下生成与动作同步的柔和接触阴影。禁止边缘闪烁、贴片感、尺度漂移或背景滑动。
```

If foreground and background cameras move differently, pick one authoritative camera source and describe how the other layer should follow. Do not promise coherent parallax from incompatible paths without reconstruction.

## Seamless transitions

The source clips are approved assets. Do not rewrite either clip; design only the generated bridge.

### Audit boundaries

For @视频1's last usable frames and @视频2's first usable frames, note:

- dominant shape or occluder;
- subject position, scale, facing, and movement vector;
- camera movement and speed;
- light direction, color, texture, and exposure;
- audio energy and transition point.

### Choose one bridge mechanism

| Mechanism | Best anchor |
|---|---|
| Occlusion wipe | Person/object fills frame |
| Match cut | Similar shape, pose, composition, or color |
| Motion continuation | Shared direction and speed |
| Focus transition | Blur/bokeh expands then resolves |
| Light/color bridge | Flash, shadow, smoke, or color field |
| Morph with physical cause | Material or object visibly transforms |

### Specify A → bridge → B

```text
不修改@视频1和@视频2。@视频1尾帧中红伞从画面右侧向左移动并完全遮住镜头；桥接段保持伞面红色纹理、速度和方向，近景红色逐渐变为@视频2首帧的红色剧院幕布；幕布继续向左拉开，显露@视频2原首帧。连接点无黑屏、跳帧、硬切、闪烁、速度突变或主体变形。
```

If source audio matters, define the crossfade or exact sound bridge. A visual match with an abrupt audio reset is not seamless.

## Multi-panel storyboards

First decide whether one image is a sheet or each image is a separate panel. Map reading order explicitly.

```text
@图片1是一张2×3六宫格分镜，阅读顺序为左上→右上→左中→右中→左下→右下。每格是一个完整镜头，不是同一画面的拼贴元素。
```

For each panel, record:

- subject identity and position;
- shot size, angle, and composition;
- action state and story function;
- camera move or static hold;
- connection to the next panel;
- dialogue, ambience, or effect.

```text
镜头1（00:00–00:04）：还原左上格的远景构图，补全人物走入的动作。
镜头2（00:04–00:09）：通过人物抬手遮挡连接至右上格近景；身份、服装和光向不变。
```

The platform may accept up to 30 image files, but that is not a requirement to use many panels. More than five important subjects should preferably use separate single-view identity images. State which asset defines identity versus panel composition.

## Handoff and versioning

For production review, include:

- selected route and source version;
- asset map with exact tokens;
- invariant list;
- timestamped prompt;
- expected boundary frames or edit scopes;
- known risk and fallback route.

Use staged passes when one generated result becomes the approved source for a later operation, such as fine white-model rendering followed by local edit, or green-screen composite followed by BGM separation. Do not combine passes when their preservation requirements conflict.

## Validate the result

- Rough/fine white-model route matches the source fidelity.
- Every proxy character and object is mapped or explicitly discarded.
- Final prompt removes helper geometry, gray materials, and debug text.
- Green-screen foreground/background roles, perspective, light, shadow, edges, and parallax are controlled.
- Seamless transition preserves both original clips and defines a single bridge anchor.
- Multi-panel order, panel timing, character mapping, and connections are explicit.
- All asset counts and source durations pass `seedance-specs.md`.
- Compound pipelines have clear pass boundaries and approved intermediates.
