<!--
::METADATA::
type: cheatsheet
topic_id: bjt-formulas
file_id: BJT-00-Formulario-Referencia
status: stable
audience: student
last_updated: 2026-05-06
-->

> 🏠 **Navegación:** [← Módulo](../00-Index.md) | [📋 Índice Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

# Formulario de Referencia — Transistor BJT

Este documento compila las ecuaciones fundamentales para el análisis y diseño de circuitos con Transistores de Unión Bipolar (BJT) en CD.

---

## 1. Relaciones Fundamentales de Corriente

En cualquier configuración y región de operación (Leyes de Kirchhoff):
$$ I_E = I_C + I_B $$

### Ganancia en Base Común ($\alpha$)
$$ \alpha = \frac{I_C}{I_E} $$
$$ I_C = \alpha I_E + I_{CBO} $$
$$ \alpha = \frac{\beta}{\beta + 1} $$

### Ganancia en Emisor Común ($\beta$ o $h_{FE}$)
$$ \beta = \frac{I_C}{I_B} $$
$$ I_C = \beta I_B + I_{CEO} $$
$$ \beta = \frac{\alpha}{1 - \alpha} $$

### Corrientes de Fuga
$$ I_{CEO} = \frac{I_{CBO}}{1 - \alpha} $$
$$ I_{CEO} = (\beta + 1) I_{CBO} $$

### Voltajes de Nodo (Respecto a Tierra)
$$ V_E = I_E R_E $$
$$ V_B = V_{BE} + V_E $$
$$ V_C = V_{CE} + V_E $$
$$ V_C = V_{CC} - I_C R_C $$

---

## 2. Modelos de Polarización (Emisor Común)

### Polarización Fija
*   **Corriente de Base:**
$$ I_B = \frac{V_{CC} - V_{BE}}{R_B} $$
*   **Voltaje Colector-Emisor:**
$$ V_{CE} = V_{CC} - I_C R_C $$

### Polarización Estabilizada por Emisor
*   **Corriente de Base:**
$$ I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1) R_E} $$
*   **Malla de Salida:**
$$ V_{CE} = V_{CC} - I_C(R_C + R_E) $$

### Polarización por Divisor de Voltaje (Análisis Exacto)
1.  **Equivalente de Thévenin:**
$$ V_{TH} = V_{CC} \left( \frac{R_2}{R_1 + R_2} \right) $$
$$ R_{TH} = R_1 \parallel R_2 $$
$$ R_{TH} = \frac{R_1 R_2}{R_1 + R_2} $$

2.  **Corriente de Base:**
$$ I_B = \frac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1) R_E} $$

3.  **Criterio de Aproximación (Divisor Rígido):**
Si $\beta R_E \ge 10 R_2$:
$$ V_B \approx V_{TH} $$

### Polarización por Realimentación de Colector
*   **Corriente de Base:**
$$ I_B = \frac{V_{CC} - V_{BE}}{R_B + \beta(R_C + R_E)} $$
*(Nota: Si no hay resistencia de emisor, $R_E = 0$)*

---

## 3. Recta de Carga, Conmutación y Potencia

### Ecuación de la Recta de Carga DC
$$ V_{CE} = V_{CC} - I_C(R_C + R_E) $$

### Límites de Operación
*   **Corte ($I_C = 0$):**
$$ V_{CE} = V_{CC} $$
*   **Saturación Ideal ($V_{CE} = 0$):**
$$ I_{C,sat} = \frac{V_{CC}}{R_C + R_E} $$
*   **Saturación Real (Típica):**
$$ V_{CE,sat} \approx 0.2\,\text{V} $$

### Diseño como Interruptor (Switch)
*   **Corriente de Base Crítica:**
$$ I_{B,min} = \frac{I_{C,sat}}{\beta} $$
*   **Corriente de Diseño (Sobreexcitación):**
$$ I_{B,diseño} \approx (2 \text{ a } 10) \cdot I_{B,min} $$

### Disipación de Potencia
*   **Potencia Máxima en CD:**
$$ P_D = V_{CE} I_C $$

---

## 4. Glosario de Variables y Símbolos

| Símbolo | Variable | Descripción | Unidad |
|:---:|:---|:---|:---:|
| $I_B$ | Corriente de Base | Corriente de entrada/control en configuración EC. | A |
| $I_C$ | Corriente de Colector | Corriente de salida controlada por la base. | A |
| $I_E$ | Corriente de Emisor | Corriente total que fluye por el terminal del emisor. | A |
| $V_B$ | Voltaje de Base | Potencial eléctrico en el terminal de la base respecto a tierra. | V |
| $V_C$ | Voltaje de Colector | Potencial eléctrico en el terminal del colector respecto a tierra. | V |
| $V_E$ | Voltaje de Emisor | Potencial eléctrico en el terminal del emisor respecto a tierra. | V |
| $V_{BE}$ | Voltaje Base-Emisor | Caída de voltaje en la unión B-E (aprox. $0.7\,\text{V}$ para silicio). | V |
| $V_{CE}$ | Voltaje Colector-Emisor | Voltaje entre terminales de salida en configuración EC. | V |
| $V_{CB}$ | Voltaje Colector-Base | Voltaje entre terminales de salida en configuración BC. | V |
| $V_{CC}$ | Fuente de Alimentación | Voltaje de la fuente principal de CD. | V |
| $\beta$ | Ganancia Beta | Ganancia de corriente en CD ($h_{FE}$) para configuración EC. | - |
| $\alpha$ | Ganancia Alfa | Ganancia de corriente en CD para configuración BC. | - |
| $R_B$ | Resistencia de Base | Resistencia que limita la corriente $I_B$. | $\Omega$ |
| $R_C$ | Resistencia de Colector | Resistencia de carga conectada al colector. | $\Omega$ |
| $R_E$ | Resistencia de Emisor | Resistencia de estabilización en el emisor. | $\Omega$ |
| $V_{TH}$ | Voltaje de Thévenin | Voltaje equivalente del divisor de base. | V |
| $R_{TH}$ | Resistencia de Thévenin | Resistencia equivalente del divisor de base. | $\Omega$ |
| $I_{CBO}$ | Corriente de Fuga | Corriente colector-base con emisor abierto. | A |
| $I_{CEO}$ | Corriente de Fuga | Corriente colector-emisor con base abierta. | A |
| $P_D$ | Potencia Disipada | Energía por unidad de tiempo convertida en calor por el BJT. | W |
| $Q$ | Punto de Operación | Par de valores $(V_{CE}, I_C)$ en reposo. | - |

---
**Bibliografía:** Boylestad, 11va Ed. Cap 3 y 4.
