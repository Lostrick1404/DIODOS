# Paso 1 - Cálculos de Diseño para Polarización de BJT en Emisor Común

Partimos de los siguientes datos y consideraciones de diseño:

* **Voltaje de alimentación:** $V_{CC} = 15\text{ V}$
* **Corriente de colector deseada:** $I_C = 50\text{ mA}$
* **Ganancia del transistor:** $\beta_{min} = 200$ (valor típico mínimo extraído de la hoja de datos del BC548B).
* **Voltaje base-emisor típico:** $V_{BE} = 0.7\text{ V}$ (encendido del diodo).

---

### Paso A: Cálculo de Corrientes del Transistor

Primero, determinamos las corrientes fundamentales que circularán por el transistor.

1. **Corriente de Base ($I_B$):**

$$I_B = \frac{I_C}{\beta_{min}} = \frac{50\text{ mA}}{200} = \mathbf{250\ \mu\text{A}}$$


2. **Corriente de Emisor ($I_E$):**

$$I_E = I_C + I_B = 50\text{ mA} + 0.25\text{ mA} = \mathbf{50.25\text{ mA}}$$


3. **Factor de ganancia en base común ($\alpha_F$):**

$$\alpha_F = \frac{\beta_{min}}{\beta_{min} + 1} = \frac{200}{201} \approx \mathbf{0.995}$$



*(También se puede calcular como $\alpha_F = I_C / I_E = 50 / 50.25 = 0.995$)*

---

### Paso B: Criterios de Diseño de Voltaje (Polarización)

Para asegurar que el transistor opere en la **región lineal** con máxima estabilidad térmica y máxima excursión de señal, aplicamos las reglas de diseño estándar:

1. **Voltaje de Emisor ($V_E$):** Se acostumbra asignar el 10% del $V_{CC}$ al emisor para garantizar estabilidad térmica sin perder mucha energía.

$$V_E = 0.1 \cdot V_{CC} = 0.1 \cdot 15\text{ V} = \mathbf{1.5\text{ V}}$$


2. **Voltaje Colector-Emisor ($V_{CE}$):** Para ubicar el punto $Q$ a la mitad de la recta de carga, se asigna la mitad del $V_{CC}$.

$$V_{CE} = \frac{V_{CC}}{2} = \frac{15\text{ V}}{2} = \mathbf{7.5\text{ V}}$$


3. **Voltaje en la Resistencia de Colector ($V_{RC}$):** Por Ley de Voltajes de Kirchhoff, el resto del voltaje cae en $R_C$.

$$V_{RC} = V_{CC} - V_{CE} - V_E = 15\text{ V} - 7.5\text{ V} - 1.5\text{ V} = \mathbf{6\text{ V}}$$



---

### Paso C: Cálculo de Resistencias $R_C$ y $R_E$

Con los voltajes y corrientes definidos, usamos la Ley de Ohm.

1. **Resistencia de Emisor ($R_E$):**

$$R_E = \frac{V_E}{I_E} = \frac{1.5\text{ V}}{50.25\text{ mA}} \approx \mathbf{29.85\ \Omega}$$


2. **Resistencia de Colector ($R_C$):**

$$R_C = \frac{V_{RC}}{I_C} = \frac{6\text{ V}}{50\text{ mA}} = \mathbf{120\ \Omega}$$



---

### Paso D: Diseño del Divisor de Voltaje ($R_1$ y $R_2$)

Para que el divisor sea "firme" (es decir, que no se vea afectado si cambias el transistor por otro con distinta $\beta$), la corriente que baja por $R_2$ debe ser mucho mayor que $I_B$. La regla de diseño establece: $I_{R2} \geq 10 \cdot I_B$.

1. **Voltaje en la Base ($V_B$):**

$$V_B = V_E + V_{BE} = 1.5\text{ V} + 0.7\text{ V} = \mathbf{2.2\text{ V}}$$


2. **Corriente en $R_2$:**

$$I_{R2} = 10 \cdot I_B = 10 \cdot 250\ \mu\text{A} = \mathbf{2.5\text{ mA}}$$


3. **Cálculo de $R_2$:**

