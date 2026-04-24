<!--
::METADATA::
type: theory
topic_id: bjt-emisor-comun-polarizacion
file_id: Nota4
status: draft
audience: student
last_updated: 2024-05-16
-->

> 🏠 **Navegación:** [← Volver al Índice](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md) | [🔙 Notas BJT](README.md)

---

## Configuraciones de Polarización para Emisor Común

En la figura siguiente se muestra un transistor NPN en configuración de Emisor Común (E-com), el cual está polarizado por la fuente $V_{CC}$. En esta configuración, los valores de $R_B$ y $R_C$ deben ser seleccionados tal que la caída de voltaje en $R_B$ sea más grande que la caída de voltaje en $R_C$ para asegurar que la unión Base-Colector (B-C) esté polarizada inversamente.

La polarización de la unión Base-Emisor (B-E) se logra a través de $R_B$ y $V_{CC}$, estableciendo la corriente de base $I_B$. La corriente de colector $I_C$ es entonces controlada por $I_B$ ($I_C = \beta I_B$). Para que el transistor opere en la región activa (necesaria para amplificación), la unión B-E debe estar polarizada en directa y la unión B-C en inversa.

### Malla de entrada (equivalente con $V_{BE}$)

Redibujando la **sección de entrada** (base–emisor) del circuito, se puede modelar la unión B-E como un diodo con caída aproximadamente constante $V_{BE}\approx 0.7\,V$ (silicio), quedando la malla:

![Malla de entrada con $V_{BE}$](../assets/bjt-malla-entrada-vbe.png)

Aplicando **LVK** en la malla de entrada:

$$-V_{CC} + R_B I_B + V_{BE} = 0$$

Despejando $I_B$:

$$R_B I_B = V_{CC} - V_{BE} \;\;\Rightarrow\;\; I_B = \frac{V_{CC} - V_{BE}}{R_B} \approx \frac{V_{CC} - 0.7\,V}{R_B}$$

La condición para que la unión B-C esté polarizada inversamente es que el voltaje del colector ($V_C$) sea mayor que el voltaje de la base ($V_B$).

$$ V_C > V_B $$

Donde $V_C = V_{CC} - I_C R_C$ y $V_B = V_{CC} - I_B R_B$.

### Esquema de Polarización Fija (Emisor Común)

![Esquema de Polarización Fija (Emisor Común)](../assets/bjt-emisor-comun-polarizacion-fija.png)

---

## Recta de carga DC (malla de salida)

Aplicando la **Ley de Voltajes de Kirchhoff (LVK)** en la malla de salida (fuente–resistencia de colector–transistor):

$$-V_{CC} + R_C I_C + V_{CE} = 0$$

Reordenando:

$$V_{CE} = V_{CC} - R_C I_C$$

Esta ecuación es la **recta de carga DC**, porque describe todas las combinaciones posibles $(V_{CE}, I_C)$ impuestas por $V_{CC}$ y $R_C$.

> Si el circuito incluye una resistencia de emisor $R_E$ (polarización con emisor), la LVK de la malla de salida queda:
> $$-V_{CC} + I_C(R_C + R_E) + V_{CE} = 0 \;\;\Rightarrow\;\; V_{CE} = V_{CC} - I_C(R_C + R_E)$$
> La ecuación $-V_{CC} + R_C I_C + V_{CE} = 0$ es el caso particular con $R_E = 0$.

### Formas útiles para despejar $V_{CE}$ e $I_C$

- Si necesitas $V_{CE}$ en función de $I_C$:
	$$V_{CE}(I_C) = V_{CC} - R_C I_C$$

- Si necesitas $I_C$ en función de $V_{CE}$:
	$$I_C(V_{CE}) = \frac{V_{CC} - V_{CE}}{R_C}$$

### Intersecciones (puntos extremos)

- **Corte** ($I_C = 0$):
	$$V_{CE} = V_{CC}$$

- **Saturación ideal** ($V_{CE} = 0$):
	$$I_C = \frac{V_{CC}}{R_C}$$

En la práctica, en saturación suele cumplirse $V_{CE} \approx V_{CE(sat)}$ (típicamente 0.1–0.3 V), por lo que el extremo de corriente queda apenas por debajo de $V_{CC}/R_C$.

### Gráfico: recta de carga

![Recta de Carga DC](../assets/bjt_recta_carga_dc.png)

---

## Ejemplo — Punto de operación ($\beta=100$)

