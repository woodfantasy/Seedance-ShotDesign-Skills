[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | Português | [Français](README.fr.md)

<p align="center">
  <img src="assets/logo.svg" width="128" height="128" alt="Seedance Shot Design Logo">
</p>

<h1 align="center">Seedance2.0 Shot Design</h1>

<p align="center">
  <strong>Designer de Linguagem Cinematográfica</strong>
</p>

<p align="center">
  <a href=""><img src="https://img.shields.io/badge/version-1.9.0-blue.svg" alt="Versão"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT--0-green.svg" alt="Licença"></a>
  <a href=""><img src="https://img.shields.io/badge/platform-Seedance_2.0-purple.svg" alt="Plataforma"></a>
</p>

<p align="center">
  Transforme suas ideias vagas de vídeo em <strong>prompts cinematográficos profissionais</strong>, prontos para o Jimeng Seedance 2.0 — com um clique.
</p>

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
| 📦 **17 Templates de Cenários** | E-commerce / Xianxia / Curta / Gastronomia / MV / Plano-sequência / Automotivo / Macro / Natureza / Game PV / Terror / Viagem / Pets / Transformação / Loop / Edição de Vídeo / Extensão de Vídeo / Complemento de História / Narração Multiframe |
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
    ├── scenarios.md             # 20 templates de cenários verticais
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

**Verificações:**
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

### v1.9.0 (2026-04-18)
- 🎬 **Referência Rápida de Planos Narrativos Guia (novo capítulo)**: Nova Seção IX em `cinematography.md` — 8 tipos de planos de guia/seguimento/revelação (Leading Shot, Following Shot, Side Tracking, Low Angle Follow, Long Lens Follow, Epic Drone Reveal, Reveal Through, Orbit Follow), com frases-gatilho bilíngues e prompts de exemplo
- 🚁 **Epic Drone Reveal**: Adicionado como movimento de câmera Level 1 independente — ascensão lenta de trás/ângulo baixo revelando a paisagem épica; estrutura narrativa distinta dos planos aéreos genéricos
- 🌿 **Reveal from Behind / Through Shot**: Nova entrada Level 1 para planos de penetração de obstáculos (câmera empurrando por bambu/multidão/cortina para revelar), com guia de frases seguras
- 🚶 **Leading Shot**: Nova entrada Level 1 para movimento de câmera que recua à frente do sujeito, transmitindo jornada e agência do protagonista
- ⚡ **Snap Zoom / Crash Zoom**: Adicionado a combos Level 3 — salto explosivo de distância focal para impacto cômico, ênfase de susto e sincronização de beat MV
- 🌀 **Orbit Follow**: Adicionado a combos Level 3 — combinação orbit + tracking onde o ponto pivô se move com o sujeito, distinto das órbitas de sujeito estático

### v1.8.5 (2026-04-08)
- 🌐 **Adaptação à Plataforma Runway**: Limites de recursos especificados para usuários do Runway (≤5 imagens, ≤3 vídeos) e estratégias explícitas para contornar a moderação de rostos humanos realistas (desfoque ou estilos NPR).
- 🎞️ **Interpolação de Quadro Inicial e Final**: Adicionado o 7º padrão de referência multimodal (`@Image1 as start frame, @Image2 as end frame`) para transições precisas de ponto a ponto.
- 🎬 **Dois Novos Cenários de Efeitos**:
  - `Freeze Time (Tempo Congelado)`: A câmera se move dramaticamente por elementos de cena completamente congelados.
  - `Multishot Video (Vídeo Multi-Telas)`: Contorna a limitação "take único", fazendo o modelo gerar cortes rápidos de montagem em uma única execução.

- 🚀 **Cenários de POV Extremo**: Adicionado o 21º template de cenário focado na "lógica de rastreamento da cabeça humana", "FPV de projéteis em alta velocidade (espadas/flechas voadoras)" e "voo de criaturas".
- 🎧 **Exclusão de Áudio Imersivo**: Introduzidas diretivas estritas de exclusão de áudio para templates de POV (SOMENTE som ambiente, NENHUM BGM ou diálogo) para impedir que a IA quebre a imersão.
- 🧹 **Regra de Purificação de Fundo**: Esclarecido que as imagens de entidades de referência devem usar um "fundo branco puro/vazio" para evitar contaminar o ambiente de vídeo na geração da Imagem para o Vídeo.

### v1.8.4 (2026-04-08)
- 🔗 **Guia de integração CLI**: Nova seção em `seedance-specs.md` com mapeamento de comandos CLI do Jimeng (`text2video` / `image2video` / `multiframe2video` / `multimodal2video`), gerenciamento de tarefas assíncronas e documentação de canais VIP
- 🎞️ **Template de narrativa multiframe**: Novo template de cenário (#20) para `multiframe2video` — envie 2-9 imagens de quadros-chave e o motor compõe automaticamente um vídeo narrativo coerente
- 📚 **Roteamento da base de conhecimento**: Adicionadas entradas de roteamento multiframe e CLI à tabela de inferência semântica do Passo 2

### v1.8.3 (2026-04-08)
- 🎭 **Regra Descritivo > Narrativo**: Nova regra central (#12) — escrever apenas o que a câmera VÊ (palavras visuais), nunca o que o personagem SENTE (palavras emocionais). Todas as emoções devem ser convertidas em expressões físicas visíveis
- ✍️ **Inglês Progressivo**: Regras de montagem exigem forma -ing para ações em inglês (`running` não `runs`) — o progressivo implica movimento contínuo
- 🎯 **Tom de Movimento Antecipado**: O preâmbulo de estilo declara a energia de movimento geral (`dynamic motion` / `serene atmosphere`), fixando a base de movimento no início

### v1.8.2 (2026-04-07)
- 🎥 **Regra Um-Plano-Um-Movimento**: Nova regra central (#10) — um único movimento de câmera por segmento temporal. Combinar movimentos (ex: push-in + pan) causa tremura. Movimento do sujeito e da câmera devem ser descritos separadamente
- 🖼️ **Regra de Ouro I2V**: Nova regra central (#11) e seção I2V dedicada — ao gerar vídeo a partir de imagem, descrever apenas movimento/mudanças, nunca re-descrever conteúdo estático do primeiro frame. Introduz frase âncora `preserve composition and colors`
- 📏 **Comprimento Ótimo do Prompt**: Guia de ponto ideal 60-100 palavras — abaixo é vago, acima de 100 causa deriva conceitual e instruções conflitantes
- 💪 **Modificadores de Intensidade de Movimento**: Nova tabela bilíngue com 6 níveis de intensidade (violento → suave → gradual) e exemplos Do/Don't para eliminar "movimento pastoso"
- 🎤 **Ritmo sobre Especificações**: Regras de montagem preferem explicitamente palavras de ritmo semântico (gentle/gradual/smooth) sobre parâmetros técnicos (24fps/f2.8)
- 🎬 **Melhores Práticas para Vídeo de Referência**: Restrições práticas — ideal 3-8s, plano contínuo (sem cortes), intenção única (sujeito OU câmera)

### v1.8.1 (2026-04-07)
- 🛡️ **Conformidade de Segurança**: Resolvido o flag "padrões suspeitos" do ClawHub OpenClaw — validação Python convertida para checklist estruturada de 7 regras LLM-nativas. Scripts Python mantidos como ferramentas de desenvolvimento independentes
- 🎯 **Otimização de Frases Ativadoras**: Triggers reduzidos de 40+ para 15 termos profissionais de alto sinal

### v1.8.0 (2026-04-05)
- 🎤 **Sistema de Controle de Voz e Idioma**: Clonagem de timbre por referência de vídeo, controle de dialeto/sotaque, mistura de diálogos multilíngue, estilos vocais especiais (documentário/comédia/ópera/ASMR)
- 📹 **Guia de Referência Multimodal**: Atualização de 4 dicas para 6 padrões de referência core (primeiro frame/câmera/ação/câmera+ação/timbre/efeitos)
- 📏 **Cenário de Extensão de Vídeo**: Templates de extensão para frente/trás, técnicas de continuação seamless, correção cognitiva de duração
- 📋 **Cenário de Completude de História**: Storyboard→vídeo, animação de painéis, imagem→vídeo emocional
- 🎬 **Referência Rápida de Efeitos Criativos**: Keywords VFX — zoom Hitchcock, olho de peixe, partículas, speed ramp, transição freeze, tinta nanquim, morphing
- 🎭 **Guia de Performance Emocional**: Tabela de especificidade emocional, triggers de transição emocional, uso de vídeo de referência emocional

### v1.7.2 (2026-04-02)
- 🎯 **Expansão de Palavras Ativadoras**: 20+ triggers chineses e 10+ ingleses para expressões cotidianas ("faça um vídeo", "criar clip", "movimento de câmera")

### v1.7.1 (2026-03-29)
- 🔒 **Otimização de Segurança**: Resolvidos flags de segurança do ClawHub mantendo funcionalidade completa

### v1.7.0 (2026-03-28)
- 🚨 **Step 3 Regras de Montagem Obrigatórias**: Iluminação de 3 camadas em linha própria/linha SFX padronizada/itens proibidos unificados/seções não-template proibidas
- ⛔ **Step 4 Bloqueio de Validação**: Prompts reprovados na validação não são mostrados ao usuário
- 📋 **Step 5 Formato Obrigatório**: Template de saída Tema+Nota do Diretor+bloco de código
- 🎯 **Step 2 Extração de Parâmetros**: Não apenas "carregar" bases de conhecimento mas extrair e inserir parâmetros específicos

### v1.6.0 (2026-03-28)
- 🧠 **Roteamento Semântico Inteligente**: Step 2 de "trigger explícito"→roteamento de 3 camadas — carregamento permanente/inferência semântica/especificação explícita
- 🎯 **Step 1 Inferência Inteligente**: Inferência ativa de parâmetros a partir de uma frase, perguntas limitadas a 1-2

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
