
# Valores de la Hoja Técnica para BC548-B (Cálculos del Punto 1)

Para llevar a cabo el diseño del circuito de polarización solicitado en la práctica, se extraen los siguientes parámetros fundamentales de la hoja de especificaciones del fabricante para el modelo **BC548-B**:

* **Ganancia de corriente de CD mínima** ($\beta_{\text{min}}$ o $h_{FE(\text{min})}$): $200$ (Valor en el peor de los casos, referenciado a $I_C = 2.0 \, \text{mA}$ y $V_{CE} = 5.0 \, \text{V}$).

* **Ganancia de corriente de CD típica** ($\beta_{\text{typ}}$ o $h_{FE(\text{typ})}$): $290$ (Referenciado a $I_C = 2.0 \, \text{mA}$ y $V_{CE} = 5.0 \, \text{V}$).

* **Voltaje Base-Emisor de encendido** ($V_{BE(\text{on})}$): $0.55 \, \text{V}$ como mínimo y hasta $0.7 \, \text{V}$ como máximo a $I_C = 2.0 \, \text{mA}$. *(Nota: Para cálculos teóricos de malla de entrada, el estándar asume típicamente $0.7 \, \text{V}$)*.

* **Corriente de Colector continua máxima** ($I_{C(\text{max})}$): $100 \, \text{mA}$. *(Este valor valida que la operación solicitada a $I_C = 50 \, \text{mA}$ se encuentra dentro del rango seguro de operación)*.

* **Voltaje Colector-Emisor de ruptura** ($V_{CEO}$): $30 \, \text{V}$. *(Este valor valida que la fuente de alimentación del diseño $V_{CC} = 15 \, \text{V}$ es adecuada y segura)*.

* **Voltaje Colector-Emisor en saturación** ($V_{CE(\text{sat})}$): $0.2 \, \text{V}$ típico a $0.6 \, \text{V}$ máximo (Referenciado a un escenario de $I_C = 100 \, \text{mA}$ y $I_B = 5.0 \, \text{mA}$).

* **Disipación total del dispositivo** ($P_D$): $625 \, \text{mW}$ medido a $T_A = 25^\circ\text{C}$. *(Útil para el cálculo final de potencias disipadas en el transistor)*.
