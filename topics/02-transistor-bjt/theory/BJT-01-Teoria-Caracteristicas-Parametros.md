<!--
::METADATA::
type: theory
topic_id: bjt-01
file_id: BJT-01-Teoria-Caracteristicas-Parametros
status: review
audience: both
last_updated: 2026-05-06
-->

> 🏠 **Navegación:** [← Módulo](../00-Index.md) | [📋 Índice Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

# 2.1 — Características, Parámetros y Punto de Operación

El **transistor de unión bipolar** (BJT, por sus siglas en inglés *Bipolar Junction Transistor*) es un dispositivo de tres terminales fabricado con material semiconductor (silicio o germanio). A diferencia del diodo, que es un dispositivo de dos terminales que controla el flujo de corriente en una dirección, el BJT es un dispositivo de control que utiliza una pequeña corriente en una terminal para controlar una corriente mucho mayor entre las otras dos terminales.

## 1. Estructura y Simbología

El BJT consta de tres capas de material semiconductor dopado, formando dos uniones PN. Existen dos tipos básicos:

| Tipo | Capas | Símbolo | terminales |
|---|---|---|---|
| **NPN** | N-P-N | Flecha en el emisor apuntando hacia afuera | Colector (C), Base (B), Emisor (E) |
| **PNP** | P-N-P | Flecha en el emisor apuntando hacia adentro | Colector (C), Base (B), Emisor (E) |

*   **Emisor (E):** Fuertemente dopado. Su función es inyectar portadores de carga.
*   **Base (B):** Muy delgada y ligeramente dopada. Controla el flujo de portadores.
*   **Colector (C):** Moderadamente dopado. Recolecta los portadores provenientes del emisor.

## 2. Relaciones Fundamentales de Corriente

En cualquier configuración, se cumple la Ley de Kirchhoff de corrientes para el transistor como un todo:

$$ \boxed{I_E = I_C + I_B} $$

### Ganancia de Corriente en Base Común ($\alpha$)
Relaciona la corriente de colector con la de emisor. Indica qué fracción de los portadores del emisor logran llegar al colector.
$$ \alpha_{dc} = \frac{I_C}{I_E} \quad \implies \quad I_C = \alpha I_E $$
*(Rango típico: 0.95 a 0.998)*

### Ganancia de Corriente en Emisor Común ($\beta$)
También conocida como $h_{FE}$. Relaciona la corriente de colector con la corriente de control (base).
$$ \beta_{dc} = \frac{I_C}{I_B} \quad \implies \quad I_C = \beta I_B $$
*(Rango típico: 50 a 500)*

### Relación entre $\alpha$ y $\beta$
$$ \beta = \frac{\alpha}{1 - \alpha} \qquad \alpha = \frac{\beta}{\beta + 1} $$

## 3. Regiones de Operación

El comportamiento del BJT depende de la polarización de sus dos uniones: la unión Base-Emisor (JBE) y la unión Colector-Base (JCB).

| Región | JBE | JCB | Aplicación Principal |
|---|---|---|---|
| **Corte** | Inversa | Inversa | Interruptor abierto |
| **Activa** | Directa | Inversa | Amplificación Lineal |
| **Saturación** | Directa | Directa | Interruptor cerrado |
| **Activa Inversa** | Inversa | Directa | Poco común (baja ganancia) |

## 4. El Punto de Operación ($Q$)

El **Punto Q** (punto de reposo o *quiescent point*) es el conjunto de valores de corriente y voltaje ($I_C, V_{CE}$ o $I_C, V_{CB}$) que definen el estado del transistor cuando no hay señal de CA aplicada.

*   **Ubicación:** Se establece mediante el circuito de polarización DC.
*   **Importancia:** Determina el margen dinámico de la señal, la estabilidad térmica y la linealidad de la amplificación.

---
*Nota: Para profundizar en las curvas características de cada configuración, consulte los temas 2.2.1 (Emisor Común) y 2.2.2 (Base Común).*
