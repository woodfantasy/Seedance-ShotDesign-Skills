[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | Português | [Français](README.fr.md)

# 🎬 Seedance2.0 Shot Design — Designer de Linguagem Cinematográfica

[![Versão](https://img.shields.io/badge/version-1.8.0-blue.svg)]()
[![Licença](https://img.shields.io/badge/license-MIT--0-green.svg)](LICENSE)
[![Plataforma](https://img.shields.io/badge/platform-Seedance_2.0-purple.svg)]()

> Transforme suas ideias vagas de vídeo em **prompts cinematográficos profissionais**, prontos para o Jimeng Seedance 2.0 — com um clique.

Um Claude Skill construído sobre a especificação [Agent Skills](https://agentskills.io), que une a estética cinematográfica de Hollywood com as práticas da indústria audiovisual chinesa. Projetado para ajudar criadores a superar a armadilha do vídeo IA que "fica bonito, mas é aleatório" e alcançar uma **narrativa visual precisa e controlável**.

---

## ✨ Capacidades Principais

| Capacidade | Descrição |
|------------|-----------|
| 🎭 **Produção de Drama Cômico IA & Curta-metragem IA** | Suporte completo para dramas cômicos IA (漫剧) e curtas-metragens IA — diálogos / narração / bloqueio de atores / close-ups de expressões exageradas / movimentos de câmera narrativos / seletor rápido de estilo / 4 variantes de templates (CN/EN × diálogo/narração), com templates de cenários e exemplos completos |
| 🎨 **28+ Presets de Diretores e Estilos** | Nolan / Villeneuve / Fincher / Deakins / Kurosawa / Makoto Shinkai / Wong Kar-wai / Zhang Yimou / Xianxia / Cel-Shaded CG / Anime / Xiaohongshu… |
| 🎬 **Dicionário Profissional de Movimentos de Câmera** | Sistema de câmera em 3 níveis + 14 distâncias focais + 6 controles de foco + 7 montagens físicas, com referências bilíngues CN/EN |
| 💡 **Estrutura de Iluminação em Três Camadas** | Fonte de Luz → Comportamento → Tom de Cor — chega de "bota uma luz aí" |
| 📐 **Storyboard com Marcação Temporal** | `0-3s / 3-8s / …` controle preciso da timeline para evitar sangramento visual entre planos |
| 🎯 **Montagem de Seis Elementos** | Sujeito / Ação / Cena / Iluminação / Câmera / Som — fórmula estruturada de alta conversão |
| 🎬 **Storyboard Multi-Segmento Inteligente** | Vídeos >15s divididos automaticamente em segmentos independentes com estilo, iluminação, som unificados e transições seamless |
| 📦 **17 Templates de Cenários** | E-commerce / Xianxia / Curta / Gastronomia / MV / Plano-sequência / Automotivo / Macro / Natureza / Game PV / Terror / Viagem / Pets / Transformação / Loop / Edição de Vídeo |
| 🎵 **Vocabulário de Som e ASMR** | Biblioteca de onomatopeias baseada em física: ambiental / ação / vocal / música |
| 🌐 **Saída Bilíngue de Prompts** | Usuários chineses → chinês / demais → inglês, detecção automática |
| 🛡️ **Proteção de PI Segura** | Estratégia progressiva de recuo de PI em três níveis para evitar bloqueios |
| 🔍 **Validação Rigorosa com Python** | Contagem de palavras / câmera / lógica temporal / enchimento / conflitos ópticos / matriz de conflitos de estilo |

---

## 🚀 Início Rápido

### 1. Instalar o Skill

<details>
<summary><b>Claude Code</b></summary>

Coloque a pasta `seedance-shot-design/` em `.claude/skills/` na raiz do projeto:

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git .claude/skills/seedance-shot-design
```

O Claude Code detectará e carregará o Skill automaticamente.
</details>

<details>
<summary><b>OpenClaw</b></summary>

No seu app de mensagens conectado (WeChat, Feishu, etc.), envie ao Agent do OpenClaw:

```
Por favor, aprenda este skill: https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills
```

O Agent baixará e aprenderá o skill automaticamente.
</details>

<details>
<summary><b>Codex</b></summary>

Coloque a pasta do Skill no diretório de instrução de agents do Codex:

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git agents/skills/seedance-shot-design
```
</details>

<details>
<summary><b>Cursor</b></summary>

Coloque a pasta do Skill em `.cursor/skills/` na raiz do projeto:

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git .cursor/skills/seedance-shot-design
```
</details>

### 2. Uso

Basta dizer ao Claude:

```
Escreva um prompt de vídeo de 15 segundos de uma perseguição na chuva cyberpunk
```

O Skill ativa automaticamente e gera o prompt em 5 etapas:
1. **Análise de Requisitos** — Confirmar duração / proporção / assets / estilo
2. **Diagnóstico Visual** — Selecionar linguagem de câmera e estilo de direção
3. **Montagem de Seis Elementos** — Composição precisa segundo a fórmula
4. **Validação Obrigatória** — Executar o script Python para revisão de qualidade
5. **Entrega Profissional** — Declaração do diretor + prompt completo

### 3. Exemplos

#### Demonstração Completa

**Entrada do usuário:**
```
Escreva um prompt de vídeo de 10 segundos para um curta de fantasia oriental Xianxia
```

**Saída do Skill:**

> **Prompt de Vídeo Seedance**
>
> **Tema**: Um jovem de branco apanha uma folha vermelha ao amanhecer num templo ancestral, alcançando a iluminação
>
> **Declaração do Diretor** (apenas para contexto criativo — não copiar):
> Progressão de câmera: aérea → dolly → empurrão lento. O grão de filme 35mm acrescenta textura artesanal, e a paleta dourado-azulada reflete a harmonia com a natureza.
>
> **Prompt Completo** (copiar diretamente no Jimeng):

```
10 segundos de fantasia chinesa, estética cinematográfica oriental realista, paleta dourado-azulada, som ambiente etéreo.
0-3s: Plano zenital aéreo de um templo entre nuvens, empurrão aéreo lento, neblina matinal nos vales, sino distante, raios Tyndall atravessando nuvens.
3-7s: Dolly pelo portão do templo até o pátio, jovem de branco apanha folha vermelha que cai, grão 35mm, profundidade de campo reduzida na mão.
7-10s: Close-up do jovem levantando o olhar, empurrão lento, vento levanta mangas e cabelo para a direita, luz espiritual subindo em espiral.
Som: Ambiente converge num toque de espada cristalino.
Proibido: Texto, legendas, logos ou marcas d'água
```

#### Mais Casos de Uso

```
# Drama Cômico IA
Prompt de 10s estilo cômico IA de CEO dominador, vertical 9:16, com diálogos e close-ups exagerados

# Anúncio E-commerce
Prompt de vídeo publicitário de relógio de luxo de 8s, 9:16 vertical

# Curta com Diálogos
Prompt de 12s de cena de curta com reviravolta e diálogos

# Plano-sequência
Prompt de 15s de passeio por museu em plano-sequência

# Com Referências
Enviei 3 imagens de personagens e 1 vídeo de referência — gere uma cena de luta Xianxia de 15s
```

---

## 📁 Estrutura do Projeto

```
seedance-shot-design/
├── SKILL.md                     # Instruções principais (o cérebro do Skill)
├── README.md                    # Este arquivo
├── scripts/
│   ├── validate_prompt.py       # Script de validação industrial
│   └── test_validate.py         # Casos de teste
└── references/
    ├── cinematography.md        # Dicionário de câmera e distâncias focais
    ├── director-styles.md       # Mapeamento de estilos de direção (28+)
    ├── seedance-specs.md        # Especificações oficiais Seedance 2.0
    ├── quality-anchors.md       # Âncoras de qualidade e iluminação
    ├── scenarios.md             # 17 templates de cenários verticais
    └── audio-tags.md            # Tags de áudio e efeitos sonoros
```

---

## 🔬 Script de Validação

Ferramenta Python independente, via linha de comando:

```bash
python scripts/validate_prompt.py --text "seu prompt"
python scripts/validate_prompt.py --file prompt.txt
python scripts/validate_prompt.py --text "your prompt" --lang en
python scripts/validate_prompt.py --text "seu prompt" --json
```

**Verificações (v1.5):**
- ❌ Excesso de palavras (Chinês >500 caracteres / Inglês >1000 palavras)
- ❌ Terminologia profissional de câmera ausente
- ❌ Bloqueio duro de enchimento (masterpiece / obra-prima / ultra-nítido → error)
- ❌ Conflitos óptico-físicos (ultra grande-angular+bokeh, câmera na mão+simetria perfeita)
- ❌ Matriz de conflitos de estilo (IMAX vs VHS, filme vs digital, tinta vs UE5, Cel-Shaded vs PBR, Câmera Lenta vs Speed Ramp)
- ❌ Overflow de assets (imagens >9 / vídeos >3 / áudio >3 / total >12)
- ❌ Vídeo longo (>5s) sem divisão temporal → bloqueio
- ⚠️ Lacunas ou sobreposições na divisão temporal
- ⚠️ Descompasso duração declarada vs ponto final do segmento
- ⚠️ Conflitos de lógica de movimento no segmento
- ⚠️ Termos de câmera em inglês soltos (Dolly / Aerial / Crane / Pan / Arc / Dutch / Steadicam)
- 🌐 Detecção automática de idioma (chinês / inglês)
- 🎬 Consistência entre múltiplos segmentos

**Executar Testes:**
```bash
python -m unittest scripts.test_validate -v
# 54 testes passam (11 classes de teste)
```

---

## 🏗️ Filosofia de Design

### Carregamento Progressivo de Conhecimento

- **SKILL.md** (~4000 tokens): Fluxo principal + templates + checklist
- **references/** (sob demanda): Lidos apenas quando necessário
- **scripts/** (sob demanda): Validação apenas após gerar o prompt

### Vantagens Competitivas

| Dimensão | Comum | Este Skill |
|----------|-------|------------|
| Validação | Sugestões em texto | **Python rigoroso (óptica/estilo + segurança)** |
| Estilos | Diretores internacionais | **Internacional + Chinês + Curta + IA + SNS + Anime + Cel-Shaded + Xiaohongshu** |
| Cenários | Cinema épico | **17 verticais + anime + edição + amortecimento físico** |
| Som | Menções breves | **Acústica espacial + onomatopeias por material** |
| Iluminação | "Bota uma luz" | **Fonte→Comportamento→Tom + receitas + materiais** |
| Multilíngue | Apenas chinês | **Bilíngue CN/EN, detecção automática** |
| Segurança na revisão | Não considerado | **Desambiguação de termos + detecção de palavras soltas** |

---

## 📋 Histórico de Versões

### v1.5.0 (2026-03-27)
- 🎭 **Sistema de Bloqueio de Atores**: Posicionamento de 3 elementos (posição + direção facial + foco do olhar) + vocabulário de modificadores emocionais
- 🎙️ **Separação Narração/Diálogo**: Templates distintos para diálogos vs. narração/monólogo interior, com diretiva anti-lip-sync
- 📐 **Especificidade do Ângulo de Câmera**: Mapeamento vago→específico com 5 pares comparativos
- 🎬 **Movimento de Câmera com Motivação Narrativa**: Movimentos emparelhados com propósito narrativo
- 🔀 **Estratégia de Transição entre Segmentos**: 6 tipos de transição para coerência multi-plano
- 🎨 **Seletor Rápido de Estilo**: Combo de 4 dimensões (tipo visual × estilo de render × tom × gênero)
- 📝 Templates de curta expandidos de 1 para 4 variantes (CN/EN × diálogo/narração)
- 📝 5 exemplos completos de curta-metragem
- ✅ 54 testes passam

### v1.4.0 (2026-03-21)
- 🎬 **Storyboard Multi-Segmento Inteligente**: Vídeos >15s auto-divididos (cada ≤15s, mín ≥8s)
- 📝 Coerência multi-segmento unificada
- 📝 Template de saída multi-segmento (CN / EN)
- 📝 Exemplo 60s deserto Kali/Escrima 4 segmentos
- 🔧 `validate_multi_segment()` consistência entre segmentos
- ✅ 54 testes passam

### v1.3.0 (2026-03-21)
- 🌐 **Saída Bilíngue**: Chinês→chinês, outros→inglês, detecção automática
- 🛡️ **Desambiguação de Câmera (Regra 9)**
- 🔧 `check_ambiguous_terms()` + `--lang` + contagem por palavras
- ✅ 50 testes passam

### v1.2.0 (2026-03-21)
- 🎨 **Cel-Shaded CG**: Registro parametrizado em 4 eixos
- 🧱 **Materiais Anime/NPR**: 4 materiais não fotorrealistas
- ✅ Conflito Cel-Shade vs PBR

### v1.1.0 (2026-03-20)
- 🎬 Psicologia focal, foco dinâmico, 7 montagens especiais
- 🎨 Fincher / Deakins / Kurosawa / Shinkai + Anime + Xiaohongshu
- 💡 Anti-plástico, filmes, texturas, iluminação, imperfeições orgânicas
- 🎬 6 novos cenários (total 16) + amortecimento físico
- 🔧 Enchimento→error, conflitos ópticos/estilo, 35 testes

### v1.0.0 (2026-03-19)
- 🎉 Primeiro lançamento

---

## 📄 Licença

MIT-0 (MIT No Attribution) License
