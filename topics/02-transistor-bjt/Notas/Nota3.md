<!--
::METADATA::
type: theory
topic_id: bjt-emisor-comun-corrientes
file_id: Nota3
status: draft
audience: student
last_updated: 2024-05-15
-->

> 🏠 **Navegación:** [← Volver al Índice](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md) | [🔙 Notas BJT](README.md)

---

## Relación entre Corrientes en Configuración Emisor Común

En esta sección se determina la corriente inversa de fuga $I_{CEO}$ y la ganancia de corriente ($\beta$) para un transistor BJT en configuración de Emisor Común (E-com).

Partimos de las relaciones fundamentales de corriente en un transistor BJT:

1.  La corriente de colector ($I_C$) en función de la corriente de emisor ($I_E$) y la corriente de fuga inversa colector-base ($I_{CBO}$):
    $$ I_C = \alpha I_E + I_{CBO} $$
    Donde $\alpha$ es la ganancia de corriente en configuración de base común.

    Despejando $I_E$ de esta ecuación, obtenemos:
    $$ \alpha I_E = I_C - I_{CBO} $$
    $$ I_E = \frac{I_C}{\alpha} - \frac{I_{CBO}}{\alpha} $$

2.  La relación entre las corrientes de emisor ($I_E$), colector ($I_C$) y base ($I_B$):
    $$ I_E = I_C + I_B $$

Nuestro objetivo es expresar $I_C$ en términos de $I_B$, $\alpha$ e $I_{CBO}$, lo cual es característico de la configuración de emisor común.

Sustituimos la ecuación (2) en la ecuación (1) (la forma original de la ecuación de $I_C$):
$$ I_C = \alpha (I_C + I_B) + I_{CBO} $$

Distribuimos $\alpha$ en el paréntesis:
$$ I_C = \alpha I_C + \alpha I_B + I_{CBO} $$

Agrupamos los términos que contienen $I_C$ en un lado de la ecuación:
$$ I_C - \alpha I_C = \alpha I_B + I_{CBO} $$

Factorizamos $I_C$:
$$ I_C (1 - \alpha) = \alpha I_B + I_{CBO} $$

Finalmente, despejamos $I_C$:
$$ \boxed{I_C = \frac{\alpha}{1 - \alpha} I_B + \frac{I_{CBO}}{1 - \alpha}} $$

Para simplificar esta expresión, se aplican los siguientes cambios de variable:

*   **Ganancia de corriente en emisor común ($\beta$ o $h_{FE}$):**
    $$ \beta = \frac{\alpha}{1 - \alpha} $$
    Este parámetro relaciona la corriente de colector con la corriente de base, indicando la capacidad de amplificación de corriente del transistor en esta configuración.

*   **Corriente de fuga colector-emisor con base abierta ($I_{CEO}$):**
    $$ I_{CEO} = \frac{I_{CBO}}{1 - \alpha} $$
    Esta es la corriente de colector que fluye cuando la base está en circuito abierto ($I_B = 0$), y es significativamente mayor que $I_{CBO}$ debido al efecto de amplificación.

Así, la ecuación de corriente de colector en emisor común se puede reescribir como:
$$ \boxed{I_C = \beta I_B + I_{CEO}} $$

En muchas aplicaciones prácticas, especialmente cuando la corriente de base $I_B$ es lo suficientemente grande, la corriente de fuga $I_{CEO}$ es despreciable en comparación con el término $\beta I_B$. En estos casos, la ecuación de colector se simplifica a:

$$ I_C \approx \beta I_B $$

Es importante notar que, dado que $\alpha$ es un valor muy cercano a la unidad (típicamente entre 0.98 y 0.998), la relación $\beta = \frac{\alpha}{1 - \alpha}$ implica que $\beta$ será un valor grande (e.g., 50 a 500). Si $\alpha$ fuera exactamente 1, $\beta$ tendería a infinito, lo cual es una idealización. En las hojas de datos, la ganancia de corriente en DC se suele encontrar como $h_{FE}$ (que es $\beta$), mientras que la ganancia de corriente para pequeña señal se denota como $h_{fe}$.

---

## Características de Entrada en Emisor Común

Dado que la entrada en un transistor en configuración de Emisor Común (E-com) es la base, las **características de entrada** describen la relación entre la corriente de base ($I_B$) y el voltaje base-emisor ($V_{BE}$). Estas características producen una familia de curvas, similar a las de un diodo, ya que la unión Base-Emisor está polarizada en directa.

