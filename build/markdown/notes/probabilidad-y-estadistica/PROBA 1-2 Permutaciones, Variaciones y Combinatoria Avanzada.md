---
created: 2026-02-24T20:34:00
title: Permutaciones, Variaciones y Combinatoria Avanzada
semester: 4
subject:
  - "[[PROBA 0-0 Nota Informativa|Probabilidad y Estadística]]"
unit: 1
status: done
---

<h1 id="main-title"  align="center"> Permutaciones, Variaciones y Combinatoria Avanzada </h1>

> [!TLDR] SÍNTESIS 
> La **combinatoria avanzada** y los modelos de conteo (que abarcan **permutaciones**, **variaciones** y **combinaciones**) constituyen el fundamento matemático indispensable para dimensionar con exactitud el **espacio de estados** de sistemas discretos y evaluar la **tractabilidad computacional**. Al considerar simetrías internas, restricciones de inventario y repeticiones, estas herramientas formales permiten resolver problemas complejos de asignación y optimización evitando errores críticos de escala.

Dimensionar con exactitud el espacio de estados $\vert{}\Omega\vert{}$ de un sistema discreto resulta indispensable para calcular probabilidades bajo el modelo de Laplace y determinar si un problema es computacionalmente tratable. Sin embargo, aplicar el principio multiplicativo de forma directa suele conducir a errores graves cuando las configuraciones del sistema poseen simetrías internas o restricciones de inventario.

Para formular el conteo correcto en cualquier arquitectura lógica, es necesario responder dos preguntas antes de escribir una ecuación: si intercambiar la posición de dos elementos produce un estado observable distinto, y si un mismo tipo de elemento puede seleccionarse múltiples veces o posee copias idénticas entre sí. Cuando cada unidad disponible es única y su posición relativa define el funcionamiento del sistema, el problema se reduce a construir secuencias ordenadas sin reemplazo.

# 1. Ordenamientos Secuenciales sin Repetición: Permutaciones y Variaciones

El punto de partida del conteo estructurado ocurre cuando se dispone de un conjunto de $n$ elementos distintos y se desea formar secuencias ordenadas sin reutilizar ninguno de ellos. Dependiendo de si se emplea la totalidad del conjunto o únicamente un subconjunto de tamaño $r$, surgen dos formulaciones directamente conectadas por el principio multiplicativo.

## 1.1. Permutaciones Simples de un Conjunto Completo

Cuando todos los $n$ elementos disponibles deben participar obligatoriamente en la secuencia y la posición de cada uno altera el resultado, el problema consiste en determinar de cuántas maneras distintas pueden reordenarse entre sí.

> [!QUOTE] **Teorema 1:** Permutaciones Simples
> Sea $S$ un conjunto finito con $n$ elementos distintos ($n \in \mathbb{N}$). El número total de arreglos ordenados que incluyen a todos los elementos de $S$ sin repetición está dado por:
> 
> $$P_n = n! = n \cdot (n - 1) \cdot (n - 2) \cdots 2 \cdot 1$$
> 
> donde por convención algebraica se define $0! = 1$.

Imagina que tienes un conjunto de elementos y quieres ordenarlos todos en una fila. Para elegir el primer elemento de la secuencia, tienes total libertad y puedes escoger cualquiera de los $n$ elementos disponibles, usando ese elemento como un punto de partida o pivote. Una vez que fijas ese primero, para la segunda posición ya solo te quedan $n - 1$ elementos disponibles de los cuales elegir. Para la tercera posición el número de opciones se reduce a $n - 2$, y así sucesivamente de forma consecutiva, restando una unidad en cada paso hasta que en la última posición queda un único elemento posible. Al multiplicar las opciones de cada una de estas etapas independientes, el cálculo resultante se reduce a una multiplicación decreciente continua, que es exactamente lo que define al factorial.

> [!EXAMPLE] **Ejemplo 1:** Planificación de Procesos en un Núcleo Mono-hilo
> 
> Un planificador «batch» en un procesador de un solo núcleo recibe $n = 6$ tareas independientes ($T_1, T_2, T_3, T_4, T_5, T_6$) que deben ejecutarse secuencialmente hasta completarse sin interrupciones. ¿Cuántas trazas de ejecución distintas puede generar el planificador?

En este ejercicio analizamos un sistema de procesamiento secuencial donde la totalidad de las tareas disponibles debe entrar en la cola de ejecución sin omisiones ni duplicados. Lo que se busca es determinar la cantidad exacta de trazas de ejecución posibles aplicando el modelo de permutaciones simples, dado que cualquier reordenamiento modifica los tiempos de espera y finalización del sistema.

