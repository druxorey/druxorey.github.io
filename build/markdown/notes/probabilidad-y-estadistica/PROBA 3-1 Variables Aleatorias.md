---
created: 2026-04-27 16:23
title: Variables Aleatorias
semester: 4
subject:
  - "[[PROBA 0-0 Nota Informativa|Probabilidad y Estadística]]"
unit: 3
status: done
---

<h1 id="main-title"  align="center"> Variables Aleatorias </h1>

> [!TLDR] SÍNTESIS 
> Una **variable aleatoria** es una función medible que transforma los resultados cualitativos de un experimento en **números reales**, permitiendo realizar análisis cuantitativos. Su comportamiento se caracteriza mediante la **Función de Densidad de Probabilidad**, que describe la distribución de frecuencias en recorridos **discretos** o **continuos**, y la **Función de Distribución Acumulada**, herramienta fundamental para evaluar probabilidades en intervalos.

En la observación de fenómenos sujetos al azar, los resultados de un experimento suelen expresarse mediante descripciones cualitativas (por ejemplo anotar si una moneda cae en «cara» o «sello»). Aunque la teoría de conjuntos permite agrupar estos desenlaces en subconjuntos y asignarles probabilidades individuales, el análisis cuantitativo exige sumar resultados, calcular promedios o integrar variaciones a lo largo del tiempo.

El problema principal es que las operaciones del álgebra no pueden ejecutarse sobre conceptos como «cara» o «defectuoso», sino exclusivamente sobre números reales. Por ello resulta indispensable construir un mecanismo formal que transforme cada resultado elemental del experimento en una magnitud numérica medible sobre $\mathbb{R}$ y clasifique el conjunto de valores resultantes.

# 1. Variable Aleatoria

Para trasladar ese universo cualitativo al terreno del análisis real, se establece una regla de asignación numérica sobre cada elemento de $\Omega$.

> [!QUOTE] **Definición Formal 1:** Variable Aleatoria y Recorrido ($\mathbb{R}_X$)
> 
> Sea $(\Omega, \mathcal{F}, \mathbb{P})$ un espacio de probabilidad. Una **variable aleatoria** (abreviada v.a.) es una función medible $X: \Omega \to \mathbb{R}$ que asigna a cada resultado elemental $\omega \in \Omega$ un único número real $X(\omega)$:
> $$\omega \mapsto X(\omega) \in \mathbb{R}$$
> 
> El conjunto imagen de esta aplicación constituye el **rango** o **recorrido** de la variable aleatoria, denotado por $\mathbb{R}_X$:
> $$\mathbb{R}_X = \{x \in \mathbb{R} \mid \exists \omega \in \Omega \text{ tal que } X(\omega) = x\} \subseteq \mathbb{R}$$

Por convención estándar, se utilizan letras mayúsculas ($X, Y, Z$) para designar a la variable aleatoria como función, mientras que se emplean letras minúsculas ($x, y, z$) para representar un valor numérico concreto que dicha variable puede adoptar tras realizar el experimento. Asimismo, la condición técnica de que $X$ sea «medible» garantiza que, para cualquier subconjunto numérico $B \subseteq \mathbb{R}_X$, el conjunto de resultados que producen dichos valores, $E = \{\omega \in \Omega \mid X(\omega) \in B\}$, sea un evento válido dentro de $\mathcal{F}$ con probabilidad bien definida $\mathbb{P}(B) = \mathbb{P}(E)$.

> [!EXAMPLE] **Ejemplo 1:** Variable Aleatoria en el Lanzamiento de Dos Monedas
> 
> Se lanzan dos monedas regulares al azar y se observa la cara superior de cada una. Defina formalmente el espacio muestral $\Omega$, construya la variable aleatoria $X =$ «cantidad de veces que sale cara», determine su recorrido $\mathbb{R}_X$ y calcule las probabilidades inducidas sobre cada valor del rango.

En este ejercicio partimos de un experimento aleatorio elemental cuyo espacio muestral está compuesto por secuencias simbólicas de caras y sellos. Lo que se busca es ilustrar cómo una variable aleatoria transforma esas etiquetas cualitativas en números reales manejables y traslada las probabilidades originales hacia el nuevo conjunto numérico $\mathbb{R}_X$.

1. Construimos el espacio muestral $\Omega$ listando los cuatro resultados elementales posibles al lanzar dos monedas (donde $C$ representa «cara» y $S$ representa «sello»), todos equiprobables con probabilidad $\frac{1}{4}$ por simetría física.

$$\Omega = \{SS, SC, CS, CC\}, \qquad \mathbb{P}(\omega) = \frac{1}{4} \quad \forall \omega \in \Omega$$

2. Evaluamos la función $X: \Omega \to \mathbb{R}$ sobre cada resultado elemental contando cuántas caras aparecen en la pareja observada, y reunimos las imágenes obtenidas para delimitar el recorrido $\mathbb{R}_X$.

$$X(SS) = 0, \quad X(SC) = 1, \quad X(CS) = 1, \quad X(CC) = 2 \implies \mathbb{R}_X = \{0, 1, 2\}$$

3. Calculamos la probabilidad de cada valor del recorrido sumando las probabilidades de los eventos equivalentes en $\Omega$ que son mapeados hacia dicho número real.

$$\mathbb{P}(X = 0) = \mathbb{P}(\{SS\}) = \frac{1}{4}$$
$$\mathbb{P}(X = 1) = \mathbb{P}(\{SC, CS\}) = \frac{2}{4} = \frac{1}{2}$$
$$ \qquad \mathbb{P}(X = 2) = \mathbb{P}(\{CC\}) = \frac{1}{4}$$

## 1.1. Variables Aleatorias Discretas

