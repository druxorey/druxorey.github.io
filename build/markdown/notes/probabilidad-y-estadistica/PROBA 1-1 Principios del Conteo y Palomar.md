---
created: 2026-02-18 18:53
title: Principios del Conteo y Palomar
semester: 4
subject:
  - "[[PROBA 0-0 Nota Informativa|Probabilidad y Estadística]]"
unit: 1
status: done
---

<h1 id="main-title"  align="center"> Principios del Conteo y Palomar </h1>

> [!TLDR] SÍNTESIS 
> Los **principios del conteo** determinan analíticamente la **cardinalidad** de un **espacio muestral discreto** evitando la búsqueda exhaustiva. Mediante las reglas de la **suma**, del **producto** y de la **división**, junto con el principio de **inclusión-exclusión** y el **principio del palomar**, estas herramientas fundamentan el **modelo clásico de probabilidad**, dimensionan espacios de estados y establecen cotas de colisión en sistemas computacionales.

En el diseño de algoritmos, protocolos de red y sistemas criptográficos, conocer de antemano cuántas configuraciones posibles admite un sistema resulta indispensable para evaluar su viabilidad técnica y calcular probabilidades bajo incertidumbre. Sin embargo, listar una por una todas las configuraciones de un sistema real pronto se vuelve inviable: a medida que crecen los parámetros de entrada, el universo de combinaciones posibles se expande hasta superar la capacidad de almacenamiento y procesamiento de cualquier arquitectura física. Surge así la necesidad de contar de forma indirecta y estructurada, deduciendo el tamaño exacto de un conjunto de resultados mediante leyes lógicas y algebraicas en lugar de recorrerlo elemento por elemento.

# 1. El Espacio Muestral Discreto y la Medición Combinatoria

Para evaluar la incertidumbre de un proceso o el costo de explorar sus estados, primero es necesario delimitar con rigor matemático el universo completo de resultados posibles. Si los límites del sistema son ambiguos, cualquier cálculo posterior arrastrará omisiones o duplicaciones.

## 1.1. Definición y Cardinalidad del Espacio Muestral

El enfoque intuitivo para analizar un experimento consiste en anotar los resultados observables a medida que ocurren. El obstáculo surge cuando no existe garantía de haber contemplado todas las posibilidades ni de que los resultados registrados sean mutuamente independientes entre sí. Para eliminar esta ambigüedad, la teoría de la probabilidad formaliza el concepto de espacio muestral discreto.

> [!QUOTE] **Definición Formal 1:** Espacio Muestral Discreto y Cardinalidad
> Dado un experimento no determinístico, se define el **espacio muestral** $\Omega$ como el conjunto de todos sus resultados elementales posibles $\omega$, formulados de manera que sean mutuamente excluyentes y colectivamente exhaustivos.
> 
> Bajo el **modelo clásico de Laplace** (equiprobabilidad de resultados elementales, donde $\mathbb{P}(\omega) = 1/\vert{}\Omega\vert{}$ para todo $\omega \in \Omega$), la probabilidad de cualquier evento $E \subseteq \Omega$ queda determinada por la razón de cardinalidades:
> 
> $$\mathbb{P}(E) = \frac{\vert{}E\vert{}}{\vert{}\Omega\vert{}}$$

Es decir, el espacio muestral es el conjunto de todos los resultados posibles de un experimento, donde cada elemento representa un desenlace único y excluyente. La cardinalidad es simplemente el número total de elementos que contiene ese espacio muestral.

> [!EXAMPLE] **Ejemplo 1:** Espacio Muestral de dos Lanzamientos de Moneda
> 
> Se lanzan dos monedas consecutivas. Determine la cardinalidad del espacio muestral $\Omega$ y la probabilidad equiprobable del evento $E$: «obtener al menos una cara ($C$)».

En este ejercicio analizamos un experimento aleatorio discreto y finito compuesto por el lanzamiento secuencial de dos monedas equilibradas. Lo que se busca es formalizar el conjunto de todos los desenlaces posibles de manera que sean mutuamente excluyentes y colectivamente exhaustivos, evitando omisiones o ambigüedades al registrar los resultados.

A partir de esa delimitación del espacio muestral, se pide cuantificar su tamaño total y aislar los casos favorables al evento de obtener al menos una cara, para finalmente calcular su probabilidad aplicando la razón de cardinalidades del modelo clásico de Laplace.