1. Identificamos que todas las $n = 6$ tareas participan obligatoriamente en la secuencia ($r = n = 6$), que no se permite repetir una misma tarea y que el orden de ejecución altera el comportamiento del sistema, por lo que corresponde aplicar permutaciones simples ($P_n = n!$).

$$n = 6, \qquad P_n = n!$$

2. Aplicamos el principio multiplicativo sobre las $6$ ranuras temporales de la cola de ejecución, reduciendo en una unidad el número de tareas disponibles tras cada asignación hasta completar la última posición.

$$P_6 = 6! = 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 720 \text{ trazas de ejecución}$$

## 1.2. Variaciones o $r$-Permutaciones de Subconjuntos

En muchas arquitecturas de ingeniería, el catálogo de recursos disponibles contiene $n$ elementos distintos, pero el sistema únicamente dispone de $r$ ranuras o posiciones que llenar, con $0 \le r \le n$. En este escenario, los $n - r$ elementos no seleccionados quedan fuera del arreglo final.

> [!QUOTE] **Teorema 2:** Variaciones ($r$-Permutaciones sin Repetición)
> Dados enteros $n$ y $r$ tales que $0 \le r \le n$, el número de arreglos ordenados de longitud $r$ que pueden formarse extrayendo elementos sin reposición de un conjunto total de $n$ objetos distintos (denotado $V_n^r$ o $P_n^r$) es:
> 
> $$V_n^r = P_n^r = \frac{n!}{(n - r)!} = n \cdot (n - 1) \cdot (n - 2) \cdots (n - r + 1)$$

La deducción sigue la misma lógica de llenado de casillas, pero el proceso se detiene exactamente al completar la casilla número $r$, donde aún quedan $n - (r - 1) = n - r + 1$ opciones disponibles. Para compactar este producto truncado en notación factorial, se multiplica y divide simultáneamente por $(n - r)!$, completando la cadena descendente hasta $1$ en el numerador y cancelando los factores de los elementos sobrantes en el denominador. Nótese que en parte de la literatura del curso esta expresión se escribe como $P_M^N = \frac{M!}{(M - N)!}$, donde $M$ representa el tamaño de la población y $N$ el tamaño de la muestra ordenada.

> [!EXAMPLE] **Ejemplo 2:** Asignación de Roles Jerárquicos en un Clúster
> 
> Una arquitectura de alta disponibilidad cuenta con $n = 10$ servidores físicos idénticos en hardware, pero distintos por su dirección IP. Para desplegar un servicio replicado se requiere asignar exactamente $r = 3$ servidores a tres roles jerárquicos exclusivos: «Nodo Líder», «Réplica Síncrona 1» y «Réplica Síncrona 2». ¿Cuántas topologías de despliegue distintas existen?

A diferencia del caso anterior, aquí el catálogo de recursos supera la cantidad de puestos disponibles, por lo que una parte de los servidores quedará fuera de la selección final. La finalidad del ejercicio es contabilizar el número de topologías válidas mediante variaciones sin repetición, reflejando que la jerarquía de red distingue qué servidor ocupa cada rol específico.

1. Reconocemos que los $n = 10$ servidores son distinguibles por su IP, que solo se asignan $r = 3$ roles sin reutilizar un mismo servidor y que intercambiar los servidores asignados a «Nodo Líder» y «Réplica Síncrona 1» produce una topología funcionalmente distinta, lo cual corresponde a una variación sin repetición ($V_n^r$).

$$n = 10, \quad r = 3, \qquad V_n^r = P_n^r = \frac{n!}{(n - r)!}$$

2. Sustituimos los parámetros en la fórmula factorial y cancelamos los factores correspondientes a los $n - r = 7$ servidores no seleccionados.

$$V_{10}^3 = P_{10}^3 = \frac{10!}{(10 - 3)!} = \frac{10!}{7!} = 10 \cdot 9 \cdot 8$$

3. Efectuamos el producto truncado equivalente a multiplicar las $10$ opciones para el Nodo Líder por las $9$ restantes para la Réplica 1 y las $8$ disponibles para la Réplica 2.

$$V_{10}^3 = 720 \text{ topologías posibles}$$

# 2. Selecciones sin Orden y Estructura de los Coeficientes Binomiales