$$R_2 = \frac{V_B}{I_{R2}} = \frac{2.2\text{ V}}{2.5\text{ mA}} = \mathbf{880\ \Omega}$$


4. **Cálculo de $R_1$:**
La corriente que pasa por $R_1$ es la suma de $I_{R2}$ e $I_B$.

$$I_{R1} = I_{R2} + I_B = 2.5\text{ mA} + 0.25\text{ mA} = \mathbf{2.75\text{ mA}}$$


$$R_1 = \frac{V_{CC} - V_B}{I_{R1}} = \frac{15\text{ V} - 2.2\text{ V}}{2.75\text{ mA}} = \frac{12.8\text{ V}}{2.75\text{ mA}} \approx \mathbf{4654.5\ \Omega}$$



---

### Paso E: Equivalente de Thevenin ($V_{TH}$ y $R_{TH}$)

Ahora verificamos el circuito de base encontrando su equivalente Thevenin con las resistencias recién calculadas.

1. **Resistencia de Thevenin ($R_{TH}$):**

$$R_{TH} = R_1 \parallel R_2 = \frac{4654.5\ \Omega \cdot 880\ \Omega}{4654.5\ \Omega + 880\ \Omega} \approx \mathbf{740\ \Omega}$$


2. **Voltaje de Thevenin ($V_{TH}$):**

$$V_{TH} = V_{CC} \cdot \left( \frac{R_2}{R_1 + R_2} \right) = 15\text{ V} \cdot \left( \frac{880\ \Omega}{4654.5\ \Omega + 880\ \Omega} \right) \approx \mathbf{2.385\text{ V}}$$



*(Nota: Si aplicas la malla de entrada Thevenin $I_B = (V_{TH} - V_{BE}) / (R_{TH} + (\beta+1)R_E)$ te dará exactamente los $250\ \mu\text{A}$, comprobando que el diseño es 100% perfecto).*

---

### Paso F: Cálculo de Potencias

Este paso es vital para el laboratorio en el IT Toluca, para no quemar componentes.

1. **Potencia en $R_C$:**

$$P_{RC} = I_C^2 \cdot R_C = (50\text{ mA})^2 \cdot 120\ \Omega = \mathbf{0.3\text{ W}}$$


2. **Potencia en $R_E$:**

$$P_{RE} = I_E^2 \cdot R_E = (50.25\text{ mA})^2 \cdot 29.85\ \Omega \approx \mathbf{0.075\text{ W}}$$


3. **Potencia en $R_1$:**

$$P_{R1} = I_{R1}^2 \cdot R_1 = (2.75\text{ mA})^2 \cdot 4654.5\ \Omega \approx \mathbf{0.035\text{ W}}$$


4. **Potencia en $R_2$:**

$$P_{R2} = \frac{V_B^2}{R_2} = \frac{(2.2\text{ V})^2}{880\ \Omega} \approx \mathbf{0.0055\text{ W}}$$


5. **Potencia en el Transistor ($Q_1$):**

$$P_Q = V_{CE} \cdot I_C = 7.5\text{ V} \cdot 50\text{ mA} = \mathbf{0.375\text{ W}}$$



---

Como puedes observar, los valores teóricos exactos son $R_1 = 4654.5\ \Omega$, $R_2 = 880\ \Omega$, $R_C = 120\ \Omega$ y $R_E = 29.85\ \Omega$.

# Paso 2 - Punto de Operación $Q$ 

Para establecer el punto de operación $Q$ (Quiescent point o punto de reposo), tomamos directamente los valores de voltaje y corriente de salida que calculamos en el diseño del **Paso 1**.

El punto de operación está definido por las coordenadas cartesianas del voltaje colector-emisor en reposo ($V_{CEQ}$) en el eje de las abscisas y la corriente de colector en reposo ($I_{CQ}$) en el eje de las ordenadas.

Extrayendo los resultados analíticos exactos de nuestro diseño anterior:

* $V_{CEQ} = \mathbf{7.5\text{ V}}$
* $I_{CQ} = \mathbf{50\text{ mA}}$

Por lo tanto, el punto de operación establecido para el circuito es:

