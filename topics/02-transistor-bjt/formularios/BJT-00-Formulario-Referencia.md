> 🏠 **Navegación:** [← Módulo](../00-Index.md) | [📋 Índice Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

# Formulario de Referencia — Transistor BJT

Este documento compila las ecuaciones fundamentales para el análisis y diseño de circuitos con Transistores de Unión Bipolar (BJT) en CD.

---

## 1. Relaciones Fundamentales de Corriente

En cualquier configuración y región de operación (Leyes de Kirchhoff):
$$I_E = I_C + I_B$$

### Ganancia en Base Común ($\alpha$)
$$\alpha = \frac{I_C}{I_E}$$
$$I_C = \alpha I_E + I_{CBO}$$
$$\alpha = \frac{\beta}{\beta + 1}$$

### Ganancia en Emisor Común ($\beta$ o $h_{FE}$)
$$\beta = \frac{I_C}{I_B}$$
$$I_C = \beta I_B + I_{CEO}$$
$$\beta = \frac{\alpha}{1 - \alpha}$$

### Corrientes de Fuga
$$I_{CEO} = \frac{I_{CBO}}{1 - \alpha}$$
$$I_{CEO} = (\beta + 1) I_{CBO}$$

### Relaciones derivadas (útiles en CD)
* **En activa, despreciando fugas:**
$$I_C \approx \beta I_B$$
* **Corriente de emisor aproximada** (de $I_E=I_C+I_B$ e $I_C\approx\beta I_B$):
$$I_E \approx (\beta+1)I_B$$
* **Relación considerando fugas:**
$$I_C = \beta I_B + (\beta+1)I_{CBO}$$
* **Relación con Alfa (con $I_{CBO}$ despreciable):**
$$I_C \approx \alpha I_E$$
$$I_E \approx \frac{I_C}{\alpha}$$

### Voltajes de Nodo y Relaciones entre Terminales
* **Definición de voltajes entre terminales:**
$$V_{BE} = V_B - V_E$$
$$V_{CE} = V_C - V_E$$
$$V_{CB} = V_C - V_B$$
* **Suma de voltajes y simetría:**
$$V_{CE} = V_{CB} + V_{BE}$$
$$V_{BC} = -V_{CB}$$
* **Voltajes de nodo (respecto a tierra):**
$$V_E = I_E R_E$$
$$V_B = V_{BE} + V_E$$
$$V_C = V_{CE} + V_E$$
$$V_C = V_{CC} - I_C R_C$$

### Modelo Exponencial (CD)
* **Ecuación de Shockley (Relación con $V_{BE}$):**
$$I_C = I_S \left( e^{\frac{V_{BE}}{n V_T}} - 1 \right)$$
* **Aproximación para $V_{BE} \gg nV_T$:**
$$I_C \approx I_S e^{\frac{V_{BE}}{n V_T}}$$
* **Voltaje térmico ($V_T$):**
$$V_T = \frac{kT}{q} \approx 25.9\text{ mV} \quad (\text{a } T=300\text{ K})$$
> **Nota de validez:** Útil para la región activa; no se debe usar como modelo de saturación.

---

## 2. Modelos de Polarización (CD)

> **Nota de notación:** en este documento se usa $V_{TH}, R_{TH}$ (equivalentes a $V_{th}, R_{th}$).

### Polarización Fija
* **Corriente de Base:**
$$I_B = \frac{V_{CC} - V_{BE}}{R_B}$$
* **Corriente de Colector:**
$$I_C = \beta I_B$$
* **Voltaje Colector-Emisor:**
$$V_{CE} = V_{CC} - I_C R_C$$

### Polarización Estabilizada por Emisor
* **Corriente de Base:**
$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1) R_E}$$
* **Corriente de Colector:**
$$I_C = \beta I_B$$
* **Malla de Salida:**
$$V_{CE} = V_{CC} - I_C R_C - I_E R_E$$
$$V_{CE} \approx V_{CC} - I_C(R_C + R_E) \quad (I_E \approx I_C,\; \beta \gg 1)$$