El enfoque de variaciones falla cuando el sistema trata como equivalentes a dos arreglos que contienen exactamente los mismos elementos en distinto orden. Si un balanceador de carga selecciona tres nodos para almacenar fragmentos de un archivo sin asignarles jerarquía, elegir los nodos $\{A, B, C\}$ produce exactamente la misma topología que elegir $\{C, B, A\}$. Contar con $V_n^r$ sobreestima el espacio real porque registra cada subconjunto múltiples veces.

## 2.1. Combinaciones Simples y Deducción mediante la Regla de la División

Para eliminar la redundancia generada por el orden interno de los elementos seleccionados, se recurre a la regla de la división, que colapsa clases de equivalencia de tamaño uniforme.

> [!QUOTE] **Teorema 3:** Combinaciones Simples (Coeficiente Binomial)
> Para enteros $n$ y $r$ con $0 \le r \le n$, el número de subconjuntos desordenados de tamaño $r$ que pueden extraerse de un conjunto de $n$ elementos distintos está dado por el coeficiente binomial:
> 
> $$C_n^r = \binom{n}{r} = \frac{n!}{r!(n - r)!}$$

La deducción formal parte de observar que todo arreglo ordenado de $r$ elementos ($V_n^r$) puede construirse en dos etapas secuenciales mediante el principio multiplicativo: primero se elige el subconjunto desordenado de $r$ elementos de $\binom{n}{r}$ maneras posibles, y luego se ordenan internamente esos $r$ elementos de $P_r = r!$ formas distintas. Esto establece la identidad fundamental:

$$V_n^r = \binom{n}{r} \cdot r!$$

Al aplicar la regla de la división (dividiendo el total de variaciones ordenadas entre la multiplicidad $d = r!$ de permutaciones internas equivalentes) se purga el orden y emerge la expresión factorial cerrada:

$$\binom{n}{r} = \frac{V_n^r}{r!} = \frac{\frac{n!}{(n - r)!}}{r!} = \frac{n!}{r!(n - r)!}$$

> [!EXAMPLE] **Ejemplo 3:** Selección Simétrica de Nodos para Balanceo de Carga
> 
> De un grupo de $n = 10$ servidores disponibles en un centro de datos, un balanceador simétrico debe seleccionar un subconjunto de $r = 3$ nodos para distribuir copias idénticas de una caché de lectura sin distinción de jerarquía. Calcule cuántos subconjuntos de servidores pueden formarse.

En este problema se parte del mismo catálogo de servidores que en el ejemplo anterior, pero se elimina por completo la jerarquía entre los nodos escogidos. Se busca demostrar cómo la regla de la división purga el orden interno mediante combinaciones simples, evitando sobreestimar el espacio de configuraciones reales al tratar como equivalentes todos los arreglos que contienen los mismos servidores.

1. Determinamos primero el número de secuencias ordenadas de $r = 3$ servidores extraídos de un total de $n = 10$ nodos distintos mediante variaciones sin repetición.

$$V_{10}^3 = \frac{10!}{(10 - 3)!} = 10 \cdot 9 \cdot 8 = 720$$

2. Identificamos que cada subconjunto de $3$ nodos puede permutarse internamente de $P_3 = 3!$ maneras que representan exactamente el mismo grupo de caché en el balanceador simétrico.

$$d = 3! = 3 \cdot 2 \cdot 1 = 6$$

3. Aplicamos la regla de la división (coeficiente binomial $C_{10}^3$) dividiendo las variaciones ordenadas entre la multiplicidad interna $3!$ para obtener la cantidad de subconjuntos únicos.

$$C_{10}^3 = \binom{10}{3} = \frac{10!}{3!(10 - 3)!} = \frac{720}{6} = 120 \text{ subconjuntos}$$

## 2.2. Simetría Combinatoria e Identidad de Pascal

Los coeficientes binomiales $\binom{n}{r}$ obedecen propiedades estructurales que simplifican tanto el análisis algebraico como el diseño de algoritmos recursivos y de programación dinámica.

> [!QUOTE] **Teorema 4:** Propiedades Fundamentales de los Coeficientes Binomiales
> Para todo par de enteros $n, r$ con $0 \le r \le n$ (y $1 \le k \le n - 1$ en la recurrencia), se cumplen:
> 1. **Propiedad de Simetría Combinatoria:**
> 
> $$\binom{n}{r} = \binom{n}{n - r}$$
> 
> 1. **Identidad de Pascal:**
> 
> $$\binom{n}{k} = \binom{n - 1}{k} + \binom{n - 1}{k - 1}$$

