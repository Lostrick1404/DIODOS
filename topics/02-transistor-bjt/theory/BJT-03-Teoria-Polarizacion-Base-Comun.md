<!--
::METADATA::
type: theory
topic_id: bjt-03
file_id: BJT-03-Teoria-Polarizacion-Base-Comun
status: review
audience: both
last_updated: 2026-05-06
-->

> 🏠 **Navegación:** [← Módulo](../00-Index.md) | [📋 Índice Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

# 2.2.2 — Polarización en Base Común

La configuración de **base común** (B-com) se caracteriza porque la terminal de la base es el punto de referencia común tanto para el circuito de entrada (emisor) como para el de salida (colector). Típicamente, la base se conecta directamente a tierra o a un potencial de referencia fijo.

En esta topología, la señal de entrada se inyecta por el emisor y la señal de salida se extrae por el colector.

![Esquema de configuración en base común](../assets/bjt-base-comun-esquema.png)

## 1. Características de Entrada

Las **características de entrada** describen la relación entre la corriente de entrada ($I_E$) y el voltaje de entrada ($V_{BE}$). Dado que la unión base-emisor está polarizada en directa para la operación normal, esta curva se comporta de manera idéntica a la de un diodo de silicio.

$$ I_E = I_S \left( e^{\frac{V_{BE}}{n V_T}} - 1 \right) \approx I_S e^{\frac{V_{BE}}{n V_T}} $$

### Influencia del Voltaje de Salida ($V_{CB}$)
Al graficar $I_E$ vs $V_{BE}$ para distintos valores de $V_{CB}$, se observa que un incremento en el voltaje colector-base desplaza la curva ligeramente hacia la izquierda. Este fenómeno se debe al **efecto Early** (modulación del ancho de base):
1. Un mayor $V_{CB}$ (polarización inversa) ensancha la región de deplexión de la unión C-B.
2. Esto reduce el ancho efectivo de la base neutral.
3. El gradiente de concentración de portadores aumenta, lo que incrementa ligeramente $I_E$ para un mismo $V_{BE}$.

![Características de entrada en base común](../assets/bjt-base-comun-entrada.png)

## 2. Características de Salida

Las **características de salida** relacionan la corriente de colector ($I_C$) con el voltaje colector-base ($V_{CB}$) para distintos niveles de corriente de emisor ($I_E$).

![Características de salida en base común](../assets/bjt-base-comun-salida.png)

### Regiones de Operación

1.  **Región Activa:**
    *   **Condición:** Unión B-E en directa y unión C-B en inversa ($V_{CB} > 0$).
    *   **Comportamiento:** $I_C$ es prácticamente independiente de $V_{CB}$. Las curvas son casi horizontales, indicando una **impedancia de salida muy alta**.
    *   **Ganancia Alfa ($\alpha$):** Se define como la relación entre la corriente de colector y la de emisor:
        $$ \alpha_{dc} = \frac{I_C}{I_E} $$
        Típicamente $\alpha$ oscila entre 0.95 y 0.998. Nunca es mayor a 1.

2.  **Región de Saturación:**
    *   **Condición:** Ambas uniones polarizadas en directa ($V_{CB} < 0$).
    *   *Comportamiento:** La corriente de colector cae drásticamente. El transistor pierde su capacidad de control y se comporta como un interruptor cerrado.

3.  **Región de Corte:**
    *   **Condición:** $I_E = 0$.
    *   **Comportamiento:** Solo fluye una corriente de fuga extremadamente pequeña denominada $I_{CBO}$ (corriente de colector a base con el emisor abierto).

## 3. Parámetros Fundamentales

En esta configuración, el parámetro más importante es $\alpha$, que representa la eficiencia de transporte de portadores a través de la base.

*   $I_C = \alpha I_E + I_{CBO}$
*   Dado que $I_{CBO}$ es despreciable a temperatura ambiente: $I_C \approx \alpha I_E$.

---
*Nota: Para el análisis de polarización DC específico, consulte las técnicas de divisor de voltaje y realimentación adaptadas a esta configuración (Contenido en desarrollo).*
