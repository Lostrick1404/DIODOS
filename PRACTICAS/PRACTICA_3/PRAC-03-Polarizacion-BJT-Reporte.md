
<!--
::METADATA::
type: solution
topic_id: practica-3-bjt-ec-divisor
file_id: PRACTICA_3_COMPLETA
status: draft
audience: student
last_updated: 2026-05-05
-->

# INSTITUTO TECNOLÓGICO DE TOLUCA
## Ingeniería Electrónica
### Diodos y Transistores
#### Práctica-3 — Polarización BJT en Emisor Común (Divisor de voltaje)

---

## Plan de trabajo (solo teoría + secciones pendientes)

Con base en el manual de la práctica y la hoja de datos (Motorola) del **BC548-B**, el trabajo se organiza en tres bloques:

### 1) Datos teóricos y de diseño (proporcionados)

- **Configuración:** Emisor Común con polarización por **divisor de voltaje**.
- **Transistor:** BJT NPN **BC548-B**.
- **Voltaje de alimentación:** $V_{CC}=15\,V$.
- **Corriente de operación deseada:** $I_C=50\,mA$.
- **Ganancia mínima (peor caso):** $\beta_{min}=200$ (referida en datasheet a $I_C=2\,mA$ y $V_{CE}=5\,V$).
- **Voltaje base-emisor:** usar $V_{BE(on)}\approx0.7\,V$ como estándar de cálculo.
	- Nota: el datasheet también reporta valores máximos mayores en otras condiciones (p.ej. $0.77\,V$ a $10\,mA$), por lo que simulación/medición pueden diferir.

### 2) Valores teóricos a calcular (diseño analítico)

- Corrientes: $I_B$, $\alpha_F$, $I_E$.
- Voltajes: $V_E$, $V_{CE}$ (y nodos auxiliares $V_B$, $V_C$).
- Equivalente de Thévenin en base: $V_{TH}$ y $R_{TH}$.
- Resistencias a dimensionar: $R_C$, $R_E$, $R_1$, $R_2$.
- Potencias: $P_{R1}$, $P_{R2}$, $P_{RC}$, $P_{RE}$.
- Punto de operación teórico: $Q=(V_{CEQ}, I_{CQ})$.

### 3) Datos pendientes (gráfico, simulación y laboratorio)

Estos resultados se obtienen con la recta de carga sobre curvas del fabricante, con PSpice y con medición física. Se dejan como **secciones a llenar** con simbología estándar:

- Punto Q **gráfico** (curvas del fabricante): $V_{CEQ\_graf}$, $I_{CQ\_graf}$.
- Resultados de **simulación** (Bias Point): variables con sufijo `_sim`.
- Resultados **experimentales** (laboratorio): variables con sufijo `_exp`.

---

## Objetivo

Diseñar la polarización de CD para localizar el punto de operación $Q$ del transistor en la región activa (lineal) en configuración de **Emisor Común** con **divisor de voltaje**, usando el peor caso $\beta_{min}$ del datasheet. La simulación (PSpice) y la implementación física se dejan como apartados a completar.

---

## Material

1. Transistor BC548-B
2. Resistencias según diseño

## Equipo

1. Multímetro
2. Fuente de alimentación de CD
3. Software OrCAD PSpice (pendiente)

---

## 1. Diseño analítico (Thévenin, peor caso $\beta_{min}$)

### 1.1 Criterios de diseño elegidos

Como el enunciado fija $V_{CC}$ e $I_C$ pero no fija explícitamente $V_{CEQ}$, se adopta un criterio clásico de diseño centrado:

- $V_{CEQ} \approx \frac{V_{CC}}{2} = 7.5\,V$
- $V_E \approx 0.1 V_{CC} = 1.5\,V$
- $V_{BE} \approx 0.7\,V$

> Estos criterios buscan margen dinámico y estabilidad con realimentación por $R_E$.

### 1.2 Corrientes (usando $I_C=50\,mA$ y $\beta_{min}=200$)

Corriente de base:
$$I_B = \frac{I_C}{\beta_{min}} = \frac{50\,mA}{200} = 0.25\,mA$$

Factor $\alpha_F$:
$$\alpha_F = \frac{\beta}{1+\beta} = \frac{200}{201} \approx 0.9950$$

Corriente de emisor:
$$I_E = I_C + I_B = 50\,mA + 0.25\,mA = 50.25\,mA$$

### 1.3 Voltajes de nodos objetivo

Voltaje de base:
$$V_B = V_E + V_{BE} = 1.5\,V + 0.7\,V = 2.2\,V$$

Voltaje de colector (para lograr $V_{CEQ}=7.5\,V$):
$$V_C = V_{CEQ} + V_E = 7.5\,V + 1.5\,V = 9.0\,V$$

### 1.4 Dimensionamiento de $R_C$ y $R_E$

Resistencia de colector:
$$R_C = \frac{V_{CC}-V_C}{I_C} = \frac{15-9}{0.05} = 120\,\Omega$$

Resistencia de emisor:
$$R_E = \frac{V_E}{I_E} = \frac{1.5}{0.05025} \approx 29.85\,\Omega$$

### 1.5 Diseño del divisor $R_1$–$R_2$ (regla $I_2 \approx 10 I_B$)

Para minimizar el efecto de carga de la base, se adopta una regla práctica:
$$I_2 \approx 10 I_B = 10(0.25\,mA) = 2.5\,mA$$

Entonces:
$$R_2 = \frac{V_B}{I_2} = \frac{2.2}{0.0025} = 880\,\Omega$$

La corriente por $R_1$ es:
$$I_1 = I_2 + I_B = 2.5\,mA + 0.25\,mA = 2.75\,mA$$

