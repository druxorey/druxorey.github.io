---
created: 2026-02-24 20:34
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
> Un planificador «batch» en un procesador de un solo núcleo recibe $n = 6$ tareas independientes ($T_1, T_2, T_3, T_4, T_5, T_6$) que deben ejecutarse secuencialmente hasta completarse sin interrupciones. ¿Cuántas trazas de ejecución distintas puede generar el planificador?
> **Solución:**
> 
> $$P_6 = 6! = 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 720 \text{ trazas de ejecución}$$

**Paso 1:** Identificamos que todas las tareas deben ejecutarse ($r = n = 6$) y que alterar el orden modifica los tiempos de espera y finalización del sistema, por lo que el orden es estricto.

**Paso 2:** Aplicamos el principio multiplicativo sobre las $6$ ranuras temporales de la cola de ejecución, reduciendo en una unidad las tareas disponibles tras cada asignación hasta obtener $720$ ordenamientos posibles.

## 1.2. Variaciones o $r$-Permutaciones de Subconjuntos

En muchas arquitecturas de ingeniería, el catálogo de recursos disponibles contiene $n$ elementos distintos, pero el sistema únicamente dispone de $r$ ranuras o posiciones que llenar, con $0 \le r \le n$. En este escenario, los $n - r$ elementos no seleccionados quedan fuera del arreglo final.

> [!QUOTE] **Teorema 2:** Variaciones ($r$-Permutaciones sin Repetición)
> Dados enteros $n$ y $r$ tales que $0 \le r \le n$, el número de arreglos ordenados de longitud $r$ que pueden formarse extrayendo elementos sin reposición de un conjunto total de $n$ objetos distintos (denotado $V_n^r$ o $P_n^r$) es:
> 
> $$V_n^r = P_n^r = \frac{n!}{(n - r)!} = n \cdot (n - 1) \cdot (n - 2) \cdots (n - r + 1)$$

La deducción sigue la misma lógica de llenado de casillas, pero el proceso se detiene exactamente al completar la casilla número $r$, donde aún quedan $n - (r - 1) = n - r + 1$ opciones disponibles. Para compactar este producto truncado en notación factorial, se multiplica y divide simultáneamente por $(n - r)!$, completando la cadena descendente hasta $1$ en el numerador y cancelando los factores de los elementos sobrantes en el denominador. Nótese que en parte de la literatura del curso esta expresión se escribe como $P_M^N = \frac{M!}{(M - N)!}$, donde $M$ representa el tamaño de la población y $N$ el tamaño de la muestra ordenada.

> [!EXAMPLE] **Ejemplo 2:** Asignación de Roles Jerárquicos en un Clúster
> Una arquitectura de alta disponibilidad cuenta con $n = 10$ servidores físicos idénticos en hardware, pero distintos por su dirección IP. Para desplegar un servicio replicado se requiere asignar exactamente $r = 3$ servidores a tres roles jerárquicos exclusivos: «Nodo Líder», «Réplica Síncrona 1» y «Réplica Síncrona 2». ¿Cuántas topologías de despliegue distintas existen?
> 
> **Solución:**
> 
> $$V_{10}^3 = P_{10}^3 = \frac{10!}{(10 - 3)!} = \frac{10!}{7!} = 10 \cdot 9 \cdot 8 = 720 \text{ topologías posibles}$$

**Paso 1:** Reconocemos que la jerarquía de red hace que asignar el servidor $A$ como Líder y el $B$ como Réplica 1 sea funcionalmente distinto a invertir sus roles, confirmando que el orden importa y no hay repetición.

**Paso 2:** Multiplicamos las $10$ opciones para el Nodo Líder por las $9$ restantes para la Réplica 1 y las $8$ disponibles para la Réplica 2, obteniendo $720$ configuraciones válidas.

# 2. Selecciones sin Orden y Estructura de los Coeficientes Binomiales

El enfoque de variaciones falla cuando el sistema trata como equivalentes a dos arreglos que contienen exactamente los mismos elementos en distinto orden. Si un balanceador de carga selecciona tres nodos para almacenar fragmentos de un archivo sin asignarles jerarquía, elegir los nodos $\{A, B, C\}$ produce exactamente la misma topología que elegir $\{C, B, A\}$. Contar con $V_n^r$ sobreestima el espacio real porque registra cada subconjunto múltiples veces.

## 2.1. Combinaciones Simples y Deducción mediante la Regla de la División

Para eliminar la redundancia generada por el orden interno de los elementos seleccionados, se recurre a la **regla de la división**, que colapsa clases de equivalencia de tamaño uniforme.

