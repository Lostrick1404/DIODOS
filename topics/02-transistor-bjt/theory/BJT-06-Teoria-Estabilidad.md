<!--
::METADATA::
type: theory
topic_id: bjt-06
file_id: BJT-06-Teoria-Estabilidad
status: review
audience: both
last_updated: 2026-05-06
-->

> 🏠 **Navegación:** [← Módulo](../00-Index.md) | [📋 Índice Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

# 2.4 — Estabilidad del Punto de Operación

La **estabilidad** se refiere a la capacidad de un circuito de polarización para mantener el punto de operación ($Q$) constante a pesar de las variaciones en los parámetros del transistor y las condiciones ambientales (principalmente la temperatura).

## 1. Factores de Inestabilidad

El punto $Q$ ($I_C, V_{CE}$) puede desplazarse debido a tres factores principales que son altamente dependientes de la temperatura:

1.  **Ganancia de Corriente ($\beta$):** $\beta$ aumenta significativamente con la temperatura. También varía entre transistores del mismo modelo debido a tolerancias de fabricación.
2.  **Voltaje Base-Emisor ($V_{BE}$):** Disminuye aproximadamente $2.5\,\text{mV}$ por cada grado Celsius de incremento en la temperatura.
3.  **Corriente de Fuga ($I_{CO}$ o $I_{CBO}$):** Se duplica aproximadamente cada $10\,^\circ\text{C}$ de incremento térmico.

## 2. Mecanismo de Estabilización por Emisor

La técnica más efectiva para contrarrestar la inestabilidad es la **realimentación negativa** mediante la adición de una resistencia de emisor ($R_E$).

### Proceso de Compensación Automática:
1.  Si la temperatura aumenta, $\beta$ e $I_{CO}$ tienden a incrementar la corriente de colector ($I_C \uparrow$).
2.  Dado que $I_E \approx I_C$, la corriente de emisor también aumenta ($I_E \uparrow$).
3.  El voltaje en el emisor respecto a tierra sube: $V_E = I_E R_E \uparrow$.
4.  Si el voltaje de base ($V_B$) es fijo (como en el divisor de voltaje), el voltaje neto entre base y emisor disminuye:
    $$ V_{BE} = V_B - V_E \downarrow $$
5.  Al reducirse $V_{BE}$, la corriente de base disminuye ($I_B \downarrow$), lo que a su vez obliga a $I_C$ a bajar ($I_C \downarrow$), compensando el incremento inicial.

![Configuración con Estabilización de Emisor](../assets/bjt-emisor-comun-estabilizacion.png)

## 3. Factores de Estabilidad ($S$)

Matemáticamente, la estabilidad se cuantifica mediante factores de sensibilidad. El más común es el factor de estabilidad respecto a $I_{CO}$:

$$ S(I_{CO}) = \frac{\Delta I_C}{\Delta I_{CO}} $$

Para un circuito con resistencia de emisor, se demuestra que:
$$ S \approx \frac{1 + R_B/R_E}{1 + R_B/(\beta R_E)} $$

*   **Interpretación:** Un valor de $S$ bajo indica una alta estabilidad. El diseño ideal busca que $R_E$ sea grande y $R_B$ (o $R_{TH}$) sea pequeña para minimizar el factor $S$.

## 4. Comparativa de Configuraciones

| Configuración | Estabilidad | Razón |
|---|---|---|
| **Polarización Fija** | Muy Baja | $I_C$ depende directamente de $\beta$. |
| **Realimentación de Colector** | Media | $R_C$ actúa como lazo de realimentación. |
| **Divisor de Voltaje** | Muy Alta | $V_B$ es rígido y $R_E$ proporciona realimentación fuerte. |

---
*Nota: Para ver la verificación numérica de la estabilidad en un diseño real, consulte el ejemplo en el tema 2.2.1.*