1. Definimos cada resultado elemental $\omega$ como un par ordenado $(m_1, m_2)$ que indica el resultado de la primera y la segunda moneda (cara $C$ o sello $S$), listamos el espacio muestral completo y contamos el total de combinaciones admisibles.

$$\Omega = \{(C,C), (C,S), (S,C), (S,S)\} \implies \lvert \Omega \rvert = 4$$

2. Aislamos el subconjunto $E \subseteq \Omega$ conformado por todos los resultados elementales que contienen al menos una cara ($C$) y determinamos su cardinalidad.

$$E = \{(C,C), (C,S), (S,C)\} \implies \lvert E \rvert = 3$$

3. Aplicamos la regla de Laplace dividiendo la cardinalidad del evento favorable $\lvert E \rvert$ entre la cardinalidad del espacio muestral $\lvert \Omega \rvert$, obteniendo la probabilidad exacta.

$$\mathbb{P}(E) = \frac{\lvert E \rvert}{\lvert \Omega \rvert} = \frac{3}{4} = 0{,}75$$

## 1.2. Búsqueda Exhaustiva frente a Cómputo Combinatorio

Cuando se diseñan sistemas de software que operan sobre espacios muestrales de gran escala (como generadores de claves criptográficas, analizadores de consultas o simuladores de estados), calcular $\vert{}\Omega\vert{}$ plantea una disyuntiva directa en eficiencia algorítmica:

- **Búsqueda exhaustiva (fuerza bruta):** Consiste en instanciar, almacenar y recorrer explícitamente cada resultado elemental $\omega \in \Omega$ mediante iteración o recursión. Este enfoque exige una complejidad temporal y espacial de orden $O(\vert{}\Omega\vert{})$. Cuando $\vert{}\Omega\vert{}$ crece de forma exponencial (como $2^n$) o factorial ($n!$), enumerar las instancias agota la memoria disponible y bloquea el procesador en tiempos impracticables.

- **Cómputo combinatorio analítico:** Consiste en descomponer la estructura lógica del problema y calcular $\vert{}\Omega\vert{}$ mediante fórmulas cerradas (sumas, productos, potencias o factoriales) sin materializar los elementos en memoria. Este método reduce la evaluación del tamaño del espacio a una complejidad temporal $O(1)$ o $O(k)$ (donde $k$ es el número de etapas o conjuntos involucrados), permitiendo validar la tratabilidad de un algoritmo antes de asignar recursos de hardware.

# 2. Principios Aditivo y Multiplicativo de Enumeración

Para evitar la enumeración exhaustiva de orden $O(\vert{}\Omega\vert{})$, la combinatoria descompone un problema complejo en subproblemas elementales. La forma en que se combinan las cardinalidades de esos subproblemas depende de si las decisiones representan alternativas mutuamente excluyentes o etapas sucesivas de un mismo proceso.

## 2.1. Regla de la Suma y Particiones Disjuntas

La premisa más directa de conteo surge cuando una tarea puede completarse eligiendo una única opción entre varios grupos de alternativas que no tienen elementos en común. Si dos grupos compartieran alguna opción, sumar sus tamaños directamente produciría un conteo inflado. Por ello, la validez de la adición simple exige que los conjuntos formen una partición disjunta.

> [!QUOTE] **Teorema 1:** Regla de la Suma (Uniones Disjuntas)
> Sean $A_1, A_2, \dots, A_m$ conjuntos finitos mutuamente excluyentes dos a dos, es decir, tales que $A_i \cap A_j = \emptyset$ para todo $i \neq j$. La cardinalidad de su unión global es igual a la suma aritmética de sus cardinalidades individuales:
> 
> $$\left\vert{} \bigcup_{i=1}^m A_i \right\vert{} = \sum_{i=1}^m \vert{}A_i\vert{} = \vert{}A_1\vert{} + \vert{}A_2\vert{} + \dots + \vert{}A_m\vert{}$$

Si disponemos de varias cajas completamente separadas y debemos extraer un único objeto eligiendo primero qué caja abrir, el número total de objetos distintos que podemos obtener es simplemente la suma de los contenidos de cada caja. Como ningún objeto está duplicado en dos cajas a la vez, cada elección conduce a un resultado único sin riesgo de repetición.