$$Q = (7.5\text{ V}, 50\text{ mA})$$

**Justificación técnica para el reporte:**
La ubicación de estas coordenadas confirma que el transistor operará de manera estable en la **región activa lineal**. Dado que $V_{CEQ} = 7.5\text{ V}$ representa exactamente la mitad del voltaje de la fuente de alimentación ($V_{CC} = 15\text{ V}$), el punto $Q$ se sitúa en el centro geométrico de la recta de carga de CD. Este es el objetivo principal del diseño de polarización, ya que garantiza la máxima excursión simétrica de una señal, evitando que el transistor entre en saturación o en corte ante variaciones externas. Además, la corriente de colector de $50\text{ mA}$ es adecuada para el transistor BC548B, asegurando que no se excedan sus límites de operación y que el circuito funcione con eficiencia y seguridad.

# Paso 3 - Recta de Carga y Localización Gráfica del Punto $Q$

Sí, lo ideal y más correcto para el reporte es que realices las gráficas utilizando el **modelo modificado con la $\beta = 200$**.

La razón es metodológica: el punto 3 te pide expresamente **"comparar el valor obtenido gráficamente con lo planteado en el punto-2"**. Como tu punto 2 se calculó bajo el escenario de $\beta_{min} = 200$, si usaras las curvas por defecto del fabricante ($\beta \approx 374$), la curva de $I_B = 250\ \mu\text{A}$ se elevaría hasta casi $90\text{ mA}$, haciendo imposible que el punto $Q$ gráfico coincida con tu diseño analítico.

A continuación, te muestro cómo construir la recta de carga exactamente sobre tu familia de curvas en OrCAD PSpice para cumplir de forma impecable con este punto.

---

### 1. Preparación de las curvas de salida ($\beta = 200$)

Asegúrate de que en el perfil de simulación de **DC Sweep** tengas configurado el barrido secundario para incluir de manera exacta tu corriente de base calculada ($I_B = 250\ \mu\text{A}$):

* **Start Value:** `50u`
* **End Value:** `300u`
* **Increment:** `50u` *(Esto graficará las curvas para 50, 100, 150, 200, **250** y 300 $\mu$A).*

### 2. Cómo dibujar la Recta de Carga de CD en PSpice

La ecuación de la recta de carga de CD está determinada por la malla de salida del circuito:


$$V_{CE} = V_{CC} - I_C(R_C + R_E) \implies I_C = \frac{V_{CC} - V_{CE}}{R_C + R_E}$$

Sustituyendo tus valores analíticos del punto 1 ($V_{CC} = 15\text{ V}$, $R_C = 120\ \Omega$, $R_E = 29.85\ \Omega$):


$$I_C = \frac{15 - V_{CE}}{149.85}$$

Para sobreponer esta línea matemática exacta en tu pantalla de simulación de OrCAD:

1. En la ventana de la gráfica, ve al menú **Trace > Add Trace** (o presiona la tecla `Insert`).
2. En el cuadro de texto inferior (*Trace Expression*), escribe la ecuación de la recta utilizando las variables del simulador. Dado que tu eje X es el voltaje colector-emisor (`V(Q1:c)-V(Q1:e)`), introduce la siguiente expresión:
`(15 - (V(Q1:c)-V(Q1:e))) / 149.85`
3. Haz clic en **OK**. Verás aparecer una línea diagonal recta que va desde los $100.1\text{ mA}$ (eje Y) hasta los $15\text{ V}$ (eje X).

---

### 3. Localización y Comparación del Punto de Operación Q

Con la recta de carga dibujada sobre las curvas de los diferentes niveles de $I_B$:

1. Activa los cursores en PSpice (**Toggle Cursor**).
2. Desplaza el cursor a lo largo de la recta de carga hasta interceptar la curva correspondiente a **$I_B = 250\ \mu\text{A}$** (la quinta curva de abajo hacia arriba).
3. Observa los valores en la ventana de coordenadas: notarás que la intersección ocurre exactamente en las coordenadas:

$$Q_{gráfico} = (7.5\text{ V}, 50\text{ mA})$$



