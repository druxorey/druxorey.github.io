---
created: 2026-04-30T14:12:00
title: Medidas Descriptivas de Variables Aleatorias
semester: 4
subject:
  - "[[PROBA 0-0 Nota Informativa|Probabilidad y Estadística]]"
unit: 3
status: done
---

<h1 id="main-title"  align="center"> Medidas Descriptivas de Variables Aleatorias </h1>

> [!TLDR] SÍNTESIS 
> Las **medidas descriptivas de variables aleatorias** resumen el comportamiento probabilístico de un fenómeno mediante parámetros escalares clave. La **esperanza matemática** establece el centro de masa de la distribución, mientras que la **varianza** y la **desviación estándar** cuantifican la dispersión de los datos. Complementadas por la **mediana**, la **moda** y los **cuantiles**, estas métricas permiten evaluar la posición central y el grado de **asimetría** sin requerir análisis gráficos complejos.

Describir una variable aleatoria mediante toda su función de densidad o su función de distribución acumulada proporciona la información de cómo se reparte la incertidumbre a lo largo de su recorrido. Sin embargo, en la práctica cotidiana resulta poco manejable comparar dos fenómenos (como el tiempo de espera en dos taquillas de atención o la duración de dos lotes de bombillas) analizando curvas o tablas completas punto por punto: para tomar decisiones rápidas es necesario resumir todo ese comportamiento en unos pocos números representativos.

El problema surge al intentar condensar una función completa en escalares aislados sin perder información crítica. Un único valor promedio puede ocultar fluctuaciones extremas o verse arrastrado hacia un extremo por unos pocos resultados atípicos. Para identificar dónde se concentra una distribución, qué tan dispersos están sus valores y hacia qué lado se inclina su forma, resulta indispensable construir un sistema ordenado de métricas escalares partiendo del punto de equilibrio fundamental de la probabilidad.

# 1. Esperanza Matemática

El primer paso consiste en hallar un único número que represente el valor promedio teórico del experimento tras un número infinito de repeticiones. Dependiendo de si el recorrido $\mathbb{R}_X$ de una [[PROBA 3-1 Variables Aleatorias|variable aleatoria]] está formado por puntos aislados o por un intervalo continuo sobre la recta real, la ponderación de cada resultado por su peso probabilístico se formula mediante una sumatoria o una integral.

> [!QUOTE] **Definición Formal 1:** Esperanza Matemática ($\mathbb{E}[X]$)
> 
> Sea $X$ una variable aleatoria definida sobre un espacio de probabilidad. Su **esperanza matemática** (también llamada **valor esperado** o **media**), denotada por $\mathbb{E}[X]$ o $\mu$, se define como:
> 
> $$\mathbb{E}[X] = \begin{cases} \displaystyle \sum_{x \in \mathbb{R}_X} x \cdot p_X(x) & \text{si } X \text{ es discreta} \\ \displaystyle \int_{-\infty}^{+\infty} x \cdot f_X(x) \, dx & \text{si } X \text{ es continua} \end{cases}$$
> 
> siendo $p_X(x)$ y $f_X(x)$ las correspondientes funciones de densidad de probabilidad discreta y continua de $X$, siempre que la serie o la integral converjan de manera absoluta, es decir, que $\sum_{x \in \mathbb{R}_X} \vert{}x\vert{}\,p_X(x) < \infty$ o $\int_{-\infty}^{+\infty} \vert{}x\vert{}\,f_X(x)\,dx < \infty$.

La esperanza matemática funciona exactamente como el **centro de masa** (o centro de gravedad) de la distribución. Si se reparte una masa unitaria total ($1\text{ kg}$) a lo largo de una varilla rígida graduada (ya sea mediante masas puntuales $p_X(x)$ en posiciones discretas o mediante una lámina de densidad lineal $f_X(x)$), el valor $\mu = \mathbb{E}[X]$ señala la coordenada exacta donde debe situarse el punto de apoyo para que la varilla permanezca en equilibrio horizontal.

Es importante destacar que $\mathbb{E}[X]$ viene expresada exactamente en las mismas unidades físicas que la variable $X$, aunque no tiene por qué coincidir con un valor observable en un ensayo individual: al lanzar un dado legal, el valor esperado es $3.5$, un número que jamás aparece en ninguna cara pero que determina el promedio hacia el cual converge la media aritmética tras miles de lanzamientos.

