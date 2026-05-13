"""
test_calculadora.py — Pruebas unitarias para la lógica de la Practica 3
==============================================================================
Valida que los cálculos de core.py sean precisos comparándolos con los
valores teóricos de la guía de la práctica.
"""

import unittest
import sys
from pathlib import Path

# Agregar el directorio al path
sys.path.insert(0, str(Path(__file__).parent))

from core import InputParams, calcular_polarizacion

class TestCalculadoraBJT(unittest.TestCase):
    def setUp(self):
        # Valores exactos de la guía de la Práctica 3
        self.params = InputParams(
            Vcc=15.0,
            R1=4654.55,
            R2=880.0,
            Rc=120.0,
            Re=29.85,
            beta=200.0,
            Vbe=0.7
        )

    def test_thevenin(self):
        results = calcular_polarizacion(self.params)
        # Teórico: Vth ≈ 2.385 V, Rth ≈ 740 Ω
        self.assertAlmostEqual(results.Vth, 2.385, places=2)
        self.assertAlmostEqual(results.Rth, 740.0, places=0)

    def test_corrientes(self):
        results = calcular_polarizacion(self.params)
        # Teórico: Ic = 50 mA, Ib = 0.25 mA
        self.assertAlmostEqual(results.Ic * 1000, 50.0, places=1)
        self.assertAlmostEqual(results.Ib * 1000, 0.25, places=2)

    def test_voltajes_punto_q(self):
        results = calcular_polarizacion(self.params)
        # Teórico: Vce = 7.5 V, Ve = 1.5 V
        self.assertAlmostEqual(results.Vce, 7.5, places=1)
        self.assertAlmostEqual(results.Ve, 1.5, places=1)

    def test_potencias(self):
        results = calcular_polarizacion(self.params)
        # Teórico: Prc = 0.30 W
        self.assertAlmostEqual(results.Prc, 0.30, places=2)

if __name__ == "__main__":
    unittest.main()
