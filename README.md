English | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md)

# 🎬 Seedance2.0 Shot Design — Cinematic Shot Language Designer

[![Version](https://img.shields.io/badge/version-1.8.4-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT--0-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Seedance_2.0-purple.svg)]()

> Turn your vague video ideas into **cinema-grade video prompts** ready for Jimeng Seedance 2.0 — in one shot.

A Claude Skill built on the [Agent Skills](https://agentskills.io) specification, blending Hollywood-level cinematography aesthetics with Chinese film industry practices. It's designed to help creators break free from the "looks nice but random" AI video trap and achieve **precise, controllable visual storytelling**.

---

## ✨ Core Capabilities

| Capability | Description |
|------------|-------------|
| 🎭 **AI Comic Drama & Short Drama Production** | Full-pipeline support for AI comic strips (漫剧) and AI short dramas — character dialogue / voiceover / actor blocking / exaggerated expression close-ups / narrative-motivated camera / short drama style quick-selector / 4 prompt template variants (CN/EN × dialogue/voiceover), with dedicated scenario templates and complete examples |
| 🎨 **28+ Director & Style Presets** | Nolan / Villeneuve / Fincher / Deakins / Kurosawa / Makoto Shinkai / Wong Kar-wai / Zhang Yimou / Xianxia / Cel-Shaded CG / Anime / Xiaohongshu… |
| 🎬 **Pro Camera Movement Dictionary** | 3-tier camera system + 14 focal lengths + 6 focus controls + 7 physical mounts, with bilingual CN/EN references |
| 💡 **Three-Layer Lighting Structure** | Light Source → Light Behavior → Color Tone — no more vague "add a light" |
| 📐 **Timestamped Storyboarding** | `0-3s / 3-8s / …` precise timeline control to prevent visual bleeding between shots |
| 🎯 **Six-Element Precision Assembly** | Subject / Action / Scene / Lighting / Camera / Sound — a structured, high-conversion formula |
| 🎬 **Smart Multi-Segment Storyboard** | Videos >15s are automatically split into independent prompt segments with unified style, lighting, sound, and seamless transition frames |
| 📦 **20 Scenario Templates** | E-commerce / Xianxia / Short Drama / Food / MV / One-Take / Automotive / Macro / Nature / Game PV / Horror / Travel / Pets / Transformation / Loop / Video Editing / Video Extension / Story Completion / Multiframe Storytelling |
| 🎵 **Sound & ASMR Vocabulary** | Physics-based onomatopoeia library covering ambient / action / vocal / music sounds |
| 🎤 **Voice & Language Control** | Timbre cloning via video reference, dialect/accent control (Sichuan/Cantonese/Northeast/Taiwanese etc.), multilingual dialogue mixing, special voice styles (documentary/stand-up/opera/ASMR) |
| 📹 **Multimodal Reference Guide** | 6 core reference patterns (first frame / camera replication / action replication / camera+action separation / timbre reference / effect replication), multi-asset character control, consistency preservation |
| 🌐 **Bilingual Prompt Output** | Chinese users → Chinese prompts, non-Chinese users → English prompts, auto-detected |
| 🛡️ **Copyright-Safe IP Fallback** | Three-tier progressive IP fallback strategy to prevent platform content blocks |
| 🔍 **Structured Hard Validation** | Word count / camera moves / temporal logic / filler detection / optical physics conflicts / style conflict matrix — 7-rule checklist applied before every delivery |

---

## 🚀 Quick Start

### 1. Install the Skill

<details>
<summary><b>Claude Code</b></summary>

Place the `seedance-shot-design/` folder under `.claude/skills/` in your project root:

```bash
# Clone into your project's Skill directory
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git .claude/skills/seedance-shot-design
```

Claude Code will automatically detect and load the Skill.
</details>

<details>
<summary><b>OpenClaw</b></summary>

In your connected IM app (WeChat, Feishu, etc.), send a message to the OpenClaw Agent:

```
Please learn this skill: https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills
```

The Agent will fetch and learn the Seedance Shot Design skill automatically. You can start making requests right away.
</details>

<details>
<summary><b>Codex</b></summary>

Place the Skill folder under Codex's agents instruction directory:

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git agents/skills/seedance-shot-design
```

Then invoke it within a Codex conversation.
</details>

<details>
<summary><b>Cursor</b></summary>

Place the Skill folder under `.cursor/skills/` in your project root:

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git .cursor/skills/seedance-shot-design
```

Cursor Agent mode will automatically read the Skill instructions.
</details>

### 2. Usage

Just tell Claude:

```
Write a 15-second cyberpunk rain chase video prompt
```

The Skill auto-activates and generates the prompt through a 5-step workflow:
1. **Requirement Analysis** — Confirm duration / aspect ratio / assets / style
2. **Visual Diagnosis** — Select camera language & director style
3. **Six-Element Assembly** — Compose the prompt using the structured formula
4. **Mandatory Validation** — Apply 7-rule structured validation checklist
5. **Professional Delivery** — Director's statement + complete prompt

### 3. Examples

#### Full Interaction Demo

**User Input:**
```
Write a 10-second Eastern Xianxia short film video prompt
```

**Skill Output:**

> **Seedance Video Prompt**
>
> **Theme**: A young man in white catches a red leaf in a misty ancient temple at dawn, reaching enlightenment
>
> **Director's Statement** (for creative intent only — do not copy):
> Uses an aerial → dolly → slow push three-phase camera progression, transitioning from grand vista to intimate emotion.
> 35mm film grain adds a handcrafted texture, and the gold-teal palette echoes the Eastern philosophy of harmony with nature.
>
> **Full Prompt** (copy directly into Jimeng's input field):

```
10-second Chinese fantasy, realistic Eastern cinematic look, gold-teal palette, ethereal ambient sound.
0-3s: High-angle aerial shot of an ancient temple amid clouds, slow aerial push, morning mist drifting through valleys, distant bell faintly ringing, Tyndall light beams piercing through cloud layers.
3-7s: Dolly push through the temple gate into the courtyard, a young man in white raises his hand to catch a falling red leaf, 35mm film grain texture, shallow depth of field focusing on hand details.
7-10s: Close-up of the young man looking up, slow push-in, wind rises, sleeves and hair sweep to the right side of frame, spiritual light spiraling upward in the courtyard.
Sound: Ambient sound contracts into a single clear sword ring.
Forbidden: Any text, subtitles, logos, or watermarks
```

#### More Use Cases

```
# AI Comic Drama
Write a 10-second AI comic-style bossy CEO short, vertical 9:16, with dialogue and exaggerated close-up expressions

# E-commerce Ad
Write an 8-second luxury watch product ad video prompt, 9:16 vertical

# Short Drama Dialogue
Write a 12-second plot-twist short drama scene with dialogue

# One-Take
Write a 15-second one-take museum walkthrough video prompt

# With Reference Assets
I've uploaded 3 character design images and 1 reference video — generate a 15-second Xianxia fight scene
```

---

## 📁 Project Structure

```
seedance-shot-design/
├── SKILL.md                     # Core instructions (the Skill's brain)
├── README.md                    # This file
├── scripts/
│   ├── validate_prompt.py       # Industrial-grade prompt validation script
│   └── test_validate.py         # Validation script test cases
└── references/
    ├── cinematography.md        # Camera & focal length dictionary (incl. physical mounts & focal psychology)
    ├── director-styles.md       # Director style parameterized mapping (28+ styles, incl. Cel-Shaded CG)
    ├── seedance-specs.md        # Seedance 2.0 official platform specs
    ├── quality-anchors.md       # Quality anchors & lighting library (incl. NPR materials / lighting / conflict matrix)
    ├── scenarios.md             # Vertical scenario templates (20 scenarios + anime variants + video editing + physics damping toolkit)
    └── audio-tags.md            # Audio & sound effect tag specs (incl. spatial acoustics & material-based onomatopoeia)
```

---

## 🔬 Validation Script (Standalone Developer Tool)

A standalone Python validation tool for developers and CI/CD pipelines. The AI agent applies these same rules natively via its built-in 7-rule validation checklist — no Python execution required during prompt generation.

```bash
# Validate text directly
python scripts/validate_prompt.py --text "your prompt"

# Validate from file
python scripts/validate_prompt.py --file prompt.txt

# Specify language (auto=auto-detect, cn=Chinese, en=English)
python scripts/validate_prompt.py --text "your prompt" --lang en

# JSON output (for programmatic processing)
python scripts/validate_prompt.py --text "your prompt" --json
```

**Validation Checks (v1.5):**
- ❌ Over word limit (Chinese >500 chars / English >1000 words)
- ❌ Missing professional camera terminology
- ❌ Filler word hard-block (masterpiece / ultra-clear, etc. → error)
- ❌ Optical physics conflicts (ultra-wide + bokeh, handheld + perfect symmetry)
- ❌ Style conflict matrix (IMAX vs VHS, film vs digital, ink-wash vs UE5, Cel-Shaded vs realistic PBR, Slow Motion vs Speed Ramp)
- ❌ Asset reference overflow (images >9 / videos >3 / audio >3 / total >12)
- ❌ Long video (>5s) without time-slice hard-block
- ⚠️ Time-slice gaps or overlaps
- ⚠️ Declared duration vs slice endpoint mismatch
- ⚠️ In-segment motion logic conflicts
- ⚠️ Seedance review-risk bare English camera terms detection (Dolly / Aerial / Crane / Pan / Arc / Dutch / Steadicam)
- 🌐 Auto language detection (Chinese / English), adapting length standards & detection strategies per language
- 🎬 Multi-segment cross-segment consistency checks (style preamble / lighting structure / forbidden items)

**Run Tests:**
```bash
python -m unittest scripts.test_validate -v
# 54 tests pass (covering 11 test classes)
```

---

## 🏗️ Design Philosophy

### Progressive Knowledge Loading (Progressive Disclosure)

Following Agent Skills best practices:

- **SKILL.md** (~4000 tokens): Core workflow + structural templates + quality checklist
- **references/** (three-layer routing): Camera dictionary and quality anchors are always loaded (Always-On); other knowledge bases auto-matched via semantic inference or loaded on explicit user request
- **scripts/** (executed on demand): Validation runs only after prompt generation

### Competitive Advantages

| Dimension | Common Approach | This Skill |
|-----------|----------------|------------|
| Compliance | Plain-text suggestions | **Python hard validation (incl. optical / style conflict matrix + review safety detection)** |
| Director Styles | International directors only | **International + Chinese + Short Drama + AI Comic + Social Media + Anime + Cel-Shaded CG + Xiaohongshu** |
| Scene Coverage | Biased toward epic films | **17 vertical scenarios + anime variants + video editing + physics damping toolkit** |
| Sound Design | Brief mentions | **Spatial acoustics + material-based onomatopoeia library** |
| Lighting | "Add a light" | **Source → Behavior → Tone three-layer + lighting recipes + material library** |
| Multilingual | Chinese only | **Chinese / English bilingual output, auto language detection** |
| Review Safety | Not considered | **Camera term disambiguation rules + bare-word auto-detection** |

---

## 📋 Changelog

### v1.8.4 (2026-04-08)
- 🔗 **CLI Integration Guide**: New `seedance-specs.md` section mapping Shot Design modes to Jimeng CLI commands (`text2video` / `image2video` / `multiframe2video` / `multimodal2video`), with async task management and VIP channel documentation
- 🎞️ **Multiframe Storytelling Template**: New scenario template (#20) for `multiframe2video` — upload 2-9 keyframe images and let the engine auto-compose a coherent story video. Includes decision matrix for choosing between multiframe vs. multi-segment storyboard
- 📚 **Knowledge Base Routing**: Added multiframe and CLI routing entries to Step 2 semantic inference table

### v1.8.3 (2026-04-08)
- 🎭 **Descriptive Over Narrative Rule**: New core rule (#12) — only write what the camera SEES (visual words), never what characters FEEL (emotion words). All emotions must be converted to visible physical expressions (facial micro-expressions, body language, breathing rhythm, gaze direction)
- ✍️ **English Present Progressive**: Assembly rules now mandate `-ing` form for English action descriptions (`running` not `runs`) — progressive tense implies continuous motion, matching video's dynamic nature
- 🎯 **Motion Tone Front-Loading**: Style preamble now explicitly declares overall motion energy (e.g., `dynamic motion, high energy` or `serene, slow-paced atmosphere`) to lock motion baseline early in generation

### v1.8.2 (2026-04-07)
- 🎥 **One-Shot-One-Move Rule**: New core rule (#10) enforcing a single camera movement per time segment — combining movements (e.g., push-in + pan) causes jitter. Subject motion and camera motion must be described separately
- 🖼️ **I2V Golden Rule**: New core rule (#11) and dedicated I2V section — when generating video from an image, only describe motion/changes, never re-describe static content already in the first frame. Introduces `preserve composition and colors` anchor phrase
- 📏 **Optimal Prompt Length**: Added 60–100 word sweet spot guidance — below is vague, above causes concept drift and conflicting instructions
- 💪 **Motion Intensity Modifiers**: New bilingual quick-reference table in cinematography dictionary with 6 intensity tiers (violent → gentle → gradual) and do/don't examples to eliminate "mushy motion"
- 🎤 **Rhythm Over Specs**: Assembly rules now explicitly prefer semantic rhythm words (gentle/gradual/smooth) over technical parameters (24fps/f2.8) that Seedance cannot parse
- 🎬 **Reference Video Best Practices**: New practical constraints for reference clips — ideal 3–8s length, continuous shot (no cuts), single intent (subject OR camera, not both)

### v1.8.1 (2026-04-07)
- 🛡️ **Security Compliance**: Resolved ClawHub OpenClaw "Suspicious patterns" flag by converting Python-based validation to LLM-native structured 7-rule validation checklist. Python scripts remain as standalone developer tools but are no longer executed by the agent
- 🎯 **Trigger Phrase Optimization**: Reduced activation trigger phrases from 40+ to 15 high-signal professional terms, lowering unintended activation surface while preserving core discoverability

### v1.8.0 (2026-04-05)
- 🎤 **Voice & Language Control System**: New timbre cloning via video reference (`语气和音色参考@视频1`), dialect/accent control (Sichuan/Cantonese/Northeast/Taiwanese etc.), multilingual dialogue mixing, special voice styles (documentary narration / stand-up comedy / opera / ASMR)
- 📹 **Multimodal Reference Guide**: Upgraded from 4 brief tips to a structured guide with 6 core reference patterns (first frame / camera replication / action replication / camera+action separation / timbre reference / effect replication), plus multi-asset character control and consistency preservation guidance
- 📏 **Video Extension Scenario**: New forward/backward extension templates, seamless continuation techniques, duration cognition correction (generation duration = added seconds, not total)
- 📋 **Story Completion Scenario**: New storyboard-to-video, comic panel animation, and image-to-emotion-video creative modes
- 🎬 **Creative Effects Quick Reference**: New VFX trigger keywords — Hitchcock zoom, fisheye lens, particle effects, speed ramp, freeze transition, ink wash style, morphing effects (bilingual)
- 🎭 **Emotion Performance Guidance**: New emotion specificity table, emotion transition trigger words, emotion reference video usage in short drama chapter

### v1.7.2 (2026-04-02)
- 🎯 **Trigger Word Expansion**: Massively expanded Skill activation coverage — added 20+ colloquial Chinese triggers (帮我写个视频, 拍一个, 做分镜, 短视频, AI视频, 抖音视频, vlog, 运镜...) and 10+ English triggers (generate a video, make a clip, shoot a scene, video script, drone shot, camera movement...) so the Skill auto-activates on natural, everyday user expressions — not just professional terminology

### v1.7.1 (2026-03-29)
- 🔒 **Security Compliance Optimization**: Resolved ClawHub security flagging issues for shell execution, process control, and file access patterns while maintaining full functionality

### v1.7.0 (2026-03-28)
- 🚨 **Step 3 Mandatory Assembly Rules**: Three-layer lighting must be on its own line with all three layers complete; SFX line must start with `SFX:`; prohibition line standardized (no custom additions); freestyle non-template sections forbidden
- ⛔ **Step 4 Validation Blocking**: Prompts failing validation are now forbidden from being shown to users; clear 5-step validation flow
- 📋 **Step 5 Format Enforcement**: Output must follow template exactly (Theme + Director's Note + code-block-wrapped prompt); missing any section = non-compliant
- 🎯 **Step 2 Parameter Extraction Directive**: Knowledge bases must not just be "loaded" — specific parameters must be extracted and embedded into the prompt

### v1.6.0 (2026-03-28)
- 🧠 **Smart Semantic Intent Routing**: Step 2 knowledge base loading upgraded from "explicit trigger" to three-layer routing — Always-On loads camera dictionary & quality anchors every time, Semantic Intent Inference auto-detects needed knowledge bases from user's natural language, Explicit Override preserves direct user specification
- 🎯 **Step 1 Smart Inference Principle**: Agent proactively infers parameters (duration / style / scene) from a single user sentence, only asking about genuinely unknown info, limiting follow-up questions to 1-2
- 📝 Design philosophy updated from "loaded on demand" to "three-layer routing" ensuring every prompt has a quality foundation

### v1.5.0 (2026-03-27)
- 🎭 **Actor Blocking System**: Three-element positioning (placement + face direction + gaze focus) with emotion modifier vocabulary for multi-character scenes
- 🎙️ **Voiceover / Dialogue Split**: Distinct templates for on-screen dialogue vs. off-screen voiceover / inner monologue, with anti-lip-sync directive for VO scenes
- 📐 **Camera Angle Specificity**: Vague → specific angle mapping (e.g., "close-up" → "over-shoulder medium close-up, focus on listener") with 5 comparison pairs
- 🎬 **Narrative-Motivated Camera Movement**: Camera moves now paired with storytelling purpose (e.g., "slow push-in — revealing inner turmoil")
- 🔀 **Segment Transition Strategy**: 6 transition types (gaze continuity / emotional escalation / contrast cut / spatial leap / temporal ellipsis / sensory bridge) for multi-shot coherence
- 🎨 **Short Drama Style Quick-Selector**: 4-dimension combo system (visual type × render style × color tone × genre)
- 📝 Short drama prompt templates expanded from 1 to 4 variants (CN dialogue / CN voiceover / EN dialogue / EN voiceover)
- 📝 Multi-segment Director's Note template adds transition strategy declaration
- 📝 5 complete short drama examples covering: plot-twist dialogue / voiceover monologue / action conflict / 2D anime / transition strategy
- ✅ 54 tests pass

### v1.4.0 (2026-03-21)
- 🎬 **Smart Multi-Segment Storyboard**: Videos >15s auto-split into multiple independent prompts (each ≤15s, min ≥8s)
- 📝 Multi-segment coherence: unified style preamble / three-layer lighting / sound design / transition frames / forbidden items
- 📝 Step 5 adds multi-segment output format template (CN / EN)
- 📝 New 60-second desert Kali/Escrima 4-segment full example
- 🔧 Validation script adds `validate_multi_segment()` cross-segment consistency check
- ✅ 54 tests pass (incl. 4 new multi-segment validation tests)

### v1.3.0 (2026-03-21)
- 🌐 **Bilingual Prompt Output**: Chinese users → Chinese, non-Chinese → English, with auto language detection
- 📝 All structural templates, delivery formats, and multimodal tips now include English versions
- 🛡️ **Camera Term Disambiguation (Rule 9)**: Chinese uses Chinese camera terms, English uses full phrases — avoids Seedance review false positives
- 🔧 Validation adds `check_ambiguous_terms()` bare-word detection + `--lang` flag + English word-count length check
- 🔧 New Slow Motion vs Speed Ramp conflict detection
- 🔧 `detect_language()` expanded with CJK Extension A + full-width punctuation support
- 📚 `cinematography.md` adds "Seedance Safe Phrasing" column
- ✅ 50 tests pass (incl. bilingual + review safety tests)

### v1.2.0 (2026-03-21)
- 🎨 **Cel-Shaded CG Style**: New complete four-axis parameterized entry (distinct from anime's explosive energy — positioned for contemplative narrative)
- 🧱 **Anime / NPR Material Library**: Anime skin / hair / cartoon metal / cartoon fabric — 4 non-photorealistic materials
- 📦 **Anime Game PV Variant**: Scenario template adds Cel-Shaded sub-template + ice-attribute character example
- ⚠️ Conflict matrix adds: Cel-Shade vs Realistic PBR material
- 🔧 Validation adds Cel-Shade vs PBR style conflict detection

### v1.1.0 (2026-03-20)
- 🎬 **Camera Upgrade**: New focal length narrative psychology, dynamic focus paradigms, physical mount chapter (7 specialty rigs)
- 🎨 **Director Styles**: New Fincher / Deakins / Kurosawa / Makoto Shinkai + Anime Explosion / Xiaohongshu Aesthetic (incl. de-named safe prompts + forbidden items)
- 💡 **Quality Upgrade**: Anti-plastic manifesto, film stock library (5 types), material texture library (8 types), lighting combo quick-reference (4 sets), organic imperfection library, quality conflict matrix
- 🎬 **Scene Expansion**: New Game PV / Horror-Thriller / Travel-City / Pet-Cute / Before-After / Meme-Loop, totaling 16 scenarios + physics damping appendix
- 🎙️ **Sound Upgrade**: Spatial acoustic modifiers (7 types), material-based onomatopoeia refinement (7 pairs)
- 🔧 **Validation Enhancement**: Filler word warning → error hard-block, optical physics conflict detection, style conflict matrix, duration-aware time-slicing, 35 tests pass

### v1.0.0 (2026-03-19)
- 🎉 Initial release
- SKILL.md core workflow
- 6 professional knowledge base files
- Python validation script + test cases
- 20+ director style mappings
- 10 vertical scenario templates

---

## 📄 License

MIT-0 (MIT No Attribution) License