### Polarización por Divisor de Voltaje (Análisis Exacto)
1.  **Equivalente de Thévenin:**
$$V_{TH} = V_{CC} \left( \frac{R_2}{R_1 + R_2} \right)$$
$$R_{TH} = R_1 \parallel R_2$$
$$R_{TH} = \frac{R_1 R_2}{R_1 + R_2}$$

2.  **Corriente de Base:**
$$I_B = \frac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1) R_E}$$

3.  **Corriente de Colector:**
$$I_C = \beta I_B$$

4.  **Criterio de Aproximación (Divisor Rígido):**
Si $R_{TH} \ll (\beta + 1)R_E$ (por ejemplo, $R_{TH} \le 0.1(\beta+1)R_E$):
$$V_B \approx V_{TH}$$

5.  **Método aproximado (con divisor rígido):**
$$I_E \approx \frac{V_B - V_{BE}}{R_E}$$
$$I_C \approx I_E$$

### Polarización por Realimentación de Colector
* **Corriente de Base:**
$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)(R_C + R_E)}$$
$$I_B \approx \frac{V_{CC} - V_{BE}}{R_B + \beta(R_C + R_E) \quad (\beta \gg 1)}$$
$$I_C = \beta I_B$$
$$V_{CE} = V_{CC} - (I_C+I_B)(R_C + R_E) \approx V_{CC} - I_C(R_C + R_E)$$
*(Nota: si no hay resistencia de emisor, $R_E = 0$)*

---

### Polarización en Base Común
$$I_E = \frac{V_{EE} - V_{BE}}{R_E}$$
$$I_C = \alpha I_E$$
$$V_C = V_{CC} - I_C R_C$$
$$V_{CB} = V_C - V_B \quad (\text{si } V_B = 0 \Rightarrow V_{CB} = V_C)$$

---

### Polarización en Colector Común (Seguidor de Emisor)
$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E}$$
$$V_E = I_E R_E \approx V_B - V_{BE}$$
$$V_{CE} = V_C - V_E \approx V_{CC} - I_E R_E \quad (\text{si } V_C = V_{CC})$$

---

## 3. Recta de Carga, Conmutación y Potencia

### Regiones de operación (resumen)

| Región | Unión BE | Unión BC | Rango de $V_{CE}$ | Comportamiento $I_C$ |
|:---|:---:|:---:|:---|:---|
| **Corte** | Inversa | Inversa | $V_{CE} = V_{CC}$ | $I_C \approx 0$ |
| **Activa** | Directa | Inversa | $V_{CE} > V_{CE,sat}$ | $I_C = \beta I_B$ |
| **Saturación** | Directa | Directa | $V_{CE} \approx V_{CE,sat}$ | $I_C < \beta I_B$ (Deja de seguir a $\beta I_B$) |

### Ecuación de la Recta de Carga DC
$$V_{CE} = V_{CC} - I_C R_C - I_E R_E$$
$$V_{CE} \approx V_{CC} - I_C(R_C + R_E) \quad (I_E \approx I_C,\; \beta \gg 1)$$

**Puntos de intersección (aprox.):**
- Eje $V_{CE}$: $I_C = 0 \Rightarrow V_{CE} = V_{CC}$
- Eje $I_C$: $V_{CE} = 0 \Rightarrow I_C \approx \frac{V_{CC}}{R_C + R_E}$

### Límites de Operación
* **Corte ($I_C = 0$):**
$$V_{CE} = V_{CC}$$
* **Saturación Real (Típica):**
$$V_{CE,sat} \approx 0.2\text{ V}$$
$$I_{C,sat} \approx \frac{V_{CC} - V_{CE,sat}}{R_C + R_E}$$

### Diseño como Interruptor (Switch)
* **Corriente de Base Crítica:**
$$I_{B,sat} = \frac{I_{C,sat}}{\beta}$$
$$R_{B(max)} = \frac{V_{CC} - V_{BE(sat)}}{I_{B,sat}}$$
* **Criterio con $\beta$ Forzada ($\beta_{forzada}$):**
$$\beta_{forzada} = \frac{I_C}{I_B} \quad (\text{en saturación})$$
* **Recomendación conservadora y corriente de diseño (Sobreexcitación):**
Típicamente se fuerza un $\beta_{forzada} \approx 10$, de tal modo que:
$$I_B \ge \frac{I_C}{\beta_{forzada}}$$
Lo cual se conecta con el criterio práctico de diseño:
$$I_{B,diseño} \approx (2 \text{ a } 10) \cdot I_{B,sat}$$

