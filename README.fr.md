[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Português](README.pt.md) | Français

# 🎬 Seedance2.0 Shot Design — Concepteur de Langage Cinématographique

[![Version](https://img.shields.io/badge/version-1.8.0-blue.svg)]()
[![Licence](https://img.shields.io/badge/license-MIT--0-green.svg)](LICENSE)
[![Plateforme](https://img.shields.io/badge/platform-Seedance_2.0-purple.svg)]()

> Transformez vos idées vidéo vagues en **prompts cinématographiques professionnels** prêts pour Jimeng Seedance 2.0 — en un clic.

Un Claude Skill construit sur la spécification [Agent Skills](https://agentskills.io), alliant l'esthétique cinématographique hollywoodienne aux pratiques de l'industrie audiovisuelle chinoise. Conçu pour aider les créateurs à dépasser le piège de la vidéo IA « jolie mais aléatoire » et atteindre une **narration visuelle précise et maîtrisée**.

---

## ✨ Capacités Principales

| Capacité | Description |
|----------|-------------|
| 🎭 **Production de Drame Comic IA & Court-métrage IA** | Support complet pour les drames comics IA (漫剧) et les courts-métrages IA — dialogues / voix off / placement d'acteurs / gros plans d'expressions exagérées / mouvements de caméra narratifs / sélecteur rapide de style / 4 variantes de templates (CN/EN × dialogue/voix off), avec modèles de scénarios et exemples complets |
| 🎨 **28+ Presets de Réalisateurs et Styles** | Nolan / Villeneuve / Fincher / Deakins / Kurosawa / Makoto Shinkai / Wong Kar-wai / Zhang Yimou / Xianxia / Cel-Shaded CG / Anime / Xiaohongshu… |
| 🎬 **Dictionnaire Pro des Mouvements de Caméra** | Système de caméra à 3 niveaux + 14 focales + 6 contrôles de mise au point + 7 montures physiques, réf. bilingues CN/EN |
| 💡 **Structure d'Éclairage en Trois Couches** | Source → Comportement → Tonalité — fini le vague « mets une lumière » |
| 📐 **Storyboard Horodaté** | `0-3s / 3-8s / …` contrôle précis de la timeline pour éviter le débordement visuel entre plans |
| 🎯 **Assemblage en Six Éléments** | Sujet / Action / Scène / Éclairage / Caméra / Son — formule structurée à haut rendement |
| 🎬 **Storyboard Multi-Segment Intelligent** | Vidéos >15s auto-découpées en segments indépendants avec style, éclairage, son unifiés et transitions fluides |
| 📦 **17 Modèles de Scénarios** | E-commerce / Xianxia / Court-métrage / Gastronomie / MV / Plan-séquence / Automobile / Macro / Nature / Game PV / Horreur / Voyage / Animaux / Transformation / Boucle / Montage vidéo |
| 🎵 **Vocabulaire Son et ASMR** | Bibliothèque d'onomatopées physiques : ambiance / action / voix / musique |
| 🌐 **Sortie Bilingue de Prompts** | Utilisateurs chinois → chinois / autres → anglais, détection automatique |
| 🛡️ **Protection PI Sécurisée** | Stratégie de repli PI progressive en trois niveaux contre les blocages de contenu |
| 🔍 **Validation Rigoureuse en Python** | Nombre de mots / caméra / logique temporelle / remplissage / conflits optiques / matrice de conflits de style |

---

## 🚀 Démarrage Rapide

### 1. Installer le Skill

<details>
<summary><b>Claude Code</b></summary>

Placez le dossier `seedance-shot-design/` dans `.claude/skills/` à la racine de votre projet :

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git .claude/skills/seedance-shot-design
```

Claude Code détectera et chargera le Skill automatiquement.
</details>

<details>
<summary><b>OpenClaw</b></summary>

Dans votre app de messagerie connectée (WeChat, Feishu, etc.), envoyez un message à l'Agent OpenClaw :

```
Merci d'apprendre ce skill : https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills
```

L'Agent téléchargera et apprendra le skill automatiquement.
</details>

<details>
<summary><b>Codex</b></summary>

Placez le dossier du Skill dans le répertoire d'instructions agents de Codex :

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git agents/skills/seedance-shot-design
```
</details>

<details>
<summary><b>Cursor</b></summary>

Placez le dossier du Skill dans `.cursor/skills/` à la racine de votre projet :

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git .cursor/skills/seedance-shot-design
```
</details>

### 2. Utilisation

Dites simplement à Claude :

```
Écris-moi un prompt vidéo de 15 secondes d'une poursuite sous la pluie cyberpunk
```

Le Skill s'active automatiquement et génère le prompt en 5 étapes :
1. **Analyse des Besoins** — Confirmer durée / ratio / assets / style
2. **Diagnostic Visuel** — Sélectionner langage caméra et style de réalisation
3. **Assemblage Six Éléments** — Composition précise selon la formule
4. **Validation Obligatoire** — Exécuter le script Python pour contrôle qualité
5. **Livraison Professionnelle** — Note de réalisation + prompt complet

### 3. Exemples

#### Démonstration Complète

**Entrée utilisateur :**
```
Écris-moi un prompt vidéo de 10 secondes pour un court-métrage de fantaisie orientale Xianxia
```

**Sortie du Skill :**

> **Prompt Vidéo Seedance**
>
> **Thème** : Un jeune homme en blanc attrape une feuille rouge à l'aube dans un temple ancestral, atteignant l'éveil
>
> **Note de Réalisation** (uniquement pour comprendre l'intention créative — ne pas copier) :
> Progression de caméra en trois phases : aérienne → dolly → poussée lente, transition du paysage grandiose vers l'émotion intime. Le grain pellicule 35mm apporte une texture artisanale, et la palette or-sarcelle reflète la philosophie orientale d'harmonie avec la nature.
>
> **Prompt Complet** (copier directement dans le champ de saisie Jimeng) :

```
10 secondes de fantaisie chinoise, esthétique cinématographique orientale réaliste, palette or-sarcelle, son ambiant éthéré.
0-3s : Plan zénithal aérien d'un temple ancestral dans une mer de nuages, poussée aérienne lente, brume matinale fluant dans les vallées, cloche lointaine, rayons Tyndall perçant les couches de nuages.
3-7s : Dolly à travers le portail du temple vers la cour, un jeune homme en blanc lève la main pour attraper une feuille rouge qui tombe, grain pellicule 35mm, faible profondeur de champ sur les détails de la main.
7-10s : Gros plan du jeune homme levant les yeux, poussée lente vers l'avant, le vent se lève, manches et cheveux ondulent vers la droite du cadre, lumière spirituelle s'élevant en spirale dans la cour.
Son : Le son ambiant converge en un unique tintement d'épée clair et cristallin.
Interdit : Tout texte, sous-titres, logos ou filigranes
```

#### Autres Cas d'Usage

```
# Drame Comic IA
Prompt de 10s style comic IA d'un PDG autoritaire, vertical 9:16, avec dialogues et gros plans exagérés

# Publicité E-commerce
Prompt vidéo publicitaire de montre de luxe de 8s, 9:16 vertical

# Court-métrage avec Dialogues
Prompt de 12s d'une scène de court-métrage avec retournement et dialogues

# Plan-séquence
Prompt de 15s d'une visite de musée en plan-séquence

# Avec Assets de Référence
J'ai envoyé 3 images de design de personnages et 1 vidéo de référence — génère une scène de combat Xianxia de 15s
```

---

## 📁 Structure du Projet

```
seedance-shot-design/
├── SKILL.md                     # Instructions principales (le cerveau du Skill)
├── README.md                    # Ce fichier
├── scripts/
│   ├── validate_prompt.py       # Script de validation industrielle
│   └── test_validate.py         # Cas de test
└── references/
    ├── cinematography.md        # Dictionnaire caméra et focales
    ├── director-styles.md       # Cartographie des styles de réalisation (28+)
    ├── seedance-specs.md        # Spécifications officielles Seedance 2.0
    ├── quality-anchors.md       # Ancres qualité et éclairage
    ├── scenarios.md             # 17 modèles de scénarios verticaux
    └── audio-tags.md            # Tags audio et effets sonores
```

---

## 🔬 Script de Validation

Outil Python autonome, utilisable en ligne de commande :

```bash
python scripts/validate_prompt.py --text "votre prompt"
python scripts/validate_prompt.py --file prompt.txt
python scripts/validate_prompt.py --text "your prompt" --lang en
python scripts/validate_prompt.py --text "votre prompt" --json
```

**Vérifications (v1.5) :**
- ❌ Dépassement du nombre de mots (Chinois >500 caractères / Anglais >1000 mots)
- ❌ Terminologie professionnelle de caméra absente
- ❌ Blocage dur des mots de remplissage (masterpiece / chef-d'œuvre / ultra-net → error)
- ❌ Conflits optique-physique (ultra grand-angle+bokeh, caméra à main+symétrie parfaite)
- ❌ Matrice de conflits de style (IMAX vs VHS, film vs numérique, encre vs UE5, Cel-Shaded vs PBR, Ralenti vs Speed Ramp)
- ❌ Dépassement de références d'assets (images >9 / vidéos >3 / audio >3 / total >12)
- ❌ Vidéo longue (>5s) sans découpe temporelle → blocage
- ⚠️ Lacunes ou chevauchements temporels
- ⚠️ Désaccord durée déclarée vs fin de segment
- ⚠️ Conflits de logique de mouvement dans le segment
- ⚠️ Termes de caméra anglais nus (Dolly / Aerial / Crane / Pan / Arc / Dutch / Steadicam)
- 🌐 Détection automatique de langue (chinois / anglais)
- 🎬 Cohérence entre segments multiples

**Exécuter les Tests :**
```bash
python -m unittest scripts.test_validate -v
# 54 tests passent (11 classes de test)
```

---

## 🏗️ Philosophie de Conception

### Chargement Progressif des Connaissances

- **SKILL.md** (~4000 tokens) : Flux principal + modèles + checklist qualité
- **references/** (à la demande) : Lus uniquement quand nécessaire
- **scripts/** (à la demande) : Validation après génération du prompt uniquement

### Avantages Concurrentiels

| Dimension | Approche Courante | Ce Skill |
|-----------|-------------------|----------|
| Validation | Suggestions texte | **Python rigoureux (optique/style + sécurité)** |
| Styles | Réalisateurs internationaux | **International + Chinois + Court + IA + Réseaux + Anime + Cel-Shaded + Xiaohongshu** |
| Scénarios | Cinéma épique | **17 verticaux + anime + montage + amortissement physique** |
| Son | Mentions brèves | **Acoustique spatiale + onomatopées par matériau** |
| Éclairage | « Mets une lumière » | **Source→Comportement→Ton + recettes + matériaux** |
| Multilingue | Chinois uniquement | **Bilingue CN/EN, détection automatique** |
| Sécurité révision | Non considéré | **Désambiguïsation des termes + détection de mots nus** |

---

## 📋 Historique des Versions

### v1.5.0 (2026-03-27)
- 🎭 **Système de Placement d'Acteurs** : Positionnement à 3 éléments (placement + direction du visage + point de regard) + vocabulaire de modificateurs émotionnels
- 🎙️ **Séparation Voix Off / Dialogues** : Modèles distincts pour dialogues vs. voix off / monologue intérieur, avec directive anti-lip-sync
- 📐 **Spécificité de l'Angle de Caméra** : Cartographie vague→spécifique avec 5 paires comparatives
- 🎬 **Mouvement de Caméra à Motivation Narrative** : Mouvements associés à un objectif narratif
- 🔀 **Stratégie de Transition entre Segments** : 6 types de transition pour la cohérence multi-plans
- 🎨 **Sélecteur Rapide de Style** : Combo 4 dimensions (type visuel × style de rendu × tonalité × genre)
- 📝 Modèles court-métrage étendus de 1 à 4 variantes (CN/EN × dialogue/voix off)
- 📝 5 exemples complets de court-métrage
- ✅ 54 tests passent

### v1.4.0 (2026-03-21)
- 🎬 **Storyboard Multi-Segment Intelligent** : Vidéos >15s auto-découpées (chaque ≤15s, min ≥8s)
- 📝 Cohérence multi-segment unifiée
- 📝 Modèle de sortie multi-segment (CN / EN)
- 📝 Exemple 60s désert Kali/Escrima en 4 segments
- 🔧 `validate_multi_segment()` cohérence inter-segments
- ✅ 54 tests passent

### v1.3.0 (2026-03-21)
- 🌐 **Sortie Bilingue** : Chinois→chinois, autres→anglais, détection auto
- 🛡️ **Désambiguïsation Caméra (Règle 9)**
- 🔧 `check_ambiguous_terms()` + `--lang` + comptage par mots
- ✅ 50 tests passent

### v1.2.0 (2026-03-21)
- 🎨 **Cel-Shaded CG** : Enregistrement paramétrique 4 axes
- 🧱 **Matériaux Anime/NPR** : 4 matériaux non photoréalistes
- ✅ Conflit Cel-Shade vs PBR

### v1.1.0 (2026-03-20)
- 🎬 Psychologie focale, mise au point dynamique, 7 montures spéciales
- 🎨 Fincher / Deakins / Kurosawa / Shinkai + Anime + Xiaohongshu
- 💡 Anti-plastique, pellicules, textures, éclairage, imperfections organiques
- 🎬 6 nouveaux scénarios (total 16) + amortissement physique
- 🔧 Remplissage→error, conflits optiques/style, 35 tests

### v1.0.0 (2026-03-19)
- 🎉 Premier lancement

---

## 📄 Licence

MIT-0 (MIT No Attribution) License
