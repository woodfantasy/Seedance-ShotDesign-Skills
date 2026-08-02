# Seedance 2.5 Long-Form Storytelling

Use this guide for continuous 30–180 second generation, narratively dense 30-second work, and long one-take designs. It turns duration into a continuity plan instead of a pile of unrelated short prompts.

## Contents

- Choose the long-form route
- Build the continuity bible
- Allocate time by story function
- Design acts and sequences
- Control character and world state
- Direct long takes
- Design dialogue and sound
- Close the narrative
- Validate the result

## Choose the long-form route

| Target | Preferred route | Reason |
|---|---|---|
| Exactly 30s, precise commercial/short-film control | Standard generation | Uses the full standard window with detailed timestamps |
| 31–180s continuous story with no approved base clip | 超长视频 | One continuous generation plan and unified state |
| Continue a source clip worth preserving | 视频延长 | Original clip remains intact; instructions govern the added interval |
| More than 180s or episodic approval is required | Planned segments | Each segment has a deliberate handoff and its own acceptance gate |

Do not split merely because the request exceeds 15 seconds. Do not use extension as a substitute for ultra-long generation when there is no meaningful source clip.

## Build the continuity bible

Write a compact bible before the timeline. Include only invariants that matter across several sequences.

```text
【角色 Bible】
林澈：28岁，短黑发，左眉浅疤，深蓝旧夹克；右手戴银戒；始终背棕色帆布包；声音克制偏低。

【场景 Bible】
废弃海边车站：候车室在轨道北侧，出口朝东，海在南侧；傍晚逐渐入夜；主光始终来自西侧落日。

【道具与状态】
纸质车票最初在林澈右手，00:42放入口袋，01:18交给女孩；除非时间轴说明，不得重置。
```

Track five state groups:

1. identity: face, hair, age, body scale, voice;
2. wardrobe and props: exact ownership, hand, condition, and location;
3. geography: entrances, exits, screen direction, light source, weather;
4. story knowledge: what each character knows and when it changes;
5. audio state: music motif, ambience, dialogue language, silence.

## Allocate time by story function

Start with a time budget, not a shot count. A practical default is:

| Function | Typical share | Purpose |
|---|---:|---|
| Establishment | 10–15% | Establish person, place, objective, and visual grammar |
| Development | 25–35% | Add causal actions and escalating obstacles |
| Turn | 10–20% | Change knowledge, goal, relationship, or physical state |
| Climax | 20–30% | Deliver the highest visual, emotional, or informational load |
| Resolution | 10–20% | Show consequence, recover motifs, and create a true endpoint |

Adjust the shares for genre. Ads usually establish faster and reserve more time for demonstration and payoff. Suspense may delay the turn. Music videos may use motif evolution instead of conventional plot.

## Design acts and sequences

Use acts for narrative function and timestamps for execution. For 60–180 seconds, prefer 5–12 sequences rather than dozens of micro-shots.

```text
全片时长90秒，16:9，720p，现实主义悬疑短片。

【故事概述】错过末班车的女孩发现站务员一直在保护她免受看不见的追踪者接近。

[00:00-00:14] 建立：空间、人物目标、规则和声音线索。
[00:14-00:34] 发展：三次因果相连的行动，危险逐渐具体。
[00:34-00:50] 转折：一个物件或信息改变人物判断。
[00:50-01:14] 高潮：选择、行动、反作用；镜头能量达到峰值。
[01:14-01:30] 收束：展示后果，回收声音/道具母题，停在可理解的结局。
```

Every sequence should answer:

- What changes between its first and last frame?
- What causes that change?
- What state must carry into the next sequence?
- Which camera and sound choice makes the change legible?

Avoid repeated sequences that only restate atmosphere.

## Control character and world state

At each transition, carry forward a short state vector:

```text
交接状态：角色位于站台右侧、面向左前方、奔跑动量尚未停止；帆布包在左肩；车票仍在右手；雨势增强；镜头正向后移动；音乐在低频持续音上。
```

When a state deliberately changes, mark the cause and the new state:

```text
00:42，她因抓住栏杆停下，将车票塞入夹克右侧口袋；此后双手空出，车票不可重新出现在手中。
```

Use screen direction consistently. If geography requires crossing the axis, stage a visible neutral angle, character turn, or camera arc so the reversal reads as intentional.

## Direct long takes

A long take needs motivated camera handoffs. Divide it into spatial beats without pretending they are cuts.

```text
[00:00-00:18] 镜头在门外低机位跟随鞋步进入；人物推门产生前景遮挡，但不切镜。
[00:18-00:39] 利用门框遮挡自然升至肩后视角，继续向室内推进。
[00:39-00:58] 人物回头时镜头沿其左侧绕至正面，保持动作速度和光线方向连续。
```

Define entrance, path, obstacles, reveal point, and endpoint. Keep camera acceleration physically plausible. Use occlusion, motivated reframing, and subject turns to change composition.

## Design dialogue and sound

For each spoken line, bind speaker, language, exact wording, delivery, and subtitle state. Leave enough time for natural speech; do not crowd a long sentence into a two-second beat.

Treat sound as a parallel continuity track:

- ambience establishes space and may evolve with location;
- foley confirms contact and physical action;
- dialogue advances information or relationship;
- music follows structural energy rather than restarting every sequence;
- silence can mark a turn, but state exactly what remains audible.

Use recurring motifs sparingly. A train bell, breath rhythm, or three-note phrase can evolve across acts and return at the close.

## Close the narrative

Do not let the final interval become generic slow motion. Close at least two of these:

- objective: achieved, failed, or transformed;
- relationship: trust, separation, alliance, reversal;
- object: transferred, consumed, broken, revealed;
- space: exited, secured, transformed, revisited;
- motif: visual or audio element returns with changed meaning.

Specify the last stable image and audio tail. If the video is designed for a later extension, state a controlled open ending without pretending it is a full resolution.

## Validate the result

- Duration and aspect ratio are stated explicitly.
- The number of sequences matches the narrative complexity.
- Each sequence produces a causal state change.
- Character, prop, geography, lighting, and audio state never reset accidentally.
- Dialogue fits the allocated time and is bound to speakers and languages.
- Camera direction is physically traversable, especially in long takes.
- The climax has more consequence or energy than the establishment.
- The ending resolves or deliberately suspends the core objective.
- The prompt does not fragment a continuous request into obsolete 15-second units.