Una variable aleatoria $X$ es discreta cuando su recorrido $\mathbb{R}_X$ es un conjunto numerable, ya sea finito ($\mathbb{R}_X = \{x_1, x_2, \dots, x_n\}$) o infinito numerable ($\mathbb{R}_X = \{x_1, x_2, x_3, \dots\}$). Surgen habitualmente de procesos de conteo («cantidad de veces que ocurre un suceso»).

Cabe señalar que, aunque toda variable que toma exclusivamente valores enteros es discreta, no es obligatorio que sus valores sean enteros: si $\mathbb{R}_X = \{-1, 0, \sqrt{2}, e, \pi\}$, la variable sigue siendo discreta porque sus elementos pueden enumerarse uno a uno sin formar intervalos continuos.

> [!EXAMPLE] **Ejemplo 2:** Variable Discreta con Recorrido Infinito Numerable
> 
> Se lanza reiteradamente una moneda equilibrada hasta que aparezca «cara» ($C$) por primera vez. Sea $X =$ «cantidad total de lanzamientos realizados hasta obtener la primera cara». Describa el espacio muestral $\Omega$, identifique el recorrido $\mathbb{R}_X$ y deduzca la probabilidad $\mathbb{P}(X = n)$ para cualquier entero positivo $n$.

En este ejercicio el ensayo no se detiene hasta que ocurre un desenlace específico, lo que abre la posibilidad teórica de observar secuencias arbitrariamente largas de sellos iniciales. La finalidad de este ejercicio es demostrar que una variable aleatoria discreta puede poseer un recorrido infinito numerable y calcular la ley de probabilidad asociada a cada conteo entero mediante la [[PROBA 2-2 Probabilidad Condicional#2. Independencia Estadística|independencia estadística]] de los lanzamientos.

1. Formulamos el espacio muestral $\Omega$ como la colección infinita numerable de secuencias que acumulan $n - 1$ sellos consecutivos antes de finalizar con una cara, y aplicamos la función $X$ para obtener su recorrido.

$$\Omega = \{C, SC, SSC, SSSC, \dots\} \implies \mathbb{R}_X = \{1, 2, 3, 4, \dots\} = \mathbb{N}$$

2. Para un entero genérico $n \ge 1$, identificamos que el evento $\{X = n\}$ corresponde exclusivamente a la secuencia única de $n - 1$ sellos seguidos de una cara, y multiplicamos las probabilidades individuales de cada lanzamiento independiente ($\mathbb{P}(C) = \mathbb{P}(S) = \frac{1}{2}$).

$$\mathbb{P}(X = n) = \mathbb{P}(\underbrace{SS\cdots S}_{n - 1\text{ veces}}C) = \left(\frac{1}{2}\right)^{n - 1} \left(\frac{1}{2}\right) = \left(\frac{1}{2}\right)^n \quad \forall n \in \{1, 2, 3, \dots\}$$

## 1.2. Variables Aleatorias Continuas

Una variable aleatoria $X$ es continua cuando su recorrido $\mathbb{R}_X$ es un conjunto infinito no numerable, constituido por uno o varios intervalos dentro de la recta real $\mathbb{R}$ (acotados como $[a, b]$ o no acotados como $(0, \infty)$). Aparecen al modelar magnitudes físicas susceptibles de medición con precisión teórica arbitraria, tales como el tiempo, la temperatura, la masa, la longitud o el voltaje.

> [!EXAMPLE] **Ejemplo 3:** Variable Continua en el Tiempo de Espera del Transporte Público
> 
> En una parada de autobús urbano, las unidades pasan con una frecuencia regular de $20\text{ minutos}$, pero un pasajero llega sin conocer el horario exacto del recorrido. Se define la variable aleatoria $X =$ «tiempo de espera (en minutos) hasta que llega el próximo autobús». Formalice el espacio muestral $\Omega$, determine el recorrido $\mathbb{R}_X$ de la variable y calcule la probabilidad de que el pasajero espere entre $5$ y $12\text{ minutos}$ bajo condiciones de uniformidad temporal.

En este ejercicio analizamos una magnitud física continua como el tiempo de espera, donde entre dos instantes cualesquiera existen infinitos valores decimales posibles. Lo que se busca es mostrar cómo una variable aleatoria proyecta un fenómeno temporal sobre un intervalo continuo no numerable de la recta real, impidiendo enumerar los desenlaces uno por uno.

Asimismo, aprovechando que todos los instantes dentro del intervalo tienen la misma factibilidad de ocurrencia, se pide cuantificar la probabilidad de un subintervalo de espera sustituyendo el conteo discreto por la medición de longitudes mediante la [[PROBA 2-1 Espacios de Probabilidad y los Axiomas de Kolmogorov#3.3. Enfoque Geométrico (Medidas Continuas)|probabilidad geométrica]].

1. Delimitamos el espacio muestral $\Omega$ como todos los instantes de espera posibles dentro del ciclo de $20\text{ minutos}$ y aplicamos la función identidad $X(\omega) = \omega$ para establecer el recorrido continuo $\mathbb{R}_X$.

$$\Omega = [0, 20]\text{ min} \implies \mathbb{R}_X = [0, 20]$$

2. Definimos el evento de interés $E$ correspondiente a esperar entre $5$ y $12\text{ minutos}$ y calculamos la longitud unidimensional tanto del subintervalo favorable como del recorrido completo.

$$E = [5, 12]\text{ min} \implies \text{Longitud}(E) = 12 - 5 = 7\text{ min}, \qquad \text{Longitud}(\mathbb{R}_X) = 20 - 0 = 20\text{ min}$$

3. Aplicamos el enfoque de probabilidad geométrica dividiendo ambas longitudes para obtener la probabilidad exacta de que el tiempo de espera caiga en dicha franja.

$$\mathbb{P}(5 \le X \le 12) = \frac{\text{Longitud}(E)}{\text{Longitud}(\mathbb{R}_X)} = \frac{7}{20} = 0.35$$

# 2. Función de Densidad de Probabilidad

Delimitar el recorrido $\mathbb{R}_X$ permite conocer los valores numéricos que puede arrojar un experimento, pero resulta insuficiente para describir su comportamiento aleatorio. Dos variables distintas pueden compartir exactamente el mismo recorrido (por ejemplo, el conjunto $\{0, 1, 2\}$ o el intervalo $[0, 10]$) y aun así diferir radicalmente en la frecuencia con la que aparecen sus distintos resultados

Para caracterizar por completo la incertidumbre de $X$, es necesario establecer una regla matemática que indique cómo se reparte la unidad total de probabilidad ($\mathbb{P}(\Omega) = 1$) a lo largo de $\mathbb{R}_X$: esa función recibe el nombre de Función de Densidad de Probabilidad (FDP), y su formulación cambia según si los valores del recorrido están aislados o forman un continuo.

## 2.1. Densidad de Probabilidad de Variables Discretas

Cuando el recorrido $\mathbb{R}_X$ está compuesto por puntos aislados, cada valor individual $x_i$ puede concentrar una fracción positiva de la probabilidad total. Para formalizar esta asignación puntual se define la Función de Densidad de Probabilidad para variables discretas.

> [!QUOTE] **Definición Formal 2:** Función de Densidad de Probabilidad (Caso Discreto)
> 
> Sea $X$ una variable aleatoria discreta con recorrido $\mathbb{R}_X$. Su **Función de Densidad de Probabilidad Discreta**, denotada por $p_X: \mathbb{R} \to [0, 1]$, asigna a cada número real $x$ la probabilidad puntual de que la variable tome exactamente ese valor:
> $$p_X(x) = \mathbb{P}(X = x) = \mathbb{P}(\{\omega \in \Omega \mid X(\omega) = x\})$$
> 
> Para que $p_X(x)$ sea una FDP legítima, debe satisfacer obligatoriamente los axiomas de no negatividad y normalización:
> 
> 1. $\forall x \in \mathbb{R}: \quad 0 \le p_X(x) \le 1$ (con $p_X(x) = 0$ si $x \notin \mathbb{R}_X$).
> 2. $\displaystyle\sum_{x \in \mathbb{R}_X} p_X(x) = 1$.

La función de densidad de probabilidad discreta $p_X(x)$ actúa como una regla de consulta directa que asigna a cada número real $x$ su peso probabilístico exacto. Si el número $x$ pertenece al recorrido $\mathbb{R}_X$, la función devuelve directamente la probabilidad puntual de que la variable aleatoria tome ese valor específico; si $x$ queda fuera del recorrido, la función simplemente le asigna el valor $0$.

Las dos condiciones que acompañan a la definición formal garantizan que este reparto de probabilidades sea matemáticamente coherente: 

1) Impide asignar probabilidades negativas o superiores a la unidad a ningún punto aislado.
2) Exige que, al sumar las probabilidades de todos los puntos posibles del recorrido, se recupere exactamente la certeza total del experimento ($\mathbb{P}(\Omega) = 1$).

![[PROBA 3-1 Variables Aleatorias - Fdp de una Variable Aleatoria Discreta.webp]]

## 2.2. Densidad de Probabilidad de Variables Continuas

Si intentáramos aplicar el esquema discreto sobre un intervalo continuo como $[0, 2]$, chocaríamos con una imposibilidad aritmética: al existir infinitos números reales no numerables dentro del intervalo, asignar una probabilidad positiva a cada punto haría que la suma total diverja hacia infinito, violando $\mathbb{P}(\Omega) = 1$.

> [!QUOTE] **Definición Formal 3:** Función de Densidad de Probabilidad (PDF)
> Una variable aleatoria $X$ es **continua** si existe una función integrable $f_X: \mathbb{R} \to [0, \infty)$, denominada **Función de Densidad de Probabilidad Contínua**, tal que para cualesquiera números reales $a \le b$, la probabilidad de que $X$ caiga en el intervalo $[a, b]$ equivale al área bajo su curva:
> 
> $$\mathbb{P}(a \le X \le b) = \int_{a}^{b} f_X(x) \, dx$$
> 
> Una función $f_X(x)$ constituye una PDF válida si y solo si cumple dos condiciones fundamentales:
> 
> 1. **No negatividad:** $\forall x \in \mathbb{R}: \quad f_X(x) \ge 0$.
> 2. **Normalización de área unitaria:** $\displaystyle\int_{-\infty}^{+\infty} f_X(x) \, dx = 1$.

A diferencia del caso discreto, la función $f_X(x)$ no entrega directamente la probabilidad de obtener un valor aislado, sino una medida de intensidad o concentración relativa alrededor de cada punto $x$. Donde la curva de $f_X(x)$ alcanza mayor altura, los valores cercanos a esa zona tienen una concentración de probabilidad más alta; donde la curva desciende cerca del eje horizontal, la probabilidad se encuentra mucho más dispersa.

Para transformar esa densidad en una probabilidad real es indispensable evaluar un intervalo completo $[a, b]$ calculando el área geométrica encerrada entre la curva $f_X(x)$ y el eje horizontal a lo largo de ese tramo. Por esta razón, las dos propiedades fundamentales exigen que la gráfica nunca tome valores negativos (evitando áreas negativas sin sentido) y que el área total acumulada bajo toda la curva sobre la recta real sea exactamente igual a $1$.

![[PROBA 3-1 Variables Aleatorias - Fdp de una Variable Aleatoria Contínua.webp]]

De la definición se desprende que para cualquier número real aislado $x_0 \in \mathbb{R}$, la probabilidad de que la variable aleatoria tome exactamente ese valor puntual es estrictamente cero:

$$\mathbb{P}(X = x_0) = \mathbb{P}(x_0 \le X \le x_0) = \int_{x_0}^{x_0} f_X(x) \, dx = 0$$

Geométricamente, un punto aislado corresponde a un rectángulo vertical de base nula ($\Delta x = 0$), cuya área es cero sin importar cuál sea la altura $f_X(x_0)$. Este resultado conlleva dos consecuencias analíticas indispensables:

1. $f_X(x)$ no es una probabilidad, sino una tasa de densidad, esto pues dado que $f_X(x_0) \neq \mathbb{P}(X = x_0)$, la función de densidad no está acotada superiormente por $1$. Es perfectamente válido que $f_X(x) > 1$ en intervalos estrechos (por ejemplo, si $1\text{ kg}$ de masa se concentra uniformemente en una barra de $0.25\text{ m}$, su densidad lineal es $f_X(x) = 4 > 1$), siempre que la integral global sobre todo $\mathbb{R}$ siga siendo igual a $1$.

2. Improbable no equivale a imposible, lo que quiere decir que $\mathbb{P}(X = x_0) = 0$ significa que el suceso puntual es improbable (tiene medida geométrica nula), pero no imposible ($x_0$ sigue perteneciendo al recorrido $\mathbb{R}_X$). Si medimos la estatura exacta de una persona adulta en centímetros, obtener exactamente $172.0000\dots1\text{ cm}$ es un resultado lógicamente posible dentro del intervalo, pero al existir infinitos valores reales vecinos indiscernibles entre sí, su probabilidad puntual es nula.

> [!EXAMPLE] **Ejemplo 4:** Validación de Densidad y Cálculo de Área en Tiempo de Espera
> El tiempo $X$ (en minutos) que transcurre hasta que ocurre un evento aleatorio, como la llegada de un cliente a una taquilla bancaria, se modela mediante la siguiente función de densidad de probabilidad:
> $$f_X(x) = \begin{cases} 2e^{-2x} & \text{si } x \ge 0 \\ 0 & \text{si } x < 0 \end{cases}$$
> 
> 
> Verifique que $f_X(x)$ constituye una PDF válida y calcule la probabilidad de que el cliente llegue entre el minuto $1$ y el minuto $2$, así como la probabilidad de que tarde más de $2\text{ minutos}$.

En este ejercicio trabajamos con una variable aleatoria continua definida sobre el semieje real no negativo $\mathbb{R}_X = [0, \infty)$, donde la densidad de probabilidad decrece exponencialmente con el paso del tiempo (observándose que en $x = 0$ la densidad alcanza $f_X(0) = 2 > 1$). Lo que se busca es comprobar que la función satisface las condiciones de no negatividad e integral unitaria, y evaluar dos probabilidades de intervalo mediante integración definida sobre las regiones correspondientes.

1. Verificamos la no negatividad observando que $2e^{-2x} > 0$ para todo $x \ge 0$ y $0$ para $x < 0$, y evaluamos la integral impropia sobre todo el eje real para confirmar que el área total bajo la curva es igual a la unidad.

$$\int_{-\infty}^{+\infty} f_X(x) \, dx = \int_{0}^{+\infty} 2e^{-2x} \, dx = \lim_{b \to +\infty} \left[ -e^{-2x} \right]_{0}^{b} = \lim_{b \to +\infty} \left( -e^{-2b} + e^{0} \right) = 0 + 1 = 1$$

2. Calculamos la probabilidad de que la llegada ocurra en la franja temporal entre $x = 1$ y $x = 2$ integrando $f_X(x)$ sobre el intervalo $[1, 2]$.

$$\mathbb{P}(1 < X < 2) = \int_{1}^{2} 2e^{-2x} \, dx = \left[ -e^{-2x} \right]_{1}^{2} = -e^{-4} - (-e^{-2})$$
$$\mathbb{P}(1 < X < 2) = e^{-2} - e^{-4} \approx 0.1353 - 0.0183 = 0.1170$$

3. Determinamos la probabilidad de que el tiempo de espera supere los $2\text{ minutos}$ integrando la densidad desde $x = 2$ hasta $+\infty$.

$$\mathbb{P}(X > 2) = \int_{2}^{+\infty} 2e^{-2x} \, dx = \lim_{b \to +\infty} \left[ -e^{-2x} \right]_{2}^{b} = 0 - (-e^{-4}) = e^{-4} \approx 0.0183$$

# 3. Función de Distribución Acumulada (FDA)

Las funciones de densidad puntual ($p_X$ y $f_X$) describen cómo se distribuye la probabilidad de manera local en cada punto o vecindad del recorrido. Sin embargo, en el análisis probabilístico suele interesar evaluar el comportamiento global hasta un umbral máximo ($\mathbb{P}(X \le x)$), además de que existen variables aleatorias (como las de naturaleza mixta) que no admiten una descripción pura mediante masas puntuales ni mediante una función de densidad continua.

Para medir esta acumulación progresiva y contar con una herramienta matemática que exista siempre para cualquier variable aleatoria sin excepción, se define la Función de Distribución Acumulada (FDA).

## 3.1. Definición Universal y Morfología por Tipo de Soporte

> [!QUOTE] **Definición Formal 4:** Función de Distribución Acumulada
> 
> Sea $X$ una variable aleatoria cualquiera definida sobre un espacio de probabilidad $(\Omega, \mathcal{F}, \mathbb{P})$. Su Función de Distribución Acumulada, denotada por $F_X: \mathbb{R} \to [0, 1]$, asigna a cada número real $x$ la probabilidad de que la variable aleatoria tome un valor menor o igual a $x$:
> 
> $$F_X(x) = \mathbb{P}(X \le x) \quad \forall x \in \mathbb{R}$$
> 
> Su cálculo adopta dos formas según el soporte de $X$:
> 
> - **Caso Discreto:** Suma de todas las masas puntuales ubicadas a la izquierda o sobre el umbral $x$:
> 
> $$F_X(x) = \sum_{x_i \le x} p_X(x_i)$$
> 
> - **Caso Continuo:** Integral de la función de densidad desde $-\infty$ hasta el límite superior $x$:
> 
> $$F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt$$

La función de distribución acumulada $F_X(x)$ recorre la recta real desde el extremo izquierdo ($-\infty$) hasta un punto de corte $x$ y va sumando toda la probabilidad que encuentra en el camino, incluyendo la del propio punto $x$. Al evaluar $F_X(x)$, lo que se obtiene es la probabilidad total acumulada de que la variable aleatoria arroje un resultado menor o igual a ese umbral.

Debido a esta mecánica de barrido de izquierda a derecha, $F_X(x)$ comienza valiendo $0$ antes de alcanzar los primeros valores posibles de la variable y crece de forma progresiva hasta estabilizarse en $1$ una vez que rebasa todo su recorrido. En el caso discreto esa acumulación se calcula sumando los pesos puntuales ubicados hasta $x$, mientras que en el caso continuo se obtiene midiendo el área acumulada bajo la curva de densidad desde $-\infty$ hasta el corte en $x$.

Esta forma de acumulación resulta en una geometría característica en la gráfica de $F_X(x)$:

* **En variables discretas:** Como la probabilidad se concentra exclusivamente en puntos aislados $x_i \in \mathbb{R}_X$, la FDA permanece completamente plana (constante) en los tramos intermedios y experimenta saltos verticales abruptos únicamente al cruzar cada punto $x_i$, donde la altura exacta del escalón coincide con $p_X(x_i)$. Su gráfica tiene el aspecto de una escalera discontinua.

* **En variables continuas:** Al no existir concentraciones puntuales de masa ($\mathbb{P}(X = x_0) = 0$), el área acumulada crece de manera gradual sin saltos verticales, generando una curva continua y suave en todo $\mathbb{R}$.

![[PROBA 3-1 Variables Aleatorias - Comparación Entre la FDA Discreta y Contínua.webp]]

> [!EXAMPLE] **Ejemplo 5:** Deducción de la FDA en los Paradigmas Discreto y Continuo
> 
> Obtenga la expresión analítica completa por tramos de la Función de Distribución Acumulada $F_X(x)$ para las dos variables estudiadas previamente:
> 
> 1. La variable discreta $X =$ «cantidad de caras al lanzar dos monedas legales» ($p_X(0) = \frac{1}{4}$, $p_X(1) = \frac{1}{2}$, $p_X(2) = \frac{1}{4}$).
> 2. La variable continua $X =$ «tiempo de espera hasta la llegada de un cliente» ($f_X(x) = 2e^{-2x}$ para $x \ge 0$ y $0$ para $x < 0$).

Este ejercicio aplica la definición en ambos dominios para contrastar cómo la acumulación opera mediante sumas parciales escalonadas cuando el recorrido es finito y mediante integración indefinida suave cuando el recorrido es un intervalo continuo. Lo que se busca es construir ambas expresiones para todo $x \in \mathbb{R}$, asegurando que la FDA quede definida incluso fuera del soporte original de la variable.

1. Para la variable discreta de las dos monedas, evaluamos la suma acumulada $F_X(x) = \sum_{x_i \le x} p_X(x_i)$ en cada intervalo delimitado por los puntos del recorrido $\{0, 1, 2\}$, observando que el valor salta en cada entero incluido y permanece constante hasta justo antes del siguiente entero.

$$F_X(x) = \begin{cases} 0 & \text{si } x < 0 \\[4pt] \dfrac{1}{4} & \text{si } 0 \le x < 1 \\[6pt] \dfrac{1}{4} + \dfrac{1}{2} = \dfrac{3}{4} & \text{si } 1 \le x < 2 \\[6pt] \dfrac{3}{4} + \dfrac{1}{4} = 1 & \text{si } x \ge 2 \end{cases}$$

2. Para la variable continua del tiempo de espera, observamos que para $x < 0$ la densidad es idénticamente nula, por lo que $F_X(x) = 0$; mientras que para $x \ge 0$ integramos la densidad $f_X(t) = 2e^{-2t}$ desde $0$ hasta el umbral variable $x$.

$$F_X(x) = \int_{0}^{x} 2e^{-2t} \, dt = \left[ -e^{-2t} \right]_{0}^{x} = -e^{-2x} - (-e^{0}) = 1 - e^{-2x} \quad (\text{para } x \ge 0)$$

3. Consolidamos la expresión por tramos de la FDA continua sobre toda la recta real $\mathbb{R}$.

$$F_X(x) = \begin{cases} 0 & \text{si } x < 0 \\ 1 - e^{-2x} & \text{si } x \ge 0 \end{cases}$$

## 3.2. Propiedades Analíticas Fundamentales de la FDA

Toda función $F_X: \mathbb{R} \to [0, 1]$ que represente la Función de Distribución Acumulada de una variable aleatoria cumple necesariamente cuatro propiedades analíticas universales, independientemente de si la variable es discreta o continua.

> [!QUOTE] **Teorema 1:** Propiedades Universales de la Función de Distribución Acumulada
> 
> Sea $F_X(x) = \mathbb{P}(X \le x)$ la FDA de una variable aleatoria $X$. Entonces se satisfacen las siguientes propiedades:
> 
> 1. **Acotación en el intervalo unitario:** $\forall x \in \mathbb{R}: \quad 0 \le F_X(x) \le 1$.
> 2. **Límites asintóticos extremos:**
> 
> $$\lim_{x \to -\infty} F_X(x) = 0 \quad \land \quad \lim_{x \to +\infty} F_X(x) = 1$$
> 
> 1. **Monotonía no decreciente:** $\forall x_1, x_2 \in \mathbb{R}: \quad x_1 \le x_2 \implies F_X(x_1) \le F_X(x_2)$.
> 2. **Continuidad por la derecha:** $\forall a \in \mathbb{R}: \quad \lim_{x \to a^+} F_X(x) = F_X(a)$.

Cada una de estas cuatro propiedades posee una justificación directa tanto intuitiva como axiomática:

- **Acotación y límites asintóticos:** Como $F_X(x)$ es la probabilidad del evento $\{X \le x\}$, los [[PROBA 2-1 Espacios de Probabilidad y los Axiomas de Kolmogorov#2. La Función Probabilística|axiomas de Kolmogórov]] garantizan que su valor nunca puede ser negativo ni mayor que $1$. Cuando el umbral $x$ retrocede hacia $-\infty$, el evento $\{X \le x\}$ se contrae hacia el conjunto vacío $\emptyset$, anulando la probabilidad; cuando $x$ avanza hacia $+\infty$, $\{X \le x\}$ abarca todo el espacio muestral $\Omega$, alcanzando la certeza absoluta de $1$.

- **Monotonía no decreciente:** Si $x_1 \le x_2$, todo resultado que cumpla $X \le x_1$ cumple automáticamente $X \le x_2$, por lo que se tiene la inclusión de conjuntos $\{X \le x_1\} \subseteq \{X \le x_2\}$. Por la propiedad de monotonía de la probabilidad, necesariamente $F_X(x_1) \le F_X(x_2)$: una función acumulada jamás puede descender.

- **Continuidad por la derecha:** En un salto discreto ubicado en $x = a$, la definición $F_X(a) = \mathbb{P}(X \le a)$ incluye el punto $a$ mediante la desigualdad no estricta ($\le$). Si nos acercamos a $a$ desde valores mayores ($x \to a^+$), siempre estamos incluyendo el salto de $a$, por lo que el límite lateral derecho coincide con $F_X(a)$ (representado gráficamente por el círculo relleno al inicio de cada escalón). En cambio, al acercarnos por la izquierda ($x \to a^-$), el límite lateral izquierdo converge a $\mathbb{P}(X < a) = F_X(a^-)$, que difiere de $F_X(a)$ exactamente en la masa puntual $p_X(a) = F_X(a) - F_X(a^-)$.

# 4. Operatoria de Intervalos e Inversión Analítica

Conocer la Función de Distribución Acumulada $F_X(x)$ proporciona una ventaja operativa inmediata: evita tener que sumar decenas de términos o resolver nuevas integrales cada vez que se desea calcular la probabilidad de un intervalo, y además contiene toda la información necesaria para reconstruir la función puntual original.

## 4.1. Cálculo de Probabilidades en Intervalos y Fronteras

Para dos números reales cualesquiera $a < b$, el evento $\{X \le b\}$ puede descomponerse como la unión de dos eventos mutuamente excluyentes: $\{X \le a\}$ y $\{a < X \le b\}$. Aplicando la aditividad axiomática, se obtiene:

$$\mathbb{P}(X \le b) = \mathbb{P}(X \le a) + \mathbb{P}(a < X \le b) \implies \mathbb{P}(a < X \le b) = F_X(b) - F_X(a)$$

Esta relación fundamental semiabierta por la izquierda es universal, pero el efecto de cambiar los signos de desigualdad estricta ($<$) por desigualdades no estrictas ($\le$) diverge radicalmente entre variables continuas y discretas:

### 4.1.1. Indiferencia de extremos en variables continuas

Como cualquier punto aislado tiene probabilidad nula ($\mathbb{P}(X = a) = \mathbb{P}(X = b) = 0$), incluir o excluir los bordes de un intervalo no altera el área bajo la curva. Las cuatro variantes de intervalo producen exactamente el mismo valor:

$$\mathbb{P}(a \le X \le b) = \mathbb{P}(a < X \le b) = \mathbb{P}(a \le X < b) = \mathbb{P}(a < X < b) = F_X(b) - F_X(a)$$

### 4.1.2. Impacto estricto de fronteras en variables discretas

Cuando $X$ es discreta, los extremos $a$ y $b$ pueden concentrar masa puntual positiva ($p_X(a) > 0$, $p_X(b) > 0$). Restar $F_X(a)$ elimina toda la masa acumulada hasta $a$ *inclusive*; por lo tanto, si se desea incluir el extremo inferior $a$ o excluir el extremo superior $b$, es obligatorio realizar ajustes puntuales:

- **Intervalo semiabierto estándar $(a, b]$:** $\mathbb{P}(a < X \le b) = F_X(b) - F_X(a)$
- **Intervalo cerrado $[a, b]$:** $\mathbb{P}(a \le X \le b) = F_X(b) - F_X(a) + p_X(a)$
- **Intervalo abierto $(a, b)$:** $\mathbb{P}(a < X < b) = F_X(b) - F_X(a) - p_X(b)$
- **Intervalo semiabierto $[a, b)$:** $\mathbb{P}(a \le X < b) = F_X(b) - F_X(a) + p_X(a) - p_X(b)$

En particular, cuando el recorrido discreto está formado por números enteros ($a, b \in \mathbb{Z}$), el valor acumulado justo antes de $a$ es $F_X(a - 1)$, lo que simplifica las expresiones de intervalos cerrados y semiabiertos:

$$\mathbb{P}(a < X \le b) = F_X(b) - F_X(a), \qquad \mathbb{P}(a \le X \le b) = F_X(b) - F_X(a - 1) \quad (\text{para } a, b \in \mathbb{Z})$$

## 4.2. Recuperación de la Función Puntual desde la CDF

Dado que la CDF se construye acumulando la función puntual, aplicar el proceso matemático inverso permite recuperar la PMF o la PDF a partir de $F_X(x)$ sin ambigüedad:

### 4.2.1. Sustracción escalonada en variables discretas

La probabilidad puntual en un valor $x$ corresponde exactamente a la altura del salto vertical que experimenta la CDF en dicho punto, es decir, la diferencia entre el valor de la función en $x$ y su límite por la izquierda $F_X(x^-)$. Si el recorrido es entero ($x \in \mathbb{Z}$), el peldaño inmediatamente anterior se evalúa en $x - 1$:

$$p_X(x) = \mathbb{P}(X = x) = F_X(x) - F_X(x^-) = F_X(x) - F_X(x - 1) \quad (\text{para } x \in \mathbb{Z})$$

### 4.2.2. Diferenciación analítica en variables continuas

Por el Teorema Fundamental del Cálculo Integral, la operación inversa de la integral definida es la derivada respecto al límite superior de integración. En todo punto $x$ donde $F_X(x)$ sea derivable, la función de densidad se recupera diferenciando directamente la acumulada:

$$F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt \iff f_X(x) = \frac{dF_X(x)}{dx} = F_X'(x)$$

# 5. Ejercicios Prácticos Resueltos

## 5.1. Verificación, Acumulación y Cálculo de Intervalos en una Variable Continua

> [!EXAMPLE] **Ejemplo 6:** Verificación y Acumulación en Tiempo de Resolución de una Prueba
> 
> El tiempo $X$ (medido en horas) que tarda un estudiante en completar un examen escrito está modelado por la siguiente función de densidad de probabilidad:
> $$f_X(x) = \begin{cases} c\,x(2 - x) & \text{si } 0 \le x \le 2 \\ 0 & \text{en otro caso} \end{cases}$$
> 
> 1. Calcule analíticamente el valor de la constante de normalización $c$ para que $f_X(x)$ sea una PDF válida.
> 2. Deduzca la expresión analítica por tramos de la Función de Distribución Acumulada $F_X(x)$ para todo $x \in \mathbb{R}$.
> 3. Determine la probabilidad $\mathbb{P}(0.5 \le X \le 1.5)$ de que el estudiante termine el examen entre media hora y hora y media.

En este ejercicio analizamos una variable aleatoria continua acotada sobre el intervalo temporal $[0, 2]\text{ h}$, cuya curva de densidad adopta una forma parabólica invertida que se anula en los extremos y alcanza su máximo en el punto medio $x = 1$. Lo que se busca es garantizar primero que la función cumpla el axioma de área total unitaria determinando el factor de escala $c$.

A partir de la densidad normalizada, se pide construir la Función de Distribución Acumulada $F_X(x)$ mediante integración definida por tramos sobre toda la recta real, para finalmente utilizar dicha función acumulada en el cálculo directo de la probabilidad dentro de un subintervalo interior sin tener que repetir el proceso de integración.

![[PROBA 3-1 Variables Aleatorias - Comparación de Distribución Parabólica Contínua.webp]]

1. Aplicamos la condición de normalización $\int_{-\infty}^{+\infty} f_X(x)\,dx = 1$ sobre el soporte activo $[0, 2]$ y despejamos la constante $c$, verificando además que $c > 0$ garantiza $f_X(x) \ge 0$ en todo $[0, 2]$.

$$\int_{0}^{2} c\,x(2 - x) \, dx = c \int_{0}^{2} (2x - x^2) \, dx = c \left[ x^2 - \frac{x^3}{3} \right]_{0}^{2} = c \left( 4 - \frac{8}{3} \right) = \frac{4}{3}c = 1 \implies c = \frac{3}{4}$$

2. Para deducir la CDF $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$ en el tramo central $0 \le x \le 2$, integramos la densidad normalizada $f_X(t) = \frac{3}{4}(2t - t^2)$ desde el límite inferior del soporte $0$ hasta un umbral genérico $x$.

$$F_X(x) = \int_{0}^{x} \frac{3}{4}(2t - t^2) \, dt = \frac{3}{4} \left[ t^2 - \frac{t^3}{3} \right]_{0}^{x} = \frac{3}{4}x^2 - \frac{1}{4}x^3 = \frac{x^2(3 - x)}{4}$$

3. Consolidamos la expresión por tramos de $F_X(x)$ para todo $x \in \mathbb{R}$, asignando $0$ antes del inicio del soporte ($x < 0$) y $1$ una vez rebasado el límite superior ($x > 2$), comprobando su continuidad en $F_X(0) = 0$ y $F_X(2) = 1$.

$$F_X(x) = \begin{cases} 0 & \text{si } x < 0 \\[4pt] \dfrac{x^2(3 - x)}{4} & \text{si } 0 \le x \le 2 \\[6pt] 1 & \text{si } x > 2 \end{cases}$$

4. Evaluamos la probabilidad $\mathbb{P}(0.5 \le X \le 1.5)$ aplicando la propiedad de intervalos continuos $\mathbb{P}(a \le X \le b) = F_X(b) - F_X(a)$ mediante fracciones exactas.

$$F_X(1.5) = F_X\left(\frac{3}{2}\right) = \frac{\left(\frac{3}{2}\right)^2 \left(3 - \frac{3}{2}\right)}{4} = \frac{\frac{9}{4} \cdot \frac{3}{2}}{4} = \frac{27}{32}$$
$$F_X(0.5) = F_X\left(\frac{1}{2}\right) = \frac{\left(\frac{1}{2}\right)^2 \left(3 - \frac{1}{2}\right)}{4} = \frac{\frac{1}{4} \cdot \frac{5}{2}}{4} = \frac{5}{32}$$

$$\mathbb{P}(0.5 \le X \le 1.5) = F_X(1.5) - F_X(0.5) = \frac{27}{32} - \frac{5}{32} = \frac{22}{32} = \frac{11}{16} = 0.6875$$

## 5.2. Reconstrucción de la PMF y Contraste de Intervalos en una FDA Escalonada

> [!EXAMPLE] **Ejemplo 7:** Reconstrucción de Función de Masa y Cálculo de Intervalos Discretos
> 
> Sea $X$ una variable aleatoria discreta que representa el número de llamadas de emergencia recibidas en una estación de bomberos durante una guardia nocturna, cuya Función de Distribución Acumulada está definida por la siguiente función escalonada:
> 
> $$F_X(x) = \begin{cases} 0 & \text{si } x < 0 \\ 0.10 & \text{si } 0 \le x < 1 \\ 0.35 & \text{si } 1 \le x < 2 \\ 0.70 & \text{si } 2 \le x < 3 \\ 0.90 & \text{si } 3 \le x < 4 \\ 1.00 & \text{si } x \ge 4 \end{cases}$$
> 
> 1. Reconstruya la Función de Masa de Probabilidad (PMF) puntual $p_X(x)$ para todo $x \in \mathbb{R}$.
> 2. Calcule la probabilidad $\mathbb{P}(1 < X \le 3)$ y compárela con $\mathbb{P}(1 \le X \le 3)$, explicando la diferencia entre ambos resultados.

En este caso práctico disponemos únicamente de la función acumulada escalonada de una variable discreta con recorrido entero $\mathbb{R}_X = \{0, 1, 2, 3, 4\}$. La finalidad del ejercicio es aplicar el procedimiento de inversión discreta para extraer la masa de probabilidad concentrada en cada punto aislado a partir de la magnitud de los saltos verticales de $F_X(x)$.

Posteriormente, se busca demostrar por qué los signos de desigualdad estricta o no estricta alteran de manera significativa el resultado en variables discretas, contrastando la evaluación de un intervalo semiabierto frente a un intervalo cerrado sobre los mismos extremos enteros.

1. Aplicamos la sustracción escalonada $p_X(x) = F_X(x) - F_X(x - 1)$ en cada punto entero de discontinuidad $x \in \{0, 1, 2, 3, 4\}$ para aislar el tamaño de cada salto vertical, y verificamos que las masas obtenidas suman exactamente $1$.

$$p_X(0) = F_X(0) - F_X(-1) = 0.10 - 0 = 0.10$$
$$p_X(1) = F_X(1) - F_X(0) = 0.35 - 0.10 = 0.25$$
$$p_X(2) = F_X(2) - F_X(1) = 0.70 - 0.35 = 0.35$$
$$p_X(3) = F_X(3) - F_X(2) = 0.90 - 0.70 = 0.20$$
$$p_X(4) = F_X(4) - F_X(3) = 1.00 - 0.90 = 0.10$$

2. Escribimos la expresión formal por partes de la Función de Masa de Probabilidad $p_X(x)$ para todo $x \in \mathbb{R}$.

$$p_X(x) = \begin{cases} 0.10 & \text{si } x = 0 \\ 0.25 & \text{si } x = 1 \\ 0.35 & \text{si } x = 2 \\ 0.20 & \text{si } x = 3 \\ 0.10 & \text{si } x = 4 \\ 0 & \text{en otro caso} \end{cases}$$

3. Calculamos $\mathbb{P}(1 < X \le 3)$ aplicando directamente la diferencia $F_X(3) - F_X(1)$, dado que el signo estricto en $1 < X$ excluye la masa puntual de $X = 1$ (equivalente a sumar $p_X(2) + p_X(3)$).

$$\mathbb{P}(1 < X \le 3) = F_X(3) - F_X(1) = 0.90 - 0.35 = 0.55$$

4. Calculamos $\mathbb{P}(1 \le X \le 3)$ incorporando el extremo inferior $x = 1$ mediante la relación $F_X(3) - F_X(1 - 1) = F_X(3) - F_X(0) = F_X(3) - F_X(1) + p_X(1)$, comprobando que ambos resultados difieren exactamente en la masa puntual $p_X(1) = 0.25$.

$$\mathbb{P}(1 \le X \le 3) = F_X(3) - F_X(0) = 0.90 - 0.10 = 0.80$$

---

> [!RESOURCES] REFERENCIAS
> - **Meyer, Paul L.** *Probabilidad y Aplicaciones Estadísticas* (Edición revisada). Addison-Wesley Iberoamericana.
> 
> - **Feller, William.** *An Introduction to Probability Theory and Its Applications*, Vol. I (3.ª ed.). John Wiley & Sons, Inc., Nueva York, 1968. Capítulos 1, 2 y 3.
> 
> - **Riordan, John.** *An Introduction to Combinatorial Analysis*. Dover Publications, Mineola, Nueva York, 2002.
> 
> - **Parzen, Emanuel.** *Modern Probability Theory and Its Applications*. John Wiley & Sons, Inc., Nueva York, 1960.
> 
> - **Lipschutz, Seymour.** *Probabilidad*. McGraw-Hill, México, 1970.
> 
> - **Universidad Central de Venezuela (UCV), Facultad de Ciencias, Escuela de Computación.** *Probabilidad y Estadística*. Caracas, Venezuela, 2023.