Intuitivamente, la simetría combinatoria establece que elegir los $r$ elementos que entran en un subconjunto equivale de manera biyectiva a elegir los $n - r$ elementos que quedan excluidos de él. Por su parte, la identidad de Pascal descompone la elección de $k$ elementos respecto a un elemento distinguido (llamémoslo $a_1$): todo subconjunto de tamaño $k$ o bien excluye a $a_1$ (obligando a elegir los $k$ elementos entre los $n - 1$ restantes), o bien incluye a $a_1$ (reduciendo la tarea a elegir $k - 1$ compañeros entre los $n - 1$ restantes).

![[PROBA 1-2 Permutaciones, Variaciones y Combinatoria Avanzada - Simetria de Coeficientes Binomiales.webp]]

### 2.2.1. Demostración Algebraica y Combinatoria de las Identidades

Para validar analíticamente ambas propiedades en pizarra, desarrollamos sus definiciones factoriales paso a paso:

**Demostración de la Simetría Combinatoria:** Partimos del miembro derecho $\binom{n}{n - r}$ y aplicamos la definición factorial del Teorema 3:

$$\binom{n}{n - r} = \frac{n!}{(n - r)! \cdot [n - (n - r)]!}$$

Simplificamos el corchete en el denominador mediante cancelación aditiva ($n - n + r = r$) y aplicamos la conmutatividad del producto:

$$\binom{n}{n - r} = \frac{n!}{(n - r)! \cdot r!} = \frac{n!}{r! \cdot (n - r)!} = \binom{n}{r} \quad \blacksquare$$

**Demostración de la Identidad de Pascal:** Desarrollamos la suma del miembro derecho $\binom{n - 1}{k} + \binom{n - 1}{k - 1}$ buscando un denominador común igual a $k!(n - k)!$:

$$\binom{n - 1}{k} + \binom{n - 1}{k - 1} = \frac{(n - 1)!}{k!(n - 1 - k)!} + \frac{(n - 1)!}{(k - 1)!(n - k)!}$$

Multiplicamos la primera fracción por $\frac{n - k}{n - k}$ y la segunda por $\frac{k}{k}$, aprovechando las identidades $(n - k) \cdot (n - k - 1)! = (n - k)!$ y $k \cdot (k - 1)! = k!$:

$$\binom{n - 1}{k} + \binom{n - 1}{k - 1} = \frac{(n - k)(n - 1)!}{k!(n - k)!} + \frac{k(n - 1)!}{k!(n - k)!}$$

Agrupamos bajo el denominador común y factorizamos $(n - 1)!$ en el numerador:

$$\binom{n - 1}{k} + \binom{n - 1}{k - 1} = \frac{(n - 1)![(n - k) + k]}{k!(n - k)!} = \frac{(n - 1)! \cdot n}{k!(n - k)!} = \frac{n!}{k!(n - k)!} = \binom{n}{k} \quad \blacksquare$$

> [!EXAMPLE] **Ejemplo 4:** Reducción de Carga Computacional por Simetría
> 
> Un sistema de auditoría debe evaluar todas las combinaciones posibles de $r = 47$ paquetes seleccionados de un lote de $n = 52$ tramas capturadas. Determine el número de combinaciones aprovechando la simetría combinatoria.

Calcular directamente un coeficiente binomial con parámetros grandes puede implicar expandir decenas de factores en el numerador y en el denominador. La finalidad de este ejercicio es aprovechar la propiedad de simetría combinatoria para transformar la selección de un subconjunto grande en la elección equivalente de los elementos descartados, minimizando así la carga de cálculo.

1. Planteamos el conteo sin orden de $r = 47$ tramas elegidas de un lote de $n = 52$ mediante el coeficiente binomial $\binom{52}{47}$ y aplicamos la propiedad de simetría combinatoria $\binom{n}{r} = \binom{n}{n - r}$, observando que elegir $47$ tramas equivale de forma biyectiva a elegir las $5$ que se excluyen.

$$\binom{52}{47} = \binom{52}{52 - 47} = \binom{52}{5}$$

2. Desarrollamos la expresión simplificada utilizando únicamente $5$ factores decrecientes en el numerador y $5!$ en el denominador.

$$\binom{52}{5} = \frac{52 \cdot 51 \cdot 50 \cdot 49 \cdot 48}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}$$

3. Evaluamos el cociente resultante para obtener el número exacto de combinaciones posibles en el sistema de auditoría.

$$\binom{52}{47} = 2.598.960 \text{ combinaciones}$$

## 2.3. Teorema del Binomio de Newton