> [!QUOTE] **Teorema 3:** Combinaciones Simples (Coeficiente Binomial)
> Para enteros $n$ y $r$ con $0 \le r \le n$, el número de subconjuntos desordenados de tamaño $r$ que pueden extraerse de un conjunto de $n$ elementos distintos está dado por el coeficiente binomial:
> 
> $$C_n^r = \binom{n}{r} = \frac{n!}{r!(n - r)!}$$

La deducción formal parte de observar que todo arreglo ordenado de $r$ elementos ($V_n^r$) puede construirse en dos etapas secuenciales mediante el principio multiplicativo: primero se elige el subconjunto desordenado de $r$ elementos de $\binom{n}{r}$ maneras posibles, y luego se ordenan internamente esos $r$ elementos de $P_r = r!$ formas distintas. Esto establece la identidad fundamental:

$$V_n^r = \binom{n}{r} \cdot r!$$

Al aplicar la regla de la división —dividiendo el total de variaciones ordenadas entre la multiplicidad $d = r!$ de permutaciones internas equivalentes— se purga el orden y emerge la expresión factorial cerrada:

$$\binom{n}{r} = \frac{V_n^r}{r!} = \frac{\frac{n!}{(n - r)!}}{r!} = \frac{n!}{r!(n - r)!}$$

> [!EXAMPLE] **Ejemplo 3:** Selección Simétrica de Nodos para Balanceo de Carga
> De un grupo de $n = 10$ servidores disponibles en un centro de datos, un balanceador simétrico debe seleccionar un subconjunto de $r = 3$ nodos para distribuir copias idénticas de una caché de lectura sin distinción de jerarquía. Calcule cuántos subconjuntos de servidores pueden formarse.
> 
> **Solución:**
> 
> $$C_{10}^3 = \binom{10}{3} = \frac{10!}{3!(10 - 3)!} = \frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1} = \frac{720}{6} = 120 \text{ subconjuntos}$$

**Paso 1:** Calculamos primero las $V_{10}^3 = 720$ secuencias ordenadas de tres servidores.

**Paso 2:** Como cada trío de servidores puede permutarse internamente de $3! = 6$ maneras que representan el mismo grupo de caché, dividimos $720 / 6$ para obtener los $120$ subconjuntos únicos.

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

Intuitivamente, la **simetría combinatoria** establece que elegir los $r$ elementos que entran en un subconjunto equivale de manera biyectiva a elegir los $n - r$ elementos que quedan excluidos de él. Por su parte, la **identidad de Pascal** descompone la elección de $k$ elementos respecto a un elemento distinguido (llamémoslo $a_1$): todo subconjunto de tamaño $k$ o bien excluye a $a_1$ (obligando a elegir los $k$ elementos entre los $n - 1$ restantes), o bien incluye a $a_1$ (reduciendo la tarea a elegir $k - 1$ compañeros entre los $n - 1$ restantes).

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
> Un sistema de auditoría debe evaluar todas las combinaciones posibles de $r = 47$ paquetes seleccionados de un lote de $n = 52$ tramas capturadas. Determine el número de combinaciones aprovechando la simetría combinatoria.
> 
> **Solución:**
> 
> $$\binom{52}{47} = \binom{52}{52 - 47} = \binom{52}{5} = \frac{52 \cdot 51 \cdot 50 \cdot 49 \cdot 48}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = 2.598.960 \text{ combinaciones}$$

**Paso 1:** En lugar de expandir $47$ factores en el numerador y denominador, aplicamos $\binom{52}{47} = \binom{52}{5}$ identificando que elegir $47$ tramas equivale a elegir las $5$ que se descartan.

**Paso 2:** Reducimos el cálculo a solo $5$ multiplicaciones y divisiones, obteniendo $2.598.960$ configuraciones idénticas a las manos de póker de cinco cartas.

## 2.3. Teorema del Binomio de Newton

La interpretación combinatoria de $\binom{n}{k}$ proporciona una demostración directa de la expansión algebraica de potencias de un binomio, conectando el conteo discreto con el álgebra polinómica y la distribución binomial de probabilidad.

> [!QUOTE] **Teorema 5:** Teorema del Binomio
> Para cualesquiera números reales (o elementos de un anillo conmutativo) $a, b$ y todo entero no negativo $n \in \mathbb{N}_0$, se verifica:
> 
> $$(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}$$

