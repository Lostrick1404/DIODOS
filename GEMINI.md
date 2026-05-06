# GEMINI.md — Contexto para Google Gemini

> **Hereda de:** [AGENTS.md](AGENTS.md) — Fuente de verdad centralizada
> **Última sincronización:** 2026-03-20

---

## Instrucciones para Gemini

1. **Leer** [AGENTS.md](AGENTS.md) como primera acción obligatoria.
2. **Consultar** `manifest.json` del módulo objetivo.
3. **Seguir** las directivas específicas en `directives.md` del módulo.

---

## Referencias Rápidas

| Documento | Propósito |
|-----------|-----------|
| [AGENTS.md](AGENTS.md) | Directiva general de comportamiento IA |
| [ARQUITECTURE.md](ARQUITECTURE.md) | **Fuente de verdad única** (Mapa, Nomenclatura, Estándares) |
| [scripts/Control_Scripts.md](scripts/Control_Scripts.md) | Registro de scripts e imágenes |
| [glossary.md](glossary.md) | Glosario de términos técnicos |
| [WIKI_INDEX.md](WIKI_INDEX.md) | Mapa de navegación |

---

### Preferencias de Estilo y GUI

- **Comentarios:** Didácticos y técnicos en todo el código.
- **GUI:** Paletas oscuras (estilo editor) para Tkinter.
- **Salida:** Tablas de resumen seguidas de gráficos.

### Directiva de mejora de redacción para Notas/

Cuando el usuario proporcione texto informal para `Notas/`, el agente **debe** mejorar automáticamente:

1. **Coherencia:** Conexión lógica entre ideas.
2. **Orden:** Estructura con encabezados y listas.
3. **Contexto:** Definiciones y notación necesarias.

Solo se mejora la forma; los valores técnicos se respetan fielmente.

### Entorno de ejecución

```bash
# Activar entorno Python
source .venv/bin/activate  # Linux/Codespaces

# Para GUI en Codespaces
export DISPLAY=:1

# Ejecutar scripts desde la raíz
python scripts/DIO-gen-curva-iv.py
```

---

## Arquitectura (Resumen)

```
topics/
├── 01-circuitos-diodos/  (DIO)
├── 02-transistor-bjt/    (BJT)
├── 03-transistor-fet/    (FET)
├── 04-amplificadores/    (AMP)
└── 05-proyecto-final/    (PRO)
```

Cada módulo contiene: `README.md`, `manifest.json`, `directives.md`, `theory/`, `assets/`, `Notas/`.

---

## Sincronización

Este archivo hereda de `AGENTS.md`. Ante cambios estructurales, actualizar primero `AGENTS.md` y luego propagar a este archivo.
