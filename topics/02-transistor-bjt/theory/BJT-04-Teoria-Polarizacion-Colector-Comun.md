<!--
::METADATA::
type: theory
topic_id: bjt-04
file_id: BJT-04-Teoria-Polarizacion-Colector-Comun
status: review
audience: both
last_updated: 2026-05-06
-->

> 🏠 **Navegación:** [← Módulo](../00-Index.md) | [📋 Índice Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

# 2.2.3 — Polarización en Colector Común

La configuración de **colector común** (C-com), también conocida como **seguidor de emisor**, se caracteriza porque el colector está conectado directamente (o a través de una fuente de alimentación de CD) a un potencial de referencia común.

En esta topología, la señal de entrada se aplica a la base y la señal de salida se toma desde el emisor.

![Configuracion colector comun](../assets/bjt-lcapy-colector-comun.png)

## 1. Características Principales

Esta configuración es única debido a sus propiedades de impedancia, lo que la hace ideal para el acoplamiento de etapas (buffer):

*   **Ganancia de Voltaje ($A_v$):** Es ligeramente menor a la unidad ($A_v \approx 1$). El voltaje de salida "sigue" al voltaje de entrada, de ahí su nombre.
*   **Ganancia de Corriente ($A_i$):** Es alta, aproximadamente igual a $\beta$.
*   **Impedancia de Entrada ($Z_{in}$):** Muy alta.
*   **Impedancia de Salida ($Z_{out}$):** Muy baja.

## 2. Análisis de Polarización DC

El análisis es similar al de emisor común con resistencia de emisor, con la diferencia de que $R_C = 0$ (o el colector va directo a $V_{CC}$).

### Malla de Entrada
$$ V_{CC} - I_B R_B - V_{BE} - I_E R_E = 0 $$
$$ I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E} $$

### Malla de Salida
$$ V_{CE} = V_{CC} - I_E R_E $$

---
## 3. Subtemas Pendientes de Desarrollo

- [ ] Análisis detallado de las características de entrada/salida.
- [ ] Modelado de impedancias para pequeña señal (Vínculo al Módulo 04).
- [ ] Ejemplos de aplicación como transformador de impedancia.

---
*Nota: Este subtema se encuentra en proceso de expansión técnica.*