### Tiempos de conmutación
$$t_{on} = t_d + t_r$$
$$t_{off} = t_s + t_f$$

### Disipación de Potencia
* **Potencia Máxima Total en CD:**
$$P_D = V_{CE} I_C + V_{BE} I_B$$
* **Aproximación típica en región activa ($I_B \ll I_C$):**
$$P_D \approx V_{CE} I_C$$
* **Potencia en Saturación:**
$$P_D = V_{CE,sat} I_C + V_{BE(sat)} I_B$$

---

## 4. Estabilidad

### Factores de estabilidad
$$S(I_{CBO}) = \frac{\partial I_C}{\partial I_{CBO}}$$
$$S(\beta) = \frac{\partial I_C}{\partial \beta}$$
$$S(V_{BE}) = \frac{\partial I_C}{\partial V_{BE}}$$

### Variación total de $I_C$
$$\Delta I_C = S(I_{CBO})\Delta I_{CBO} + S(\beta)\Delta\beta + S(V_{BE})\Delta V_{BE}$$

### Factores de estabilidad por configuración (referencia)

| Configuración | $S(I_{CBO})$ | $S(\beta)$ | $S(V_{BE})$ | Estabilidad |
|---------------|------------|-----------|------------|-------------|
| Polarización fija | $\beta + 1$ | $I_{C1}/\beta_1$ | $-\beta/R_B$ | ❌ Mala |
| Con $R_E$ (Estabilizada) | $\frac{\beta+1}{1+\beta R_E/(R_B+R_E)}$ | $\frac{I_{C1}(R_B+R_E)}{\beta_1(R_B+R_E(\beta_2+1))}$ | $\frac{-\beta}{R_B+(\beta+1)R_E}$ | ⚠️ Regular |
| Divisor de voltaje | $\frac{(\beta+1)(1+R_{TH}/R_E)}{(\beta+1)+R_{TH}/R_E}$ | $\frac{(V_{TH}-V_{BE})(R_{TH}+R_E)}{(R_{TH}+(\beta+1)R_E)^2}$ | $\frac{-\beta}{R_{TH}+(\beta+1)R_E}$ | ✅ Buena |
| Realimentación colector | $\frac{\beta+1}{1+\beta R_C/(R_B+R_C)}$ | $\frac{I_{C1}(R_B+R_C)}{\beta_1(R_B+R_C(\beta_2+1))}$ | $\frac{-\beta}{R_B+(\beta+1)R_C}$ | ⚠️ Regular |

> **Regla práctica:** $S(I_{CBO})$ ideal = 1 (inalcanzable). Valores $< 10$ se consideran aceptables.

---

## 5. Valores típicos útiles (Silicio)

| Parámetro | Valor típico | Descripción |
| :--- | :--- | :--- |
| $V_{BE}$ | $0.7\text{ V}$ | Caída típica en activa. |
| $V_{BE(sat)}$ | $0.8\text{ V}$ | Voltaje base-emisor en saturación. |
| $V_{CE(sat)}$ | $0.2\text{ V}$ | Voltaje colector-emisor en saturación. |
| $V_T$ | $25.9\text{ mV}$ | Voltaje térmico a $300\text{ K}$ ($27^\circ\text{C}$). |
| $\alpha$ | $0.95 - 0.998$ | Ganancia en base común. |
| $\beta$ | $20 - 300$ | Ganancia en emisor común. |

---

## 6. Glosario de Variables y Símbolos

