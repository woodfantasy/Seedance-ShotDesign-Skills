[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Español | [Português](README.pt.md) | [Français](README.fr.md)

# 🎬 Seedance2.0 Shot Design — Diseñador de Lenguaje Cinematográfico

[![Versión](https://img.shields.io/badge/version-1.8.0-blue.svg)]()
[![Licencia](https://img.shields.io/badge/license-MIT--0-green.svg)](LICENSE)
[![Plataforma](https://img.shields.io/badge/platform-Seedance_2.0-purple.svg)]()

> Convierte tus ideas vagas de vídeo en **prompts cinematográficos profesionales** listos para Jimeng Seedance 2.0, con un solo clic.

Un Claude Skill construido sobre la especificación [Agent Skills](https://agentskills.io), que fusiona la estética cinematográfica de Hollywood con las prácticas de la industria audiovisual china. Diseñado para ayudar a los creadores a superar la trampa del vídeo IA que "queda bonito pero es aleatorio" y lograr una **narrativa visual precisa y controlable**.

---

## ✨ Capacidades Principales

| Capacidad | Descripción |
|-----------|-------------|
| 🎭 **Producción de Drama Cómic IA y Cortometraje IA** | Soporte completo para dramas cómicos IA (漫剧) y cortometrajes IA — diálogos / voz en off / bloqueo de actores / primeros planos con expresiones exageradas / movimiento de cámara con motivación narrativa / selector rápido de estilo / 4 variantes de plantilla (CN/EN × diálogo/voz en off), con plantillas de escenario y ejemplos completos |
| 🎨 **28+ Presets de Directores y Estilos** | Nolan / Villeneuve / Fincher / Deakins / Kurosawa / Makoto Shinkai / Wong Kar-wai / Zhang Yimou / Xianxia / Cel-Shaded CG / Anime / Xiaohongshu… |
| 🎬 **Diccionario Profesional de Movimientos de Cámara** | Sistema de cámara de 3 niveles + 14 distancias focales + 6 controles de enfoque + 7 montajes físicos, con referencias bilingües CN/EN |
| 💡 **Estructura de Iluminación en Tres Capas** | Fuente de Luz → Comportamiento → Tono de Color — adiós al vago "pon una luz" |
| 📐 **Storyboard con Marcas de Tiempo** | `0-3s / 3-8s / …` control preciso del timeline para evitar el sangrado visual entre planos |
| 🎯 **Ensamblaje de Seis Elementos** | Sujeto / Acción / Escena / Iluminación / Cámara / Sonido — fórmula estructurada de alta conversión |
| 🎬 **Storyboard Multi-Segmento Inteligente** | Vídeos de >15s se dividen automáticamente en segmentos independientes con estilo, iluminación, sonido unificados y transiciones fluidas |
| 📦 **17 Plantillas de Escenarios** | E-commerce / Xianxia / Cortometraje / Gastronomía / MV / Plano Secuencia / Automoción / Macro / Naturaleza / Game PV / Terror / Viajes / Mascotas / Transformación / Loop / Edición de Vídeo |
| 🎵 **Vocabulario de Sonido y ASMR** | Biblioteca de onomatopeyas basada en física: ambiente / acción / vocal / música |
| 🌐 **Salida Bilingüe de Prompts** | Usuarios chinos → prompts en chino / resto → en inglés, detección automática |
| 🛡️ **Protección de PI segura** | Estrategia de repliegue de PI progresiva en tres niveles para evitar bloqueos de contenido |
| 🔍 **Validación Rigurosa con Python** | Conteo de palabras / movimientos de cámara / lógica temporal / detección de relleno / conflictos óptico-físicos / matriz de conflictos de estilo — más fiable que simples "sugerencias" |

---

## 🚀 Inicio Rápido

### 1. Instalar el Skill

<details>
<summary><b>Claude Code</b></summary>

Coloca la carpeta `seedance-shot-design/` en `.claude/skills/` en la raíz de tu proyecto:

```bash
# Clonar en el directorio de Skills del proyecto
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git .claude/skills/seedance-shot-design
```

Claude Code detectará y cargará el Skill automáticamente.
</details>

<details>
<summary><b>OpenClaw</b></summary>

En tu app de mensajería conectada (WeChat, Feishu, etc.), envía un mensaje al Agent de OpenClaw:

```
Por favor, aprende este skill: https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills
```

El Agent descargará y aprenderá el skill Seedance Shot Design automáticamente. Puedes empezar a hacer solicitudes de inmediato.
</details>

<details>
<summary><b>Codex</b></summary>

Coloca la carpeta del Skill en el directorio de instrucciones de agents de Codex:

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git agents/skills/seedance-shot-design
```

Luego invócalo dentro de una conversación de Codex.
</details>

<details>
<summary><b>Cursor</b></summary>

Coloca la carpeta del Skill en `.cursor/skills/` en la raíz de tu proyecto:

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git .cursor/skills/seedance-shot-design
```

El modo Agent de Cursor leerá las instrucciones del Skill automáticamente.
</details>

### 2. Uso

Simplemente dile a Claude:

```
Escríbeme un prompt de vídeo de 15 segundos de una persecución bajo la lluvia en estilo cyberpunk
```

El Skill se activa automáticamente y genera el prompt mediante un flujo de 5 pasos:
1. **Análisis de Requisitos** — Confirmar duración / relación de aspecto / assets / estilo
2. **Diagnóstico Visual** — Seleccionar lenguaje de cámara y estilo de dirección
3. **Ensamblaje de Seis Elementos** — Composición precisa según la fórmula estructurada
4. **Validación Obligatoria** — Ejecutar el script Python para revisión de calidad
5. **Entrega Profesional** — Declaración del director + prompt completo

### 3. Ejemplos

#### Demostración de Interacción Completa

**Entrada del usuario:**
```
Escríbeme un prompt de vídeo para un cortometraje de fantasía oriental Xianxia de 10 segundos
```

**Salida del Skill:**

> **Prompt de Vídeo Seedance**
>
> **Tema**: Un joven de blanco atrapa una hoja roja al amanecer en un templo ancestral entre la niebla, alcanzando la iluminación
>
> **Declaración del Director** (solo para entender la intención creativa — no copiar):
> Progresión de cámara en tres fases: aérea → dolly → empuje lento, transitando del paisaje grandioso a la emoción íntima.
> El grano de película 35mm aporta textura artesanal, y la paleta dorado-azulada refleja la filosofía oriental de armonía con la naturaleza.
>
> **Prompt Completo** (copiar directamente en el campo de entrada de Jimeng):

```
10 segundos de fantasía china, estética cinematográfica oriental realista, paleta dorado-azulada, sonido ambiental etéreo.
0-3s: Plano cenital aéreo de un templo ancestral entre un mar de nubes, empuje aéreo lento, niebla matinal fluyendo por los valles, campana lejana sonando tenuemente, rayos Tyndall atravesando las capas de nubes.
3-7s: Dolly a través de la puerta del templo hacia el patio, un joven de blanco alza la mano para atrapar una hoja roja que cae, textura de grano 35mm, profundidad de campo reducida enfocando los detalles de la mano.
7-10s: Primer plano del joven levantando la mirada, empuje lento hacia adelante, se levanta el viento, las mangas y el cabello ondean hacia la derecha del encuadre, luz espiritual ascendiendo en espiral en el patio.
Sonido: El sonido ambiente converge en un único tañido de espada claro y cristalino.
Prohibido: Cualquier texto, subtítulos, logos o marcas de agua
```

#### Más Casos de Uso

```
# Drama Cómic IA
Escríbeme un prompt de 10 segundos estilo cómic AI de un CEO dominante, vertical 9:16, con diálogos y primeros planos exagerados

# Anuncio de E-commerce
Escríbeme un prompt de vídeo publicitario de reloj de lujo de 8 segundos, 9:16 vertical

# Cortometraje con Diálogos
Escríbeme un prompt de 12 segundos de una escena de cortometraje con giro argumental y diálogos

# Plano Secuencia
Escríbeme un prompt de 15 segundos de un recorrido por un museo en plano secuencia

# Con Assets de Referencia
He subido 3 imágenes de diseño de personajes y 1 vídeo de referencia — genera una escena de lucha Xianxia de 15 segundos
```

---

## 📁 Estructura del Proyecto

```
seedance-shot-design/
├── SKILL.md                     # Instrucciones principales (el cerebro del Skill)
├── README.md                    # Este archivo
├── scripts/
│   ├── validate_prompt.py       # Script de validación industrial de prompts
│   └── test_validate.py         # Casos de prueba del script de validación
└── references/
    ├── cinematography.md        # Diccionario de cámara y distancias focales (incl. montajes físicos y psicología focal)
    ├── director-styles.md       # Mapeo parametrizado de estilos de dirección (28+ estilos, incl. Cel-Shaded CG)
    ├── seedance-specs.md        # Especificaciones oficiales de la plataforma Seedance 2.0
    ├── quality-anchors.md       # Anclas de calidad y biblioteca de iluminación (incl. materiales NPR / iluminación / matriz de conflictos)
    ├── scenarios.md             # Plantillas de escenarios verticales (17 escenarios + variantes anime + edición de vídeo + kit de amortiguación física)
    └── audio-tags.md            # Especificaciones de etiquetas de audio y efectos sonoros (incl. acústica espacial y onomatopeyas por material)
```

---

## 🔬 Script de Validación

Herramienta de validación Python independiente, utilizable desde la línea de comandos:

```bash
# Validar texto directamente
python scripts/validate_prompt.py --text "tu prompt"

# Validar desde archivo
python scripts/validate_prompt.py --file prompt.txt

# Especificar idioma (auto=detección automática, cn=chino, en=inglés)
python scripts/validate_prompt.py --text "your prompt" --lang en

# Salida en formato JSON (para procesamiento programático)
python scripts/validate_prompt.py --text "tu prompt" --json
```

**Comprobaciones de Validación (v1.5):**
- ❌ Exceso de palabras (Chino >500 caracteres / Inglés >1000 palabras)
- ❌ Terminología profesional de cámara ausente
- ❌ Bloqueo duro de palabras de relleno (masterpiece / obra maestra / ultra-nítido, etc. → error)
- ❌ Conflictos óptico-físicos (ultra gran angular + bokeh, cámara en mano + simetría perfecta)
- ❌ Matriz de conflictos de estilo (IMAX vs VHS, película vs digital, tinta china vs UE5, Cel-Shaded vs PBR realista, Cámara Lenta vs Speed Ramp)
- ❌ Desbordamiento de referencias de assets (imágenes >9 / vídeos >3 / audio >3 / total >12)
- ❌ Bloqueo duro para vídeos largos (>5s) sin división temporal
- ⚠️ Huecos o solapamientos en la división temporal
- ⚠️ Desajuste entre la duración declarada y el punto final del segmento
- ⚠️ Conflictos de lógica de movimiento dentro del segmento
- ⚠️ Detección de riesgo de revisión Seedance: términos de cámara en inglés sin contexto (Dolly / Aerial / Crane / Pan / Arc / Dutch / Steadicam)
- 🌐 Detección automática de idioma (chino / inglés), adaptando estándares de longitud y estrategias de detección por idioma
- 🎬 Comprobaciones de consistencia entre segmentos múltiples (preámbulo de estilo / estructura de iluminación / elementos prohibidos)

**Ejecutar Tests:**
```bash
python -m unittest scripts.test_validate -v
# 54 tests pasan (cubriendo 11 clases de test)
```

---

## 🏗️ Filosofía de Diseño

### Carga Progresiva de Conocimiento (Progressive Disclosure)

Siguiendo las mejores prácticas de Agent Skills:

- **SKILL.md** (~4000 tokens): Flujo de trabajo principal + plantillas estructurales + checklist de calidad
- **references/** (carga bajo demanda): Solo se leen cuando el usuario menciona necesidades de estilo / cámara / calidad
- **scripts/** (ejecución bajo demanda): La validación se ejecuta solo después de generar el prompt

### Ventajas Competitivas

| Dimensión | Enfoque Común | Este Skill |
|-----------|---------------|------------|
| Validación de conformidad | Sugerencias en texto plano | **Validación rigurosa con Python (incl. matriz de conflictos ópticos / de estilo + detección de seguridad de revisión)** |
| Estilos de dirección | Solo directores internacionales | **Internacional + Chino + Cortometraje + Cómic IA + Redes Sociales + Anime + Cel-Shaded CG + Xiaohongshu** |
| Cobertura de escenas | Sesgado hacia cine épico | **17 escenarios verticales + variantes anime + edición de vídeo + kit de amortiguación física** |
| Diseño de sonido | Menciones breves | **Acústica espacial + biblioteca de onomatopeyas por material** |
| Iluminación | "Pon una luz" | **Fuente → Comportamiento → Tono en tres capas + recetas de iluminación + biblioteca de materiales** |
| Multilingüe | Solo chino | **Salida bilingüe chino / inglés, detección automática de idioma** |
| Seguridad en revisión | No contemplado | **Reglas de desambiguación de términos de cámara + detección automática de palabras sueltas** |

---

## 📋 Historial de Versiones

### v1.5.0 (2026-03-27)
- 🎭 **Sistema de Bloqueo de Actores**: Posicionamiento de tres elementos (ubicación + dirección facial + foco de mirada) con vocabulario de modificadores emocionales para escenas multi-personaje
- 🎙️ **Separación Voz en Off / Diálogos**: Plantillas distintas para diálogos en cámara vs. voz en off / monólogo interior, con directiva anti-lip-sync para escenas de VO
- 📐 **Especificidad del Ángulo de Cámara**: Mapeo de ángulos vagos → específicos (ej: "primer plano" → "plano medio corto sobre el hombro, foco en el oyente") con 5 pares comparativos
- 🎬 **Movimiento de Cámara con Motivación Narrativa**: Movimientos de cámara emparejados con propósito narrativo (ej: "empuje lento — revelando conflicto interno")
- 🔀 **Estrategia de Transición entre Segmentos**: 6 tipos de transición (continuidad de mirada / escalada emocional / corte por contraste / salto espacial / elipsis temporal / puente sensorial)
- 🎨 **Selector Rápido de Estilo para Cortometrajes**: Sistema combo de 4 dimensiones (tipo visual × estilo de render × tono de color × género)
- 📝 Plantillas de cortometraje de 1 a 4 variantes (CN diálogo / CN voz en off / EN diálogo / EN voz en off)
- 📝 Nota del Director multi-segmento añade declaración de estrategia de transición
- 📝 5 ejemplos completos: diálogo con giro / monólogo voz en off / conflicto de acción / anime 2D / estrategia de transición
- ✅ 54 tests pasan

### v1.4.0 (2026-03-21)
- 🎬 **Storyboard Multi-Segmento Inteligente**: Vídeos de >15s se dividen automáticamente en múltiples prompts independientes (cada uno ≤15s, mínimo ≥8s)
- 📝 Coherencia multi-segmento: preámbulo de estilo / iluminación en tres capas / diseño sonoro / fotogramas de transición / elementos prohibidos unificados
- 📝 Paso 5 añade plantilla de formato de salida multi-segmento (CN / EN)
- 📝 Nuevo ejemplo completo de 4 segmentos de 60 segundos de Kali/Escrima en el desierto
- 🔧 Script de validación añade `validate_multi_segment()` comprobación de consistencia entre segmentos
- ✅ 54 tests pasan (incl. 4 nuevos tests de validación multi-segmento)

### v1.3.0 (2026-03-21)
- 🌐 **Salida Bilingüe de Prompts**: Usuarios chinos → chino, no chinos → inglés, con detección automática
- 📝 Todas las plantillas estructurales, formatos de entrega y consejos multimodales incluyen ahora versión en inglés
- 🛡️ **Desambiguación de Términos de Cámara (Regla 9)**: Chino usa términos chinos, Inglés usa frases completas — evita falsos positivos en la revisión de Seedance
- 🔧 Validación añade detección de palabras sueltas `check_ambiguous_terms()` + flag `--lang` + conteo por palabras en inglés
- 🔧 Nueva detección de conflicto Cámara Lenta vs Speed Ramp
- 🔧 `detect_language()` ampliado con CJK Extension A + soporte de puntuación de ancho completo
- 📚 `cinematography.md` añade columna "Formato Seguro para Seedance"
- ✅ 50 tests pasan (incl. tests bilingües + de seguridad de revisión)

### v1.2.0 (2026-03-21)
- 🎨 **Estilo Cel-Shaded CG**: Nuevo registro parametrizado completo en cuatro ejes (distinto de la energía explosiva del anime — posicionado para narrativa contemplativa)
- 🧱 **Biblioteca de Materiales Anime/NPR**: Piel anime / cabello / metal cartoon / tela cartoon — 4 materiales no fotorrealistas
- 📦 **Variante Game PV Anime**: Plantilla de escenario añade sub-plantilla Cel-Shaded + ejemplo de personaje con atributo de hielo
- ⚠️ Matriz de conflictos añade: Cel-Shade vs Material PBR Realista
- 🔧 Validación añade detección de conflicto de estilo Cel-Shade vs PBR

### v1.1.0 (2026-03-20)
- 🎬 **Mejora de Cámara**: Psicología narrativa de distancias focales, paradigmas de enfoque dinámico, capítulo de montajes físicos (7 rigs especiales)
- 🎨 **Estilos de Dirección**: Fincher / Deakins / Kurosawa / Makoto Shinkai + Explosión Anime / Estética Xiaohongshu (incl. prompts seguros sin nombres + elementos prohibidos)
- 💡 **Mejora de Calidad**: Manifiesto anti-plástico, biblioteca de películas (5 tipos), biblioteca de texturas de materiales (8 tipos), referencia rápida de combos de iluminación (4 sets), biblioteca de imperfecciones orgánicas, matriz de conflictos de calidad
- 🎬 **Expansión de Escenas**: Game PV / Terror-Thriller / Viaje-Ciudad / Mascotas / Before-After / Meme-Loop, total 16 escenarios + apéndice de amortiguación física
- 🎙️ **Mejora de Sonido**: Modificadores de acústica espacial (7 tipos), refinamiento de onomatopeyas por material (7 pares)
- 🔧 **Mejora de Validación**: Palabras de relleno warning → error bloqueo duro, detección de conflictos óptico-físicos, matriz de conflictos de estilo, división temporal sensible a la duración, 35 tests pasan

### v1.0.0 (2026-03-19)
- 🎉 Primer lanzamiento
- SKILL.md flujo de trabajo principal
- 6 archivos de base de conocimiento profesional
- Script de validación Python + casos de prueba
- 20+ mapeos de estilos de dirección
- 10 plantillas de escenarios verticales

---

## 📄 Licencia

MIT-0 (MIT No Attribution) License
