"""
plotting.py — Visualización para la calculadora de BJT
==============================================================================
Módulo para graficar la recta de carga y el punto de operación.

::SCRIPT_METADATA::
script_id    : practica3-plotting
module       : BJT
generates    : gráficas con matplotlib
last_updated : 2026-05-12
"""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
try:
    from core import InputParams, CalcResults
except ImportError:
    from .core import InputParams, CalcResults

def plot_load_line(fig: Figure, p: InputParams, r: CalcResults):
    """
    Dibuja la recta de carga DC y el punto Q con paleta clara.
    """
    ax = fig.add_subplot(111)
    
    # Paleta Pastel Claro
    COLOR_GRID = "#dfe6e9"
    COLOR_LINE = "#6c5ce7"   # Lavanda Intenso
    COLOR_POINT = "#ff7675"  # Rojo Pastel
    COLOR_TEXT = "#2d3436"   # Gris Oscuro
    COLOR_BG = "#ffffff"     # Blanco Puro
    
    # Eje X: Vce, Eje Y: Ic
    vce_vals = np.array([0, r.Vce_off])
    ic_vals = np.array([r.Ic_sat * 1000, 0]) # en mA
    
    # Dibujar recta de carga
    ax.plot(vce_vals, ic_vals, color=COLOR_LINE, linewidth=2.5, label="Recta de Carga DC")
    
    # Dibujar punto Q
    q_vce = r.Vce
    q_ic = r.Ic * 1000 # mA
    ax.plot(q_vce, q_ic, 'o', color=COLOR_POINT, markersize=10, markeredgecolor='white', label=f"Punto Q ($V_{{CE}}$={q_vce:.2f}V, $I_{{C}}$={q_ic:.2f}mA)")
    
    # Líneas punteadas al punto Q
    ax.axhline(q_ic, color=COLOR_POINT, linestyle='--', alpha=0.3)
    ax.axvline(q_vce, color=COLOR_POINT, linestyle='--', alpha=0.3)
    
    # Configuración de ejes
    ax.set_title("Recta de Carga DC - Emisor Común", color=COLOR_TEXT, fontsize=12, fontweight='bold', pad=15)
    ax.set_xlabel("$V_{CE}$ (V)", color=COLOR_TEXT)
    ax.set_ylabel("$I_C$ (mA)", color=COLOR_TEXT)
    
    # Ajustar límites
    ax.set_xlim(0, max(p.Vcc, q_vce) * 1.1)
    ax.set_ylim(0, max(r.Ic_sat * 1000, q_ic) * 1.1)
    
    ax.grid(True, linestyle='-', color=COLOR_GRID, alpha=0.7)
    ax.legend(facecolor=COLOR_BG, edgecolor=COLOR_GRID, labelcolor=COLOR_TEXT, framealpha=0.9)
    
    # Estilo de fondo
    ax.set_facecolor(COLOR_BG)
    fig.patch.set_facecolor(COLOR_BG)
    
    for spine in ax.spines.values():
        spine.set_color("#b2bec3")
    
    ax.tick_params(colors=COLOR_TEXT)