Un transistor **NPN de silicio** en **emisor común** (E-com) está polarizado como se muestra (emisor a tierra). Datos:

- $V_{CC}=12\,V$
- $R_B=376.67\,k\Omega$
- $R_C=2\,k\Omega$
- $\beta=100$
- Supón $V_{BE}\approx 0.7\,V$ y $V_{CE(sat)}\approx 0.2\,V$

![Circuito ejemplo EC](../assets/bjt-ejemplo-ec-circuito-12v-rb-rc.png)

### A) Punto de operación (método gráfico)

**1) Recta de carga (malla de salida):**

Aplicando LVK:

$$-V_{CC}+R_C I_C+V_{CE}=0 \;\Rightarrow\; V_{CE}=V_{CC}-R_C I_C$$

Puntos de intersección:

- Si $I_C=0 \Rightarrow V_{CE}=V_{CC}=12\,V$
- Si $V_{CE}=0 \Rightarrow I_C=\dfrac{V_{CC}}{R_C}=\dfrac{12\,V}{2\,k\Omega}=6\,mA$

**2) Corriente de base (malla de entrada):**

Aplicando LVK:

$$-V_{CC}+R_B I_B+V_{BE}=0 \;\Rightarrow\; I_B=\frac{V_{CC}-V_{BE}}{R_B}$$

> Nota: no es correcto escribir $I_B=V_{CC}-\frac{V_{BE}}{R_B}$; el despeje correcto es $I_B=\frac{V_{CC}-V_{BE}}{R_B}$.

Sustituyendo $V_{BE}=0.7\,V$ y $R_B=376.67\,k\Omega$:

$$I_B=\frac{12-0.7}{376.67\times10^3}\approx 30\,\mu A$$

**3) Punto de operación $Q$ (intersección gráfica):**

En la gráfica de curvas de salida, se toma la curva cercana a $I_B\approx 30\,\mu A$ y se intersecta con la recta de carga.

En este caso, la intersección da aproximadamente:

$$Q=(V_{CEQ}, I_{CQ})\approx (6.0\,V,\; 3.0\,mA)$$

Como $V_{CEQ}\gg V_{CE(sat)}$, el transistor opera en **región activa**.

![Curvas de salida + recta de carga (ejemplo)](../assets/bjt-ejemplo-ec-curvas-q-recta-carga.png)

### B) Punto de operación (método analítico)

**1) Malla de entrada (LVK):**

$$-V_{CC}+R_B I_B+V_{BE}=0 \;\Rightarrow\; I_B=\frac{V_{CC}-V_{BE}}{R_B}$$

Sustituyendo:

$$I_B=\frac{12-0.7}{376.67\times10^3}\approx 30.0\,\mu A$$

**2) Corriente de colector (región activa):**

Como $\beta=\dfrac{I_C}{I_B}$, entonces (despreciando corrientes de fuga):

$$I_{CQ}=\beta I_B\approx 100\,(30\,\mu A)=3.0\,mA$$

**3) Malla de salida (recta de carga):**

$$V_{CEQ}=V_{CC}-R_C I_{CQ}=12-(2\,k\Omega)(3.0\,mA)=6.0\,V$$

Como $V_{CEQ}=6.0\,V \gg V_{CE(sat)}$, el transistor queda en **región activa** y el punto calculado es consistente.

### C) Punto de operación (gráfico) si $R_B=161.43\,k\Omega$

Primero, la nueva corriente de base:

$$I_B=\frac{12-0.7}{161.43\times10^3}\approx 70.0\,\mu A$$

Si estuviera en activa, $I_C=\beta I_B\approx 7.0\,mA$. Pero la recta de carga limita la corriente máxima a:

$$I_{C(\max)}\approx \frac{V_{CC}}{R_C}=\frac{12}{2\,k\Omega}=6.0\,mA$$

Por lo tanto, el punto Q se desplaza hacia **saturación** (cerca de $V_{CE(sat)}$). Gráficamente (intersección de la recta de carga con la región de saturación):

En la gráfica, se toma la curva cercana a $I_B\approx 70\,\mu A$ y se intersecta con la recta de carga. La intersección ocurre en la zona de saturación y da aproximadamente:

$$Q=(V_{CEQ}, I_{CQ})\approx (0.17\,V,\; 5.9\,mA)$$

Como verificación rápida (aproximación típica de saturación):

$$I_{CQ}\approx \frac{V_{CC}-V_{CE(sat)}}{R_C}=\frac{12-0.2}{2\,k\Omega}\approx 5.9\,mA$$