La interpretación combinatoria de $\binom{n}{k}$ proporciona una demostración directa de la expansión algebraica de potencias de un binomio, conectando el conteo discreto con el álgebra polinómica y la distribución binomial de probabilidad.

> [!QUOTE] **Teorema 5:** Teorema del Binomio
> Para cualesquiera números reales (o elementos de un anillo conmutativo) $a, b$ y todo entero no negativo $n \in \mathbb{N}_0$, se verifica:
> 
> $$(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}$$

Al expandir el producto de $n$ factores idénticos $(a + b)(a + b)\cdots(a + b)$, cada término elemental resultante se forma eligiendo exactamente una variable ($a$ o $b$) de cada uno de los $n$ paréntesis. Para obtener el monomio $a^k b^{n-k}$, es necesario seleccionar la variable $a$ en exactamente $k$ paréntesis y la variable $b$ en los $n - k$ paréntesis restantes. Como la multiplicación es conmutativa, el número de veces que aparece el término $a^k b^{n-k}$ coincide exactamente con el número de formas de elegir $k$ posiciones entre los $n$ factores sin importar el orden, es decir, $\binom{n}{k}$. Evaluando esta identidad en $a = 1, b = 1$ se demuestra inmediatamente que la cardinalidad del conjunto potencia de un conjunto de $n$ elementos es $\sum_{k=0}^n \binom{n}{k} = 2^n$.

> [!EXAMPLE] **Ejemplo 5:** Conteo de Cadenas Binarias por Peso de Hamming
> 
> ¿Cuántas cadenas binarias de longitud $n = 8$ bits contienen exactamente $k = 3$ bits en estado lógico $1$ (peso de Hamming igual a $3$)?

Este ejercicio conecta el conteo combinatorio con la representación polinómica del Teorema del Binomio de Newton en un contexto de codificación digital. Se busca determinar cuántas palabras de $8\text{ bits}$ tienen un peso de Hamming específico interpretando cada bit de la cadena como la elección de una variable en la expansión de un binomio.

1. Asociamos cada una de las $n = 8$ posiciones de la palabra binaria a un factor del binomio $(x + 1)^8$, donde seleccionar $x$ representa fijar un bit en estado $1$ y seleccionar $1$ representa fijar un bit en estado $0$.

$$(x + 1)^8 = \sum_{k=0}^8 \binom{8}{k} x^k \cdot 1^{8 - k}$$

2. Identificamos que el número de cadenas con exactamente $k = 3$ bits en estado $1$ corresponde al coeficiente binomial que acompaña al término $x^3$ en dicha expansión.

$$\text{Cadenas con } k = 3 \text{ unos} = \binom{8}{3}$$

3. Desarrollamos el coeficiente binomial y efectuamos la simplificación aritmética para obtener el total de cadenas binarias válidas.

$$\binom{8}{3} = \frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = 56 \text{ cadenas}$$

# 3. Agrupamientos con Repetición y Restricciones de Identidad

Los modelos anteriores asumen dos condiciones ideales: cada elemento seleccionado desaparece del catálogo (sin reposición) y todos los objetos son distinguibles entre sí. En los sistemas computacionales reales ambas hipótesis suelen romperse: los alfabetos de símbolos se reutilizan en cada carácter de una cadena, los hilos de ejecución idénticos se reparten entre múltiples núcleos y los paquetes de red repetidos viajan mezclados en una misma ráfaga.

## 3.1. Variaciones con Repetición Permitida

Cuando se construye una secuencia ordenada de longitud $r$ tomando símbolos de un alfabeto o catálogo de $n$ tipos distintos con disponibilidad ilimitada, la elección en una posición no restringe las opciones de las posiciones siguientes.

> [!QUOTE] **Teorema 6:** Variaciones con Repetición (Permutaciones con Reposición)
> El número de secuencias ordenadas de tamaño $r$ que pueden formarse a partir de un conjunto de $n$ elementos distintos cuando se permite repetir cada elemento de forma ilimitada es:
> 
> $$VR_n^r = n^r$$

A diferencia de las variaciones simples, aquí no existe la restricción $r \le n$, pues el alfabeto nunca se agota. Cada una de las $r$ casillas de la secuencia admite exactamente $n$ posibilidades independientes; aplicando la regla del producto $r$ veces consecutivas se obtiene $n \cdot n \cdots n = n^r$.

> [!EXAMPLE] **Ejemplo 6:** Espacio de Claves en Generación de Contraseñas
> 
> Un sistema de autenticación exige contraseñas de longitud exacta $r = 5$ caracteres construidas exclusivamente sobre un alfabeto reducido de $n = 16$ símbolos hexadecimales ($\{0\text{--}9, \text{A--F}\}$), permitiendo repetir símbolos. Determine la cardinalidad del espacio de búsqueda para un ataque de fuerza bruta.

