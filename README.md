English | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md)

# 🎬 Seedance2.0 Shot Design — Cinematic Shot Language Designer

[![Version](https://img.shields.io/badge/version-1.4.0-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT--0-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Seedance_2.0-purple.svg)]()

> Turn your vague video ideas into **cinema-grade video prompts** ready for Jimeng Seedance 2.0 — in one shot.

A Claude Skill built on the [Agent Skills](https://agentskills.io) specification, blending Hollywood-level cinematography aesthetics with Chinese film industry practices. It's designed to help creators break free from the "looks nice but random" AI video trap and achieve **precise, controllable visual storytelling**.

---

## ✨ Core Capabilities

| Capability | Description |
|------------|-------------|
| 🎨 **28+ Director & Style Presets** | Nolan / Villeneuve / Fincher / Deakins / Kurosawa / Makoto Shinkai / Wong Kar-wai / Zhang Yimou / Xianxia / Cel-Shaded CG / Anime / Xiaohongshu… |
| 🎬 **Pro Camera Movement Dictionary** | 3-tier camera system + 14 focal lengths + 6 focus controls + 7 physical mounts, with bilingual CN/EN references |
| 💡 **Three-Layer Lighting Structure** | Light Source → Light Behavior → Color Tone — no more vague "add a light" |
| 📐 **Timestamped Storyboarding** | `0-3s / 3-8s / …` precise timeline control to prevent visual bleeding between shots |
| 🎯 **Six-Element Precision Assembly** | Subject / Action / Scene / Lighting / Camera / Sound — a structured, high-conversion formula |
| 🎬 **Smart Multi-Segment Storyboard** | Videos >15s are automatically split into independent prompt segments with unified style, lighting, sound, and seamless transition frames |
| 📦 **17 Scenario Templates** | E-commerce / Xianxia / Short Drama / Food / MV / One-Take / Automotive / Macro / Nature / Game PV / Horror / Travel / Pets / Transformation / Loop / Video Editing |
| 🎵 **Sound & ASMR Vocabulary** | Physics-based onomatopoeia library covering ambient / action / vocal / music sounds |
| 🌐 **Bilingual Prompt Output** | Chinese users → Chinese prompts, non-Chinese users → English prompts, auto-detected |
| 🛡️ **Copyright-Safe IP Fallback** | Three-tier progressive IP fallback strategy to prevent platform content blocks |
| 🔍 **Python Hard Validation** | Word count / camera moves / temporal logic / filler detection / optical physics conflicts / style conflict matrix — more reliable than "suggestions" |

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
4. **Mandatory Validation** — Run the Python script for quality review
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
    ├── scenarios.md             # Vertical scenario templates (17 scenarios + anime variants + video editing + physics damping toolkit)
    └── audio-tags.md            # Audio & sound effect tag specs (incl. spatial acoustics & material-based onomatopoeia)
```

---

## 🔬 Validation Script

A standalone Python validation tool, usable from the command line:

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

**Validation Checks (v1.4):**
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
- **references/** (loaded on demand): Only read when the user mentions style / camera / quality needs
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