Un aspecto importante de estas curvas es la influencia del voltaje colector-emisor ($V_{CE}$). Se puede observar que, para un valor fijo de $V_{BE}$, la corriente de base ($I_B$) se **incrementa cuando $V_{CE}$ se reduce**.

Esto se debe al efecto Early (o modulación del ancho de base). Cuando se aplica un valor de $V_{CE}$ que produce un voltaje de polarización inverso alto en la unión Colector-Base, este voltaje incrementa la barrera de potencial y ensancha la región de deplexión, reduciendo el ancho efectivo de la base. Una base más estrecha disminuye las recombinaciones de portadores minoritarios en la base, lo que resulta en una **menor corriente de base ($I_B$)** para el mismo $V_{BE}$. Por el contrario, si $V_{CE}$ se reduce (disminuyendo la polarización inversa en C-B), el ancho efectivo de la base aumenta, incrementando las recombinaciones y, por ende, la corriente de base $I_B$ para un $V_{BE}$ constante.

<!-- TODO: Generar gráfica de I_B vs V_BE para distintos V_CE -->
<!-- ![Características de entrada en emisor común](../assets/bjt-emisor-comun-entrada.png) -->

---

## Características de Salida en Emisor Común

Las **características de salida** en la configuración de Emisor Común (E-com) describen la relación entre la corriente de colector ($I_C$) y el voltaje colector-emisor ($V_{CE}$). Estas curvas son fundamentales para entender el comportamiento del transistor como amplificador y como interruptor.

En la gráfica de características de salida, se representa una familia de curvas que muestran cómo varía $I_C$ en función de $V_{CE}$ para diferentes valores constantes de la corriente de entrada, que en esta configuración es la **corriente de base ($I_B$)**.

![Familia de Curvas de Salida — BJT NPN](../assets/bjt_familia_curvas_ic_vce.png)

> **Figura 1.** Familia de curvas de salida $I_C$ vs $V_{CE}$ para un transistor BJT NPN en configuración de Emisor Común, mostrando las regiones de operación.

A partir de esta familia de curvas, se pueden identificar las tres regiones de operación del transistor y extraer las siguientes conclusiones:

1.  **Región de Corte:**
    *   Corresponde a la curva donde $I_B = 0$ (o $I_B$ es muy pequeña, insuficiente para polarizar la unión B-E).
    *   En esta región, la corriente de colector $I_C$ es prácticamente cero (solo fluye la corriente de fuga $I_{CEO}$).
    *   El transistor se comporta como un **interruptor abierto**.

2.  **Región Activa:**
    *   Es la región de operación normal para la amplificación lineal.
    *   La unión Base-Emisor está polarizada en directa y la unión Colector-Base está polarizada en inversa.
    *   Para un valor fijo de $I_B$, la corriente de colector $I_C$ es casi constante e independiente de $V_{CE}$, y está relacionada con $I_B$ por la ganancia de corriente $\beta$:
        $$ \beta = \frac{I_C}{I_B} $$
        $$ I_C = \beta I_B $$
    *   Las curvas son casi horizontales, lo que indica una **alta impedancia de salida**.
    *   El ligero aumento de $I_C$ con $V_{CE}$ en esta región se debe al efecto Early (modulación del ancho de base), que reduce el ancho efectivo de la base y aumenta el gradiente de concentración de portadores.

3.  **Región de Saturación:**
    *   Ocurre cuando **ambas uniones** (Base-Emisor y Colector-Base) están **polarizadas en directa**.
    *   Esto sucede cuando $V_{CE}$ es muy bajo, típicamente $V_{CE} < V_{CE(sat)}$, donde $V_{CE(sat)}$ es el voltaje de saturación (aproximadamente $0.2\,\text{V}$ para transistores de silicio).
    *   En esta región, la corriente de colector $I_C$ ya no está controlada por $I_B$ de manera lineal, sino que está limitada por la resistencia externa del circuito de colector.
    *   El transistor se comporta como un **interruptor cerrado** con una pequeña caída de voltaje.

4.  **Región de Ruptura (Breakdown):**
    *   Si el voltaje $V_{CE}$ se incrementa más allá de un límite seguro, la corriente de colector ($I_C$) puede aumentar drásticamente, incluso si $I_B$ es cero (en la curva de corte).
    *   Este fenómeno se conoce como **ruptura colector-emisor con base abierta ($BV_{CEO}$)**. Cuando $V_{CE}$ sobrepasa este límite, la unión Colector-Base entra en ruptura por avalancha o Zener, y la corriente $I_C$ se incrementa rápidamente.
    *   Operar el transistor en esta región puede causar daños permanentes al dispositivo debido a la excesiva disipación de potencia.

---
