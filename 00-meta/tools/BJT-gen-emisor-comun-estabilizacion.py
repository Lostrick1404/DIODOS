"""
::SCRIPT_METADATA::
script_id: BJT-gen-emisor-comun-estabilizacion
module: BJT
generates:
  - bjt-emisor-comun-estabilizacion.png
referenced_by:
  - topics/02-transistor-bjt/Notas/Nota4.md
last_updated: 2026-04-22
"""

import matplotlib

matplotlib.use("Agg")

from pathlib import Path

import schemdraw
import schemdraw.elements as elm


OUTPUT_PATH = Path("topics/02-transistor-bjt/assets/bjt-emisor-comun-estabilizacion.png")


def build_diagram() -> schemdraw.Drawing:
    d = schemdraw.Drawing(show=False)
    d.config(unit=3.5, fontsize=14)

    # Transistor NPN (Emisor común)
    q = d.add(elm.BjtNpn(circle=True).at((0, 0)))

    # Emisor -> RE -> tierra
    d.add(elm.Line().down().at(q.emitter).length(0.8))
    node_e = d.here
    d.add(elm.Resistor().down().label("$R_E$", loc="right", ofst=0.2).label("$I_E$", loc="left", ofst=0.2))
    d.add(elm.Ground())

    # Colector -> RC -> VCC
    d.add(elm.Line().up().at(q.collector).length(0.8))
    node_c = d.here
    d.add(elm.Resistor().up().label("$R_C$", loc="right", ofst=0.2).label("$I_C$", loc="left", ofst=0.2))
    node_vcc_c = d.here

    # Fuente VCC (bus superior)
    d.add(elm.Line().up().at(node_vcc_c).length(0.5))
    vcc = d.add(elm.Vdd().label("$V_{CC}$"))
    vcc_top = d.here

    # Rama del divisor: desde bus superior hacia base
    d.add(elm.Line().left().at(vcc_top).length(2.4))
    node_vcc_div = d.here

    r1 = d.add(elm.Resistor().down().label("$R_1$", loc="right", ofst=0.2))
    node_b = d.here

    d.add(elm.Resistor().down().label("$R_2$", loc="right", ofst=0.2))
    d.add(elm.Ground())

    # Conectar nodo del divisor a la base del transistor
    d.add(elm.Line().right().at(node_b).to(q.base))

    # Etiqueta de corriente de base
    d.add(elm.CurrentLabel(top=True).at(q.base).label("$I_B$"))

    # Marcador de VCE
    d.add(elm.Gap().at(node_c).to(node_e).label(["$+$", "$V_{CE}$", "$-$"]))

    return d


def main() -> None:
  OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
  diagram = build_diagram()
  diagram.save(str(OUTPUT_PATH), dpi=300, transparent=False)


if __name__ == "__main__":
    main()
