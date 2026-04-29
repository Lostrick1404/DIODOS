"""Genera un diagrama del circuito del Ejercicio (Nota 5) — Polarización por divisor (Thévenin).

Salida:
- topics/02-transistor-bjt/assets/bjt-nota5-diagrama-polarizacion-divisor.png
"""

# ::SCRIPT_METADATA::
# script_id: BJT-gen-nota5-diagrama-polarizacion-divisor
# module: BJT
# generates:
#   - topics/02-transistor-bjt/assets/bjt-nota5-diagrama-polarizacion-divisor.png
# referenced_by:
#   - topics/02-transistor-bjt/Notas/Nota5.md
# last_updated: 2026-04-29

import matplotlib

matplotlib.use("Agg")  # backend sin GUI

import schemdraw
import schemdraw.elements as elm


def main() -> None:
    # Valores (según Nota5)
    vcc = 15.0

    rc_ohm = 500.0
    re_ohm = 495.0
    r1_ohm = 12.07e3
    r2_ohm = 8.50e3

    vc_v = 10.0
    vb_v = 5.7
    ve_v = 5.0

    ic_ma = 10.0
    vce_v = 5.0

    unit = 3.2
    fontsize = 12

    d = schemdraw.Drawing(unit=unit)
    d.config(fontsize=fontsize, bgcolor="white", color="black", margin=0.3)

    # Coordenadas de referencia
    gnd_y = 0.0
    vcc_y = 6.0
    x_src = 1.0
    x_div = 5.0
    x_q = 11.0
    y_base = 3.0

    # Fuente VCC
    src = d.add(
        elm.SourceV()
        .at((x_src, gnd_y))
        .up()
        .to((x_src, vcc_y))
        .label(f"$V_{{CC}}={vcc:.0f}\\,V$", loc="left", ofst=0.25)
    )
    d.add(elm.Ground().at((x_src, gnd_y)))
    d.add(elm.Dot().at(src.end))

    # Barra superior (VCC)
    d.add(elm.Line().at(src.end).right().to((x_q + 1.5, vcc_y)))

    # Transistor (base en (x_q, y_base))
    q = d.add(elm.BjtNpn().at((x_q, y_base)))
    q.label("Q1", loc="right", ofst=0.2)
    q.label("2N2222", loc="right", ofst=0.7)

    # RC: desde barra superior hasta colector
    d.add(
        elm.Resistor()
        .down()
        .at((q.collector[0], vcc_y))
        .to(q.collector)
        .label(f"$R_C\\approx {rc_ohm:.0f}\\,\\Omega$", loc="right", ofst=0.2)
    )
    d.add(elm.Dot().at(q.collector))

    # RE: desde emisor a tierra
    d.add(
        elm.Resistor()
        .down()
        .at(q.emitter)
        .to((q.emitter[0], gnd_y))
        .label(f"$R_E\\approx {re_ohm:.0f}\\,\\Omega$", loc="right", ofst=0.2)
    )
    d.add(elm.Dot().at(q.emitter))

    # Línea de tierra (bus inferior)
    d.add(elm.Line().at((x_src, gnd_y)).right().to((x_q + 1.5, gnd_y)))

    # Divisor de base (a la izquierda del transistor)
    base_node = (x_div, y_base)
    d.add(elm.Dot().at(base_node))

    # R1: de VCC a nodo base
    d.add(
        elm.Resistor()
        .down()
        .at((x_div, vcc_y))
        .to(base_node)
        .label(f"$R_1\\approx {r1_ohm/1e3:.2f}\\,k\\Omega$", loc="right", ofst=0.2)
    )
    d.add(elm.Dot().at((x_div, vcc_y)))
    d.add(elm.Line().at((x_div, vcc_y)).left().to((x_src, vcc_y)))

    # R2: del nodo base a tierra
    d.add(
        elm.Resistor()
        .down()
        .at(base_node)
        .to((x_div, gnd_y))
        .label(f"$R_2\\approx {r2_ohm/1e3:.2f}\\,k\\Omega$", loc="right", ofst=0.2)
    )
    d.add(elm.Dot().at((x_div, gnd_y)))
    d.add(elm.Line().at((x_div, gnd_y)).right().to((x_src, gnd_y)))

    # Conexión nodo base -> base del transistor
    d.add(elm.Line().at(base_node).right().to(q.base))
    d.add(elm.Dot().at(q.base))

    # Etiquetas de voltajes y condiciones del punto Q
    d.add(elm.Label().at((q.collector[0] + 1.1, q.collector[1] + 0.15)).label(f"$V_C\\approx {vc_v:.0f}\\,V$"))
    d.add(elm.Label().at((base_node[0] - 2.2, base_node[1] + 0.15)).label(f"$V_B\\approx {vb_v:.1f}\\,V$"))
    d.add(elm.Label().at((q.emitter[0] + 1.1, q.emitter[1] - 0.35)).label(f"$V_E\\approx {ve_v:.0f}\\,V$"))

    d.add(
        elm.Label()
        .at((q.collector[0] + 2.7, q.base[1] - 1.2))
        .label(
            f"$I_C\\approx {ic_ma:.0f}\\,mA$\n"
            f"$V_{{CE}}\\approx {vce_v:.0f}\\,V$"
        )
    )

    out_path = "topics/02-transistor-bjt/assets/bjt-nota5-diagrama-polarizacion-divisor.png"
    d.save(out_path, transparent=False, dpi=300)
    print(f"Imagen guardada en: {out_path}")


if __name__ == "__main__":
    main()