> [!EXAMPLE] **Ejemplo 2:** Selección de Representantes en un Comité Académico
> 
> Un departamento universitario debe elegir a un único representante para el consejo directivo. El grupo docente cuenta con $37$ profesores y la carrera tiene $83$ estudiantes inscritos, asumiendo que ninguna persona pertenece simultáneamente a ambos grupos. Determine el número total de selecciones posibles.

Este ejercicio plantea una tarea de selección simple en la que debe escogerse a una sola persona eligiendo entre dos colectivos académicos distintos. La finalidad es aplicar la regla de la suma sobre conjuntos finitos, verificando previamente la condición de disjunción para asegurar que ningún candidato sea contabilizado dos veces.

1. Identificamos el conjunto $A_1$ de profesores y el conjunto $A_2$ de estudiantes con sus respectivas cardinalidades, y verificamos la hipótesis de exclusión mutua que garantiza que forman una partición disjunta.

$$\lvert A_1 \rvert = 37, \qquad \lvert A_2 \rvert = 83, \qquad A_1 \cap A_2 = \emptyset$$

2. Aplicamos la regla de la suma para uniones disjuntas adicionando ambas cardinalidades, lo que entrega el número total de formas distintas de ocupar la vacante sin solapamientos.

$$\lvert A_1 \cup A_2 \rvert = \lvert A_1 \rvert + \lvert A_2 \rvert = 37 + 83 = 120\text{ candidatos posibles}$$

## 2.2. Principio Multiplicativo y Decisiones en Cascada

A diferencia de la regla de la suma (donde se escoge una única vía entre varias opciones excluyentes), muchos procesos computacionales exigen completar una secuencia ordenada de pasos independientes. En este escenario, sumar las opciones de cada etapa fallaría porque el resultado final no proviene de una sola etapa, sino de la combinación encadenada de todas ellas.

> [!QUOTE] **Teorema 2:** Principio Multiplicativo (Regla del Producto)
> Si un procedimiento general se descompone en una secuencia de $k$ etapas sucesivas, donde la primera etapa puede realizarse de $n_1$ maneras y, por cada una de estas, la segunda etapa puede ejecutarse de $n_2$ maneras, y así sucesivamente hasta la $k$-ésima etapa con $n_k$ maneras independientes de las elecciones previas, entonces el procedimiento completo puede realizarse de:
> 
> $$\prod_{i=1}^k n_i = n_1 \cdot n_2 \cdots n_k \quad \text{formas distintas}$$
> 
> En términos de teoría de conjuntos, la cardinalidad del producto cartesiano de $k$ conjuntos finitos $A_1, A_2, \dots, A_k$ equivale al producto de sus cardinalidades individuales:
> 
> $$\vert{}A_1 \times A_2 \times \dots \times A_k\vert{} = \prod_{i=1}^k \vert{}A_i\vert{}$$

Esta operación se visualiza de forma natural como un **árbol de decisión** que crece desde una raíz inicial. En el primer nivel, el árbol se divide en $n_1$ ramas; de cada una de esas ramas brotan $n_2$ subramas en el segundo nivel, y el proceso continúa en cascada hasta alcanzar el nivel $k$. Contar el total de hojas terminales del árbol equivale a multiplicar el factor de ramificación de cada nivel.

> [!EXAMPLE] **Ejemplo 3:** Cadenas Binarias y Cardinalidad del Conjunto Potencia
> 
> Determine cuántas cadenas binarias de longitud exacta $L = 7$ bits existen en memoria y demuestre mediante el mismo principio que un conjunto finito $S$ posee exactamente $2^{\lvert S \rvert}$ subconjuntos.

En este ejercicio se emplea el principio multiplicativo para resolver dos problemas estructuralmente equivalentes: primero, cuantificar el universo de palabras binarias de un tamaño fijo en memoria; y segundo, generalizar ese mismo razonamiento hacia la teoría de conjuntos para demostrar la fórmula de la cardinalidad del conjunto potencia.

Lo que se busca es modelar tanto los bits de una cadena como la pertenencia de los elementos a un subconjunto mediante una cascada de decisiones binarias independientes, evitando cualquier intento de enumeración exhaustiva.