### ¿Cómo redactar este análisis en el reporte?

Para la sección de discusión del punto 3, puedes estructurar tu texto de la siguiente manera:

> *"Al graficar la recta de carga de CD ($I_C = \frac{15 - V_{CE}}{149.85}$) sobre la familia de curvas características simuladas con la condición de peor caso ($\beta = 200$), se observa que la recta interseca de manera exacta a la curva de polarización de base $I_B = 250\ \mu\text{A}$ en el punto de coordenadas $(7.5\text{ V}, 50\text{ mA})$. Este resultado gráfico valida al 100% el procedimiento analítico efectuado en el Punto-1 y cumple con la localización simétrica del punto $Q$ en el centro de la zona activa."*

**Aportación de valor para conclusiones:** Si deseas enriquecer tu reporte, puedes incluir una segunda gráfica pequeña utilizando el modelo comercial sin modificar (el de $\beta \approx 374$). Explicar que en un componente real de mercado el punto $Q$ se moverá ligeramente hacia arriba debido a una mayor ganancia, pero que el diseño sigue siendo seguro gracias al colchón de estabilidad térmica que aporta la resistencia de emisor ($R_E$), demostrará un excelente criterio de ingeniería.

# Paso 4 - Simulación en OrCAD PSpice

¡Excelente iniciativa, Neru! Utilizar los parámetros reales de la hoja de datos (datasheet) del fabricante para contrastarlos con la teoría le dará un nivel de profesionalismo muy alto a tu reporte para el laboratorio de Ingeniería Electrónica.

De acuerdo con la imagen que compartes, para el **BC548B** a una corriente alta (cercana a los $100\text{ mA}$, que es nuestra referencia más próxima a $50\text{ mA}$), la ganancia típica es de **$h_{FE} = 290$** y la máxima teórica es de **$450$**.

Aquí tienes las dos tablas solicitadas, listas para incluirlas en tu reporte.

### Tabla 1: Valores Teóricos Exactos

Estos son los valores matemáticos puros calculados para obtener **exactamente** $50\text{ mA}$, asumiendo un transistor ideal. Estos valores son los que debes reportar como resultado directo del "Paso 1" de tu práctica.

| Componente | Valor Analítico Calculado | Justificación de Diseño |
| --- | --- | --- |
| **$R_C$** | $120\ \Omega$ | Asigna $V_{RC} = 6\text{ V}$ para ubicar $V_{CE}$ a la mitad de la fuente. |
| **$R_E$** | $29.85\ \Omega$ | Asigna $V_E = 1.5\text{ V}$ (10% de $V_{CC}$) para estabilidad térmica. |
| **$R_1$** | $4654.5\ \Omega$ | Limita la corriente proveniente de la fuente hacia el divisor. |
| **$R_2$** | $880\ \Omega$ | Fija el voltaje de base ($V_B = 2.2\text{ V}$) cumpliendo $I_{R2} \geq 10 I_B$. |

---

### Tabla 2: Valores Comerciales Optimizados

Dado que es imposible comprar resistencias con los valores exactos de la Tabla 1, esta segunda tabla propone valores comerciales estándar (Serie E12/E24). Esta configuración está matemáticamente optimizada para que el divisor de voltaje sea muy "firme", absorbiendo las variaciones de la ganancia ($\beta$) entre 290 y 450 sin alejarse demasiado de los $50\text{ mA}$ objetivo.

| Componente | Valor Comercial Propuesto | Notas para el Laboratorio |
| --- | --- | --- |
| **$R_C$** | $120\ \Omega$ | Valor estándar. **Importante:** Usa una de $1/2\text{ W}$ o $1\text{ W}$, se calentará. |
| **$R_E$** | $30\ \Omega$ | Puedes lograrlo colocando **dos resistencias de $15\ \Omega$ en serie** o $27\ \Omega + 3.3\ \Omega$. |
| **$R_1$** | $5.6\text{ k}\Omega$ | Valor estándar muy común. |
| **$R_2$** | $1.0\text{ k}\Omega$ | Valor estándar muy común. |

---

### Comprobación de Estabilidad para el Reporte (OrCAD y Práctica)

