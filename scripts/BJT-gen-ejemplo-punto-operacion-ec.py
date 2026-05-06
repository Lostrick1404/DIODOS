"""BJT — Ejemplo punto de operación (Emisor Común, polarización fija).

Genera:
- Esquema del circuito NPN con VCC, RB, RC y etiqueta VCE.
- Gráfica de curvas de salida IC–VCE + recta de carga + puntos Q.

"""

# ::SCRIPT_METADATA::
# script_id: BJT-gen-ejemplo-punto-operacion-ec
# module: BJT
# generates:
#   - topics/02-transistor-bjt/assets/bjt-ejemplo-ec-circuito-12v-rb-rc.png
#   - topics/02-transistor-bjt/assets/bjt-ejemplo-ec-curvas-q-recta-carga.png
# referenced_by:
#   - topics/02-transistor-bjt/Notas/Nota4.md
# last_updated: 2026-04-22

from __future__ import annotations

import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend sin GUI

import matplotlib.pyplot as plt
import numpy as np
import schemdraw
import schemdraw.elements as elm


ASSETS_DIR = Path("topics/02-transistor-bjt/assets")

OUT_CIRCUIT = ASSETS_DIR / "bjt-ejemplo-ec-circuito-12v-rb-rc.png"
OUT_PLOT = ASSETS_DIR / "bjt-ejemplo-ec-curvas-q-recta-carga.png"


def bjt_ic(vce: np.ndarray, ib: float, *, beta: float, vce_sat: float) -> np.ndarray:
    """Modelo simplificado para curvas de salida.

    - Saturación: IC crece aproximadamente lineal con VCE hasta VCE_sat.
    - Región activa: IC ≈ beta*IB (sin efecto Early; consistente con el cálculo analítico del ejemplo).
    """

    ic = np.zeros_like(vce)
    for idx, v in enumerate(vce):
        if v < vce_sat:
            ic[idx] = beta * ib * (v / vce_sat)
        else:
            ic[idx] = beta * ib
    return ic


def build_circuit() -> schemdraw.Drawing:
    d = schemdraw.Drawing(show=False)
    d.config(unit=3.5, fontsize=13)

    q = d.add(elm.BjtNpn(circle=True).at((0, 0)))

    # Emisor a tierra
    d.add(elm.Line().down().at(q.emitter).length(1.4))
    d.add(elm.Ground())

    # Colector a RC y VCC
    d.add(elm.Line().up().at(q.collector).length(0.8))
    node_c = d.here
    d.add(elm.Resistor().up().label("$R_C=2\\,k\\Omega$", loc="right", ofst=0.2))
    node_vcc_c = d.here

    # Base a RB y VCC
    d.add(elm.Line().left().at(q.base).length(2.4))
    d.add(elm.Resistor().up().toy(node_vcc_c).label("$R_B=376.67\\,k\\Omega$", loc="left", ofst=0.2))
    node_vcc_b = d.here

    # Bus superior y fuente VCC
    d.add(elm.Line().at(node_vcc_b).to(node_vcc_c))
    d.add(elm.Line().up().at(node_vcc_c).length(0.5))
    d.add(elm.Vdd().label("$V_{CC}=12\\,V$"))

    # Etiqueta VCE
    d.add(elm.Gap().at(node_c).to(q.emitter).label(["$+$", "$V_{CE}$", "$-$"]))

    return d