Al expandir el producto de $n$ factores idénticos $(a + b)(a + b)\cdots(a + b)$, cada término elemental resultante se forma eligiendo exactamente una variable ($a$ o $b$) de cada uno de los $n$ paréntesis. Para obtener el monomio $a^k b^{n-k}$, es necesario seleccionar la variable $a$ en exactamente $k$ paréntesis y la variable $b$ en los $n - k$ paréntesis restantes. Como la multiplicación es conmutativa, el número de veces que aparece el término $a^k b^{n-k}$ coincide exactamente con el número de formas de elegir $k$ posiciones entre los $n$ factores sin importar el orden, es decir, $\binom{n}{k}$. Evaluando esta identidad en $a = 1, b = 1$ se demuestra inmediatamente que la cardinalidad del conjunto potencia de un conjunto de $n$ elementos es $\sum_{k=0}^n \binom{n}{k} = 2^n$.

> [!EXAMPLE] **Ejemplo 5:** Conteo de Cadenas Binarias por Peso de Hamming
> ¿Cuántas cadenas binarias de longitud $n = 8$ bits contienen exactamente $k = 3$ bits en estado lógico $1$ (peso de Hamming igual a $3$)?
> 
> **Solución:**
> 
> $$\text{Cadenas con } k=3 \text{ unos} = \binom{8}{3} = \frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = 56 \text{ cadenas}$$

**Paso 1:** Asociamos cada posición de la palabra de $8\text{ bits}$ a un factor del binomio $(x + 1)^8$, donde elegir $x$ equivale a fijar un bit en $1$ y elegir $1$ equivale a fijar un bit en $0$.

**Paso 2:** El coeficiente que acompaña a $x^3$ en la expansión es $\binom{8}{3} = 56$, cuantificando las palabras de $8\text{ bits}$ con exactamente tres unos.

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
> Un sistema de autenticación exige contraseñas de longitud exacta $r = 5$ caracteres construidas exclusivamente sobre un alfabeto reducido de $n = 16$ símbolos hexadecimales ($\{0\text{--}9, \text{A--F}\}$), permitiendo repetir símbolos. Determine la cardinalidad del espacio de búsqueda para un ataque de fuerza bruta.
> 
> **Solución:**
> 
> $$VR_{16}^5 = 16^5 = (2^4)^5 = 2^{20} = 1.048.576 \text{ contraseñas posibles}$$

**Paso 1:** Verificamos que el orden distingue contraseñas distintas («A1B2C» $\neq$ «C2B1A») y que los símbolos pueden repetirse («AAAAA» es válida).

**Paso 2:** Multiplicamos las $16$ opciones independientes a lo largo de las $5$ posiciones, obteniendo $2^{20} = 1.048.576$ claves posibles.

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

### 3.2.2. Caso de Estudio: Asignación de Peticiones con Cota Mínima en Réplicas

> [!EXAMPLE] **Ejemplo 7:** Asignación de Recursos Compartidos con Mínimo Garantizado
> Demuestre analíticamente de cuántas formas se pueden asignar $15$ peticiones idénticas de base de datos a $n = 4$ servidores de réplica disponibles si cada servidor debe recibir al menos $2$ peticiones para evitar subutilización.
> 
> **Solución:**
> 
> Sea $x_i$ el número de peticiones asignadas al servidor $i$ ($i = 1, 2, 3, 4$). El problema equivale a hallar el número de soluciones enteras del sistema:
> 
> $$x_1 + x_2 + x_3 + x_4 = 15, \quad \text{sujeto a } x_i \ge 2 \quad \forall i \in \{1, 2, 3, 4\}$$
> 
> Definimos el cambio de variable $y_i = x_i - 2$, de modo que $y_i \ge 0$ para todo $i$. Sustituyendo $x_i = y_i + 2$ en la ecuación de balance:
> 
> $$(y_1 + 2) + (y_2 + 2) + (y_3 + 2) + (y_4 + 2) = 15 \implies y_1 + y_2 + y_3 + y_4 = 15 - 8 = 7$$
> 
> Aplicando el modelo de estrellas y barras con $n = 4$ servidores y $r' = 7$ peticiones libres restantes:
> 
> $$N_{\text{sol}} = \binom{4 + 7 - 1}{7} = \binom{10}{7} = \binom{10}{3} = \frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1} = 120 \text{ formas de asignación}$$

**Paso 1:** Como las peticiones son idénticas entre sí y los servidores son entidades distinguibles, preasignamos deterministamente $2$ peticiones a cada uno de los $4$ servidores, consumiendo $4 \cdot 2 = 8$ peticiones del inventario para satisfacer la restricción $x_i \ge 2$.

**Paso 2:** Reducimos el problema a distribuir sin restricciones ($y_i \ge 0$) las $r' = 7$ peticiones sobrantes entre los $n = 4$ servidores, lo que requiere $4 - 1 = 3$ barras separadoras y $7$ estrellas, generando $\binom{10}{3} = 120$ repartos posibles.

