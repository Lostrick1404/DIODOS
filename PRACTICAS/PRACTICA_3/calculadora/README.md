# Calculadora Interactiva de Polarización BJT (Práctica 3)

Esta herramienta permite calcular y visualizar el punto de operación $Q$ de un transistor BJT en configuración de Emisor Común con divisor de voltaje. Ha sido diseñada siguiendo el modelo de la calculadora de la Práctica 1.

## Características

- **Cálculo de Punto Q:** Obtiene $V_{CEQ}$ e $I_{CQ}$ de forma instantánea.
- **Análisis de Thévenin:** Calcula el voltaje y resistencia equivalente en la base.
- **Voltajes y Corrientes de Nodo:** Desglose detallado de $V_B, V_C, V_E, I_B, I_C, I_E$.
- **Potencias Disipadas:** Calcula el calor generado en cada resistencia y en el propio transistor.
- **Visualización Gráfica:** Dibuja la recta de carga DC y ubica el punto $Q$ dinámicamente.
- **Interfaz Moderna:** Paleta de colores oscura tipo "Catppuccin" para reducir la fatiga visual.

## Requisitos

- Python 3.12+
- Matplotlib
- Numpy
- Tkinter (estándar en la mayoría de las instalaciones de Python)

## Ejecución

Desde la raíz del repositorio, ejecute:

```powershell
python PRACTICAS/PRACTICA_3/calculadora/main.py
```

## Estructura del Módulo

- `core.py`: Lógica matemática y fórmulas de polarización.
- `plotting.py`: Generación de la gráfica de la recta de carga.
- `ui_tkinter.py`: Interfaz gráfica de usuario.
- `main.py`: Punto de entrada del script.
