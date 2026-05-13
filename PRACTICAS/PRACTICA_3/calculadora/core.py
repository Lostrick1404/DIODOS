"""
core.py — Cálculos para polarización de BJT (Emisor Común con Divisor de Voltaje)
==============================================================================
Módulo de lógica de negocio para la Práctica 3.
Todas las funciones son puras: reciben datos, retornan resultados.

::SCRIPT_METADATA::
script_id    : practica3-core
module       : BJT
generates    : cálculos numéricos (sin gráficos)
last_updated : 2026-05-12
"""

from dataclasses import dataclass, field
from typing import List, Tuple
import numpy as np

@dataclass
class InputParams:
    """Parámetros de entrada para los cálculos de polarización BJT."""
    Vcc: float = 15.0      # Voltaje de alimentación (V)
    R1: float = 4655.0     # Resistencia divisor superior (Ohm)
    R2: float = 880.0      # Resistencia divisor inferior (Ohm)
    Rc: float = 120.0      # Resistencia de colector (Ohm)
    Re: float = 29.85      # Resistencia de emisor (Ohm)
    beta: float = 200.0    # Ganancia del transistor (hFE)
    Vbe: float = 0.7       # Voltaje base-emisor (V)

@dataclass
class CalcResults:
    """Resultados de todos los pasos de cálculo de polarización."""
    # Equivalente de Thévenin
    Vth: float = 0.0
    Rth: float = 0.0
    
    # Corrientes
    Ib: float = 0.0        # Corriente de base (A)
    Ic: float = 0.0        # Corriente de colector (A)
    Ie: float = 0.0        # Corriente de emisor (A)
    alpha: float = 0.0     # Factor alfa
    
    # Voltajes de nodos
    Vb: float = 0.0        # Voltaje en la base (V)
    Vc: float = 0.0        # Voltaje en el colector (V)
    Ve: float = 0.0        # Voltaje en el emisor (V)
    Vce: float = 0.0       # Voltaje colector-emisor (V)
    
    # Potencias
    Pr1: float = 0.0       # Potencia en R1 (W)
    Pr2: float = 0.0       # Potencia en R2 (W)
    Prc: float = 0.0       # Potencia en Rc (W)
    Pre: float = 0.0       # Potencia en Re (W)
    Pq: float = 0.0        # Potencia disipada por el transistor (W)
    
    # Recta de carga
    Ic_sat: float = 0.0    # Corriente de saturación ideal (A)
    Vce_off: float = 0.0   # Voltaje de corte (V)

def calcular_polarizacion(p: InputParams) -> CalcResults:
    """
    Calcula el punto de operación Q y parámetros del circuito.
    """
    r = CalcResults()
    
    # 1. Equivalente de Thévenin en la base
    r.Vth = p.Vcc * (p.R2 / (p.R1 + p.R2))
    r.Rth = (p.R1 * p.R2) / (p.R1 + p.R2)
    
    # 2. Corrientes
    # Ib = (Vth - Vbe) / (Rth + (beta + 1) * Re)
    denominador_ib = r.Rth + (p.beta + 1) * p.Re
    if denominador_ib != 0:
        r.Ib = (r.Vth - p.Vbe) / denominador_ib
    else:
        r.Ib = 0.0
        
    r.Ic = p.beta * r.Ib
    r.Ie = (p.beta + 1) * r.Ib
    r.alpha = p.beta / (p.beta + 1)
    
    # 3. Voltajes
    r.Ve = r.Ie * p.Re
    r.Vb = r.Ve + p.Vbe
    r.Vc = p.Vcc - (r.Ic * p.Rc)
    r.Vce = r.Vc - r.Ve
    
    # 4. Potencias
    r.Pr1 = ((p.Vcc - r.Vb)**2) / p.R1 if p.R1 != 0 else 0.0
    r.Pr2 = (r.Vb**2) / p.R2 if p.R2 != 0 else 0.0
    r.Prc = (r.Ic**2) * p.Rc
    r.Pre = (r.Ie**2) * p.Re
    r.Pq = r.Vce * r.Ic
    
    # 5. Recta de carga DC
    r.Vce_off = p.Vcc
    if (p.Rc + p.Re) != 0:
        r.Ic_sat = p.Vcc / (p.Rc + p.Re)
    else:
        r.Ic_sat = 0.0
        
    return r

def validate_params(p: InputParams) -> Tuple[bool, str]:
    """Valida que los parámetros tengan sentido físico."""
    if p.Vcc <= 0: return False, "Vcc debe ser positivo."
    if p.R1 <= 0 or p.R2 <= 0: return False, "Resistencias del divisor deben ser positivas."
    if p.Rc < 0 or p.Re < 0: return False, "Resistencias Rc y Re no pueden ser negativas."
    if p.beta <= 0: return False, "Beta debe ser mayor que cero."
    if p.Vbe < 0: return False, "Vbe no puede ser negativo."
    if p.Vcc <= p.Vbe: return False, "Vcc debe ser mayor que Vbe para polarización directa."
    return True, ""

if __name__ == "__main__":
    # Prueba rápida con valores de la práctica
    params = InputParams()
    results = calcular_polarizacion(params)
    print(f"Punto Q: Vce = {results.Vce:.2f} V, Ic = {results.Ic*1e3:.2f} mA")
    print(f"Ib = {results.Ib*1e6:.2f} uA")