1. Modelamos la cadena de $L = 7$ bits como una secuencia de $7$ casillas ordenadas donde cada posición admite exactamente $2$ estados independientes ($0$ o $1$), y multiplicamos las opciones mediante la regla del producto.

$$\lvert \Omega_{\text{bits}} \rvert = \underbrace{2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2}_{7\text{ posiciones}} = 2^7 = 128\text{ cadenas}$$

2. Para cualquier conjunto finito $S$, ordenamos arbitrariamente sus $\lvert S \rvert$ elementos y establecemos una correspondencia biyectiva entre cada subconjunto $A \subseteq S$ y una cadena binaria de longitud $\lvert S \rvert$, asignando $b_i = 1$ si el $i$-ésimo elemento pertenece a $A$ y $b_i = 0$ en caso contrario.

$$A \subseteq S \longleftrightarrow (b_1, b_2, \dots, b_{\lvert S \rvert}) \in \{0, 1\}^{\lvert S \rvert}$$

3. Observamos que cada elemento del conjunto $S$ conlleva $2$ decisiones binarias independientes (incluirse o excluirse del subconjunto), por lo que el principio multiplicativo establece que el número total de subconjuntos posibles es $2^{\lvert S \rvert}$.

$$\lvert \mathcal{P}(S) \rvert = \underbrace{2 \cdot 2 \cdots 2}_{\lvert S \rvert\text{ factores}} = 2^{\lvert S \rvert}$$

# 3. Principio de Inclusión-Exclusión y Purga de Redundancias

Las reglas aditiva y multiplicativa operan bajo condiciones ideales: conjuntos completamente disjuntos o etapas donde cada secuencia genera un resultado único. En la práctica, los conjuntos suelen solaparse y los procedimientos secuenciales generan a menudo configuraciones simétricas que representan un mismo objeto. Para resolver ambos obstáculos se introducen la sustracción de intersecciones y la división por clases de equivalencia.

## 3.1. Regla de la Resta e Inclusión-Exclusión para Dos y Tres Conjuntos

Cuando dos conjuntos $A$ y $B$ comparten elementos ($A \cap B \neq \emptyset$), aplicar la regla de la suma directa contabiliza dos veces cada elemento de su intersección. Para restaurar el conteo exacto es obligatorio sustraer la medida del solapamiento. Al extender este razonamiento a tres conjuntos, restar las intersecciones dobles elimina por completo la región central compartida por los tres, lo que obliga a reincorporarla mediante una suma final.

> [!QUOTE] **Teorema 3:** Principio de Inclusión-Exclusión para 2 y 3 Conjuntos
> Para dos conjuntos finitos arbitrarios $A$ y $B$, la cardinalidad de su unión está dada por la **regla de la resta**:
> 
> 
> 
> $$\vert{}A \cup B\vert{} = \vert{}A\vert{} + \vert{}B\vert{} - \vert{}A \cap B\vert{}$$
> 
> 
> Para tres conjuntos finitos arbitrarios $A$, $B$ y $C$, la cardinalidad de su unión compensa las intersecciones dobles y triples mediante signos alternados:
> 
> $$\vert{}A \cup B \cup C\vert{} = \vert{}A\vert{} + \vert{}B\vert{} + \vert{}C\vert{} - \big(\vert{}A \cap B\vert{} + \vert{}A \cap C\vert{} + \vert{}B \cap C\vert{}\big) + \vert{}A \cap B \cap C\vert{}$$
> 
> 

La idea central es garantizar que cada elemento se cuente exactamente una vez. Al sumar los conjuntos por separado, los elementos repetidos quedan contados de más, por lo que debemos restar las intersecciones dobles para quitar ese exceso. Sin embargo, en el caso de tres conjuntos, los elementos que están en los tres a la vez terminan anulándose (se suman tres veces al inicio y se restan tres veces en las parejas), haciendo necesario volver a sumarlos al final para recuperar su conteo.

> [!EXAMPLE] **Ejemplo 4:** Filtrado de Postulantes con Doble Titulación
> 
> Una empresa tecnológica recibe $350$ postulaciones para un cargo de infraestructura. Del total, $220$ aspirantes poseen título en Ciencias de la Computación, $147$ poseen título en Administración y $51$ cuentan con doble titulación en ambas carreras. Determine cuántos aspirantes poseen al menos uno de los dos títulos y cuántos no poseen ninguno.

