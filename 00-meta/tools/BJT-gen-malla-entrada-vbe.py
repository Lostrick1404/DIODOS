"""BJT — Diagrama malla de entrada (VCC–RB–VBE).

Genera un esquema simple para justificar la LVK de la malla de entrada en polarización fija.

"""

# ::SCRIPT_METADATA::
# script_id: BJT-gen-malla-entrada-vbe
# module: BJT
# generates:
#   - topics/02-transistor-bjt/assets/bjt-malla-entrada-vbe.png
# referenced_by:
#   - topics/02-transistor-bjt/Notas/Nota4.md
# last_updated: 2026-04-22

import os

import matplotlib

matplotlib.use("Agg")  # backend sin GUI

import schemdraw
import schemdraw.elements as elm


def main() -> None:
    out_path = (
        "/workspaces/DIODOS-Y-TRANSISTORES/topics/02-transistor-bjt/assets/"
        "bjt-malla-entrada-vbe.png"
    )
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    dpi = 300
    fontsize = 13

    with schemdraw.Drawing(show=False) as d:
        d.config(unit=3.0, fontsize=fontsize)
        vcc = d.add(elm.SourceV().up().label("$V_{CC}$", loc="left", ofst=0.3))
        d.add(elm.Line().right())

        rb = d.add(elm.Resistor().right().label("$R_B$", loc="top", ofst=0.25))
        rb.label("$I_B$", loc="bot", ofst=0.25)

        d.add(elm.Line().right())

        # Representación de la unión B-E como diodo con caída V_BE ~ 0.7 V
        d.add(elm.Diode().down().label("$V_{BE}=0.7\\,V$", loc="right", ofst=0.25))

        d.add(elm.Line().left().tox(vcc.start[0]))
        d.add(elm.Line().up().toy(vcc.start[1]))

        d.save(out_path, dpi=dpi)


if __name__ == "__main__":
    main()