Por tanto:
$$R_1 = \frac{V_{CC}-V_B}{I_1} = \frac{15-2.2}{0.00275} \approx 4654.55\,\Omega$$

### 1.6 Equivalente de Thévenin en la base ($V_{TH}$ y $R_{TH}$)

Resistencia de Thévenin:
$$R_{TH} = R_1 \| R_2 = \frac{R_1 R_2}{R_1 + R_2} \approx 740\,\Omega$$

Voltaje de Thévenin:
$$V_{TH} = V_{CC}\left(\frac{R_2}{R_1+R_2}\right) \approx 2.385\,V$$

**Verificación (método exacto de Thévenin):**
$$I_B = \frac{V_{TH}-V_{BE}}{R_{TH}+(\beta+1)R_E} =
\frac{2.385-0.7}{740 + (201)(29.85)} \approx 0.25\,mA$$

Luego:
$$I_C = \beta I_B \approx 200(0.25\,mA)=50\,mA$$

### 1.7 Resumen de resultados teóricos

| Magnitud | Símbolo | Resultado |
|---|---:|---:|
| Corriente de colector (diseño) | $I_C$ | $50\,mA$ |
| Corriente de base | $I_B$ | $0.25\,mA$ |
| Factor | $\alpha_F$ | $\approx 0.9950$ |
| Corriente de emisor | $I_E$ | $50.25\,mA$ |
| Voltaje de emisor | $V_E$ | $1.5\,V$ |
| Voltaje colector–emisor (Q) | $V_{CEQ}$ | $7.5\,V$ |
| Equivalente de Thévenin | $R_{TH}$ | $\approx 740\,\Omega$ |
| Equivalente de Thévenin | $V_{TH}$ | $\approx 2.385\,V$ |
| Resistencia de colector | $R_C$ | $120\,\Omega$ |
| Resistencia de emisor | $R_E$ | $\approx 29.85\,\Omega$ |
| Divisor (arriba) | $R_1$ | $\approx 4.655\,k\Omega$ |
| Divisor (abajo) | $R_2$ | $880\,\Omega$ |
| Potencia en $R_1$ | $P_{R1}$ | $\approx 0.035\,W$ |
| Potencia en $R_2$ | $P_{R2}$ | $\approx 0.0055\,W$ |
| Potencia en $R_C$ | $P_{RC}$ | $0.30\,W$ |
| Potencia en $R_E$ | $P_{RE}$ | $\approx 0.075\,W$ |

---

## 2. Potencias disipadas (teórico)

Potencia en $R_C$:
$$P_{RC} = I_C^2R_C = (0.05)^2(120) = 0.30\,W$$

Potencia en $R_E$:
$$P_{RE} = I_E^2R_E \approx (0.05025)^2(29.85) \approx 0.075\,W$$

Potencia en $R_1$:
$$P_{R1} = \frac{(V_{CC}-V_B)^2}{R_1} = \frac{(12.8)^2}{4654.55} \approx 0.035\,W$$

Potencia en $R_2$:
$$P_{R2} = \frac{V_B^2}{R_2} = \frac{(2.2)^2}{880} \approx 0.0055\,W$$

Chequeo de disipación del transistor en Q:
$$P_Q \approx V_{CEQ}I_C = (7.5)(0.05) = 0.375\,W < 0.625\,W$$

**Recomendación mínima de wattaje (con margen):**
- $R_C$: $\ge 1/2\,W$ (por $P_{RC}\approx0.30\,W$)
- $R_E$, $R_1$, $R_2$: $1/4\,W$ suficiente

---

## 3. Punto de operación teórico

$$Q = (V_{CEQ}, I_{CQ}) = (7.5\,V, 50\,mA)$$

---

## 4. Recta de carga DC sobre curvas del fabricante (pendiente)

Ecuación de la recta de carga DC (aproximación con $I_C$):
$$V_{CE} = V_{CC} - I_C(R_C+R_E)$$

Puntos extremos teóricos:

- Corte: $(V_{CE}=V_{CC}=15\,V,\ I_C=0)$
- Saturación ideal: $(V_{CE}=0,\ I_C=\frac{V_{CC}}{R_C+R_E})$

Con $R_C+R_E\approx 149.85\,\Omega$:
$$I_{C(sat)}\approx \frac{15}{149.85} \approx 100.1\,mA$$

Campos a llenar (resultado gráfico):

- $V_{CEQ\_graf}=\_\_\_$
- $I_{CQ\_graf}=\_\_\_$

---

## 5. Simulación en PSpice (Bias Point) — pendiente

Campos a llenar (resultados simulados):

- $V_{B\_sim}=\_\_\_$, $V_{C\_sim}=\_\_\_$, $V_{E\_sim}=\_\_\_$
- $I_{B\_sim}=\_\_\_$, $I_{C\_sim}=\_\_\_$, $I_{E\_sim}=\_\_\_$
- $V_{CE\_sim}=\_\_\_$

---

## 6. Implementación física (laboratorio) — pendiente

Campos a llenar (resultados experimentales):

- $V_{B\_exp}=\_\_\_$, $V_{C\_exp}=\_\_\_$, $V_{E\_exp}=\_\_\_$
- $I_{B\_exp}=\_\_\_$, $I_{C\_exp}=\_\_\_$, $I_{E\_exp}=\_\_\_$
- $V_{CE\_exp}=\_\_\_$

---

## 7. Conclusiones — pendiente

- Conclusión 1: \_\_\_
- Conclusión 2: \_\_\_
- Conclusión 3: \_\_\_

Elaboró: Ing. José Luis Avila Gómez