En este caso práctico de filtrado de registros, los dos conjuntos de cualificaciones académicas no son disjuntos porque existen candidatos con doble titulación. Si se sumaran directamente las cantidades de ambos perfiles, el conteo sobreestimaría el número real de personas calificadas.

La finalidad del ejercicio es corregir este doble conteo aplicando el principio de inclusión-exclusión para dos conjuntos (regla de la resta) y, a partir de esa unión exacta, determinar mediante el complemento respecto al universo total de solicitudes cuántos aspirantes carecen de ambos títulos.

1. Identificamos el universo $\Omega$ de postulantes, los conjuntos $A$ (Ciencias de la Computación) y $B$ (Administración), y su intersección $A \cap B$, advirtiendo que la suma directa $\lvert A \rvert + \lvert B \rvert = 367$ excede el tamaño real de la muestra por el solapamiento.

$$\lvert \Omega \rvert = 350, \qquad \lvert A \rvert = 220, \qquad \lvert B \rvert = 147, \qquad \lvert A \cap B \rvert = 51$$

2. Aplicamos el principio de inclusión-exclusión para dos conjuntos restando una vez la intersección $\lvert A \cap B \rvert$, de modo que los aspirantes con doble titulación queden contabilizados una sola vez en el total de candidatos calificados.

$$\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert = 220 + 147 - 51 = 316\text{ aspirantes calificados}$$

3. Sustraemos la cardinalidad de la unión $\lvert A \cup B \rvert$ del universo total $\lvert \Omega \rvert$ para obtener el número de aspirantes que no poseen ninguno de los dos títulos.

$$\lvert \Omega \setminus (A \cup B) \rvert = 350 - 316 = 34\text{ aspirantes sin ninguno de los títulos}$$

## 3.2. Generalización Analítica para $n$ Conjuntos

Al combinar varios conjuntos, el principio de inclusión-exclusión corrige el conteo sumando y restando las intersecciones de forma alternada.

> [!QUOTE] **Teorema 4:** Forma General del Principio de Inclusión-Exclusión
> Sea $\{A_1, A_2, \dots, A_n\}$ una colección finita de $n$ conjuntos finitos. La cardinalidad de su unión global se calcula mediante la suma alternada de las cardinalidades de todas sus intersecciones posibles:
> 
> $$\left\vert{}\bigcup_{i=1}^n A_i\right\vert{} = \sum_{i=1}^n \vert{}A_i\vert{} - \sum_{1 \le i < j \le n} \vert{}A_i \cap A_j\vert{} + \sum_{1 \le i < j < k \le n} \vert{}A_i \cap A_j \cap A_k\vert{} - \dots + (-1)^{n-1} \left\vert{}\bigcap_{i=1}^n A_i\right\vert{}$$
> 
> 

La validez algebraica de esta expresión reside en que cualquier elemento $x$ que pertenezca exactamente a $m$ de los $n$ conjuntos (con $1 \le m \le n$) aporta un peso neto igual a $1$ al resultado final. En la primera sumatoria ($\vert{}A_i\vert{}$), $x$ se suma $\binom{m}{1}$ veces; en las intersecciones dobles se resta $\binom{m}{2}$ veces; en las triples se suma $\binom{m}{3}$ veces, y así sucesivamente hasta el orden $m$. Por el teorema del binomio aplicado a $(1 - 1)^m = 0$, la contribución total de $x$ resulta:

$$\sum_{r=1}^m (-1)^{r-1} \binom{m}{r} = 1 - \sum_{r=0}^m (-1)^r \binom{m}{r} = 1 - (1 - 1)^m = 1$$

De este modo, ningún elemento de la unión queda omitido ni contado en exceso, sin importar cuántos conjuntos se intersecten simultáneamente.

## 3.3. Regla de la División y Clases de Equivalencia

Un segundo obstáculo en el conteo ocurre cuando un procedimiento secuencial genera $n$ configuraciones ordenadas, pero varias de ellas son estructuralmente indistinguibles bajo alguna simetría del sistema. Si cada configuración única aparece representada exactamente $d$ veces en el conteo bruto, la regla de la división purga esta redundancia uniforme.

