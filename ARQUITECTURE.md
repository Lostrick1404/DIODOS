# 🏗️ Arquitectura y Estándares del Repositorio — Diodos y Transistores

Este documento unifica los estándares, convenciones, estructura y metodologías del proyecto. Es la **fuente de verdad principal** para desarrolladores y asistentes de IA.

---

## 1. Visión General y Mapa del Repositorio

El proyecto está organizado como un **Jardín Digital**: modular, interconectado y procesable por IA.

### 📂 Estructura Principal

```text
DIODOS-Y-TRANSISTORES/
├── 00-meta/                # Plantillas (Depreciado a favor de este archivo)
├── scripts/                # Scripts de automatización y generación de assets
├── topics/                 # Contenido educativo organizado por módulos
│   ├── 01-circuitos-diodos/ # Módulo DIO: Teoría y práctica de diodos
│   ├── 02-transistor-bjt/   # Módulo BJT: Transistores de unión bipolar
│   ├── 03-transistor-fet/   # Módulo FET: Transistores de efecto de campo
│   ├── 04-amplificadores/   # Módulo AMP: Respuesta en frecuencia y diseño
│   └── 05-proyecto-final/   # Módulo PRO: Diseño de fuente de alimentación
├── AUDITORIA.md            # Historial de auditorías y validaciones (UNIFICADO)
├── outputs/                # Archivos generados temporalmente (no trackeados)
└── sandbox/                # Entorno de pruebas y experimentación
└── ARQUITECTURE.md         # [ESTE ARCHIVO] Unificación de estándares
```

### 📝 Organización de Módulos (`topics/`)

Cada módulo mantiene la siguiente estructura interna:
*   `Notas/`: Documentos conceptuales detallados y borradores.
*   `assets/`: Imágenes, esquemas y gráficos generados.
*   `theory/`: Fundamentos teóricos y ecuaciones.
*   `formularios/`: Resúmenes de fórmulas clave.

---

## 2. Convenciones de Nomenclatura

### Patrón de Nombres de Archivos
```
[PREFIJO]-[XX]-[Contenido]-[Tipo].md
```

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `PREFIJO` | 3 letras del módulo | `DIO`, `BJT`, `FET`, `AMP`, `PRO` |
| `XX` | Número de subtema (2 dígitos) | `01`, `02`, ..., `08` |
| `Contenido` | Nombre descriptivo | `Polarizacion`, `Rectificacion` |
| `Tipo` | Clasificación | `Intro`, `Teoria`, `Metodos`, `Problemas`, `Soluciones` |

### Bloques de Metadatos (`::METADATA::`)
Todo archivo `.md` debe comenzar con este bloque para facilitar el procesamiento por IA:

```markdown
<!--
::METADATA::
type: [theory|method|problem|solution|reference|index|cheatsheet]
topic_id: [id-del-tema]
file_id: [nombre-archivo-sin-extension]
status: [draft|review|stable]
audience: [student|ai_context|both]
last_updated: YYYY-MM-DD
-->
```

---

## 3. Estándares Técnicos y Directivas de IA

### Notación Matemática (LaTeX)
*   **Inline:** `$ E = mc^2 $`
*   **Bloque:** `$$ P = V \cdot I $$`
*   **Tablas:** No usar `|` dentro de fórmulas en tablas. Usar `\lvert` y `\rvert` para valor absoluto.

### Generación de Gráficas (Python + Schemdraw)
1.  **Escalas:** Usar insets o gráficas separadas para magnitudes muy dispares (ej. $I_D$ vs $I_S$).
2.  **Schemdraw — Reglas de Oro:**
    *   **No usar `\n` en `.label()`:** Para mostrar múltiples datos, usar llamadas `.label()` separadas con diferentes `loc` (ej. `loc='right'` y `loc='bot'`).
    *   **Etiquetas en Inductores:** NUNCA usar `.label()` directamente sobre `Inductor2` (los bumps tapan el texto). Usar `elm.Label()` con coordenadas explícitas y offset de `±1.1 u`.
    *   **Transformadores:** El secundario debe usar `.flip()` para que los bumps miren al núcleo. Separación mínima primario-secundario: `2.5 u`. Elevación de etiqueta de núcleo: `+0.70 u`.
    *   **Fuentes Sinusoidales:** Usar `ofst ≥ 0.55` en etiquetas para no solapar con el conductor.
    *   **Rectificadores:** Colocar $R_L$ horizontalmente a la altura media del secundario (`sec_mid_y`). Aumentar loops del primario (≥ 4) si hay solapamiento vertical.
    *   **Backend:** Usar `matplotlib.use('Agg')` al inicio de todo script para ejecución sin GUI. Para GUIs interactivas, usar `matplotlib.use('TkAgg')`.
