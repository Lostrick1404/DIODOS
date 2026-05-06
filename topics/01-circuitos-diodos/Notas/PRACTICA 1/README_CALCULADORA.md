# 🧮 Calculadora Interactiva de la Práctica 1

Este directorio contiene el script `practica1_calculadora.py`, una herramienta integral para la validación de resultados de laboratorio.

## 📝 Notas de Implementación

- **Validación:** El script ha sido validado contra `PROCEDIMIENTO_PRACTICA_1.md` y cumple con los 21 puntos de verificación (100% OK).
- **Parámetros por Defecto:**
  - Inductancia de choque ($L_H$): $1.5H$
  - Resistencia de carga ($R_L$): $40\Omega$ (típica para transformadores 120/12V@2A)
- **Bugs Corregidos:**
  - **Paso 8:** Se corrigió el cálculo de la impedancia; ahora utiliza correctamente $n \cdot \omega_{out}$ en lugar de $2 \cdot n \cdot \omega_{out}$.
  - **Paso 9:** El cálculo de rizado $V_r(pp)$ se basa ahora en el valor pico de la red $V_m$ para mayor precisión en el diseño del filtro.

## 🚀 Uso
Ejecutar desde la raíz del repositorio:
```bash
python "topics/01-circuitos-diodos/Notas/PRACTICA 1/practica1_calculadora.py"
```
*Requiere entorno gráfico (Tkinter).*