> [!QUOTE] **Teorema 5:** Regla de la División
> Si una tarea puede resolverse mediante un procedimiento que genera originalmente $n$ resultados posibles, y para cada configuración única $w$ existen exactamente $d$ resultados del procedimiento que son equivalentes a $w$ (particionando el espacio en clases de equivalencia de tamaño uniforme $d$), entonces el número de configuraciones genuinamente distintas es:
> 
> 
> 
> $$N = \frac{n}{d}$$
> 
> 

Ejemplificando: si contamos todas las huellas dejadas por un grupo de personas en la nieve y sabemos con certeza que cada persona dio exactamente $d = 2$ pasos, dividir el total de huellas $n$ entre $2$ revela el número exacto de personas que caminaron por allí. En combinatoria, este principio permite colapsar rotaciones o simetrías: siempre que cada estado único tenga el mismo grado de multiplicidad $d$, basta con dividir el conteo lineal bruto entre $d$.

> [!EXAMPLE] **Ejemplo 5:** Permutaciones Circulares en Topologías en Anillo
> 
> Cuatro nodos de procesamiento ($A, B, C, D$) deben interconectarse formando una topología física cerrada en anillo, donde dos configuraciones se consideran idénticas si cada nodo conserva exactamente los mismos vecinos a izquierda y derecha. Calcule cuántas topologías únicas en anillo existen y deduzca la fórmula general para $n$ elementos.

Cuando los elementos se disponen sobre una estructura circular cerrada en lugar de una fila recta, distintas ordenaciones lineales pueden representar exactamente la misma configuración física al rotar la posición inicial. Este ejercicio busca purgar esa simetría rotacional mediante la regla de la división, colapsando las clases de equivalencia de tamaño uniforme para hallar el conteo exacto de anillos distinguibles y generalizar la expresión resultante para $n$ nodos.

1. Calculamos primero las ordenaciones lineales como si el anillo estuviera abierto en una fila recta de $4$ posiciones, obteniendo el conteo bruto mediante el factorial de $4$.

$$n_{\text{lineal}} = 4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24\text{ ordenaciones lineales}$$

2. Identificamos que rotar todos los nodos un lugar en sentido horario mantiene intactos los vecinos adyacentes a izquierda y derecha de cada equipo; por consiguiente, cada topología en anillo única queda representada por una clase de equivalencia de tamaño uniforme $d = 4$ (por ejemplo, $ABCD$, $DABC$, $CDAB$ y $BCDA$).

$$d = 4\text{ rotaciones equivalentes por cada anillo}$$

3. Aplicamos la regla de la división dividiendo el total de permutaciones lineales entre la multiplicidad $d = 4$ para los $4$ nodos, y extendemos el mismo cociente al caso general de $n$ elementos con $d = n$ rotaciones equivalentes.

$$P_{\text{circular}}(4) = \frac{4!}{4} = \frac{24}{4} = 6\text{ topologías únicas}, \qquad P_{\text{circular}}(n) = \frac{n!}{n} = (n - 1)!$$

# 4. Principio del Palomar de Dirichlet y Cotas de Colisión

En múltiples problemas de informática no interesa calcular el tamaño total de un espacio de estados, sino demostrar con certeza determinista que, al distribuir un conjunto de datos sobre un número limitado de contenedores, se producirá inevitablemente una agrupación o colisión.

## 4.1. Principio Básico del Palomar

Cuando la cantidad de elementos que se desea almacenar supera la cantidad de casillas disponibles, resulta imposible asignar cada elemento a una casilla exclusiva. Esta observación elemental, formalizada por Peter Gustav Lejeune Dirichlet, constituye un argumento de existencia pura que no depende de distribuciones de probabilidad.

> [!QUOTE] **Teorema 6:** Principio Básico del Palomar (Dirichlet)
> Si $k$ es un entero positivo y se distribuyen $N$ objetos dentro de $k$ recipientes (casillas) cumpliendo que $N \ge k + 1$, entonces existe al menos un recipiente que contiene dos o más objetos.
> 
> 

> [!EXAMPLE] **Ejemplo 6:** Coincidencia Garantizada de Calificaciones
> 
> Un examen universitario se evalúa estrictamente con notas enteras en la escala de $0$ a $100$ puntos. Determine el número mínimo de estudiantes que deben presentar la prueba para garantizar con certeza absoluta que al menos dos obtengan la misma calificación.

