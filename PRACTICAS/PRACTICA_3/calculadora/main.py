#!/usr/bin/env python3
"""
main.py — Punto de entrada para la calculadora de BJT
==============================================================================
Ejecuta la interfaz gráfica de la calculadora de la Práctica 3.

Uso:
    python PRACTICAS/PRACTICA_3/calculadora/main.py
"""

import sys
from pathlib import Path

# Asegurar que el directorio de la calculadora esté en el path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from ui_tkinter import main

if __name__ == "__main__":
    main()