En seguridad informática, dimensionar el tamaño del espacio de claves es fundamental para evaluar la resistencia de un esquema de autenticación frente a búsquedas exhaustivas. La finalidad de este ejercicio es calcular el número total de contraseñas válidas considerando que la posición de cada carácter importa y que el alfabeto no se agota al reutilizar símbolos.

1. Verificamos que el orden distingue contraseñas diferentes (por ejemplo, «A1B2C» $\neq$ «C2B1A») y que se permite repetir un mismo símbolo en múltiples posiciones («AAAAA» es válida), lo que corresponde a variaciones con repetición ($VR_n^r = n^r$).

$$n = 16, \quad r = 5, \qquad VR_n^r = n^r$$

2. Aplicamos el principio multiplicativo asignando $16$ opciones independientes a cada una de las $5$ posiciones y expresamos el resultado en base $2$ para evaluar su magnitud binaria exacta.

$$VR_{16}^5 = 16^5 = (2^4)^5 = 2^{20} = 1.048.576 \text{ contraseñas posibles}$$

## 3.2. Combinaciones con Repetición y el Método de Estrellas y Barras

El escenario más sutil surge cuando el orden de selección no importa, pero se permite tomar múltiples copias idénticas de cada una de las $n$ categorías disponibles hasta acumular $r$ elementos. No es posible dividir $n^r$ entre $r!$ porque las secuencias con elementos repetidos tienen distinta multiplicidad de permutaciones que las secuencias con elementos todos diferentes.

> [!QUOTE] **Teorema 7:** Combinaciones con Repetición
> El número de selecciones desordenadas de tamaño $r$ extraídas de un catálogo de $n$ categorías distintas con disponibilidad ilimitada está dado por:
> 
> $$CR_n^r = \binom{n + r - 1}{r} = \binom{n + r - 1}{n - 1} = \frac{(n + r - 1)!}{r!(n - 1)!}$$

Para comprender esta fórmula sin memorizarla, se utiliza el método visual de **«estrellas y barras»** (‘stars and bars’). Imaginamos un contenedor dividido en $n$ compartimientos contiguos, uno por cada categoría disponible. Para separar físicamente $n$ compartimientos en una fila única hacen falta exactamente $n - 1$ tabiques verticales o «barras» ($\vert{}$). Por otro lado, los $r$ elementos seleccionados se representan mediante $r$ fichas indistinguibles o «estrellas» ($\star$) depositadas dentro de esos compartimientos.

### 3.2.1. Deducción Analítica de Soluciones Enteras No Negativas

Cada distribución física de estrellas y barras corresponde de manera biyectiva a una solución entera no negativa de la ecuación diofántica lineal que contabiliza cuántas unidades $x_i$ se toman de cada categoría $i \in \{1, 2, \dots, n\}$:

$$x_1 + x_2 + \dots + x_n = r, \quad \text{con } x_i \in \mathbb{Z}_{\ge 0}$$

Por ejemplo, para $n = 4$ categorías y $r = 5$ elementos, la configuración $\star \star \mid \star \mid \mid \star \star$ codifica la solución $(x_1, x_2, x_3, x_4) = (2, 1, 0, 2)$, indicando dos unidades de la primera categoría, una de la segunda, ninguna de la tercera y dos de la cuarta.

Para contar todas las configuraciones válidas, observamos que cualquier diagrama consta de una secuencia lineal de exactamente $r$ estrellas y $n - 1$ barras, sumando un total de $n + r - 1$ posiciones. Una vez que elegimos qué $r$ posiciones ocuparán las estrellas (o equivalentemente, qué $n - 1$ posiciones ocuparán las barras), el diagrama queda unívocamente determinado. Como las estrellas son indistinguibles entre sí y las barras también, el número total de soluciones enteras no negativas es:

$$N_{\text{sol}} = \binom{n + r - 1}{r} = \binom{n + r - 1}{n - 1}$$

> [!EXAMPLE] **Ejemplo 7:** Asignación de Recursos Compartidos con Mínimo Garantizado
> 
> Demuestre analíticamente de cuántas formas se pueden asignar $15$ peticiones idénticas de base de datos a $n = 4$ servidores de réplica disponibles si cada servidor debe recibir al menos $2$ peticiones para evitar subutilización.