En este ejercicio no se busca contar configuraciones ni estimar probabilidades, sino establecer una garantía determinista de colisión sobre un conjunto acotado de resultados posibles. La finalidad es aplicar el principio básico del palomar identificando las calificaciones enteras disponibles como recipientes y a los estudiantes evaluados como los objetos que se distribuyen en ellos.

1. Contamos la cantidad total de «casillas» disponibles en la escala de evaluación entera del $0$ al $100$ inclusive, determinando el número de recipientes $k$.

$$k = 100 - 0 + 1 = 101\text{ calificaciones posibles}$$

2. Aplicamos el principio básico del palomar ($N_{\min} = k + 1$): en el peor caso, hasta $101$ estudiantes podrían obtener notas todas distintas entre sí, por lo que basta añadir un estudiante adicional para forzar inevitablemente al menos una coincidencia.

$$N_{\min} = k + 1 = 101 + 1 = 102\text{ estudiantes}$$

## 4.2. Forma Generalizada con Función Techo y Umbral Crítico

Si el número de objetos $N$ multiplica varias veces la cantidad de contenedores $k$, el principio básico resulta insuficiente porque solo garantiza una pareja compartiendo casilla. Para acotar la acumulación máxima cuando $N \gg k$, se emplea la función techo $\lceil x \rceil$, definida como el menor entero mayor o igual a $x$.

> [!QUOTE] **Teorema 7:** Principio Generalizado del Palomar
> Si se distribuyen $N$ objetos dentro de $k$ recipientes, entonces existe al menos un recipiente que alberga un mínimo de $\lceil N / k \rceil$ objetos.
> 
> 
> De forma inversa, el número mínimo de objetos $N$ que debe distribuirse en $k$ recipientes para garantizar que al menos uno contenga un mínimo de $r$ objetos está dado por:
> 
> 
> 
> $$N = k(r - 1) + 1$$
> 
> 

La demostración de la cota $\lceil N/k \rceil$ procede por reducción al absurdo: si ningún recipiente contuviera al menos $\lceil N/k \rceil$ objetos, cada uno de los $k$ recipientes tendría a lo sumo $\lceil N/k \rceil - 1$ elementos. Dado que $\lceil x \rceil < x + 1$, el total máximo de objetos en todo el sistema sería estrictamente menor que $k\big((N/k + 1) - 1\big) = N$, contradiciendo el hecho de que hay $N$ objetos distribuidos.

Asimismo, para hallar el umbral mínimo $N$ que garantiza una carga de $r$ elementos en alguna casilla, analizamos el peor caso de saturación uniforme. El sistema evita alcanzar la cuota $r$ mientras logre repartir los objetos de forma equilibrada colocando exactamente $r - 1$ elementos en cada una de las $k$ casillas, lo que consume $k(r - 1)$ objetos. En cuanto se introduce un objeto adicional, este rompe el equilibrio y eleva obligatoriamente la carga de alguna casilla a $r$, fijando el umbral en $N = k(r - 1) + 1$.

> [!EXAMPLE] **Ejemplo 7:** Garantía de Nivel Académico en un Curso
> 
> En una asignatura cuya calificación final admite únicamente cinco letras posibles ($A, B, C, D, F$), determine la matrícula mínima necesaria para asegurar que al menos $6$ estudiantes reciban exactamente la misma letra.

A diferencia del problema anterior donde bastaba garantizar una pareja compartiendo casilla, aquí se exige asegurar una acumulación mínima de $6$ estudiantes bajo una misma categoría de nota. Lo que se busca es determinar el umbral crítico de matrícula mediante la forma inversa del principio generalizado del palomar, analizando el peor escenario de saturación uniforme antes de que alguna letra alcance la cuota requerida.

1. Identificamos el número de categorías de calificación disponibles ($k = 5$ letras) y la cuota mínima de repetición exigida en al menos una categoría ($r = 6$ estudiantes).

$$k = 5, \qquad r = 6$$

2. Calculamos el peor caso de saturación uniforme en el que cada una de las $5$ letras recibe exactamente $r - 1 = 5$ estudiantes sin alcanzar la meta, y sumamos $1$ estudiante adicional para garantizar de forma determinista que al menos un grupo alcance los $6$ integrantes.

$$N = k(r - 1) + 1 = 5(6 - 1) + 1 = 5 \cdot 5 + 1 = 26\text{ estudiantes}$$

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