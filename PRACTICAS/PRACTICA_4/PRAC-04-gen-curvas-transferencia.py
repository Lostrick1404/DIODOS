"""
PRAC-04-gen-curvas-transferencia.py
──────────────────────────────────
Genera las curvas de transferencia del JFET 2N5457 para la Práctica 4.

El script calcula con precisión extendida los valores teóricos y comerciales
del punto Q, y produce dos figuras: una para el diseño teórico y otra para
los valores comerciales del divisor de compuerta.

::SCRIPT_METADATA::
script_id: PRAC-04-gen-curvas-transferencia
module: PRAC
generates:
  - PRAC-04-curvas-transferencia-teorica.png
  - PRAC-04-curvas-transferencia-comercial.png
referenced_by:
  - PRACTICAS/PRACTICA_4/Calculos.md
last_updated: 2026-05-20

Dependencias: numpy, matplotlib
Salida: PRACTICAS/PRACTICA_4/assets/

Ejecutar desde la raíz del repositorio:
    g:/REPOSITORIOS GITHUB/DIODOS Y TRANSISTORES/.venv/Scripts/python.exe PRACTICAS/PRACTICA_4/PRAC-04-gen-curvas-transferencia.py
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP, getcontext
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


getcontext().prec = 60
getcontext().rounding = ROUND_HALF_UP


BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

ONE = Decimal("1")
ZERO = Decimal("0")
VDD = Decimal("15")
VDS_TARGET = Decimal("6")
ID_TARGET = Decimal("0.004")
VG_THEORETICAL = Decimal("0.15")
R2_THEORETICAL = Decimal("10000")
R1_COMMERCIAL = Decimal("1000000")
R2_COMMERCIAL = Decimal("10000")
RD_COMMERCIAL = Decimal("2200")
RS_COMMERCIAL = Decimal("180")

# Referencia exacta de alta precisión (2026-05-20).
# No editar sin volver a ejecutar el script con Decimal de alta precisión.
#
# Diseño teórico:
#   VGS = -0.633436854000504728617983195045 V
#   VS  = 0.783436854000504728617983195045 V
#   RS  = 195.8592135001261821544957987612 Ω
#   RD  = 2054.1407864998738178455042012388 Ω
#   R1  = 990000 Ω
#   R2  = 10000 Ω
#   Qmín = (IDQ 0.8986616595931250 mA, VGSQ -0.026011165850628 V, VDSQ 12.978011265915469 V)
#   Qprom = (IDQ 2.4288243823501601 mA, VGSQ -0.325707633257032 V, VDSQ 9.535145139712140 V)
#   Qmáx = (IDQ 4.0000000000000000 mA, VGSQ -0.633436854000505 V, VDSQ 6.000000000000000 V)
#
# Valores comerciales:
#   VG  = 0.148514851485148514851485148515 V
#   R1  = 1000000 Ω
#   R2  = 10000 Ω
#   RS  = 180 Ω
#   RD  = 2200 Ω
#   Qmín = (IDQ 0.9275701674948409 mA, VGSQ -0.018447778663923 V, VDSQ 12.792383001362279 V)
#   Qprom = (IDQ 2.4763600313306244 mA, VGSQ -0.297229954154364 V, VDSQ 9.106263125433114 V)
#   Qmáx = (IDQ 4.0730748433973186 mA, VGSQ -0.584638620326369 V, VDSQ 5.306081872714382 V)


@dataclass(frozen=True)
class TransferCase:
    name: str
    idss: Decimal
    vp: Decimal
    color: str
    marker: str


@dataclass(frozen=True)
class BiasConfiguration:
    name: str
    vg: Decimal
    rs: Decimal
    rd: Decimal
    r1: Decimal
    r2: Decimal


@dataclass(frozen=True)
class OperatingPoint:
    name: str
    id_a: Decimal
    vgs: Decimal
    vds: Decimal


def quantizer(places: int = 15) -> Decimal:
    return Decimal("1").scaleb(-places)


def fmt_sigfig(value: Decimal, sig_figs: int = 3) -> str:
    if value.is_zero():
        return "0." + ("0" * (sig_figs - 1))

    exponent = value.adjusted()
    places = sig_figs - 1 - exponent
    quant = Decimal("1").scaleb(-places)
    rounded = value.quantize(quant)
    return format(rounded, "f")


def fmt_voltage(value_v: Decimal, sig_figs: int = 3) -> str:
    return fmt_sigfig(value_v, sig_figs)


def fmt_current_milliamps(value_a: Decimal, sig_figs: int = 3) -> str:
    return fmt_sigfig(value_a * Decimal("1000"), sig_figs)


def fmt_resistance(value_ohm: Decimal, sig_figs: int = 3) -> str:
    abs_value = abs(value_ohm)
    if abs_value >= Decimal("1000000"):
        return f"{fmt_sigfig(value_ohm / Decimal('1000000'), sig_figs)} MΩ"
    if abs_value >= Decimal("1000"):
        return f"{fmt_sigfig(value_ohm / Decimal('1000'), sig_figs)} kΩ"
    return f"{fmt_sigfig(value_ohm, sig_figs)} Ω"


def solve_design_bias() -> BiasConfiguration:
    idss = Decimal("0.005")
    vp = Decimal("-6")

    vgs = vp * (ONE - (ID_TARGET / idss).sqrt())
    vs = VG_THEORETICAL - vgs
    rs = vs / ID_TARGET
    rd = (VDD - VDS_TARGET) / ID_TARGET - rs
    r1 = R2_THEORETICAL * (VDD / VG_THEORETICAL - ONE)

    return BiasConfiguration(
        name="Diseño teórico",
        vg=VG_THEORETICAL,
        rs=rs,
        rd=rd,
        r1=r1,
        r2=R2_THEORETICAL,
    )


def solve_commercial_bias() -> BiasConfiguration:
    vg = VDD * R2_COMMERCIAL / (R1_COMMERCIAL + R2_COMMERCIAL)
    return BiasConfiguration(
        name="Valores comerciales",
        vg=vg,
        rs=RS_COMMERCIAL,
        rd=RD_COMMERCIAL,
        r1=R1_COMMERCIAL,
        r2=R2_COMMERCIAL,
    )


def solve_operating_point(case: TransferCase, bias: BiasConfiguration) -> OperatingPoint:
    # Resolver de forma cerrada usando y = sqrt(ID / IDSS).
    a = case.idss * bias.rs
    b = -case.vp
    c = case.vp - bias.vg

    discriminant = b * b - Decimal("4") * a * c
    root = discriminant.sqrt()

    candidates = [(-b + root) / (Decimal("2") * a), (-b - root) / (Decimal("2") * a)]
    y = None
    for candidate in candidates:
        if ZERO <= candidate <= ONE:
            y = candidate
            break

    if y is None:
        raise ValueError(f"No valid Q-point found for {case.name}")

    id_a = case.idss * y * y
    vgs = bias.vg - id_a * bias.rs
    vds = VDD - id_a * (bias.rs + bias.rd)

    return OperatingPoint(name=case.name, id_a=id_a, vgs=vgs, vds=vds)


def transfer_curve(case: TransferCase, points: int = 700) -> tuple[np.ndarray, np.ndarray]:
    vgs = np.linspace(float(case.vp), 0.0, points)
    id_ma = float(case.idss) * 1000.0 * (1.0 - vgs / float(case.vp)) ** 2
    return vgs, id_ma


def bias_line(vgs: np.ndarray, bias: BiasConfiguration) -> np.ndarray:
    return (float(bias.vg) - vgs) / float(bias.rs) * 1000.0


def print_configuration_summary(bias: BiasConfiguration, points: list[OperatingPoint]) -> None:
    print(f"\n=== {bias.name} ===")
    print(f"V_G  = {fmt_voltage(bias.vg)} V")
    print(f"R_S  = {fmt_resistance(bias.rs)}")
    print(f"R_D  = {fmt_resistance(bias.rd)}")
    print(f"R_1  = {fmt_resistance(bias.r1)}")
    print(f"R_2  = {fmt_resistance(bias.r2)}")
    print("Puntos Q:")
    for point in points:
        print(
            f"- {point.name}: IDQ = {fmt_current_milliamps(point.id_a)} mA, "
            f"VGSQ = {fmt_voltage(point.vgs)} V, VDSQ = {fmt_voltage(point.vds)} V"
        )


def plot_transfer_figure(
    cases: list[TransferCase],
    bias: BiasConfiguration,
    output_name: str,
    title_suffix: str,
) -> list[OperatingPoint]:
    points = [solve_operating_point(case, bias) for case in cases]

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(11, 8))

    for case in cases:
        vgs, id_ma = transfer_curve(case)
        ax.plot(
            vgs,
            id_ma,
            color=case.color,
            linewidth=2.6,
            label=f"{case.name} (IDSS={fmt_current_milliamps(case.idss, 3)} mA, VP={fmt_voltage(case.vp, 3)} V)",
        )

    vgs_bias = np.linspace(float(min(case.vp for case in cases)) - 0.35, 0.35, 500)
    ax.plot(
        vgs_bias,
        bias_line(vgs_bias, bias),
        color="#111111",
        linestyle="--",
        linewidth=2.2,
        label=f"Recta de polarización ({bias.name.lower()})",
    )

    offsets = {
        "Mínimo": (0.45, 0.85),
        "Promedio": (0.45, 0.95),
        "Máximo": (-2.10, 0.90),
    }

    for case, point in zip(cases, points):
        x = float(point.vgs)
        y = float(point.id_a * Decimal("1000"))
        ax.scatter(x, y, s=90, color=case.color, edgecolor="#111111", linewidth=0.8, zorder=5, marker=case.marker)

        dx, dy = offsets[case.name]
        ax.annotate(
            f"{case.name}\nIDQ={fmt_current_milliamps(point.id_a)} mA\nVDSQ={fmt_voltage(point.vds)} V",
            xy=(x, y),
            xytext=(x + dx, y + dy),
            textcoords="data",
            fontsize=9,
            color="#111111",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor=case.color, alpha=0.97),
            arrowprops=dict(arrowstyle="->", color=case.color, lw=1.4),
        )

    ax.set_title(f"Curvas de transferencia del JFET 2N5457\n{title_suffix}", fontsize=15, pad=12)
    ax.set_xlabel(r"$V_{GS}$ [V]", fontsize=12)
    ax.set_ylabel(r"$I_D$ [mA]", fontsize=12)
    ax.axhline(0, color="#111111", linewidth=1.0)
    ax.axvline(0, color="#111111", linewidth=1.0)
    ax.set_xlim(float(min(case.vp for case in cases)) - 0.40, 0.35)
    ax.set_ylim(0, max(float(max(case.idss for case in cases)) * 1000.0 * 1.18, 5.8))
    ax.legend(loc="upper left", fontsize=9, frameon=True)
    ax.grid(True, linestyle="--", linewidth=0.8, alpha=0.35)
    fig.tight_layout()

    output_path = ASSETS_DIR / output_name
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Generada: {output_path}")
    return points


def main() -> None:
    cases = [
        TransferCase("Mínimo", Decimal("0.001"), Decimal("-0.5"), "#2563EB", "o"),
        TransferCase("Promedio", Decimal("0.003"), Decimal("-3.25"), "#EA580C", "s"),
        TransferCase("Máximo", Decimal("0.005"), Decimal("-6"), "#16A34A", "^") ,
    ]

    design_bias = solve_design_bias()
    commercial_bias = solve_commercial_bias()

    design_points = plot_transfer_figure(
        cases,
        design_bias,
        "PRAC-04-curvas-transferencia-teorica.png",
        "Diseño teórico con precisión extendida",
    )
    commercial_points = plot_transfer_figure(
        cases,
        commercial_bias,
        "PRAC-04-curvas-transferencia-comercial.png",
        "Valores comerciales redondeados a laboratorio",
    )

    print_configuration_summary(design_bias, design_points)
    print_configuration_summary(commercial_bias, commercial_points)
    print(f"\nSalida: {ASSETS_DIR}")


if __name__ == "__main__":
    main()