En este caso de estudio modelamos un problema de reparto de carga donde los elementos distribuidos son indistinguibles entre sí, pero los destinos son identificables y están sujetos a una cota inferior de asignación. Se busca hallar el número total de repartos válidos reduciendo la restricción mínima mediante un cambio de variable para aplicar el método de estrellas y barras (combinaciones con repetición).

1. Definimos $x_i$ como el número de peticiones asignadas al servidor $i$ ($i = 1, 2, 3, 4$) y formulamos el problema como el conteo de soluciones enteras de una ecuación diofántica sujeta a la restricción de mínimo garantizado.

$$x_1 + x_2 + x_3 + x_4 = 15, \quad \text{sujeto a } x_i \ge 2 \quad \forall i \in \{1, 2, 3, 4\}$$

2. Preasignamos deterministamente $2$ peticiones a cada uno de los $4$ servidores (consumiendo $4 \cdot 2 = 8$ peticiones del inventario) mediante el cambio de variable $y_i = x_i - 2$, de manera que las nuevas incógnitas sean enteras no negativas ($y_i \ge 0$).

$$(y_1 + 2) + (y_2 + 2) + (y_3 + 2) + (y_4 + 2) = 15 \implies y_1 + y_2 + y_3 + y_4 = 15 - 8 = 7$$

3. Aplicamos el modelo de estrellas y barras para distribuir sin restricciones las $r' = 7$ peticiones libres restantes entre los $n = 4$ servidores (lo cual requiere $4 - 1 = 3$ barras separadoras y $7$ estrellas) y simplificamos usando simetría combinatoria.

$$N_{\text{sol}} = \binom{4 + 7 - 1}{7} = \binom{10}{7} = \binom{10}{3} = \frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1} = 120 \text{ formas de asignación}$$

## 3.3. Permutaciones con Elementos Indistinguibles y Fórmula Multinomial

Un último caso fundamental aparece cuando se ordena una secuencia completa de $n$ elementos con inventario fijo, pero el conjunto no está formado por $n$ objetos distintos, sino por $k$ clases de objetos idénticos entre sí. Si se calcula $n!$, el modelo tratará como diferentes dos secuencias obtenidas al intercambiar copias idénticas de la misma clase.

> [!QUOTE] **Teorema 8:** Coeficiente Multinomial (Permutaciones con Grupos Indistinguibles)
> Dado un conjunto de $n$ elementos particionado en $k$ grupos de objetos indistinguibles de tamaños $n_1, n_2, \dots, n_k$ tales que $\sum_{i=1}^k n_i = n$, el número de permutaciones distinguibles de los $n$ elementos es:
> 
> $$\binom{n}{n_1, n_2, \dots, n_k} = \frac{n!}{n_1! \cdot n_2! \cdots n_k!}$$

La demostración aplica la **regla de la división** de forma iterativa. Si etiquetáramos artificialmente a todos los objetos con subíndices únicos para hacerlos distinguibles, existirían $n!$ ordenamientos lineales. Sin embargo, los $n_1$ clones del primer grupo pueden permutar entre sí de $n_1!$ maneras sin alterar la secuencia observable; por cada una de ellas, los $n_2$ clones del segundo grupo permutan de $n_2!$ formas sin efecto visible, y así hasta el grupo $k$. Por el principio multiplicativo, cada secuencia distinguible aparece repetida exactamente $d = n_1! \cdot n_2! \cdots n_k!$ veces en el conteo bruto, por lo que dividir $n!$ entre dicho producto entrega el total exacto.

> [!EXAMPLE] **Ejemplo 8:** Transmisión de Tramas de Control en Protocolos de Enlace
> 
> Un protocolo de enlace envía una ráfaga de $12$ paquetes de control: $5$ paquetes ACK, $4$ paquetes NACK y $3$ paquetes SYN, todos idénticos entre sí según su tipo. Calcule el número total de secuencias distinguibles que pueden recibirse en el nodo destino.

Al analizar ráfagas de tráfico en protocolos de red, el orden de llegada de los comandos altera el estado del receptor, pero intercambiar dos paquetes del mismo tipo produce exactamente la misma secuencia observable. La finalidad de este ejercicio es cuantificar con exactitud el espacio de secuencias distinguibles aplicando la fórmula multinomial para descontar las permutaciones internas de cada clase de paquetes idénticos.

1. Identificamos los tamaños de los $k = 3$ grupos de tramas indistinguibles ($n_1 = 5$ ACK, $n_2 = 4$ NACK y $n_3 = 3$ SYN) y verificamos que su suma coincide con la longitud total de la ráfaga.