> [!EXAMPLE] **Ejemplo 1:** Esperanza Matemática en un Dado Legal y en un Tiempo de Espera Continuo
> 
> Calcule el valor esperado $\mathbb{E}[X]$ para las siguientes dos variables aleatorias:
> 
> 1. La variable discreta $X =$ «resultado obtenido al lanzar un dado legal de seis caras», cuya [[PROBA 3-1 Variables Aleatorias#2.1. Densidad de Probabilidad de Variables Discretas|función de densidad de probabilidad discreta]] es $p_X(x) = \frac{1}{6}$ para $x \in \{1, 2, 3, 4, 5, 6\}$.
> 2. La variable continua $T =$ «tiempo en minutos que transcurre hasta la llegada de un cliente a una taquilla bancaria», modelada por la [[PROBA 3-1 Variables Aleatorias#2.2. Densidad de Probabilidad de Variables Continuas|función de densidad de probabilidad continua]] $f_T(t) = 2e^{-2t}$ para $t \ge 0$ (y $0$ para $t < 0$).

En este ejercicio calculamos el centro de masa en los dos dominios fundamentales de la teoría de probabilidad. Lo que se busca es aplicar la suma ponderada en el caso discreto y resolver una integral impropia mediante integración por partes en el caso continuo, interpretando el significado físico de cada resultado.

1. Para el lanzamiento del dado legal, multiplicamos cada elemento del recorrido $\mathbb{R}_X = \{1, 2, 3, 4, 5, 6\}$ por su probabilidad uniforme $\frac{1}{6}$ y sumamos los seis términos.

$$\mathbb{E}[X] = \sum_{x=1}^{6} x \cdot \frac{1}{6} = \frac{1 + 2 + 3 + 4 + 5 + 6}{6} = \frac{21}{6} = \frac{7}{2} = 3.5$$

2. Para el tiempo continuo de llegada del cliente, planteamos la integral impropia sobre el soporte activo $[0, \infty)$ e integramos por partes escogiendo $u = t$ ($du = dt$) y $dv = 2e^{-2t}\,dt$ ($v = -e^{-2t}$).

$$\mathbb{E}[T] = \int_{0}^{+\infty} t \cdot 2e^{-2t} \, dt = \lim_{b \to +\infty} \left( \left[ -t\,e^{-2t} \right]_{0}^{b} + \int_{0}^{b} e^{-2t} \, dt \right)$$

3. Evaluamos los límites aplicando la regla de L'Hôpital en el primer término ($\lim_{b \to +\infty} b\,e^{-2b} = 0$) y resolviendo la integral exponencial restante, obteniendo un tiempo promedio de espera de medio minuto ($30\text{ segundos}$).

$$\mathbb{E}[T] = \lim_{b \to +\infty} \left( -b\,e^{-2b} + 0 + \left[ -\frac{1}{2}e^{-2t} \right]_{0}^{b} \right) = 0 - \frac{1}{2}\left(0 - 1\right) = \frac{1}{2}\text{ min}$$

## 1.1. Esperanza de una Variable Transformada

A veces interesa calcular el valor esperado no de la variable original $X$, sino de una transformación funcional $Y = G(X)$, como el área de un cuadrado cuyo lado aleatorio es $X$ o una penalización proporcional a $X^2$. El enfoque directo consistiría en deducir primero la distribución de probabilidad completa de $Y$ y luego aplicar la definición. El Teorema del Estadístico Inconsciente permite prescindir de ese paso intermedio.

> [!QUOTE] **Teorema 1:** Esperanza Matemática de una Función $G(X)$
> 
> Sea $X$ una variable aleatoria y sea $G: \mathbb{R} \to \mathbb{R}$ una función real medible. La esperanza matemática de la variable transformada $G(X)$ se calcula directamente a partir de la función de densidad de probabilidad original de $X$:
> 
> $$\mathbb{E}[G(X)] = \begin{cases} \displaystyle \sum_{x \in \mathbb{R}_X} G(x) \cdot p_X(x) & \text{si } X \text{ es discreta} \\ \displaystyle \int_{-\infty}^{+\infty} G(x) \cdot f_X(x) \, dx & \text{si } X \text{ es continua} \end{cases}$$
> 
> siempre que la suma o la integral converjan de manera absoluta.

Este teorema establece que para hallar el promedio de cualquier función $G(X)$ basta con sustituir el factor lineal $x$ de la fórmula de la esperanza por la expresión transformada $G(x)$, ponderándola directamente con los mismos pesos $p_X(x)$ o $f_X(x)$ de la variable de partida. De este modo, no hace falta reconstruir el recorrido $\mathbb{R}_Y$ ni recalcular probabilidades inducidas cada vez que se aplica una transformación algebraica sobre $X$.

> [!EXAMPLE] **Ejemplo 2:** Cálculo del Valor Esperado de una Transformación Cuadrática
> 
> Al lanzar un dado legal de seis caras con resultado $X \in \{1, 2, 3, 4, 5, 6\}$, un juego de azar otorga un premio en monedas igual al cuadrado del número obtenido, es decir, $G(X) = X^2$. Calcule el premio promedio esperado $\mathbb{E}[X^2]$ utilizando el Teorema 1 y compárelo con $(\mathbb{E}[X])^2$.

En este ejercicio aplicamos el Teorema 1 sobre una variable aleatoria discreta uniforme para evaluar la esperanza de una transformación no lineal. La finalidad es calcular directamente $\mathbb{E}[X^2]$ ponderando cada cuadrado perfecto por $\frac{1}{6}$ y comprobar una desigualdad esencial del cálculo probabilístico: cuando $G$ no es una función lineal, en general $\mathbb{E}[G(X)] \neq G(\mathbb{E}[X])$.

1. Aplicamos la fórmula discreta del Teorema 1 sustituyendo $G(x) = x^2$ y ponderando cada valor por la probabilidad uniforme $p_X(x) = \frac{1}{6}$.

$$\mathbb{E}[X^2] = \sum_{x=1}^{6} x^2 \cdot p_X(x) = \frac{1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2}{6}$$

2. Desarrollamos la suma de los cuadrados de los seis primeros enteros positivos y simplificamos el cociente resultante.

$$\mathbb{E}[X^2] = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} \approx 15.17\text{ monedas}$$

3. Comparamos este resultado con el cuadrado de la media obtenida en el ejemplo previo ($\mathbb{E}[X] = \frac{7}{2}$), verificando que $\mathbb{E}[X^2] > (\mathbb{E}[X])^2$.

$$(\mathbb{E}[X])^2 = \left(\frac{7}{2}\right)^2 = \frac{49}{4} = 12.25 \neq \frac{91}{6}$$

## 1.2. Propiedades de la Esperanza Matemática

El operador esperanza $\mathbb{E}[\cdot]$ hereda directamente la estructura lineal de las sumatorias e integrales, lo que permite simplificar expresiones algebraicas sin volver a sumar o integrar desde cero:

1. **Linealidad estricta:** Para cualesquiera constantes reales $a, b \in \mathbb{R}$ y funciones $h_1(X), \dots, h_n(X)$ con esperanzas finitas, el operador distribuye sobre sumas y extrae constantes multiplicativas:

$$\mathbb{E}[aX + b] = a\mathbb{E}[X] + b, \qquad \mathbb{E}\left[\sum_{i=1}^{n} a_i h_i(X) + b\right] = \sum_{i=1}^{n} a_i \mathbb{E}[h_i(X)] + b$$

2. **Aditividad general:** Para cualesquiera dos variables aleatorias $X$ e $Y$ definidas sobre el mismo espacio de probabilidad, la esperanza de su suma es siempre igual a la suma de sus esperanzas individuales, sin importar si son dependientes o independientes:

$$\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$$

> [!DANGER]  La esperanza de un producto solo se factoriza como $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$ cuando existe [[PROBA 2-2 Probabilidad Condicional#2. Independencia Estadística|independencia estadística]] entre ambas variables.

3. **Positividad y nulidad:** Si una variable aleatoria toma exclusivamente valores no negativos ($X \ge 0$), su esperanza es necesariamente no negativa ($\mathbb{E}[X] \ge 0$). Más aún, para una variable no negativa, su esperanza se anula si y solo si toda la probabilidad se concentra en el cero con certeza total:

$$X \ge 0 \implies \mathbb{E}[X] \ge 0, \qquad \text{y además } \mathbb{E}[X] = 0 \iff \mathbb{P}(X = 0) = 1$$

4. **Monotonía y acotación modular:** Si $h(X) \le g(X)$ en todo el recorrido, sus esperanzas conservan la desigualdad ($\mathbb{E}[h(X)] \le \mathbb{E}[g(X)]$). Asimismo, por la desigualdad triangular de sumas e integrales, siempre se cumple $\vert{}\mathbb{E}[X]\vert{} \le \mathbb{E}[\vert{}X\vert{}]$.

### 1.3.1. Demostración de Linealidad Estricta

Para demostrar la identidad $\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$ en el dominio continuo (siendo el caso discreto completamente análogo al sustituir la integral por una sumatoria sobre $\mathbb{R}_X$), aplicamos el Teorema 1 con $G(x) = ax + b$:

$$\mathbb{E}[aX + b] = \int_{-\infty}^{+\infty} (ax + b)\,f_X(x) \, dx$$

Por la linealidad de la integral definida, separamos la integral de la suma y extraemos las constantes $a$ y $b$ fuera del integrando:

$$\mathbb{E}[aX + b] = a \int_{-\infty}^{+\infty} x\,f_X(x) \, dx + b \int_{-\infty}^{+\infty} f_X(x) \, dx$$

Reconocemos que la primera integral es por definición $\mathbb{E}[X]$ y que la segunda integral equivale a $1$ por el axioma de normalización de toda función de densidad de probabilidad continua:

$$\mathbb{E}[aX + b] = a\mathbb{E}[X] + b(1) = a\mathbb{E}[X] + b \quad \blacksquare$$

En la práctica, esta propiedad garantiza que cualquier cambio de escala o de origen (como convertir temperaturas de grados Celsius a Fahrenheit mediante $F = 1.8\,C + 32$) transforma el promedio exactamente con la misma relación lineal sin tener que deducir la nueva función de densidad.

# 2. Teoría General de Momentos

Así como en mecánica se calculan los momentos de una distribución de masa respecto a un punto de referencia para determinar su equilibrio y resistencia a la rotación, en probabilidad se evalúan las esperanzas de las potencias enteras de una variable aleatoria para caracterizar la geometría de su distribución.

## 2.1. Momentos Ordinarios y Momentos Centrados

Dependiendo de si las distancias se miden respecto al origen cero de la recta real o respecto al propio centro de masa $\mu$, surgen dos familias complementarias de momentos.

> [!QUOTE] **Definición Formal 2:** Momentos Ordinarios y Momentos Centrados de Orden $k$
> 
> Sea $X$ una variable aleatoria y sea $k \in \mathbb{N}$ un entero positivo ($k = 1, 2, 3, \dots$). Siempre que las esperanzas correspondientes existan de forma finita, se definen:
> 
> 1. **Momento ordinario (o respecto al origen) de orden $k$:**
> 
> $$\alpha_k = \mathbb{E}[X^k]$$
> 
> 1. **Momento centrado (o respecto a la media $\mu = \mathbb{E}[X]$) de orden $k$:**
> 
> $$\mu_k = \mathbb{E}\big[(X - \mu)^k\big]$$

Los momentos ordinarios $\alpha_k = \mathbb{E}[X^k]$ miden las potencias de la variable tomando como referencia fija el cero numérico, por lo que sus valores combinan tanto la ubicación global de la distribución en la recta real como su amplitud interna. En cambio, los momentos centrados $\mu_k = \mathbb{E}[(X - \mu)^k]$ restan previamente la media $\mu$ a cada observación, trasladando el origen de coordenadas al propio centro de gravedad de la variable para aislar su forma interna.

El primer momento ordinario coincide exactamente con la media ($\alpha_1 = \mathbb{E}[X] = \mu$), mientras que los momentos centrados de orden $k = 2, 3, 4$ miden respectivamente la dispersión (varianza), la asimetría y el apuntamiento (curtosis) de la distribución.

## 2.2. Demostración de Nulidad del Primer Momento Centrado

Al evaluar el momento centrado de primer orden ($k = 1$), se obtiene el valor esperado de las desviaciones simples $(X - \mu)$ alrededor de la media. Sin embargo, este parámetro carece de utilidad como medida de dispersión porque se anula idénticamente para cualquier variable aleatoria.

Para demostrarlo, partimos de la definición de $\mu_1$ y aplicamos la linealidad estricta de la esperanza matemática, recordando que $\mu = \mathbb{E}[X]$ es una constante real:

$$\mu_1 = \mathbb{E}\big[(X - \mu)^1\big] = \mathbb{E}[X - \mu]$$

Distribuimos el operador esperanza sobre la resta y extraemos la constante $\mu$:

$$\mu_1 = \mathbb{E}[X] - \mathbb{E}[\mu] = \mathbb{E}[X] - \mu$$

Sustituimos $\mathbb{E}[X] = \mu$ y simplificamos:

$$\mu_1 = \mu - \mu = 0 \quad \blacksquare$$

Geométricamente, que $\mu_1 = 0$ confirma que $\mu$ es el verdadero punto de equilibrio de la distribución: las desviaciones positivas de los valores mayores que la media ($X > \mu$) compensan exactamente en peso probabilístico a las desviaciones negativas de los valores menores que la media ($X < \mu$). Como los signos opuestos se cancelan entre sí, para cuantificar qué tan alejados se encuentran los valores respecto al centro es necesario elevar las desviaciones al cuadrado, pasando al segundo momento centrado.

# 3. Medidas de Dispersión y Escalamiento

Conocer únicamente el centro de masa $\mu$ resulta insuficiente para caracterizar un fenómeno aleatorio. Dos regiones distintas pueden registrar exactamente la misma temperatura media anual de $20\,^\circ\text{C}$: en una la temperatura oscila suavemente entre $18\,^\circ\text{C}$ y $22\,^\circ\text{C}$, mientras que en otra alterna entre inviernos de $-5\,^\circ\text{C}$ y veranos de $45\,^\circ\text{C}$. Cuantificar esa amplitud de fluctuación exige definir medidas de dispersión.

## 3.1. Varianza y Desviación Estándar

Al elevar al cuadrado la distancia $(X - \mu)$ antes de calcular su esperanza, se eliminan los signos negativos sin introducir puntos no derivables (como ocurriría con el valor absoluto $|X - \mu|$) y se ponderan con mayor peso las desviaciones grandes respecto a la media.

> [!QUOTE] **Definición Formal 3:** Varianza ($\sigma^2$) y Desviación Estándar ($\sigma$)
> 
> Sea $X$ una variable aleatoria con media finita $\mu = \mathbb{E}[X]$. Se define la **varianza** de $X$, denotada por $\mathrm{Var}(X)$ o $\sigma^2$, como su segundo momento centrado:
> 
> $$\mathrm{Var}(X) = \sigma^2 = \mu_2 = \mathbb{E}\big[(X - \mu)^2\big] = \begin{cases} \displaystyle \sum_{x \in \mathbb{R}_X} (x - \mu)^2 \cdot p_X(x) & \text{si } X \text{ es discreta} \\[12pt] \displaystyle \int_{-\infty}^{+\infty} (x - \mu)^2 \cdot f_X(x) \, dx & \text{si } X \text{ es continua} \end{cases}$$
> 
> La **desviación estándar** (o desviación típica), denotada por $\sigma$, se define como la raíz cuadrada no negativa de la varianza:
> 
> $$\sigma = \sqrt{\mathrm{Var}(X)} = \sqrt{\mathbb{E}\big[(X - \mu)^2\big]}$$

Por la propiedad de positividad de la esperanza sobre la variable no negativa $(X - \mu)^2 \ge 0$, la varianza satisface siempre $\mathrm{Var}(X) \ge 0$, y se anula ($\sigma^2 = 0$) únicamente en el caso degenerado en que toda la probabilidad se concentra en un único punto constante ($\mathbb{P}(X = \mu) = 1$).

La razón por la que se introduce la desviación estándar $\sigma$ junto a la varianza $\sigma^2$ es estrictamente dimensional. Si la variable $X$ mide el tiempo de duración de una bombilla en $\text{horas}$, entonces $(X - \mu)^2$ y la varianza $\sigma^2$ quedan expresadas en $\text{horas}^2$, una unidad cuadrática sin interpretación física directa. Al extraer la raíz cuadrada, la desviación estándar $\sigma$ devuelve la medida de dispersión a $\text{horas}$ lineales, permitiendo compararla directamente con la media $\mu$.

## 3.2. Teorema de König

Calcular la varianza mediante su definición integral o sumatoria exige restar $\mu$ a cada valor $x$ y elevar ese binomio al cuadrado antes de operar, lo cual resulta algebraicamente laborioso cuando $\mu$ es una fracción o un número irracional. El **teorema de König** (o fórmula abreviada de la varianza) evita ese desarrollo relacionando $\sigma^2$ directamente con los dos primeros momentos ordinarios.

> [!QUOTE] **Teorema 2:** Teorema de König para la Varianza
> 
> Para toda variable aleatoria $X$ con segundo momento ordinario finito ($\mathbb{E}[X^2] < \infty$), la varianza equivale a la diferencia entre el segundo momento ordinario y el cuadrado de la esperanza matemática:
> 
> $$\mathrm{Var}(X) = \sigma^2 = \mathbb{E}[X^2] - \big(\mathbb{E}[X]\big)^2 = \mathbb{E}[X^2] - \mu^2 = \alpha_2 - \alpha_1^2$$

Partimos de la definición formal de varianza y desarrollamos el cuadrado del binomio dentro del operador esperanza:

$$\mathrm{Var}(X) = \mathbb{E}\big[(X - \mu)^2\big] = \mathbb{E}\big[X^2 - 2\mu X + \mu^2\big]$$

Aplicamos la propiedad de linealidad estricta de la esperanza para separar los tres sumandos y extraer los factores constantes $-2\mu$ y $\mu^2$:

$$\mathrm{Var}(X) = \mathbb{E}[X^2] - 2\mu\mathbb{E}[X] + \mu^2$$

Sustituimos $\mathbb{E}[X] = \mu$ y reducimos los términos semejantes en $\mu^2$:

$$\mathrm{Var}(X) = \mathbb{E}[X^2] - 2\mu(\mu) + \mu^2 = \mathbb{E}[X^2] - 2\mu^2 + \mu^2 = \mathbb{E}[X^2] - \mu^2 \quad \blacksquare$$

Además de simplificar los cálculos manuales, esta identidad demuestra de inmediato que $\mathbb{E}[X^2] \ge (\mathbb{E}[X])^2$ para cualquier variable aleatoria, dado que $\mathrm{Var}(X) \ge 0$.

## 3.3. Impacto de Transformaciones Lineales en la Varianza

Cuando una variable aleatoria $X$ se somete a un cambio de escala y desplazamiento $Y = aX + b$, su dispersión responde de manera distinta a su esperanza matemática.

> [!QUOTE] **Teorema 3:** Varianza de una Transformación Lineal
> 
> Sean $a, b \in \mathbb{R}$ constantes reales y $X$ una variable aleatoria con varianza finita. Entonces:
> 
> $$\mathrm{Var}(aX + b) = a^2 \mathrm{Var}(X)$$
> 
> y, en consecuencia, la desviación estándar escalada satisface $\sigma_{aX + b} = |a|\,\sigma_X$.

Aplicamos la definición formal de varianza sobre la variable transformada $Y = aX + b$ y sustituimos $\mathbb{E}[aX + b] = a\mu + b$ por linealidad de la esperanza:

$$\mathrm{Var}(aX + b) = \mathbb{E}\Big[\big((aX + b) - \mathbb{E}[aX + b]\big)^2\Big] = \mathbb{E}\Big[\big((aX + b) - (a\mu + b)\big)^2\Big]$$

Cancelamos las constantes de traslación $+b$ y $-b$, factorizamos $a$ dentro del cuadrado y extraemos la constante $a^2$ fuera del operador esperanza:

$$\mathrm{Var}(aX + b) = \mathbb{E}\Big[\big(a(X - \mu)\big)^2\Big] = \mathbb{E}\Big[a^2(X - \mu)^2\Big] = a^2 \mathbb{E}\big[(X - \mu)^2\big] = a^2 \mathrm{Var}(X) \quad \blacksquare$$

Este teorema manifiesta dos propiedades geométricas fundamentales:

- **Invarianza ante traslaciones ($b$):** Sumar o restar una constante $b$ desplaza toda la distribución hacia la derecha o hacia la izquierda sobre la recta real, pero no modifica la separación relativa entre sus valores; por ello $b$ desaparece por completo de la varianza.

- **Escalamiento cuadrático ($a^2$):** Multiplicar la variable por $a$ estira o contrae las distancias por un factor $\vert{}a\vert{}$; al estar la varianza definida en unidades cuadráticas, el factor sale elevado a $a^2$ (y si $a = -1$, reflejar la distribución conserva intacta su dispersión: $\mathrm{Var}(-X) = \mathrm{Var}(X)$).

> [!EXAMPLE] **Ejemplo 3:** Varianza mediante König y Cambio de Escala en un Dado Legal
> 
> Sea $X$ el resultado obtenido al lanzar un dado legal de seis caras ($\mathbb{E}[X] = \frac{7}{2}$ y $\mathbb{E}[X^2] = \frac{91}{6}$). Calcule su varianza $\mathrm{Var}(X)$ y su desviación estándar $\sigma_X$ mediante el teorema de König. Posteriormente, si un juego asigna una puntuación lineal $Y = 10X - 15$, determine $\mathbb{E}[Y]$, $\mathrm{Var}(Y)$ y $\sigma_Y$ sin reconstruir la distribución de $Y$.

En este ejercicio aplicamos el teorema de König junto con las leyes de transformación lineal de esperanza y varianza. Lo que se busca es comprobar cómo el teorema de König evita calcular seis diferencias fraccionarias al cuadrado, y cómo el desplazamiento ($-15$) modifica el promedio pero deja inalterada la dispersión escalada únicamente por el factor $10$.

1. Calculamos la varianza de $X$ sustituyendo los momentos ordinarios $\mathbb{E}[X^2] = \frac{91}{6}$ y $\mathbb{E}[X] = \frac{7}{2}$ en la fórmula del teorema de König.

$$\mathrm{Var}(X) = \mathbb{E}[X^2] - \big(\mathbb{E}[X]\big)^2 = \frac{91}{6} - \left(\frac{7}{2}\right)^2 = \frac{91}{6} - \frac{49}{4} = \frac{182 - 147}{12} = \frac{35}{12} \approx 2.9167$$

2. Extraemos la raíz cuadrada no negativa para obtener la desviación estándar $\sigma_X$ en las mismas unidades del dado.

$$\sigma_X = \sqrt{\frac{35}{12}} \approx 1.7078$$

3. Calculamos la esperanza de la puntuación transformada $Y = 10X - 15$ aplicando la propiedad de linealidad estricta $\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$.

$$\mathbb{E}[Y] = \mathbb{E}[10X - 15] = 10\,\mathbb{E}[X] - 15 = 10\left(\frac{7}{2}\right) - 15 = 35 - 15 = 20\text{ puntos}$$

4. Evaluamos la varianza y la desviación estándar de $Y$ aplicando $\mathrm{Var}(aX + b) = a^2\mathrm{Var}(X)$, observando que el término constante $-15$ no altera la dispersión.

$$\mathrm{Var}(Y) = 10^2 \cdot \mathrm{Var}(X) = 100 \cdot \frac{35}{12} = \frac{875}{3} \approx 291.67\text{ puntos}^2$$
$$\sigma_Y = |10|\,\sigma_X = 10\sqrt{\frac{35}{12}} \approx 17.078\text{ puntos}$$

# 4. Medidas de Tendencia Central y Asimetría

La media $\mu = \mathbb{E}[X]$  puede resultar engañosa cuando la distribución tiene colas alargadas o valores extremos aislados. Para obtener una visión más completa del comportamiento central de un fenómeno, la estadística complementa la media con la moda y la mediana.

## 4.1. Moda

Mientras que la media pondera todos los valores del recorrido según su magnitud, la moda identifica exclusivamente dónde se encuentra la mayor concentración local de probabilidad.

> [!QUOTE] **Definición Formal 4:** Moda ($x_m$)
> 
> La **moda** de una variable aleatoria $X$, denotada por $x_m$, es aquel valor del recorrido $\mathbb{R}_X$ donde la función de densidad de probabilidad alcanza su máximo global:
> 
> $$x_m = \arg\max_{x \in \mathbb{R}_X} p_X(x) \quad (\text{caso discreto}) \qquad \text{o bien} \qquad x_m = \arg\max_{x \in \mathbb{R}_X} f_X(x) \quad (\text{caso continuo})$$
> 
> Es decir, $p_X(x) \le p_X(x_m)$ para todo $x \in \mathbb{R}_X$ en el caso discreto, o $f_X(x) \le f_X(x_m)$ para todo $x \in \mathbb{R}_X$ en el caso continuo.

Según la cantidad de máximos globales que presente la distribución, se distinguen tres casos:

- **Distribución unimodal:** Posee un único valor modal bien definido (por ejemplo, al lanzar dos monedas equilibradas, la cantidad de caras $X \in \{0, 1, 2\}$ tiene una única moda en $x_m = 1$ con probabilidad $0.50$).

- **Distribución multimodal:** Presenta dos o más picos aislados de máxima probabilidad (bimodal si tiene dos máximos locales diferenciados).

- **Distribución amodal:** Ocurre cuando todos los valores del recorrido tienen exactamente la misma probabilidad o densidad constante, como sucede al lanzar un dado legal donde $p_X(x) = \frac{1}{6}$ para todos los valores del $1$ al $6$.

## 4.2. Mediana

La segunda alternativa central divide la masa probabilística exactamente por la mitad, sin importar qué tan lejos se extiendan los valores extremos de las colas.

> [!QUOTE] **Definición Formal 5:** Mediana ($m$)
> 
> La **mediana** de una variable aleatoria continua $X$, denotada por $m$ o $\tilde{\mu}$, es el punto de la recta real donde la [[PROBA 3-1 Variables Aleatorias#3. Función de Distribución Acumulada (FDA)|función de distribución acumulada (FDA)]] alcanza exactamente el valor $0.5$:
> 
> $$F_X(m) = \mathbb{P}(X \le m) = 0.5 \iff m = F_X^{-1}(0.5)$$
> 
> (En variables discretas donde $F_X(x)$ avanza mediante saltos escalonados, la mediana se define como cualquier valor $m$ que satisfaga simultáneamente $\mathbb{P}(X < m) \le 0.5$ y $\mathbb{P}(X \le m) \ge 0.5$.)

En una distribución continua la mediana $m$ es la recta vertical que corta el área total bajo la curva $f_X(x)$ en dos regiones de exactamente $0.5$ de área cada una ($50\%$ de probabilidad a la izquierda y $50\%$ a la derecha).

Su ventaja fundamental frente a la media es su inmunidad (robustez) frente a valores atípicos. Si se estudia la variable aleatoria $X =$ «ingreso personal anual en dólares» de una población con fuerte desigualdad económica, donde el $99\%$ de los habitantes percibe menos de $10\,000\text{ USD}$ anuales y el $1\%$ restante percibe ingresos superiores a $100\,000\text{ USD}$, ese pequeño $1\%$ arrastra el centro de masa $\mu = \mathbb{E}[X]$ hacia un valor intermedio que no representa el ingreso habitual de la mayoría. La mediana $m$, en cambio, permanece anclada en el centro real de la distribución poblacional sin inmutarse por los valores extremos de la cola superior.

## 4.3. Orden Relativo entre Media, Mediana y Moda

La comparación simultánea de la media ($\mu$), la mediana ($m$) y la moda ($x_m$) en una distribución unimodal revela de inmediato su grado y dirección de asimetría (o sesgo):

1. **Distribución simétrica ($\mu = m = x_m$):** Cuando la función de densidad es especular respecto a un eje central, el pico máximo, el punto que divide el área por la mitad y el centro de equilibrio coinciden exactamente en el mismo lugar. Un ejemplo clásico es la distribución normal $N(\mu, \sigma^2)$ o la distribución triangular sobre $[a, b]$ con vértice en el punto medio $c = \frac{a + b}{2}$.

2. **Asimetría positiva o sesgo a la derecha ($x_m < m < \mu$):** La distribución concentra la mayor parte de su masa en valores bajos (a la izquierda) y extiende una cola larga hacia valores altos (a la derecha). Esa cola derecha actúa como un brazo de palanca largo que arrastra la media $\mu$ hacia la derecha, dejando la mediana en posición intermedia. Un ejemplo directo es el número de lanzamientos de una moneda legal hasta obtener la primera cara: el resultado más probable es $x_m = 1$ (con probabilidad $0.5$), mientras que la posibilidad de rachas largas de sellos eleva la media hasta $\mu = 2$.

3. **Asimetría negativa o sesgo a la izquierda ($\mu < m < x_m$):** La distribución concentra la mayor parte de su masa en valores altos (a la derecha) y presenta una cola alargada hacia valores bajos (a la izquierda). En este escenario, los valores bajos desplazan el centro de masa hacia la izquierda, situando $\mu$ por debajo de la mediana y de la moda.

![[PROBA 3-2 Medidas Descriptivas de Variables Aleatorias - Orden de Tendencia Central Según la Asimetría.webp]]

> [!EXAMPLE] **Ejemplo 4:** Localización de Media, Mediana y Moda en una Distribución Triangular
> 
> Considere una variable aleatoria continua $X$ que representa el tiempo en minutos de atención en una ventanilla bancaria, modelada por una distribución triangular sobre el intervalo $[0, 6]\text{ min}$ con pico máximo en $c = 1\text{ min}$, cuya función de densidad de probabilidad continua es:
> 
> $$f_X(x) = \begin{cases} \dfrac{x}{3} & \text{si } 0 \le x \le 1 \\[6pt] \dfrac{6 - x}{15} & \text{si } 1 < x \le 6 \\[6pt] 0 & \text{en otro caso} \end{cases}$$
> 
> Calcule analíticamente la moda $x_m$, la mediana $m$ y la media $\mu = \mathbb{E}[X]$, y clasifique la asimetría de la distribución justificando sus posiciones relativas.

En este ejercicio estudiamos una distribución continua triangular asimétrica definida por tramos lineales, analizando cómo una cola derecha más prolongada desplaza las medidas de localización central. Lo que se busca es determinar el máximo global de la densidad para hallar la moda, integrar hasta acumular $0.5$ para despejar la mediana y evaluar el centro de masa mediante integración por tramos, verificando finalmente el orden característico $x_m < m < \mu$.

1. Identificamos la moda $x_m$ observando que $f_X(x)$ crece linealmente en $[0, 1]$ hasta alcanzar su máximo absoluto $f_X(1) = \frac{1}{3}$ y luego decrece en $(1, 6]$ hasta anularse en $x = 6$.

$$x_m = 1\text{ min}, \qquad f_X(1) = \frac{1}{3}$$

2. Para hallar la mediana $m$, comprobamos primero cuánta probabilidad se acumula hasta la moda $x = 1$: como $\int_0^1 \frac{x}{3}\,dx = \frac{1}{6} < 0.5$, la mediana debe ubicarse en el segundo tramo $(1, 6]$, por lo que integramos desde $0$ hasta $m$ e igualamos a $\frac{1}{2}$.



$$\int_{0}^{1} \frac{x}{3}\,dx + \int_{1}^{m} \frac{6 - x}{15}\,dx = \frac{1}{6} + \left[ \frac{6x}{15} - \frac{x^2}{30} \right]_{1}^{m} = \frac{1}{2}$$

3. Simplificamos la ecuación cuadrática resultante en $m$ y seleccionamos la raíz comprendida dentro del intervalo $(1, 6]$.

$$\frac{1}{6} + \frac{12m - m^2 - 11}{30} = \frac{1}{2} \implies 5 + 12m - m^2 - 11 = 15 \implies m^2 - 12m + 21 = 0$$

$$m = \frac{12 \pm \sqrt{144 - 84}}{2} = 6 \pm \sqrt{15} \implies m = 6 - \sqrt{15} \approx 2.127\text{ min}$$

4. Calculamos la media $\mu = \mathbb{E}[X]$ integrando $x\,f_X(x)$ sobre ambos tramos (o aplicando la fórmula general de la triangular $\frac{a + b + c}{3}$).

$$\mu = \int_{0}^{1} \frac{x^2}{3}\,dx + \int_{1}^{6} \frac{6x - x^2}{15}\,dx$$
$$\mu = \left[\frac{x^3}{9}\right]_{0}^{1} + \left[\frac{3x^2}{15} - \frac{x^3}{45}\right]_{1}^{6} = \frac{1}{9} + \left(\frac{108}{15} - \frac{216}{45}\right) - \left(\frac{3}{15} - \frac{1}{45}\right) = \frac{7}{3} \approx 2.333\text{ min}$$

5. Comparamos las tres métricas obtenidas y concluimos que la distribución presenta asimetría positiva (sesgo a la derecha), ya que la cola extendida hacia $x = 6$ arrastra la media por encima de la mediana y de la moda.

$$x_m = 1 < m \approx 2.127 < \mu \approx 2.333$$

# 5. Medidas de Posición No Central

En muchas aplicaciones prácticas no basta con conocer el centro de la distribución: interesa saber por debajo de qué umbral cae el $90\%$ de los tiempos de espera, o cuál es el margen que abarca el $50\%$ más habitual de las observaciones sin dejarse contaminar por anomalías extremas. Para responder estas preguntas se generaliza el concepto de mediana mediante los cuantiles.

## 5.1. Cuantiles, Percentiles y Cuartiles

> [!QUOTE] **Definición Formal 6:** Cuantil de Orden $\alpha$ ($x_{(\alpha)}$)
> 
> Sea $X$ una variable aleatoria continua con [[PROBA 3-1 Variables Aleatorias#3. Función de Distribución Acumulada (FDA)|función de distribución acumulada (FDA)]] estrictamente creciente $F_X(x)$, y sea $\alpha \in (0, 1)$ una proporción de probabilidad dada. El **cuantil de orden $\alpha$**, denotado por $x_{(\alpha)}$ o $q_\alpha$, es el valor del recorrido que acumula una probabilidad exacta igual a $\alpha$ a su izquierda:
> 
> $$F_X\big(x_{(\alpha)}\big) = \mathbb{P}\big(X \le x_{(\alpha)}\big) = \alpha \iff x_{(\alpha)} = F_X^{-1}(\alpha)$$

El cuantil $x_{(\alpha)}$ actúa como una frontera numérica sobre la recta real que divide el recorrido en dos zonas: una fracción $\alpha$ (o $100\alpha\%$) de los resultados ocurre en o por debajo de $x_{(\alpha)}$, y la fracción complementaria $1 - \alpha$ ocurre por encima de él. Dependiendo de la subdivisión porcentual elegida, los cuantiles reciben nombres específicos:

- **Percentiles ($P_1, P_2, \dots, P_{99}$):** Dividen la distribución en $100$ intervalos equiprobables de $1\%$ de probabilidad cada uno. El $k$-ésimo percentil corresponde al cuantil de orden $\alpha = k/100$, es decir, $P_k = x_{(k/100)} = F_X^{-1}(k/100)$. Por ejemplo, el percentil $95$ ($P_{95} = x_{(0.95)}$) indica el umbral que solo es superado por el $5\%$ de los casos más extremos.

- **Cuartiles ($Q_1, Q_2, Q_3$):** Dividen la distribución en $4$ bloques equiprobables de $25\%$ cada uno:

- **Primer cuartil ($Q_1$):** Equivale al percentil $25$ ($Q_1 = x_{(0.25)} = F_X^{-1}(0.25)$), acumulando el $25\%$ inferior de la distribución.

- **Segundo cuartil ($Q_2$):** Equivale al percentil $50$ ($Q_2 = x_{(0.50)} = F_X^{-1}(0.50)$), coincidiendo exactamente con la **mediana** $m$.

- **Tercer cuartil ($Q_3$):** Equivale al percentil $75$ ($Q_3 = x_{(0.75)} = F_X^{-1}(0.75)$), acumulando el $75\%$ de la probabilidad a su izquierda.

## 5.2. Rango Intercuartílico como Medida Robusta de Dispersión

Así como la media es sensible a los valores atípicos y encuentra su alternativa robusta en la mediana, la desviación estándar $\sigma$ también puede inflarse artificialmente por unas pocas observaciones extremas en las colas. Para medir la dispersión del núcleo central de la distribución ignorando los extremos, se utiliza la amplitud comprendida entre el tercer y el primer cuartil.

> [!QUOTE] **Definición Formal 7:** Rango Intercuartílico ($\text{RIC}$ / $\text{IQR}$)
> 
> El **Rango Intercuartílico** (abreviado $\text{RIC}$ en español o $\text{IQR}$ del inglés ‘Interquartile Range’) se define como la diferencia entre el tercer cuartil y el primer cuartil de la distribución:
> $$\text{RIC} = Q_3 - Q_1 = x_{(0.75)} - x_{(0.25)} = F_X^{-1}(0.75) - F_X^{-1}(0.25)$$

El $\text{RIC}$ mide el ancho del intervalo $[Q_1, Q_3]$ que encierra exactamente al $50\%$ central de la probabilidad total ($\mathbb{P}(Q_1 \le X \le Q_3) = F_X(Q_3) - F_X(Q_1) = 0.75 - 0.25 = 0.50$). Dado que descarta el $25\%$ más bajo y el $25\%$ más alto de la distribución, el $\text{RIC}$ es completamente insensible a las colas pesadas o mediciones anómalas en los extremos, conservando además las mismas unidades lineales de la variable $X$.

![[PROBA 3-2 Medidas Descriptivas de Variables Aleatorias - Cuartiles y Rango Intercuantílico.webp]]

# 6. Ejercicios Prácticos Resueltos

## 6.1. Evaluación de Sesgo en una Distribución Polinómica Acotada

> [!EXAMPLE] **Ejemplo 5:** Análisis Completo de Localización, Dispersión y Asimetría
> 
> Sea $X$ una variable aleatoria continua que modela la fracción de capacidad utilizada en un depósito de agua antes de iniciar su vaciado automático, cuya función de densidad de probabilidad continua está definida por:
> 
> $$f_X(x) = \begin{cases} 3x^2 & \text{si } 0 < x < 1 \\ 0 & \text{en otro caso} \end{cases}$$
> 
> Calcule analíticamente la media $\mu = \mathbb{E}[X]$, la varianza $\sigma^2$ mediante el teorema de König, la desviación estándar $\sigma$, la moda $x_m$ y la mediana $m$. Clasifique la asimetría de la distribución justificando las posiciones relativas de sus medidas de tendencia central.

En este ejercicio trabajamos con una variable aleatoria continua acotada en el intervalo unitario $(0, 1)$, cuya densidad crece de forma cuadrática a medida que $x$ se aproxima al extremo superior $1$. Lo que se busca es caracterizar integralmente la distribución calculando su centro de masa, su dispersión alrededor de la media y sus puntos de concentración y partición.

A partir de los valores obtenidos, se pide comparar la posición relativa de la media, la mediana y la moda para determinar si la curva presenta sesgo positivo, simetría o sesgo negativo, explicando el mecanismo geométrico que produce dicho desplazamiento.

1. Verificamos que $f_X(x) \ge 0$ en $(0, 1)$ y que su integral total es igual a $1$, y calculamos la esperanza matemática $\mu = \mathbb{E}[X]$ integrando $x\,f_X(x)$ sobre el soporte activo.

$$\int_{0}^{1} 3x^2 \, dx = \Big[x^3\Big]_{0}^{1} = 1, \qquad \mu = \mathbb{E}[X] = \int_{0}^{1} x\,(3x^2) \, dx = \int_{0}^{1} 3x^3 \, dx = \left[\frac{3}{4}x^4\right]_{0}^{1} = \frac{3}{4} = 0.75$$

2. Calculamos el segundo momento ordinario $\alpha_2 = \mathbb{E}[X^2]$ aplicando el Teorema 1 con $G(x) = x^2$.

$$\mathbb{E}[X^2] = \int_{0}^{1} x^2\,(3x^2) \, dx = \int_{0}^{1} 3x^4 \, dx = \left[\frac{3}{5}x^5\right]_{0}^{1} = \frac{3}{5} = 0.60$$

3. Aplicamos el teorema de König ($\mathrm{Var}(X) = \mathbb{E}[X^2] - \mu^2$) para hallar la varianza exacta y extraemos su raíz cuadrada no negativa para obtener la desviación estándar $\sigma$.

$$\sigma^2 = \mathrm{Var}(X) = \frac{3}{5} - \left(\frac{3}{4}\right)^2 = \frac{3}{5} - \frac{9}{16} = \frac{48 - 45}{80} = \frac{3}{80} = 0.0375$$

$$\sigma = \sqrt{\frac{3}{80}} = \frac{\sqrt{15}}{20} \approx 0.1936$$

4. Determinamos la moda $x_m$ analizando la derivada primera $f_X'(x) = 6x > 0$ para todo $x \in (0, 1)$: al ser estrictamente creciente, la densidad alcanza su supremo global en el extremo derecho del intervalo.

$$x_m = \lim_{x \to 1^-} \arg\max f_X(x) = 1$$

5. Deducimos la función de distribución acumulada $F_X(x) = \int_0^x 3t^2\,dt = x^3$ para $x \in (0, 1)$ e igualamos $F_X(m) = 0.5$ para despejar la mediana $m$.

$$F_X(m) = m^3 = \frac{1}{2} \implies m = \left(\frac{1}{2}\right)^{1/3} = \frac{1}{\sqrt[3]{2}} \approx 0.7937$$

6. Comparamos las tres medidas centrales obtenidas ($\mu = 0.75 < m \approx 0.7937 < x_m = 1$) y clasificamos la distribución como asimétrica negativa (sesgada a la izquierda): la mayor parte de la masa probabilística se agrupa cerca de $x = 1$, mientras que la cola extendida hacia $x = 0$ desplaza el centro de masa $\mu$ por debajo de la mediana y de la moda.

$$\mu = 0.7500 < m \approx 0.7937 < x_m = 1.0000$$

## 6.2. Cálculo de Cuantiles y Rango Intercuartílico en Tiempos de Atención

> [!EXAMPLE] **Ejemplo 6:** Cuartiles y Dispersión Robusta en Tiempos de Atención Acumulados
> 
> El tiempo total $X$ (en minutos) necesario para atender consecutivamente a dos clientes en una oficina de atención al público sigue una distribución continua cuya función de distribución acumulada (FDA) está dada por:
> 
> $$F_X(x) = \begin{cases} 1 - (1 + x)e^{-x} & \text{si } x \ge 0 \\ 0 & \text{si } x < 0 \end{cases}$$
> 
> Plantee las ecuaciones exactas para los cuantiles de orden $\alpha$, deduzca el primer cuartil $Q_1$, la mediana $Q_2$ y el tercer cuartil $Q_3$, y calcule el Rango Intercuartílico ($\text{RIC}$) para evaluar la dispersión robusta del proceso.

En este ejercicio partimos directamente de la función de distribución acumulada de una variable continua no acotada superiormente ($x \ge 0$). La finalidad es determinar las fronteras que delimitan el $25\%$, $50\%$ y $75\%$ de los tiempos de servicio y obtener la amplitud del $50\%$ central mediante el Rango Intercuartílico, evitando el efecto de las esperas excepcionalmente largas en la cola superior.

Dado que la ecuación $1 - (1 + x)e^{-x} = \alpha$ combina un término lineal con una exponencial decreciente, no admite despeje mediante funciones elementales básicas; por ello, formularemos primero la relación trascendente exacta (cuya solución cerrada corresponde a la rama secundaria de la función $W$ de Lambert) y resolveremos numéricamente cada cuartil mediante aproximación iterativa.

1. Planteamos la condición general de cuantil $F_X(x_{(\alpha)}) = \alpha$ para $\alpha \in (0, 1)$ sobre el soporte activo $x \ge 0$ y reordenamos la ecuación trascendente resultante (equivalente analíticamente a $x_{(\alpha)} = -1 - W_{-1}\!\left(-\frac{1-\alpha}{e}\right)$).

$$1 - \big(1 + x_{(\alpha)}\big)e^{-x_{(\alpha)}} = \alpha \iff \big(1 + x_{(\alpha)}\big)e^{-x_{(\alpha)}} = 1 - \alpha$$

2. Sustituimos $\alpha = 0.25$ para obtener la ecuación del primer cuartil $Q_1 = x_{(0.25)}$ y resolvemos numéricamente mediante el método de Newton-Raphson sobre $g(x) = (1 + x)e^{-x} - 0.75 = 0$ (con derivada $g'(x) = -x\,e^{-x}$).

$$(1 + Q_1)e^{-Q_1} = 0.75 \implies Q_1 \approx 0.9613\text{ min}$$

3. Sustituimos $\alpha = 0.50$ para determinar de forma análoga la mediana $Q_2 = x_{(0.50)}$, comprobando que la mitad de los servicios concluye antes de $1.68\text{ minutos}$.

$$(1 + Q_2)e^{-Q_2} = 0.50 \implies Q_2 \approx 1.6783\text{ min}$$

4. Sustituimos $\alpha = 0.75$ para calcular el tercer cuartil $Q_3 = x_{(0.75)}$, que marca el umbral superado únicamente por el $25\%$ de las atenciones más prolongadas.

$$(1 + Q_3)e^{-Q_3} = 0.25 \implies Q_3 \approx 2.6926\text{ min}$$

5. Calculamos el Rango Intercuartílico ($\text{RIC} = Q_3 - Q_1$), concluyendo que el $50\%$ central de las atenciones consecutivas se concentra dentro de una franja de amplitud aproximada de $1.73\text{ minutos}$ alrededor de la mediana.

$$\text{RIC} = Q_3 - Q_1 \approx 2.6926 - 0.9613 = 1.7313\text{ min}$$

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