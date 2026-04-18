[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Español | [Português](README.pt.md) | [Français](README.fr.md)

<p align="center">
  <img src="assets/logo.svg" width="128" height="128" alt="Seedance Shot Design Logo">
</p>

<h1 align="center">Seedance2.0 Shot Design</h1>

<p align="center">
  <strong>Diseñador de Lenguaje Cinematográfico</strong>
</p>

<p align="center">
  <a href=""><img src="https://img.shields.io/badge/version-1.9.0-blue.svg" alt="Versión"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT--0-green.svg" alt="Licencia"></a>
  <a href=""><img src="https://img.shields.io/badge/platform-Seedance_2.0-purple.svg" alt="Plataforma"></a>
</p>

<p align="center">
  Convierte tus ideas vagas de vídeo en <strong>prompts cinematográficos profesionales</strong> listos para Jimeng Seedance 2.0, con un solo clic.
</p>

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
| 📦 **20 Plantillas de Escenarios** | E-commerce / Xianxia / Cortometraje / Gastronomía / MV / Plano Secuencia / Automoción / Macro / Naturaleza / Game PV / Terror / Viajes / Mascotas / Transformación / Loop / Edición de Vídeo / Extensión de Vídeo / Completado de Historia / Narración Multiframe |
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
    ├── scenarios.md             # Plantillas de escenarios verticales (20 escenarios + variantes anime + edición de vídeo + kit de amortiguación física)
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

**Comprobaciones de Validación:**
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
| Cobertura de escenas | Sesgado hacia cine épico | **20 escenarios verticales + variantes anime + edición de vídeo + kit de amortiguación física** |
| Diseño de sonido | Menciones breves | **Acústica espacial + biblioteca de onomatopeyas por material** |
| Iluminación | "Pon una luz" | **Fuente → Comportamiento → Tono en tres capas + recetas de iluminación + biblioteca de materiales** |
| Multilingüe | Solo chino | **Salida bilingüe chino / inglés, detección automática de idioma** |
| Seguridad en revisión | No contemplado | **Reglas de desambiguación de términos de cámara + detección automática de palabras sueltas** |

---

## 📋 Historial de Versiones

### v1.9.0 (2026-04-18)
- 🎬 **Referencia Rápida de Planos Guía-Narrativos (nuevo capítulo)**: Nueva Sección IX en `cinematography.md` — 8 tipos de planos de guía/seguimiento/revelación (Leading Shot, Following Shot, Side Tracking, Low Angle Follow, Long Lens Follow, Epic Drone Reveal, Reveal Through, Orbit Follow), con frases gatillo bilingües y prompts de ejemplo
- 🚁 **Epic Drone Reveal**: Añadido como movimiento de cámara Level 1 independiente — ascenso lento desde detrás/ángulo bajo revelando el paisaje épico; estructura narrativa distinta a los planos aéreos genéricos
- 🌿 **Reveal from Behind / Through Shot**: Nueva entrada Level 1 para planos de penetración de obstáculos (cámara empujando a través de bambú/multitud/cortina para revelar), con guía de frases seguras
- 🚶 **Leading Shot**: Nueva entrada Level 1 para movimiento de cámara que retrocede delante del sujeto, transmitiendo viaje y agencia del protagonista
- ⚡ **Snap Zoom / Crash Zoom**: Añadido a combos Level 3 — salto explosivo de distancia focal para impacto cómico, énfasis de susto y sincronización de beat MV
- 🌀 **Orbit Follow**: Añadido a combos Level 3 — órbita + tracking simultáneos donde el punto pivote se mueve con el sujeto, distinto de las órbitas de sujeto estático

### v1.8.5 (2026-04-08)
- 🌐 **Adaptación a Runway**: Límites de activos clarificados para usuarios de Runway (≤5 imágenes, ≤3 videos) y estrategias claras de bypass para la moderación de rostros humanos (difuminado o cambio de estilo NPR).
- 🎞️ **Interpolación de Fotograma Inicial y Final**: Se agregó el 7º patrón de referencia multimodal (`@Image1 as start frame, @Image2 as end frame`) para transiciones precisas.
- 🎬 **Dos Nuevos Escenarios de Efectos**:
  - `Freeze Time (Tiempo Congelado)`: La cámara se mueve dramáticamente a través de elementos del escenario completamente congelados.
  - `Multishot Video (Video Multitoma)`: Evitas la restricción de "toma única", permitiendo generar múltiples cortes de montaje rápidos en una sola generación.

- 🚀 **Escenarios POV Extremos**: Se agregó la nueva plantilla de escenario #21 que se centra en "lógica de seguimiento de la cabeza", "FPV de proyectiles a alta velocidad (espadas/flechas voladoras)" y "vuelo de criaturas".
- 🎧 **Exclusión de Audio Inmersivo**: Directivas estrictas de exclusión de audio introducidas para plantillas POV (SOLO sonido ambiental, SIN BGM ni diálogos) para evitar que la IA arruine la inmersión.
- 🧹 **Regla de Purificación de Fondo**: Se aclaró que las imágenes de personajes de referencia deben usar un "fondo blanco puro/en blanco" para evitar contaminar el entorno de video en la generación de Imagen a Video.

### v1.8.4 (2026-04-08)
- 🔗 **Guía de integración CLI**: Nueva sección en `seedance-specs.md` con mapeo de comandos CLI de Jimeng (`text2video` / `image2video` / `multiframe2video` / `multimodal2video`), gestión de tareas asíncronas y documentación de canales VIP
- 🎞️ **Plantilla de narración multiframe**: Nueva plantilla de escenario (#20) para `multiframe2video` — sube 2-9 imágenes de fotogramas clave y el motor compone automáticamente un video narrativo coherente
- 📚 **Enrutamiento de base de conocimientos**: Se añadieron entradas de enrutamiento multiframe y CLI a la tabla de inferencia semántica del Paso 2

### v1.8.3 (2026-04-08)
- 🎭 **Regla Descriptivo > Narrativo**: Nueva regla central (#12) — solo escribir lo que la cámara VE (palabras visuales), nunca lo que el personaje SIENTE (palabras emocionales). Todas las emociones deben convertirse en expresiones físicas visibles
- ✍️ **Inglés Progresivo**: Reglas de ensamblaje requieren forma -ing para acciones en inglés (`running` no `runs`) — el progresivo implica movimiento continuo
- 🎯 **Tono de Movimiento Anticipado**: El preámbulo de estilo declara la energía de movimiento general (`dynamic motion` / `serene atmosphere`), fijando la base de movimiento al inicio

### v1.8.2 (2026-04-07)
- 🎥 **Regla Un-Plano-Un-Movimiento**: Nueva regla central (#10) — un solo movimiento de cámara por segmento temporal. Combinar movimientos (ej: push-in + pan) causa vibración. Movimiento del sujeto y de la cámara deben describirse por separado
- 🖼️ **Regla de Oro I2V**: Nueva regla central (#11) y sección I2V dedicada — al generar vídeo desde imagen, solo describir movimiento/cambios, nunca re-describir el contenido estático del primer fotograma. Introduce frase ancla `preserve composition and colors`
- 📏 **Longitud Óptima del Prompt**: Guía de punto óptimo 60-100 palabras — menos es vago, más de 100 causa deriva conceptual e instrucciones conflictivas
- 💪 **Modificadores de Intensidad de Movimiento**: Nueva tabla de referencia bilingüe con 6 niveles de intensidad (violento → suave → gradual) y ejemplos Do/Don't para eliminar "movimiento pastoso"
- 🎤 **Ritmo sobre Especificaciones**: Las reglas de ensamblaje prefieren explícitamente palabras de ritmo semántico (gentle/gradual/smooth) sobre parámetros técnicos (24fps/f2.8)
- 🎬 **Mejores Prácticas para Vídeo de Referencia**: Restricciones prácticas — ideal 3-8s, plano continuo (sin cortes), intención única (sujeto O cámara, no ambos)

### v1.8.1 (2026-04-07)
- 🛡️ **Cumplimiento de Seguridad**: Resuelto el flag "patrones sospechosos" de ClawHub OpenClaw — validación Python convertida a checklist estructurada de 7 reglas LLM-nativas. Scripts Python mantenidos como herramientas de desarrollo independientes
- 🎯 **Optimización de Frases Activadoras**: Triggers reducidos de 40+ a 15 términos profesionales de alta señal, reduciendo activaciones no deseadas

### v1.8.0 (2026-04-05)
- 🎤 **Sistema de Control de Voz e Idioma**: Clonación de timbre por referencia de vídeo, control de dialecto/acento, mezcla de diálogos multilingüe, estilos vocales especiales (documental/comedia/ópera/ASMR)
- 📹 **Guía de Referencia Multimodal**: Actualización de 4 tips a 6 patrones de referencia core (primer fotograma/cámara/acción/cámara+acción/timbre/efectos)
- 📏 **Escenario de Extensión de Vídeo**: Templates de extensión adelante/atrás, técnicas de continuación seamless, corrección cognitiva de duración
- 📋 **Escenario de Completado de Historia**: Storyboard→vídeo, animación de viñetas, imagen→vídeo emocional
- 🎬 **Referencia Rápida de Efectos Creativos**: Keywords VFX — zoom Hitchcock, ojo de pez, partículas, speed ramp, transición freeze, tinta china, morphing
- 🎭 **Guía de Interpretación Emocional**: Tabla de especificidad emocional, triggers de transición emocional, uso de vídeo de referencia emocional

### v1.7.2 (2026-04-02)
- 🎯 **Expansión de Palabras Activadoras**: 20+ triggers chinos y 10+ ingleses para expresiones cotidianas ("haz un vídeo", "crear clip", "movimiento de cámara")

### v1.7.1 (2026-03-29)
- 🔒 **Optimización de Seguridad**: Resueltos flags de seguridad de ClawHub manteniendo funcionalidad completa

### v1.7.0 (2026-03-28)
- 🚨 **Step 3 Reglas de Ensamblaje Obligatorias**: Iluminación de tres capas en línea propia/línea SFX estandarizada/elementos prohibidos unificados/secciones no-template prohibidas
- ⛔ **Step 4 Bloqueo de Validación**: Prompts que no pasan validación no se muestran al usuario
- 📋 **Step 5 Formato Obligatorio**: Template de salida Tema+Nota del Director+bloque de código
- 🎯 **Step 2 Extracción de Parámetros**: No solo "cargar" bases de conocimiento sino extraer e insertar parámetros específicos

### v1.6.0 (2026-03-28)
- 🧠 **Enrutamiento Semántico Inteligente**: Step 2 de "trigger explícito" a enrutamiento de tres capas — carga permanente/inferencia semántica/especificación explícita
- 🎯 **Step 1 Inferencia Inteligente**: Inferencia activa de parámetros desde una sola frase, preguntas limitadas a 1-2

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