| Símbolo | Variable | Descripción | Unidad |
|:---:|:---|:---|:---:|
| $I_B$ | Corriente de Base | Corriente de entrada/control en configuración EC. | A |
| $I_C$ | Corriente de Colector | Corriente de salida controlada por la base. | A |
| $I_E$ | Corriente de Emisor | Corriente total que fluye por el terminal del emisor. | A |
| $I_S$ | Corriente de Saturación | Corriente de saturación inversa de la unión. | A |
| $V_B$ | Voltaje de Base | Potencial eléctrico en el terminal de la base respecto a tierra. | V |
| $V_C$ | Voltaje de Colector | Potencial eléctrico en el terminal del colector respecto a tierra. | V |
| $V_E$ | Voltaje de Emisor | Potencial eléctrico en el terminal del emisor respecto a tierra. | V |
| $V_{BE}$ | Voltaje Base-Emisor | Caída de voltaje en la unión B-E. | V |
| $V_{CE}$ | Voltaje Colector-Emisor | Voltaje entre terminales de salida en configuración EC. | V |
| $V_{CB}$ | Voltaje Colector-Base | Voltaje entre terminales de salida en configuración BC. | V |
| $V_{BC}$ | Voltaje Base-Colector | Caída de voltaje B-C (Inverso de $V_{CB}$). | V |
| $V_{CC}$ | Fuente de Alimentación | Voltaje de la fuente principal de CD. | V |
| $V_{EE}$ | Fuente (Emisor) | Fuente usada en polarización con base común. | V |
| $V_T$ | Voltaje Térmico | Potencial equivalente a la temperatura ($kT/q$). | V |
| $k$ | Cte. de Boltzmann | Relación entre energía térmica y temperatura ($1.38 \times 10^{-23}\text{ J/K}$). | J/K |
| $q$ | Carga elemental | Magnitud de la carga del electrón ($1.6 \times 10^{-19}\text{ C}$). | C |
| $T$ | Temp. absoluta | Temperatura en escala Kelvin. | K |
| $\beta$ | Ganancia Beta | Ganancia de corriente en CD ($h_{FE}$) para configuración EC. | - |
| $\beta_{forzada}$ | Beta Forzada | Relación $I_C/I_B$ en saturación (usada en diseño). | - |
| $\alpha$ | Ganancia Alfa | Ganancia de corriente en CD para configuración BC. | - |
| $n$ | Factor de Idealidad | Factor de idealidad de la unión (1 a 2). | - |
| $R_1$ | Resistencia superior | Resistencia conectada entre $V_{CC}$ y base en un divisor. | $\Omega$ |
| $R_2$ | Resistencia inferior | Resistencia conectada entre base y tierra en un divisor. | $\Omega$ |
| $R_B$ | Resistencia de Base | Resistencia que limita la corriente $I_B$. | $\Omega$ |
| $R_C$ | Resistencia de Colector | Resistencia de carga conectada al colector. | $\Omega$ |
| $R_E$ | Resistencia de Emisor | Resistencia de estabilización en el emisor. | $\Omega$ |
| $V_{TH}$ | Voltaje de Thévenin | Voltaje equivalente del divisor de base. | V |
| $R_{TH}$ | Resistencia de Thévenin | Resistencia equivalente del divisor de base. | $\Omega$ |
| $I_{CBO}$ | Corriente de Fuga | Corriente colector-base con emisor abierto ($I_{CO}$). | A |
| $I_{CEO}$ | Corriente de Fuga | Corriente colector-emisor con base abierta. | A |
| $S(I_{CBO})$ | Factor de Estabilidad | Sensibilidad de $I_C$ ante cambios en $I_{CBO}$. | - |
| $V_{BE(sat)}$ | Saturación B-E | Voltaje base-emisor en saturación. | V |
| $V_{CE,sat}$ | Saturación C-E | Voltaje colector-emisor en saturación. | V |
| $t_{on}$ | Tiempo de encendido | $t_{on}=t_d+t_r$. | s |
| $t_{off}$ | Tiempo de apagado | $t_{off}=t_s+t_f$. | s |
| $P_D$ | Potencia Disipada | Energía por unidad de tiempo convertida en calor. | W |
| $Q$ | Punto de Operación | Par de valores $(V_{CE}, I_C)$ en reposo. | - |

---
**Bibliografía:** Boylestad, 11va Ed. Cap 3 y 4.