"""
::SCRIPT_METADATA::
script_id: BJT-gen-emisor-comun-polarizacion-fija
module: BJT
generates:
  - bjt-emisor-comun-polarizacion-fija.png
referenced_by:
  - topics/02-transistor-bjt/Notas/Nota4.md
last_updated: 2026-04-22
"""

import matplotlib
matplotlib.use('Agg')

from pathlib import Path

import schemdraw
import schemdraw.elements as elm


OUTPUT_PATH = Path("topics/02-transistor-bjt/assets/bjt-emisor-comun-polarizacion-fija.png")


def build_diagram() -> schemdraw.Drawing:
    d = schemdraw.Drawing(unit=3.0, fontsize=14)

    # Transistor
    q = d.add(elm.BjtNpn(circle=True).at((0, 0)))

    # Emitter to ground
    d.add(elm.Line().down().at(q.emitter).length(1.5))
    d.add(elm.Ground())

    # Collector to Rc
    d.add(elm.Line().up().at(q.collector).length(1))
    node_c = d.here
    rc = d.add(elm.Resistor().up().label('$R_C$', loc='bot').label('$I_C$', loc='top'))
    node_vcc_c = d.here

    # Base to Rb
    d.add(elm.Line().left().at(q.base).length(2.5))
    node_b = d.here
    rb = d.add(elm.Resistor().up().toy(node_vcc_c).label('$R_B$', loc='bot').label('$I_B$', loc='top'))
    node_vcc_b = d.here

    # Connect Rb and Rc to Vcc
    d.add(elm.Line().at(node_vcc_b).to(node_vcc_c))
    d.add(elm.Line().up().at(node_vcc_c).length(0.5))
    d.add(elm.Vdd().label('$V_{CC}$'))

    # Input (Base)
    d.add(elm.Capacitor().left().at(node_b).label('$C_1$', loc='top'))
    d.add(elm.Dot(open=True))
    d.add(elm.Label().label('$V_i$', loc='left'))

    # Output (Collector)
    d.add(elm.Line().right().at(node_c).length(1.5))
    d.add(elm.Capacitor().right().label('$C_2$', loc='top'))
    d.add(elm.Dot(open=True))
    d.add(elm.Label().label('$V_o$', loc='right'))

    # VCE and VBE labels
    d.add(elm.Gap().at(node_c).to(q.emitter).label(['$+$', '$V_{CE}$', '$-$']))
    
    # For VBE, we can add a gap from base to emitter, but space might be tight.
    # We can place it slightly to the right of the base.
    d.add(elm.Gap().at(q.base).to(q.emitter).label(['$+$', '$V_{BE}$', '$-$'], loc='left'))

    return d


def main() -> None:
    # Ensure directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Build and save
    diagram = build_diagram()
    diagram.save(str(OUTPUT_PATH), dpi=600)


if __name__ == "__main__":
    main()
