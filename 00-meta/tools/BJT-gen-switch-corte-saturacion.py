"""Genera recursos didácticos: BJT como switch (corte y saturación).

Salida:
- topics/02-transistor-bjt/assets/bjt-switch-01-circuito.png
- topics/02-transistor-bjt/assets/bjt-switch-02-estados.png
- topics/02-transistor-bjt/assets/bjt-switch-03-curvas-corte-saturacion.png
"""

# ::SCRIPT_METADATA::
# script_id: BJT-gen-switch-corte-saturacion
# module: BJT
# generates:
#   - topics/02-transistor-bjt/assets/bjt-switch-01-circuito.png
#   - topics/02-transistor-bjt/assets/bjt-switch-02-estados.png
#   - topics/02-transistor-bjt/assets/bjt-switch-03-curvas-corte-saturacion.png
# referenced_by:
#   - topics/02-transistor-bjt/Notas/Nota5.md
# last_updated: 2026-04-29

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # backend sin GUI

import matplotlib.pyplot as plt
import numpy as np
import schemdraw
import schemdraw.elements as elm


OUT_CIRCUIT = "topics/02-transistor-bjt/assets/bjt-switch-01-circuito.png"
OUT_STATES = "topics/02-transistor-bjt/assets/bjt-switch-02-estados.png"
OUT_CURVES = "topics/02-transistor-bjt/assets/bjt-switch-03-curvas-corte-saturacion.png"


def build_switch_circuit() -> schemdraw.Drawing:
    """NPN low-side switch con carga resistiva en el colector."""

    vcc = 12
    rl = 1.0
    rb = 10.0

    d = schemdraw.Drawing(unit=3.2)
    d.config(fontsize=12, bgcolor="white", color="black", margin=0.3)

    gnd_y = 0.0
    vcc_y = 6.0
    x_src = 1.0
    x_in = 4.5
    x_q = 10.0
    y_base = 3.0

    # Fuente VCC
    src = d.add(
        elm.SourceV()
        .at((x_src, gnd_y))
        .up()
        .to((x_src, vcc_y))
        .label(f"$V_{{CC}}={vcc}\\,V$", loc="left", ofst=0.25)
    )
    d.add(elm.Ground().at((x_src, gnd_y)))

    # Bus VCC
    d.add(elm.Dot().at(src.end))
    d.add(elm.Line().at(src.end).right().to((x_q + 2.0, vcc_y)))

    # Transistor
    q = d.add(elm.BjtNpn().at((x_q, y_base)))
    q.label("Q1", loc="right", ofst=0.2)
    q.label("NPN", loc="right", ofst=0.7)

    # Carga (R_L) al colector
    d.add(
        elm.Resistor()
        .down()
        .at((q.collector[0], vcc_y))
        .to(q.collector)
        .label(f"$R_L$", loc="right", ofst=0.2)
        .label(f"$\\approx {rl:.1f}\\,k\\Omega$", loc="right", ofst=0.9)
    )
    d.add(elm.Dot().at(q.collector))

    # Emisor a tierra
    d.add(elm.Line().at(q.emitter).down().to((q.emitter[0], gnd_y)))
    d.add(elm.Dot().at(q.emitter))

    # Bus GND
    d.add(elm.Line().at((x_src, gnd_y)).right().to((x_q + 2.0, gnd_y)))

    # Entrada Vin con resistor RB hacia base
    vin = d.add(
        elm.SourceV()
        .at((x_in, gnd_y))
        .up()
        .to((x_in, y_base))
        .label("$V_{in}$", loc="left", ofst=0.25)
    )
    d.add(elm.Ground().at((x_in, gnd_y)))
    d.add(elm.Dot().at(vin.end))

    d.add(
        elm.Resistor()
        .right()
        .at(vin.end)
        .to((q.base[0] - 1.2, y_base))
        .label("$R_B$", loc="top", ofst=0.2)
        .label(f"$\\approx {rb:.0f}\\,k\\Omega$", loc="top", ofst=0.9)
    )
    d.add(elm.Line().at((q.base[0] - 1.2, y_base)).right().to(q.base))
    d.add(elm.Dot().at(q.base))

    # Etiquetas de voltajes estándar
    # Vout en colector
    d.add(elm.Label().at((q.collector[0] + 2.0, q.collector[1] + 0.2)).label("$V_{out}=V_C$"))

    # VCE (entre colector y emisor)
    d.add(
        elm.Gap()
        .at((q.collector[0] + 1.0, (q.collector[1] + q.emitter[1]) / 2))
        .down()
        .label(["+", "$V_{CE}$", "−"], loc="right")
    )

    # VBE (entre base y emisor)
    d.add(
        elm.Gap()
        .at((q.base[0] - 0.2, (q.base[1] + q.emitter[1]) / 2))
        .down()
        .label(["+", "$V_{BE}$", "−"], loc="left")
    )

    # Nota de regiones
    d.add(
        elm.Label()
        .at((x_q + 3.0, y_base - 1.6))
        .label("Corte: $I_B\\approx 0$\nSaturación: $V_{CE}\\approx V_{CE(sat)}$")
    )

    return d