def build_plot() -> None:
    # Parámetros del ejemplo
    vcc = 12.0
    rc = 2000.0
    beta = 100.0
    vbe = 0.7
    vce_sat = 0.2

    rb_1 = 376.67e3
    rb_2 = 161.43e3

    ib_1 = (vcc - vbe) / rb_1
    ib_2 = (vcc - vbe) / rb_2

    # Familia de curvas y recta de carga
    vce = np.linspace(0, vcc, 2400)

    # IB alrededor de los casos (incluye 30 µA y 70 µA aprox.)
    ib_values = [10e-6, 20e-6, 30e-6, 40e-6, 50e-6, 60e-6, 70e-6, 80e-6]

    fig, ax = plt.subplots(figsize=(10, 7))

    for ib in ib_values:
        ic = bjt_ic(vce, ib, beta=beta, vce_sat=vce_sat)
        ax.plot(vce, ic * 1e3, linewidth=1.8, alpha=0.75, label=f"$I_B={ib*1e6:.0f}$ $\\mu A$")

    # Recta de carga: VCE = VCC - IC*RC
    ic_eje = vcc / rc
    ax.plot([0, vcc], [ic_eje * 1e3, 0], "k-", linewidth=2.8, label="Recta de carga")

    # Región de saturación (referencia)
    ax.axvline(vce_sat, color="gray", linestyle=":", alpha=0.7)
    ax.text(vce_sat + 0.08, ic_eje * 1e3 * 0.95, "$V_{CE(sat)}$", color="gray", fontsize=10)

    # Punto Q caso 1 (activa)
    ic_q1 = beta * ib_1
    vce_q1 = vcc - ic_q1 * rc

    ax.plot(vce_q1, ic_q1 * 1e3, "ro", markersize=10, zorder=5)
    ax.annotate(
        f"Q (RB=376.67kΩ)\n$V_{{CE}}={vce_q1:.1f}\\,V$\n$I_C={ic_q1*1e3:.1f}\\,mA$",
        xy=(vce_q1, ic_q1 * 1e3),
        xytext=(vce_q1 + 0.9, ic_q1 * 1e3 + 0.8),
        fontsize=10,
        color="red",
        arrowprops=dict(arrowstyle="->", color="red", linewidth=1.2),
    )

    # Punto Q caso 2: intersección real (recta de carga vs curva IB) en saturación
    ic_curve_2 = bjt_ic(vce, ib_2, beta=beta, vce_sat=vce_sat)
    ic_load = (vcc - vce) / rc
    idx2 = int(np.argmin(np.abs(ic_curve_2 - ic_load)))
    vce_q2 = float(vce[idx2])
    ic_q2 = float(ic_load[idx2])

    ax.plot(vce_q2, ic_q2 * 1e3, "ms", markersize=9, zorder=6)
    ax.annotate(
        f"Q (RB=161.43kΩ)\n(saturación)\n$V_{{CE}}\\approx{vce_q2:.2f}\\,V$\n$I_C\\approx{ic_q2*1e3:.1f}\\,mA$",
        xy=(vce_q2, ic_q2 * 1e3),
        xytext=(vce_q2 + 1.4, ic_q2 * 1e3 - 1.4),
        fontsize=10,
        color="purple",
        arrowprops=dict(arrowstyle="->", color="purple", linewidth=1.2),
    )

    # Puntos de corte/saturación ideal
    ax.plot(vcc, 0, "gs", markersize=7)
    ax.annotate("Corte\n$V_{CE}=V_{CC}$", xy=(vcc, 0), xytext=(vcc - 2.3, 0.8), fontsize=9, color="green")

    ax.plot(0, ic_eje * 1e3, "bs", markersize=7)
    ax.annotate(
        "$I_C=V_{CC}/R_C$",
        xy=(0, ic_eje * 1e3),
        xytext=(0.7, ic_eje * 1e3 + 0.4),
        fontsize=9,
        color="blue",
    )

    ax.set_title("Curvas de salida + recta de carga (EC, $V_{CC}=12V$, $R_C=2k\\Omega$, $\\beta=100$)")
    ax.set_xlabel("$V_{CE}$ [V]")
    ax.set_ylabel("$I_C$ [mA]")
    ax.set_xlim(-0.2, vcc + 0.5)
    ax.set_ylim(-0.2, ic_eje * 1e3 * 1.35)
    ax.grid(True, linestyle="--", alpha=0.35)
    ax.legend(loc="upper right", fontsize=8, ncols=2)
    fig.tight_layout()

    OUT_PLOT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PLOT, dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    OUT_CIRCUIT.parent.mkdir(parents=True, exist_ok=True)

    d = build_circuit()
    d.save(str(OUT_CIRCUIT), dpi=300)

    build_plot()


if __name__ == "__main__":
    main()