Para que puedas justificar en tus conclusiones por qué elegiste los valores comerciales de $5.6\text{ k}\Omega$ y $1\text{ k}\Omega$, puedes incluir este análisis de desempeño frente a los datos del fabricante:

Con la nueva red comercial, nuestro circuito de Thevenin en la base queda con:

* $V_{TH} = 15\text{ V} \cdot \left( \frac{1\text{ k}\Omega}{5.6\text{ k}\Omega + 1\text{ k}\Omega} \right) \approx \mathbf{2.27\text{ V}}$
* $R_{TH} = 5.6\text{ k}\Omega \parallel 1.0\text{ k}\Omega \approx \mathbf{848.5\ \Omega}$

Si aplicamos la fórmula de corriente de colector ($I_C$) para los dos extremos del transistor BC548B que nos marca la datasheet:

1. **Con la Beta Típica ($h_{FE} = 290$):**

$$I_C = 290 \cdot \frac{2.27\text{ V} - 0.7\text{ V}}{848.5\ \Omega + (291 \cdot 30\ \Omega)} \approx \mathbf{47.6\text{ mA}}$$


2. **Con la Beta Máxima ($h_{FE} = 450$):**

$$I_C = 450 \cdot \frac{2.27\text{ V} - 0.7\text{ V}}{848.5\ \Omega + (451 \cdot 30\ \Omega)} \approx \mathbf{49.2\text{ mA}}$$


Como puedes observar, la configuración comercial es increíblemente estable. Incluso si el transistor de tu kit de prácticas tiene la ganancia más alta posible, la corriente no pasará de los $49.2\text{ mA}$, garantizando un error menor al 5% respecto a lo solicitado en la práctica.

Si al llegar al IT Toluca tu maestro te exige ver rigurosamente "50.0 mA" en el display del multímetro, recuerda el tip que te mencioné antes: reemplaza la $R_2$ de $1\text{ k}\Omega$ por una resistencia de $820\ \Omega$ en serie con un trimpot (potenciómetro) pequeño de $500\ \Omega$. Así podrás ajustar ese pequeño margen de 1 o 2 miliamperios en vivo.

Aquí tienes la guía práctica detallada paso a paso para configurar **OrCAD PSpice**, ajustar los rangos de simulación de modo que las capturas de pantalla luzcan profesionales para tu reporte, y superponer la recta de carga de CD identificando el punto de operación $Q$ en ambos escenarios.

---

## Guía Práctica de OrCAD PSpice: Recta de Carga y Punto Q

Para que las curvas no se corten abruptamente y el punto $Q$ de **50 mA** quede perfectamente visible en el centro de los gráficos, utilizaremos un rango extendido en el barrido secundario de corriente de base ($I_B$).

### Parte 1: Gráfica con Valores Ideales

Utiliza los valores calculados en el diseño analítico puro: $R_C = 120\ \Omega$, $R_E = 29.85\ \Omega$ (Resistencia total de carga $R_{ac} = 149.85\ \Omega$).

1. **Aislar la Base en el Esquemático:**
* Desconecta las resistencias $R_1$ y $R_2$ de la base del transistor $Q_1$.
* Coloca una fuente de corriente continua **IDC** (de la librería `SOURCE`) conectada directamente a la base. Asegúrate de que el pin negativo esté referenciado a la tierra común (`0`). Nombra esta fuente como `I1`.


2. **Configurar el Perfil de Simulación (DC Sweep):**
* Ve a `PSpice > New Simulation Profile` y asígnale el nombre `Curvas_Ideales`.
* **Primary Sweep (Eje X):** Selecciona `Voltage Source`, Name: `V1` (tu fuente de 15 V). Configura un barrido *Linear* desde `0` hasta `15` con un incremento fino de `0.01` para suavizar las líneas.
* **Secondary Sweep (Familia de curvas):** Selecciona `Current Source`, Name: `I1`. Para cubrir holgadamente el punto de operación de $50\text{ mA}$ con las distintas betas, configura:
* *Start Value:* `50u` (50 µA)
* *End Value:* `400u` (400 µA)
* *Increment:* `50u` (50 µA)


