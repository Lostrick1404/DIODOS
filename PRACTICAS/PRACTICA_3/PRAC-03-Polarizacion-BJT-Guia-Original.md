# INSTITUTO TECNOLÓGICO DE TOLUCA
## Ingeniería Electrónica
### Diodos y Transistores
#### Práctica-3

**Objetivo.-** El objetivo de la presente práctica es que el estudiante realice el diseño de polarización para localizar el punto de operación $Q$ del transistor en la región lineal con base al procedimiento de diseño visto en clase para la configuración de Emisor Común. Una vez terminado el diseño, simularlo mediante el software OrCAD PSpice y finalmente implementarlo en el laboratorio para comprobar de manera física las corrientes y voltajes calculados de manera teórica.

**Material**
1.- Transistor BC548-B
2.- Resistencias según diseño

**Equipo**
1.- Multímetro
2.- Fuente de alimentación de CD
3.- Software OrCAD PSpice

**PROCEDIMIENTO.**

1.- Diseñe el circuito de polarización de voltaje de CD para un transistor BC548-B configurado en Emisor Común, utilizando divisor de voltaje en la base, considerando la $\beta_{min}$ o el peor de los casos a partir de la hoja técnica del transistor. También se requiere que el transistor proporcione una corriente de operación de colector de $I_C = 50$ mA, el voltaje de alimentación $V_{CC}$ es de 15 V.
Utilizando la técnica de diseño para un divisor de voltaje encuentre los valores de: $I_B$, $\alpha_F$, $I_E$, $V_E$, $V_{CE}$, $R_{TH}$, $V_{TH}$ para encontrar las resistencias: $R_C$, $R_E$, $R_1$ y $R_2$ y las potencias respectivas en cada una de las resistencias.

> **[Diagrama de Circuito]:** Esquema de polarización por divisor de voltaje. El circuito consta de una fuente de alimentación $V_{CC}$ de 15 V de corriente directa, cuyo terminal negativo está conectado a tierra. Cuenta con un divisor de tensión formado por las resistencias $R_1$ y $R_2$, donde el nodo central se conecta a la base de un transistor bipolar NPN $Q_1$, identificado como BC548-B. El colector del transistor $Q_1$ está conectado a la línea de 15 V a través de la resistencia $R_C$. El emisor de $Q_1$ está conectado a tierra a través de la resistencia $R_E$.

2.- Con base a los cálculos y resultados del punto-1, establezca el punto de operación: $Q = (V_{CEQ}, I_{CQ})$.

3.- Construya la recta de carga de CD sobre la familia de curvas de salida: $V_{CE}$ e $I_C$, proporcionadas por el fabricante del transistor; una vez dibujada la recta de carga, localizar el punto de operación seleccionando la curva adecuada de $I_B$ y comparar el valor obtenido gráficamente con lo planteado en el punto-2.

4.- Realice la simulación utilizando el software PSpice, para lo cual el transistor se extrae de la librería "EBIPOLAR" y en Simulation Settings seleccionar como tipo de análisis "Bias Point" y en Options seleccionar "General Settings". Ejecute la simulación y compare con los resultados analíticos de corrientes y voltajes que circulan por el circuito.

5.- Finalmente implemente el circuito de manera física comprobando todas las corrientes y voltajes que circulan por el circuito de manera práctica mediante un voltímetro y un amperímetro, para finalmente comparar las mediciones reales con los valores analíticos.

6.- Realice sus conclusiones.

Elaboró: Ing. José Luis Avila Gómez