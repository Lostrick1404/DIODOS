# 🗺️ Mapa del Repositorio (Repo-Map)

Este documento proporciona una visión estructurada del proyecto para facilitar la navegación y la comprensión de la arquitectura de contenidos y herramientas.

## 📂 Estructura Principal

```text
DIODOS-Y-TRANSISTORES/
├── 00-meta/                # Configuración, estándares y herramientas transversales
│   ├── naming-conventions.md # Reglas de nomenclatura para archivos y símbolos
│   ├── repo-map.md          # [ESTE ARCHIVO] Mapa estructural del repo
│   ├── standards.md         # Estándares técnicos (LaTeX, Schemdraw)
│   └── tools/               # Scripts de automatización y generación de assets
├── topics/                 # Contenido educativo organizado por módulos
│   ├── 01-circuitos-diodos/ # Módulo DIO: Teoría y práctica de diodos
│   ├── 02-transistor-bjt/   # Módulo BJT: Transistores de unión bipolar
│   ├── 03-transistor-fet/   # Módulo FET: Transistores de efecto de campo
│   ├── 04-amplificadores/   # Módulo AMP: Respuesta en frecuencia y diseño
│   └── 05-proyecto-final/   # Módulo PRO: Diseño de fuente de alimentación
├── audits/                 # Reportes de calidad y validación del repositorio
├── outputs/                # Archivos generados temporalmente (no trackeados)
└── sandbox/                # Entorno de pruebas y experimentación
```

## 🛠️ Herramientas y Automatización (`00-meta/tools/`)

Los scripts siguen la convención `[PREFIJO]-gen-[nombre].py`:

*   **DIO:** Generación de curvas I-V, rectificadores y circuitos con diodos.
*   **BJT:** Curvas características, polarización y modelos equivalentes (Thévenin).
*   **FET/AMP:** Respuesta en frecuencia y curvas de transferencia.

## 📝 Convenciones de Contenido

Cada módulo en `topics/` mantiene la siguiente estructura interna:
*   `Notas/`: Documentos conceptuales detallados (ej. `Nota4.md`).
*   `assets/`: Imágenes, esquemas y gráficos generados.
*   `theory/` / `methods/`: Fundamentos y procedimientos paso a paso.
*   `problems/` / `solutions/`: Ejercicios prácticos de aplicación.

---
> 🏠 [Volver al README](../../README.md) | 📑 [Índice de la Wiki](../../WIKI_INDEX.md)