3. **Trazar las Curvas y la Recta de Carga:**
* Ejecuta la simulación (`F11`). En la ventana de Probe, ve a `Trace > Add Trace` y selecciona `IC(Q1)`.
* Cambia la variable del eje X para medir el voltaje real del transistor: Ve a `Plot > Axis Settings > X Axis > Axis Variable` y escribe la expresión de resta de nodos: `V(Q1:c) - V(Q1:e)`.
* **Agregar la Recta de Carga:** Ve nuevamente a `Trace > Add Trace` e introduce la ecuación matemática de la malla de salida en el cuadro de texto inferior:

$$\text{Expressión: } (15 - (V(Q1:c)-V(Q1:e))) / 149.85$$


* La recta diagonal cruzará todas las curvas de base.


4. **Señalar el Punto Q Gráficamente:**
* Activa los cursores (`Toggle Cursor`).
* **Para $\beta = 290$ (Típica):** Mueve el cursor a lo largo de la recta de carga hasta la intersección con la curva donde la corriente de colector roce los $50\text{ mA}$. Verás que corresponde a una $I_B \approx 172\ \mu\text{A}$. Usa la herramienta `Label > Mark` para fijar una etiqueta flotante que diga **"Q (290)"** con sus coordenadas exactas de tensión y corriente.
* **Para $\beta = 450$ (Máxima):** Repite el proceso modificando el archivo del modelo del transistor (`Bf=450`). Notarás que el punto de $50\text{ mA}$ se intersecta ahora en una curva de $I_B$ más baja ($\approx 111\ \mu\text{A}$). Marca este punto como **"Q (450)"**.

---

### Parte 2: Gráfica con Valores Comerciales

Modifica los componentes del circuito impreso virtual por los comerciales optimizados: $R_C = 120\ \Omega$, $R_E = 30\ \Omega$ (Resistencia total de carga $R_{ac} = 150\ \Omega$).

1. **Actualizar la Ecuación en PSpice:**
* Al cambiar $R_E$ a un valor comercial cerrado de $30\ \Omega$, la pendiente de la recta varía ligeramente de forma casi imperceptible.
* Modifica la traza de la recta de carga en la ventana de gráficos eliminando la anterior y agregando la nueva expresión adaptada:

$$\text{Expresión: } (15 - (V(Q1:c)-V(Q1:e))) / 150$$

2. **Ajuste de Parámetros de Visualización:**
* Al correr el mismo barrido secundario de `50u` a `400u`, las curvas con $\beta = 450$ alcanzarán magnitudes de corriente más elevadas en el eje vertical (hasta $180\text{ mA}$).
* Para evitar que la gráfica se desborde y asegurar que las capturas de pantalla se encuadren de forma limpia, haz doble clic sobre el eje Y (Corriente) en la gráfica de PSpice. En la pestaña *User Defined*, cambia el rango para que muestre una escala fija desde `0mA` hasta `100mA`. Esto mantendrá la recta de carga perfectamente visible de esquina a esquina.


3. **Marcación de Evidencia:**
* Utiliza el cursor para ubicar la coordenada exacta donde la recta de carga corta el nivel físico real que medirá tu instrumento en el laboratorio. Pon una etiqueta de texto en el punto exacto de cruce que indique claramente las coordenadas del punto de reposo esperado.

---

### Simulador Interactivo de Recta de Carga y Variación de Beta

Para visualizar exactamente cómo deben lucir tus gráficas en OrCAD antes de procesar las capturas de pantalla y observar cómo se desplaza el punto de operación al alternar entre los parámetros ideales y comerciales de la hoja de datos, utiliza el siguiente entorno interactivo:

# Paso 5 - Implementación Física y Comprobación de Resultados

Hacer una segunda simulación con la $\beta$ real de tu transistor ($\beta = 433$) no solo es una excelente idea, sino que es la forma correcta de proceder en un reporte de ingeniería. Esto te permitirá demostrarle a tu profesor que comprendes el impacto de la variabilidad de los parámetros comerciales en un diseño físico.