3.  **Estándar H3 para Circuitos Complejos (Multiplicadores, Fuentes):**
    *   **Parámetros:** `unit=3.5`, `comp_length=3.5`, `separation=2.0`, `fontsize=13`, `dpi=300`.
    *   **Layout:** Flujo L→R. Línea superior para positivos, línea inferior para GND.
    *   **Paleta de Colores:** Azul (Fuente), Rojo (Diodo), Verde (Capacitor), Naranja (Resistor), Gris (Conexión), Violeta (Voltaje).
    *   **Etiquetas:** Prohibido el solapamiento. Superior: `loc='top'`, `ofst=0.3`. Inferior: usar coordenadas absolutas desplazadas `(x - 0.5, y)`.
4.  **Registro:** Todo script en `scripts/` debe registrarse en `Control_Scripts.md` y seguir el patrón `[PREFIJO]-gen-[nombre].py`. Debe incluir metadatos `::SCRIPT_METADATA::`.

### Gestión de Imágenes
*   **Limpieza:** `media/generated/` solo debe contener archivos con uso actual. Imágenes reemplazadas deben eliminarse.
*   **Referencia:** Toda imagen debe estar en un `.md` y en `Control_Scripts.md`. No se permiten cargas manuales; todas deben provenir de scripts.

### Entorno de Ejecución y Herramientas
*   **Python:** `.venv/bin/activate` (Linux) o `.venv/Scripts/Activate.ps1` (Windows). Ejecutar scripts siempre desde la raíz.
*   **Shell (IA):** Preferir Bash. En Windows, usar rutas con forward slash (`/`).
*   **PowerShell (Local):** Usar el operador de llamada `&` para ejecutar Python: `& "ruta/python.exe" "script.py"`. Separar comandos con `;`.
*   **Librerías Clave:** `numpy`, `matplotlib`, `scipy`, `schemdraw`, `sympy`, `SciencePlots`.

---

## 4. Temario y Mapeo de Contenidos

| Módulo | Prefijo | Temas Principales |
|--------|---------|-------------------|
| **01. Diodos** | `DIO` | Rectificación, Zener, Recortadores, Sujetadores. |
| **02. BJT** | `BJT` | Polarización (EC, BC, CC), Conmutación, Estabilidad. |
| **03. FET** | `FET` | JFET, MOSFET, Autopolarización, Divisor de voltaje. |
| **04. Amplificadores** | `AMP` | Pequeña señal, Modelos $r_e$ e híbrido, Respuesta en frecuencia. |
| **05. Proyecto** | `PRO` | Diseño de fuente de alimentación regulada. |

---

## 6. Bibliografía de Referencia

### Fuentes Principales

1. **Boylestad & Nashelsky:** *Electrónica: Teoría de Circuitos*. (Pearson, 11ª ed.)
   - Cap. 1-3: Diodos | Cap. 4-5: BJT | Cap. 6-7: FET | Cap. 8-10: Pequeña señal.
2. **Sedra & Smith:** *Circuitos Microelectrónicos*. (Oxford, 7ª ed.)
   - Cap. 3: Diodos | Cap. 5: BJT/MOSFET | Cap. 6-7: Amplificadores.
3. **Malvino & Bates:** *Principios de Electrónica*. (McGraw-Hill, 7ª ed.)
   - Cap. 2-4: Diodos | Cap. 5-8: BJT | Cap. 13-14: FET | Cap. 18: Fuentes reguladas.

---

## 7. Metodología de Estudio y Trabajo

### Ruta de Aprendizaje y Prerrequisitos
1.  **Fundamentos (DIO):** Diodos e introducción a semiconductores.
    - *Prerrequisito:* Análisis de circuitos DC, Ley de Ohm, Kirchhoff.
2.  **Dispositivos (BJT/FET):** Polarización DC.
    - *Prerrequisito:* Módulo 01 completo.
3.  **Sistemas (AMP):** Amplificadores (Análisis AC).
    - *Prerrequisito:* Módulos 02 y 03 completos, análisis AC básico.
4.  **Aplicación (PRO):** Proyecto final de fuente de poder.
    - *Prerrequisito:* Todos los módulos anteriores.

### Flujo de Trabajo en Subtemas
Para cada subtema, el orden de creación/estudio es:
`Intro` → `Teoria` → `Metodos` → `Problemas` → `Solutions`.

---

## 🤖 Instrucciones para Asistentes de IA

1.  **Contexto Obligatorio:** Antes de cualquier modificación, lee este archivo (`ARQUITECTURE.md`) y el `AGENTS.md` en la raíz.
2.  **Sincronización:** Si creas un nuevo archivo, asegúrate de que cumpla con las **Convenciones de Nomenclatura** y el bloque de **Metadatos**.
3.  **Redacción:** Mejora automáticamente la coherencia y estructura de los textos en `Notas/`, manteniendo la precisión técnica.
4.  **Generación de Código:** Sigue estrictamente las directivas de la Sección 3 para scripts de Python y Schemdraw.
