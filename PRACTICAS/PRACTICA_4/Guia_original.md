# INSTITUTO TECNOLÓGICO DE TOLUCA

## Diodos y Transistores

### Práctica No. 4

**Objetivo.-** El objetivo de la presente práctica es que el estudiante calcule el valor de las resistencias de polarización por divisor de voltaje para un transistor FET de canal-N, de tal manera que cumpla con los requerimientos de diseño.

**Equipo:**
* Computadora personal
* Software de simulación electrónica (Pspice, Multisim o equivalente)

**Material:**
* Transistor JFET: 2N5457 / 2N3819 / 2N5951
* Resistencias según diseño

**PROCEDIMIENTO:**

1.- Diseñe el circuito de polarización para el transistor FET canal-N con matrícula 2N5457 mostrado en la figura siguiente, de tal manera que se obtenga una corriente de operación de dren de $I_D = 4 \, \text{mA}$, un voltaje de operación $V_{DS} = 6 \, \text{V}$ y con un voltaje de alimentación $V_{DD} = 15 \, \text{V}$.

---

### Descripción del Diagrama de Circuito

> **[Diagrama de Circuito]:** Se presenta un circuito de polarización por divisor de tensión para un transistor JFET de canal-N referenciado como $J_2$. En el extremo izquierdo se observa una fuente de alimentación de corriente directa $V_{DD} = 15 \, \text{V}$ conectada respecto a la referencia de tierra ($0$). La red de polarización consta de un divisor de voltaje en la compuerta formado por las resistencias $R_1$ (conectada a $V_{DD}$) y $R_2$ (conectada a tierra). El drenaje del transistor se conecta a $V_{DD}$ a través de la resistencia $R_D$, mientras que la fuente se conecta a tierra mediante la resistencia $R_S$.

---

### Netlist del Circuito (Formato SPICE)

```spice
* Netlist SPICE - Circuito de Polarización JFET (Práctica 4)

* Fuentes de Alimentación
VDD net_vdd 0 DC 15V

* Red del Divisor de Voltaje (Compuerta / Gate)
R1 net_vdd net_gate {R1_val}
R2 net_gate 0 {R2_val}

* Red de Terminales de Salida (Drenaje y Fuente)
RD net_vdd net_drain {RD_val}
RS net_source 0 {RS_val}

* Transistor JFET Canal-N (Modelo de diseño: 2N5457)
* Sintaxis: J_instancia nodo_drenaje nodo_compuerta nodo_fuente modelo
J2 net_drain net_gate net_source J2N5457

.model J2N5457 NJF(Beta=1.3m Vto=-2.5)
.END
```

Para el diseño, considere una variación de $I_D$ del +/- 0.4mA de su valor nominal $I_D = 4 \, \text{mA}$, así como su cambio correspondiente de $I_{DSS}$ máximo y mínimo, así como los valores correspondientes de $V_p$ máximo y mínimo con base a la hoja técnica del transistor FET, por lo tanto para cumplir con los requerimientos de diseño calcule los valores de R1, R2, RD y Rs con base al método de diseño visto en clase.

2.- Grafique las curvas de transferencia para el transistor para $I_{Dmax}$, $I_{Dmin}$ y $I_{Dpromedio}$, con base a la ecuación para la corriente de dren del JFET auxiliándose de la hoja técnica proporcionada por el fabricante y utilizando la ecuación de la corriente de dren dada por:

$$
I_D = I_{DSS} \left( 1 - \frac{V_{GS}}{V_p} \right)^2
$$

Una vez graficadas las curvas de transferencia, encuentre las respectivas corrientes de dren de operación $I_{DQ}$ y calcule los respectivos voltajes de salida $V_{DSQ}$ de operación para cada valor de $V_{GS}$.

3.- Posteriormente implemente el circuito en el laboratorio y compruebe los voltajes y corrientes obtenidos analíticamente: $V_G$, $I_D$ y $V_{DS}$.

4.- Finalmente simule el circuito verificando los parámetros de operación Q.

<br>

<div align="right">Elaboró: Ing. José Luís Avila Gómez</div>