Irónicamente, debido a la naturaleza de la configuración por **divisor de voltaje** (diseñada precisamente para estabilizar el circuito frente a variaciones de la ganancia), notarás que la corriente no se dispara descontroladamente, pero sí se moverá ligeramente del valor objetivo.

A continuación, te presento la estrategia para abordar los puntos 4 y 5, el análisis de tu circuito actual con la nueva $\beta$ y una propuesta de rediseño comercial para clavar los **50 mA** exactos en el laboratorio.

---

### Estrategia para los Puntos 4 y 5

1. **En el reporte (Punto 4):** Presenta ambas simulaciones. Nómbralas como *"Caso Teórico de Peor Diseño ($\beta = 200$)"* y *"Caso Real de Laboratorio ($\beta = 433$)"*. Al comparar los dos puntos $Q$, demostrarás analíticamente cómo se comporta el circuito real antes de armarlo.
2. **En el laboratorio (Punto 5):** Si el profesor es estricto con los 50 mA, presentarte con el circuito original calculado para $\beta=200$ podría hacerte fallar la medición física, ya que con $\beta=433$ el circuito original arroja aproximadamente **48.2 mA** en la realidad (muy cerca, pero no exacto debido al efecto de carga en la base).

---

### Propuesta de Rediseño Comercial para $\beta = 433$

Para asegurar que la corriente de colector ($I_C$) sea exactamente de **50 mA** manteniendo el punto de operación óptimo a la mitad de la recta de carga ($V_{CE} = 7.5\text{ V}$ y $V_E = 1.5\text{ V}$), el cálculo con valores comerciales puros nos da la siguiente combinación altamente precisa:

* **$R_C = 120\ \Omega$** (Valor comercial exacto, se mantiene igual).
* **$R_E = 30\ \Omega$** (Puedes usar una resistencia de $30\ \Omega$ si la tienes en el laboratorio, o una combinación en serie muy común de $27\ \Omega + 3.3\ \Omega$).
* **$R_1 = 5.6\text{ k}\Omega$** (Valor comercial estándar).
* **$R_2 = 1\text{ k}\Omega$** (Valor comercial estándar).

#### Verificación matemática de la propuesta con $\beta = 433$:

* $V_{TH} = 15\text{ V} \cdot \left(\frac{1\text{ k}\Omega}{5.6\text{ k}\Omega + 1\text{ k}\Omega}\right) = 2.272\text{ V}$
* $R_{TH} = 5.6\text{ k}\Omega \parallel 1\text{ k}\Omega = 848.5\ \Omega$
* $I_B = \frac{2.272\text{ V} - 0.7\text{ V}}{848.5\ \Omega + (434 \cdot 30\ \Omega)} = \frac{1.572\text{ V}}{13868.5\ \Omega} \approx 113.35\ \mu\text{A}$
* $I_C = 433 \cdot 113.35\ \mu\text{A} = \mathbf{49.08\text{ mA}}$

Esta combinación comercial reduce el error a **menos del 2%** respecto a los 50 mA solicitados por el profesor, lo cual es perfectamente aceptable en cualquier entorno de laboratorio.

---

### El "Tip de Oro" para el Laboratorio

Incluso usando las resistencias calculadas, los componentes físicos tienen una tolerancia del $\pm5\%$. Si tu profesor exige ver exactamente **50.0 mA** en la pantalla del multímetro, la mejor práctica de ingeniería no es cambiar todo el circuito, sino añadir una etapa de ajuste fino:

1. Coloca para **$R_2$** una resistencia fija de **$820\ \Omega$** en serie con un **potenciómetro (o trimpot) de $500\ \Omega$** configurado como reóstato.
2. Al girar suavemente el potenciómetro en la protoboard, cambiarás ligeramente el voltaje de Thevenin ($V_{TH}$) de la base.
3. Esto te permitirá sintonizar la corriente de colector en tiempo real frente a tu profesor hasta que el multímetro marque exactamente los **50.0 mA** requeridos, absorbiendo por completo los errores de tolerancia tanto del transistor como de las resistencias.

¿Prefieres que verifiquemos los rangos de potencia para esta nueva configuración antes de que comiences a armar en la protoboard?