$$n = n_1 + n_2 + n_3 = 5 + 4 + 3 = 12$$

2. Planteamos el coeficiente multinomial dividiendo las $12!$ permutaciones brutas entre el producto de las simetrías internas ($n_1! \cdot n_2! \cdot n_3!$) de los paquetes idénticos de cada tipo.

$$\binom{12}{5, 4, 3} = \frac{12!}{5! \cdot 4! \cdot 3!}$$

3. Evaluamos los factoriales y efectuamos la división para determinar el número exacto de secuencias de control distinguibles en el nodo destino.

$$\binom{12}{5, 4, 3} = \frac{479.001.600}{120 \cdot 24 \cdot 6} = \frac{479.001.600}{17.280} = 27.720 \text{ secuencias distinguibles}$$

# 4. Síntesis Taxonómica y Compromisos de Ingeniería Computacional

Elegir el modelo combinatorio correcto exige cruzar las dos variables de decisión del problema (orden y repetición) y trasladar la fórmula resultante a una implementación numérica segura en hardware.

## 4.1. Cuadro Comparativo de Modelos Combinatorios

La siguiente tabla consolida las seis estructuras de enumeración desarrolladas junto con su dominio directo en ingeniería de sistemas:

| **Tipo de Arreglo** | **¿Importa el Orden?** | **¿Permite Repetición?** | **Modelo Matemático Formal** | **Dominio de Aplicación** |
| --- | --- | --- | --- | --- |
| **Permutaciones Simples** | Sí | No | $P_n = n!$ | Orden de ejecución en planificador de CPU mono-hilo. |
| **Variaciones ($r$-Permutaciones)** | Sí | No | $V_n^r = \frac{n!}{(n-r)!}$ | Asignación de roles jerárquicos (Líder, Réplica 1, Réplica 2). |
| **Combinaciones Simples** | No | No | $C_n^r = \binom{n}{r} = \frac{n!}{r!(n-r)!}$ | Selección de nodos de un clúster para balanceo simétrico. |
| **Variaciones con Repetición** | Sí | Sí | $VR_n^r = n^r$ | Generación de cadenas binarias o contraseñas de tamaño $r$. |
| **Combinaciones con Repetición** | No | Sí | $CR_n^r = \binom{n+r-1}{r}$ | Distribución de $r$ hilos idénticos entre $n$ núcleos de cómputo. |
| **Permutación Multinomial** | Sí | No (stock fijo) | $\frac{n!}{n_1! n_2! \dots n_k!}$ | Secuencias de tramas de red con tipos de paquetes repetidos. |

## 4.2. Desbordamiento Aritmético (‘Overflow’) y Cómputo Iterativo Entrelazado

Trasladar directamente la expresión cerrada $\binom{n}{r} = \frac{n!}{r!(n-r)!}$ a código de bajo nivel constituye un error crítico de ingeniería numérica. En arquitecturas de $64\text{ bits}$, el máximo entero sin signo representable (`uint64_t`) es $2^{64} - 1 = 18.446.744.073.709.551.615 \approx 1,84 \times 10^{19}$. Mientras que $20! \approx 2,43 \times 10^{18}$ cabe en un registro de $64\text{ bits}$, el siguiente término $21! \approx 5,11 \times 10^{19}$ supera ese límite y provoca un desbordamiento aritmético (‘overflow’), incluso cuando el resultado final $\binom{21}{2} = 210$ es diminuto.

Para evitar la saturación prematura de los registros del procesador y reducir el tiempo de ejecución, se aplican dos optimizaciones simultáneas:

1. **Reducción por Simetría:** Antes de iniciar el bucle, se evalúa si $r > n - r$; en caso afirmativo, se reemplaza $r \leftarrow n - r$ invocando $\binom{n}{r} = \binom{n}{n-r}$, lo que acota el número de iteraciones a $\lfloor n/2 \rfloor$.


2. **Multiplicación y División Entrelazadas:** En lugar de acumular todo el numerador antes de dividir, se reescribe el coeficiente binomial como un producto incremental de fracciones exactas:

$$\binom{n}{r} = \prod_{i=1}^r \frac{n - i + 1}{i}$$

En cada paso $i$, el acumulador parcial corresponde exactamente a $\binom{n}{i}$, un número entero garantizado por la teoría combinatoria; por ello, multiplicar primero por $(n - i + 1)$ y dividir inmediatamente entre $i$ mantiene el resultado intermedio en la mínima magnitud posible en cada ciclo.

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