def plot_switch_states() -> None:
    """Gráfica conceptual de los dos estados: corte y saturación."""

    vcc = 12.0
    v_be_on = 0.7
    v_ce_sat = 0.2

    vin = np.linspace(0, 5, 400)

    # Modelo conceptual (no físico): salida alta en corte, baja en saturación
    vout = np.where(vin < v_be_on, vcc, v_ce_sat)

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(vin, vout, linewidth=2, color="#2563EB")

    ax.axvline(v_be_on, linestyle="--", linewidth=1.5, color="black")
    ax.text(v_be_on + 0.05, vcc * 0.55, "$V_{BE}\\approx 0.7\\,V$", fontsize=10)

    ax.axhline(vcc, linestyle=":", linewidth=1.2, color="gray")
    ax.axhline(v_ce_sat, linestyle=":", linewidth=1.2, color="gray")

    ax.text(0.15, vcc - 0.8, "Corte (OFF)\n$V_{out}\\approx V_{CC}$", fontsize=10)
    ax.text(2.2, v_ce_sat + 0.6, "Saturación (ON)\n$V_{out}\\approx V_{CE(sat)}$", fontsize=10)

    ax.set_title("BJT como switch: estados OFF (corte) y ON (saturación)")
    ax.set_xlabel("$V_{in}$ [V]")
    ax.set_ylabel("$V_{out}$ [V]")
    ax.set_xlim(0, 5)
    ax.set_ylim(0, vcc + 1)
    ax.grid(True, linestyle="--", alpha=0.35)
    fig.tight_layout()
    fig.savefig(OUT_STATES, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_output_curves_cutoff_saturation() -> None:
    """Curvas IC-VCE conceptuales para ilustrar corte y saturación.

    Se grafica una familia de curvas aproximadas (por distintos I_B),
    una recta de carga, y se marcan los puntos de corte y saturación.
    """

    # Parámetros típicos (ejemplo didáctico)
    vcc = 12.0
    rc = 1_000.0
    beta = 100.0
    vce_sat = 0.2

    # Eje VCE
    vce = np.linspace(0, vcc, 600)

    # Recta de carga: IC = (VCC - VCE)/RC
    ic_load = (vcc - vce) / rc

    # Corriente de saturación (aprox ideal) y corriente de base mínima (aprox)
    # Nota: en saturación real suele cumplirse IC ≈ (VCC - VCE(sat))/RC.
    ic_sat_ideal = vcc / rc
    ic_sat_at_vce_sat = (vcc - vce_sat) / rc
    ib_sat = ic_sat_ideal / beta

    # Familia de corrientes de base para mostrar:
    # - corte (IB=0)
    # - un caso intermedio
    # - el mínimo para saturación (aprox)
    # - un caso sobredimensionado para forzar saturación
    ib_list = np.array([0.0, 0.5 * ib_sat, 1.0 * ib_sat, 1.2 * ib_sat])

    # Modelo suave para las curvas: IC ~ (beta*IB) con una "rodilla" cerca de VCE~0
    # (solo para ilustración; no es un modelo físico exacto)
    vknee = 0.25
    curves = []
    for ib in ib_list:
        ic_active = beta * ib
        ic_curve = ic_active * np.tanh(vce / vknee)
        curves.append(ic_curve)

    fig, ax = plt.subplots(figsize=(8.8, 5.2))

    # Dibujar familia de curvas
    for ib, ic_curve in zip(ib_list, curves, strict=True):
        label = "$I_B=0$ (corte)" if ib == 0 else f"$I_B={ib*1e6:.0f}\u03bcA$"
        ax.plot(vce, ic_curve * 1e3, linewidth=2, label=label)

    # Recta de carga
    ax.plot(vce, ic_load * 1e3, linestyle="--", color="black", linewidth=1.8, label="Recta de carga")

    # Punto de corte (IB=0): (VCE=VCC, IC=0)
    ax.scatter([vcc], [0.0], color="black", zorder=5)
    ax.annotate(
        "Corte (OFF)\n$V_{CE}\u2248V_{CC}$, $I_C\u22480$",
        xy=(vcc, 0.0),
        xytext=(vcc - 3.6, 2.5),
        arrowprops=dict(arrowstyle="->", color="black"),
        fontsize=10,
    )

    # Punto de saturación (aprox): (VCE~VCE(sat), IC~(VCC - VCE(sat))/RC ≈ VCC/RC)
    ax.scatter([vce_sat], [ic_sat_at_vce_sat * 1e3], color="black", zorder=5)
    ax.annotate(
        "Saturación (ON)\n$V_{CE}\u2248V_{CE(sat)}$, $I_C\u2248(V_{CC}-V_{CE(sat)})/R_C$",
        xy=(vce_sat, ic_sat_at_vce_sat * 1e3),
        xytext=(1.6, ic_sat_at_vce_sat * 1e3 - 3.5),
        arrowprops=dict(arrowstyle="->", color="black"),
        fontsize=10,
    )

    # Líneas guía
    ax.axvline(vce_sat, linestyle=":", color="gray", linewidth=1.2)
    ax.axhline(ic_sat_at_vce_sat * 1e3, linestyle=":", color="gray", linewidth=1.2)

    ax.set_title("Curvas $I_C$–$V_{CE}$ (conceptuales) para ilustrar corte y saturación")
    ax.set_xlabel("$V_{CE}$ [V]")
    ax.set_ylabel("$I_C$ [mA]")
    ax.set_xlim(0, vcc)
    ic_max = max(beta * float(ib_list.max()), ic_sat_ideal)
    ax.set_ylim(0, (ic_max * 1e3) * 1.15)
    ax.grid(True, linestyle="--", alpha=0.35)
    ax.legend(loc="upper right", fontsize=9)

    fig.tight_layout()
    fig.savefig(OUT_CURVES, dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    d = build_switch_circuit()
    d.save(OUT_CIRCUIT, transparent=False, dpi=300)
    print(f"Imagen guardada en: {OUT_CIRCUIT}")

    plot_switch_states()
    print(f"Imagen guardada en: {OUT_STATES}")

    plot_output_curves_cutoff_saturation()
    print(f"Imagen guardada en: {OUT_CURVES}")


if __name__ == "__main__":
    main()