## 3.3. Permutaciones con Elementos Indistinguibles y Fórmula Multinomial

Un último caso fundamental aparece cuando se ordena una secuencia completa de $n$ elementos con inventario fijo, pero el conjunto no está formado por $n$ objetos distintos, sino por $k$ clases de objetos idénticos entre sí. Si se calcula $n!$, el modelo tratará como diferentes dos secuencias obtenidas al intercambiar copias idénticas de la misma clase.

> [!QUOTE] **Teorema 8:** Coeficiente Multinomial (Permutaciones con Grupos Indistinguibles)
> Dado un conjunto de $n$ elementos particionado en $k$ grupos de objetos indistinguibles de tamaños $n_1, n_2, \dots, n_k$ tales que $\sum_{i=1}^k n_i = n$, el número de permutaciones distinguibles de los $n$ elementos es:
> 
> $$\binom{n}{n_1, n_2, \dots, n_k} = \frac{n!}{n_1! \cdot n_2! \cdots n_k!}$$

La demostración aplica la **regla de la división** de forma iterativa. Si etiquetáramos artificialmente a todos los objetos con subíndices únicos para hacerlos distinguibles, existirían $n!$ ordenamientos lineales. Sin embargo, los $n_1$ clones del primer grupo pueden permutar entre sí de $n_1!$ maneras sin alterar la secuencia observable; por cada una de ellas, los $n_2$ clones del segundo grupo permutan de $n_2!$ formas sin efecto visible, y así hasta el grupo $k$. Por el principio multiplicativo, cada secuencia distinguible aparece repetida exactamente $d = n_1! \cdot n_2! \cdots n_k!$ veces en el conteo bruto, por lo que dividir $n!$ entre dicho producto entrega el total exacto.

### 3.3.1. Caso de Estudio: Secuencias de Tramas de Control en Protocolos de Enlace

> [!EXAMPLE] **Ejemplo 8:** Transmisión de Tramas de Control en Protocolos de Enlace
> Un protocolo de enlace envía una ráfaga de $12$ paquetes de control: $5$ paquetes ACK, $4$ paquetes NACK y $3$ paquetes SYN, todos idénticos entre sí según su tipo. Calcule el número total de secuencias distinguibles que pueden recibirse en el nodo destino.
> 
> **Solución:**
> 
> Verificamos que la suma de subgrupos iguala el total de paquetes: $n = 5 + 4 + 3 = 12$. Aplicando la fórmula multinomial:
> 
> $$\binom{12}{5, 4, 3} = \frac{12!}{5! \cdot 4! \cdot 3!} = \frac{479.001.600}{120 \cdot 24 \cdot 6} = \frac{479.001.600}{17.280} = 27.720 \text{ secuencias distinguibles}$$

**Paso 1:** Identificamos que el orden de llegada de los comandos altera el estado de la máquina de protocolo, pero intercambiar dos tramas ACK entre sí no produce un mensaje nuevo.

**Paso 2:** Dividimos las $12!$ permutaciones brutas entre las simetrías internas de cada tipo de trama ($5! \cdot 4! \cdot 3! = 17.280$), reduciendo el espacio de estados efectivos a $27.720$ secuencias posibles.

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
> 
> - **Meyer, Paul L.** _Probabilidad y Aplicaciones Estadísticas_ (Edición revisada). Addison-Wesley Iberoamericana. Capítulo 1 («Introducción a la probabilidad») y Capítulo 2 («Espacios muestrales finitos», secciones «Métodos de enumeración», «Combinaciones» y «Permutaciones»).
>     
> - **Feller, William.** _An Introduction to Probability Theory and Its Applications_, Vol. I (3.ª ed.). John Wiley & Sons, Inc., Nueva York, 1968. Capítulo 2 («Elements of Combinatorial Analysis»).
>     
> - **Riordan, John.** _An Introduction to Combinatorial Analysis_. Dover Publications, Mineola, Nueva York, 2002.
>     
> - **Parzen, Emanuel.** _Modern Probability Theory and Its Applications_. John Wiley & Sons, Inc., Nueva York, 1960.
>     
> - **Lipschutz, Seymour.** _Probabilidad_. McGraw-Hill, México, 1970.
>     
> - **Universidad Central de Venezuela (UCV), Facultad de Ciencias, Escuela de Computación.** _Probabilidad y Estadística: Introducción a la Probabilidad (G01) y Práctica Nº 0: Repaso de Combinatoria y Probabilidades (A00)_. Caracas, Venezuela, 2023.
