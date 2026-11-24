---
created: 2026-03-04 14:25
title: Espacios de Probabilidad y los Axiomas de Kolmogorov
semester: 4
subject:
  - "[[PROBA 0-0 Nota Informativa|Probabilidad y Estadística]]"
unit: 2
status: done
---

<h1 id="main-title"  align="center"> Espacios de Probabilidad y los Axiomas de Kolmogorov </h1>

> [!TLDR] SÍNTESIS 
> Un **espacio de probabilidad** constituye el marco matemático riguroso que formaliza la cuantificación de la incertidumbre en fenómenos **estocásticos**, integrando un **espacio muestral** de resultados posibles, una **𝜎-álgebra** de eventos medibles y una **medida de probabilidad** regida por los **axiomas de Kolmogorov**. Esta estructura garantiza la coherencia lógica en el cálculo métrico de eventos tanto en dominios discretos como en sistemas continuos complejos.

En la vida cotidiana numerosas variables operativas escapan al control exacto de sus condiciones iniciales. Cuando un sistema exhibe este comportamiento fluctuante, intentar predecir una ejecución aislada mediante ecuaciones rígidas resulta inviable; sin embargo, al observar el fenómeno de manera colectiva, emergen patrones estables que permiten acotar riesgos y garantizar niveles de servicio.

Para transformar esa observación en una herramienta de cálculo exacta, resulta indispensable separar dos niveles de análisis que suelen confundirse en el lenguaje cotidiano: identificar qué desenlaces son lógicamente concebibles dentro de un sistema y medir qué tan factible es cada uno de ellos. Construir este puente exige dotar a los conjuntos de resultados de una estructura métrica libre de contradicciones tanto en dominios finitos como en intervalos continuos.

# 1. Fundamentos Estocásticos y Estructura del Espacio de Probabilidad

El punto de partida del análisis de la incertidumbre consiste en caracterizar la naturaleza del mecanismo que genera los datos. Cuando al fijar las entradas y el estado inicial de un procedimiento se obtiene siempre una salida idéntica e inequívoca (como ocurre al evaluar una función pura sin efectos secundarios), el fenómeno recibe el nombre de **determinista**. Por el contrario, cuando las condiciones experimentales no determinan un desenlace único, sino únicamente el patrón estadístico con el que emergen los distintos resultados observables, nos encontramos ante un experimento **estocástico** o **no determinista**.

## 1.1. Regularidad Estadística y Posibilidad frente a Certidumbre Métrica

Para que un fenómeno sujeto a variabilidad pueda estudiarse rigurosamente mediante modelos probabilísticos, debe reunir tres propiedades estructurales:

- **Repetibilidad:** El procedimiento puede ejecutarse reiteradamente sin alterar sus condiciones esenciales de partida.

- **Incertidumbre del resultado particular:** Resulta imposible anticipar con certeza qué salida arrojará una ejecución aislada, aunque sí es posible delimitar el catálogo completo de desenlaces admisibles.

- **Regularidad estadística:** A medida que el experimento se repite un número creciente de veces ($N \to \infty$), las frecuencias relativas de los resultados individuales dejan de oscilar de manera errática y se estabilizan en torno a proporciones matemáticas constantes.

Esta separación entre el catálogo de desenlaces y su peso numérico obliga a distinguir dos categorías conceptuales: la **posibilidad cualitativa** y la **certidumbre métrica** (probabilidad). La posibilidad es una propiedad binaria de pertenencia a conjuntos: un resultado elemental $\omega$ es «posible» si forma parte del universo de resultados concebibles del experimento, y es «imposible» si corresponde al conjunto vacío $\emptyset$. La probabilidad, en cambio, es una función métrica que opera sobre eventos posibles para asignarles una valoración numérica de ocurrencia en el intervalo $[0, 1]$.

En consecuencia, todo evento imposible es necesariamente improbable ($\mathbb{P}(\emptyset) = 0$), pero un evento puede ser perfectamente posible desde el punto de vista lógico y tener probabilidad nula. Al medir el instante continuo $T \in [0, 24]\text{ h}$ en que una persona llega a su puesto de trabajo, que el incidente ocurra exactamente a las $T = 8.0000\text{ h}$ es posible por pertenecer al intervalo temporal real, pero al existir infinitos instantes no numerables en un día, su medida puntual es $\mathbb{P}(T = 8) = 0$.

## 1.2. El Espacio Muestral, los Eventos y la Función Probabilística

Instintivamente, para estudiar un experimento no determinístico podríamos pensar en anotar los posibles resultados, sin embargo no existe garantía de haber contemplado todas las posibilidades ni de evitar ambigüedades sobre qué estamos midiendo exactamente. Para resolver este problema, se formalizan tres elementos básicos:

> [!QUOTE] **Definición Formal 1:** Espacio Muestral ($\Omega$) y Evento ($E$)
> 
> Dado un experimento no determinístico, el **espacio muestral** $\Omega$ (denotado como $S$ en parte de la literatura) es el conjunto de todos sus resultados elementales posibles $\omega$, formulados de manera mutuamente excluyente y colectivamente exhaustiva.
> 
> Un **evento** (o suceso) $E$ es cualquier subconjunto del espacio muestral ($E \subseteq \Omega$). En particular, el propio $\Omega$ es el _evento seguro_ y el conjunto vacío $\emptyset$ es el _evento imposible_.

En palabras sencillas, el espacio muestral funciona como un archivador cerrado donde cada carpeta representa un único resultado indivisible del experimento: al ejecutar el ensayo una vez, se extrae exactamente una carpeta y ninguna otra. Un evento $E$ es simplemente una agrupación de carpetas que comparten una característica de interés (por ejemplo, «que salga un número par» al lanzar un dado). Según la cantidad y naturaleza de los elementos que contiene, el espacio muestral $\Omega$ se clasifica en tres tipos:

1. **Discreto finito:** Posee un número acotado de resultados posibles ($\lvert \Omega \rvert = n < \infty$), como las $6$ caras de un dado ($\Omega = \{1, 2, 3, 4, 5, 6\}$) o las $16$ secuencias al lanzar una moneda cuatro veces.
    
2. **Discreto infinito numerable:** Sus elementos pueden ponerse en correspondencia uno a uno con los números naturales $\mathbb{N}$, como contar cuántos artículos se inspeccionan hasta encontrar el primero defectuoso.
    
3. **Continuo (infinito no numerable):** Sus resultados abarcan intervalos completos de números reales $\mathbb{R}$ o regiones geométricas, como el tiempo total $t \ge 0$ que funciona una bombilla antes de quemarse ($\Omega = \{t \mid t \ge 0\}$).

Una vez delimitados $\Omega$ y los eventos $E \subseteq \Omega$, surge la necesidad de asignar a cada evento un número que mida qué tan factible es su ocurrencia. El dominio natural para evaluar cualquier combinación lógica de resultados es el conjunto potencia $\text{Partes}(\Omega)$, que reúne a todos los subconjuntos posibles de $\Omega$. Cuando $\Omega$ es discreto y finito con $n$ elementos, $\text{Partes}(\Omega)$ contiene exactamente $2^n$ eventos. (En teoría avanzada de la medida, cuando $\Omega$ es continuo no numerable se restringe el dominio a una familia cerrada de subconjuntos admisibles llamada $\sigma$-álgebra para evitar paradojas geométricas con conjuntos sin longitud o área definidas; en las aplicaciones habituales del curso trabajamos directamente sobre $\text{Partes}(\Omega)$).

> [!QUOTE] **Definición Formal 2:** Función Probabilística ($P$)
> 
> La **función probabilística** es una aplicación matemática $P: \text{Partes}(\Omega) \to [0, 1]$ que asigna a cada evento $E \subseteq \Omega$ un número real que indica el grado de incertidumbre sobre su ocurrencia:
> 
> - $P(E) = 0$ indica que es _improbable_ que ocurra $E$.
>     
> - $P(E) = 1$ indica que $E$ ocurre con _total certeza_.

De manera intuitiva, la función probabilística $P$ actúa como una balanza calibrada entre $0$ y $1$ que pesa cada subconjunto de $\text{Partes}(\Omega)$. Es fundamental no confundir _improbable_ ($P(E) = 0$) con _imposible_ ($E = \emptyset$): todo evento imposible es necesariamente improbable, pero un evento improbable puede ser lógicamente posible. Como ilustra la nota de clase, que un meteorito aterrice justo a nuestro lado mientras leemos este apunte es un evento _improbable_ ($P(E) \approx 0$), pero no _imposible_ ($E \neq \emptyset$).

> [!EXAMPLE] **Ejemplo 1:** Espacio Muestral y Eventos en el Lanzamiento de Tres Monedas
> 
> Se lanza una moneda regular tres veces consecutivas y se registra la secuencia de caras ($C$) y sellos ($S$) obtenida. Describa el espacio muestral $\Omega$, el tamaño de $\text{Partes}(\Omega)$ y los elementos del evento $E$: «salen más caras que sellos».

Para resolver este ejercicio primero analizamos la estructura del experimento estocástico: al lanzar una moneda cuatro veces consecutivas, se busca determinar la probabilidad de un evento específico mediante la construcción formal del espacio muestral y la identificación de sus subconjuntos favorables.

1. Construimos cada resultado elemental $\omega$ como una palabra de cuatro letras perteneciente a $\{C, S\}^4$, garantizando que las $16$ secuencias sean mutuamente excluyentes y cubran todos los desenlaces posibles del experimento.

$$\Omega = {CCC, CCS, CSC, SCC, CSS, SCS, SSC, SSS}$$

2. Observamos que, al ser $\Omega$ un espacio discreto finito de $16$ elementos, el dominio $\text{Partes}(\Omega)$ contiene $2^{16} = 65\,536$ subconjuntos medibles distintos.

$$\lvert \Omega \rvert = 2^3 = 8 \implies \lvert \text{Partes}(\Omega) \rvert = 2^8 = 256$$

3. Aislamos dentro de $\Omega$ las secuencias que contienen al menos $3$ caras ($4$ caras o $3$ caras y $1$ sello), delimitando exactamente los $5$ resultados favorables que conforman el evento $E \subseteq \Omega$.

$$E = {CCC, CCS, CSC, SCC} \implies \lvert E \rvert = 4$$

# 2. Axiomática de la Función Probabilística y Corolarios Derivados

Definida la función probabilística $P: \text{Partes}(\Omega) \to [0, 1]$, hace falta establecer las reglas mínimas que garantizan que cualquier asignación de probabilidades sea coherente y libre de contradicciones internas. Esta fundamentación axiomática, introducida por Andréi Kolmogórov, permite construir todo el cálculo de probabilidades a partir de tres postulados básicos.

## 2.1. Los Tres Axiomas Fundamentales

> [!QUOTE] **Definición Formal 3:** Axiomas de la Función Probabilística
> 
> Sea $\Omega$ un espacio muestral. Una función $P: \text{Partes}(\Omega) \to [0, 1]$ es una **función probabilística** legítima si y solo si satisface los siguientes tres axiomas:
> 
> 1. **Acotación en el intervalo unitario:** $\forall E \subseteq \Omega : 0 \le P(E) \le 1$.
>     
> 2. **Probabilidad de los eventos extremos:** $P(\emptyset) = 0 \land P(\Omega) = 1$.
>     
> 3. **Aditividad para eventos mutuamente excluyentes:** $\forall E, F \subseteq \Omega : \text{Si } E \cap F = \emptyset \text{ entonces } P(E \cup F) = P(E) + P(F)$.

Eestos tres axiomas establecen que la probabilidad se comporta exactamente como una masa física total de $1u$  repartida sobre el espacio muestral:

- El **Axioma 1** impide asignar pesos negativos o superiores al total disponible ($0 \le P(E) \le 1$).
    
- El **Axioma 2** fija las referencias absolutas: la ausencia de resultados pesa $0u$ ($P(\emptyset) = 0$) y la totalidad del universo pesa exactamente $1u$ ($P(\Omega) = 1$).
    
- El **Axioma 3** indica que, si dos regiones $E$ y $F$ no se solapan en absoluto ($E \cap F = \emptyset$), el peso de reunir ambas equivale simplemente a sumar sus pesos por separado. (En teoría avanzada de espacios continuos infinitos, Kolmogórov extiende este tercer axioma a una sucesión infinita numerable de eventos disjuntos dos a dos, mientras que en nuestro desarrollo partimos de la aditividad finita para dos eventos).

> [!EXAMPLE] **Ejemplo 2:** Asignación Axiomática en un Espacio Muestral Finito
> 
> Suponga que solo tres resultados elementales son posibles en un experimento: $\Omega = \{a_1, a_2, a_3\}$. Además, se sabe que la ocurrencia de $a_1$ es dos veces más probable que la de $a_2$, la cual, a su vez, es dos veces más probable que la de $a_3$. Determine la probabilidad de cada resultado elemental $p_1 = P(\{a_1\})$, $p_2 = P(\{a_2\})$ y $p_3 = P(\{a_3\})$.

Para resolver este ejercicio partimos de un espacio muestral discreto y finito cuyos resultados no son equiprobables, sino que guardan una relación de proporcionalidad entre sí. Lo que se busca es asignar una medida de probabilidad numérica a cada desenlace individual garantizando la consistencia lógica con los axiomas de Kolmogórov.

Para lograrlo, debemos traducir las condiciones de peso relativo en ecuaciones algebraicas y combinarlas con la restricción de que la masa probabilística total del espacio muestral debe ser exactamente igual a la unidad.

1. Identificamos que los eventos elementales $\{a_1\}$, $\{a_2\}$ y $\{a_3\}$ son mutuamente excluyentes dos a dos y su unión conforma todo el espacio muestral $\Omega$, además de expresar las relaciones de proporcionalidad del enunciado en términos de $p_3$.

$$\Omega = \{a_1\} \cup \{a_2\} \cup \{a_3\}, \qquad p_1 = 2p_2, \quad p_2 = 2p_3 \implies p_1 = 4p_3$$

2. Aplicamos el Axioma 3 de forma reiterada para descomponer $P(\Omega)$ como la suma de las probabilidades elementales e igualamos esa suma a $1$ según el Axioma 2, sustituyendo cada término en función de $p_3$.

$$P(\Omega) = p_1 + p_2 + p_3 = 1 \implies 4p_3 + 2p_3 + p_3 = 1 \implies 7p_3 = 1$$

3. Despejamos $p_3$, calculamos $p_2$ y $p_1$ a partir de las proporciones dadas y verificamos que los tres valores cumplen el Axioma 1 al ubicarse estrictamente dentro del intervalo $[0, 1]$.

$$p_3 = \frac{1}{7}, \qquad p_2 = \frac{2}{7}, \qquad p_1 = \frac{4}{7}$$

## 2.2. Propiedades Universales como Corolarios de los Axiomas

La potencia del enfoque axiomático radica en que las demás reglas del cálculo de probabilidades no requieren ser postuladas ni verificadas experimentalmente: se demuestran como **corolarios** lógicos utilizando exclusivamente los tres axiomas anteriores y los corolarios ya demostrados.

### 2.2.1. Probabilidad del Evento Complementario

> [!QUOTE] **Corolario 1:** Regla del Complemento
> 
> Para todo evento $E \subseteq \Omega$, la probabilidad de su evento complementario $E^c = \Omega \setminus E$ satisface:
> 
> $$P(E^c) = 1 - P(E)$$

Por definición de complemento en teoría de conjuntos, un evento $E$ y su complemento $E^c$ no comparten ningún elemento ($E \cap E^c = \emptyset$) y su unión reconstruye el espacio muestral completo ($E \cup E^c = \Omega$). Al ser mutuamente excluyentes, aplicamos el **Axioma 3**:

$$P(E \cup E^c) = P(E) + P(E^c)$$

Sustituyendo $E \cup E^c = \Omega$ y aplicando el **Axioma 2** ($P(\Omega) = 1$):

$$1 = P(E) + P(E^c)$$

Despejando $P(E^c)$ obtenemos directamente $P(E^c) = 1 - P(E)$. En la práctica, este corolario resulta sumamente útil cuando resulta más sencillo calcular la probabilidad de que _no_ ocurra un suceso (por ejemplo, «ningún artículo sale defectuoso») que contar todas las combinaciones en las que ocurre al menos una vez.

### 2.2.2. Aditividad Finita para $n$ Eventos Mutuamente Excluyentes

> [!QUOTE] **Corolario 2:** Aditividad Finita Generalizada
> 
> Si $E_1, E_2, \dots, E_n \subseteq \Omega$ son $n$ eventos mutuamente excluyentes dos a dos ($E_i \cap E_j = \emptyset$ para todo $i \neq j$), entonces:
> 
> $$P\left(\bigcup_{i=1}^n E_i\right) = \sum_{i=1}^n P(E_i)$$

Procedemos por inducción matemática sobre el número de eventos $n$:

- **Caso base ($n = 2$):** Para dos eventos disjuntos $E_1$ y $E_2$, la igualdad $P(E_1 \cup E_2) = P(E_1) + P(E_2)$ es cierta directamente por el **Axioma 3**.
    
- **Hipótesis inductiva:** Supongamos que la propiedad se cumple para cualquier colección de $n - 1$ eventos mutuamente excluyentes dos a dos:
    
$$P\left(\bigcup_{i=1}^{n-1} E_i\right) = \sum_{i=1}^{n-1} P(E_i)$$
    
- **Paso inductivo:** Definimos el evento compuesto $A = \bigcup_{i=1}^{n-1} E_i$. Por la ley distributiva de la intersección sobre la unión y dado que $E_i \cap E_n = \emptyset$ para todo $i \le n - 1$, verificamos que $A$ y $E_n$ son mutuamente excluyentes:
    
$$A \cap E_n = \left(\bigcup_{i=1}^{n-1} E_i\right) \cap E_n = \bigcup_{i=1}^{n-1} (E_i \cap E_n) = \bigcup_{i=1}^{n-1} \emptyset = \emptyset$$
    
    Aplicando el **Axioma 3** a los eventos disjuntos $A$ y $E_n$, y luego la hipótesis inductiva sobre $P(A)$:
    
$$P\left(\bigcup_{i=1}^n E_i\right) = P(A \cup E_n) = P(A) + P(E_n) = \sum_{i=1}^{n-1} P(E_i) + P(E_n) = \sum_{i=1}^n P(E_i)$$
    

### 2.2.3. Monotonía por Inclusión de Conjuntos

> [!QUOTE] **Corolario 3:** Propiedad de Monotonía
> 
> Sean $E, F \subseteq \Omega$ dos eventos tales que $E$ está contenido en $F$ ($E \subseteq F$). Entonces:
> 
> $$P(E) \le P(F)$$

Dado que $E \subseteq F$, podemos descomponer el conjunto mayor $F$ en la unión de dos subconjuntos mutuamente excluyentes: la parte que coincide con $E$ y los elementos de $F$ que no pertenecen a $E$ ($F \cap E^c$):

$$F = E \cup (F \cap E^c), \quad \text{con } E \cap (F \cap E^c) = \emptyset$$

Al ser eventos disjuntos, aplicamos el **Axioma 3**:

$$P(F) = P(E) + P(F \cap E^c)$$

Por el **Axioma 1**, sabemos que la probabilidad de cualquier evento es mayor o igual que cero, por lo que $P(F \cap E^c) \ge 0$. Al sumar una cantidad no negativa a $P(E)$, resulta $P(F) \ge P(E)$, es decir, $P(E) \le P(F)$. Intuitivamente, si la ocurrencia de $E$ obliga a que ocurra $F$, entonces $F$ debe ser al menos tan probable como $E$.

### 2.2.4. Ley Aditiva General para Dos Eventos

> [!QUOTE] **Corolario 4:** Probabilidad de la Unión de Dos Eventos Cualesquiera
> 
> Para cualesquiera dos eventos $E, F \subseteq \Omega$ (no necesariamente mutuamente excluyentes), la probabilidad de que ocurra al menos uno de ellos es:
> 
> $$P(E \cup F) = P(E) + P(F) - P(E \cap F)$$

Para utilizar el Axioma 3, descomponemos la unión $E \cup F$ en dos regiones sin solapamiento: todo el evento $E$ junto con la porción de $F$ que queda fuera de $E$ ($F \cap E^c$):

$$E \cup F = E \cup (F \cap E^c), \quad \text{con } E \cap (F \cap E^c) = \emptyset$$

Aplicando el **Axioma 3**:

$$P(E \cup F) = P(E) + P(F \cap E^c)$$

Por otro lado, el propio evento $F$ puede partirse en dos subconjuntos mutuamente excluyentes: su intersección con $E$ y su diferencia con $E$:

$$F = (E \cap F) \cup (F \cap E^c), \quad \text{con } (E \cap F) \cap (F \cap E^c) = \emptyset$$

Aplicando nuevamente el **Axioma 3**, tenemos $P(F) = P(E \cap F) + P(F \cap E^c)$, de donde despejamos $P(F \cap E^c) = P(F) - P(E \cap F)$. Sustituyendo esta expresión en la primera igualdad obtenemos:

$$P(E \cup F) = P(E) + P(F) - P(E \cap F)$$

Intuitivamente, al sumar $P(E) + P(F)$, los resultados comunes en $E \cap F$ se contabilizan dos veces; restar $P(E \cap F)$ elimina esa duplicidad. Cuando $E$ y $F$ son disjuntos, $P(E \cap F) = P(\emptyset) = 0$ por el **Axioma 2** y se recupera el **Axioma 3**.

### 2.2.5. Generalización para $N$ Eventos (Principio de Inclusión-Exclusión)

> [!QUOTE] **Corolario 5:** Ley Aditiva Generalizada para $N$ Eventos
> 
> Para una colección finita de $N$ eventos cualesquiera $E_1, E_2, \dots, E_N \subseteq \Omega$, la probabilidad de su unión está dada por:
> 
> $$P\left(\bigcup_{i=1}^N E_i\right) = \sum_{i=1}^N P(E_i) - \sum_{i < j} P(E_i \cap E_j) + \sum_{i < j < k} P(E_i \cap E_j \cap E_k) - \dots + (-1)^{N-1} P\left(\bigcap_{i=1}^N E_i\right)$$

Se establece por inducción matemática apoyándose en el **Corolario 4**. Para $N = 3$ eventos ($E_1, E_2, E_3$), agrupamos asociativamente $E_1 \cup E_2 \cup E_3 = (E_1 \cup E_2) \cup E_3$ y aplicamos el **Corolario 4** dos veces consecutivas junto con la propiedad distributiva $(E_1 \cup E_2) \cap E_3 = (E_1 \cap E_3) \cup (E_2 \cap E_3)$:

$$P(E_1 \cup E_2 \cup E_3) = P(E_1 \cup E_2) + P(E_3) - P((E_1 \cap E_3) \cup (E_2 \cap E_3))$$

$$= P(E_1) + P(E_2) - P(E_1 \cap E_2) + P(E_3) - \big[P(E_1 \cap E_3) + P(E_2 \cap E_3) - P(E_1 \cap E_2 \cap E_3)\big]$$

$$= P(E_1) + P(E_2) + P(E_3) - P(E_1 \cap E_2) - P(E_1 \cap E_3) - P(E_2 \cap E_3) + P(E_1 \cap E_2 \cap E_3)$$

La extensión a $N$ eventos conserva la misma alternancia de signos al sumar intersecciones simples, restar las dobles, sumar las triples y continuar sucesivamente hasta la intersección de los $N$ conjuntos.

### 2.2.6. Desigualdad de Boole (Subaditividad Finita)

> [!QUOTE] **Corolario 6:** Desigualdad de Boole
> 
> Para cualesquiera $n$ eventos $E_1, E_2, \dots, E_n \subseteq \Omega$, la probabilidad de su unión nunca supera la suma de sus probabilidades individuales:
> 
> $$P\left(\bigcup_{i=1}^n E_i\right) \le \sum_{i=1}^n P(E_i)$$

**Demostración:** Procedemos por inducción matemática sobre $n$ utilizando únicamente el **Corolario 4** y el **Axioma 1**:

- **Caso base ($n = 2$):** Por el **Corolario 4**, sabemos que $P(E_1 \cup E_2) = P(E_1) + P(E_2) - P(E_1 \cap E_2)$. Dado que el **Axioma 1** garantiza que $P(E_1 \cap E_2) \ge 0$, al restar una cantidad no negativa se obtiene:
    
$$P(E_1 \cup E_2) \le P(E_1) + P(E_2)$$
    
- **Hipótesis inductiva:** Supongamos que la desigualdad es válida para $n - 1$ eventos cualesquiera:
    
$$P\left(\bigcup_{i=1}^{n-1} E_i\right) \le \sum_{i=1}^{n-1} P(E_i)$$
    
- **Paso inductivo:** Sea $A = \bigcup_{i=1}^{n-1} E_i$. Aplicando el caso base ($n = 2$) a los eventos $A$ y $E_n$, y sustituyendo luego la hipótesis inductiva:
    
$$P\left(\bigcup_{i=1}^n E_i\right) = P(A \cup E_n) \le P(A) + P(E_n) \le \sum_{i=1}^{n-1} P(E_i) + P(E_n) = \sum_{i=1}^n P(E_i)$$

> [!EXAMPLE] **Ejemplo 3:** Cálculo mediante Corolarios de Complemento y Unión
> 
> Sean $A$, $B$ y $C$ tres eventos asociados a un experimento tales que $P(A) = P(B) = P(C) = \frac{1}{4}$, $P(A \cap B) = P(C \cap B) = 0$ y $P(A \cap C) = \frac{1}{8}$. Calcule la probabilidad de que ocurra al menos uno de los eventos $A$, $B$ o $C$, y la probabilidad de que no ocurra ninguno de ellos.

En este ejercicio no se conoce la estructura interna de los resultados elementales de $\Omega$, sino únicamente las probabilidades de tres eventos y sus intersecciones por pares. La finalidad es demostrar cómo pueden calcularse probabilidades de sucesos compuestos (la ocurrencia de al menos un evento y su negación conjunta) utilizando exclusivamente los corolarios deducidos de la axiomática.

1. Formulamos el evento «ocurre al menos uno de los tres eventos» como la unión $A \cup B \cup C$ y aplicamos el Corolario 5 (principio de inclusión-exclusión para $3$ eventos).

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

2. Determinamos el valor de la intersección triple $P(A \cap B \cap C)$ observando que dicho conjunto está contenido en $A \cap B$, cuya probabilidad es cero; por el Corolario 3 (monotonía) y el Axioma 1, su probabilidad queda acotada a cero.

$$(A \cap B \cap C) \subseteq (A \cap B) \implies 0 \le P(A \cap B \cap C) \le P(A \cap B) = 0 \implies P(A \cap B \cap C) = 0$$

3. Sustituimos las probabilidades individuales y las intersecciones conocidas en la expresión de inclusión-exclusión, obteniendo un valor menor o igual que la cota $\frac{3}{4}$ garantizada por la Desigualdad de Boole (Corolario 6).

$$P(A \cup B \cup C) = \frac{1}{4} + \frac{1}{4} + \frac{1}{4} - 0 - \frac{1}{8} - 0 + 0 = \frac{3}{4} - \frac{1}{8} = \frac{5}{8} = 0.625$$

4. Aplicamos el Corolario 1 (regla del complemento) sobre el evento unión para calcular la probabilidad de que no ocurra ninguno de los eventos $A$, $B$ o $C$.

$$P\big((A \cup B \cup C)^c\big) = 1 - P(A \cup B \cup C) = 1 - \frac{5}{8} = \frac{3}{8} = 0.375$$

# 3. Enfoques Metodológicos de Asignación Probabilística

Para determinar los valores de $P(E)$ es necesario saber cómo asignar un valor numérico concreto a cada resultado de un problema real; existen cuatro enfoques metodológicos distintos, cuya elección depende de la simetría física, repetibilidad y naturaleza continua o discreta del espacio muestral.

## 3.1. Modelo Clásico de Laplace (Equiprobabilidad)

Cuando el espacio muestral $\Omega$ es discreto y finito y las condiciones físicas del experimento garantizan simetría absoluta entre todos los resultados elementales (ningún resultado tiene ventaja sobre otro), la probabilidad se calcula mediante conteo directo.

> [!QUOTE] **Definición Formal 4:** Probabilidad Clásica de Laplace
> 
> Sea $\Omega$ un espacio muestral discreto y finito cuyos resultados elementales $\omega \in \Omega$ son igualmente probables, es decir, $\forall \omega \in \Omega : P(\omega) = \frac{1}{\lVert \Omega \rVert}$. Para cualquier evento $E \subseteq \Omega$, su probabilidad se define como el cociente entre el número de casos favorables y el número de casos totales:
> 
> $$P(E) = \frac{\lVert E \rVert}{\lVert \Omega \rVert}$$

El modelo de Laplace reparte la unidad de probabilidad en porciones idénticas entre todos los resultados posibles, reduciendo el problema a contar cuántas opciones cumplen la condición buscada y dividirlas entre el total de opciones del universo.

Su falla estructural radica en dos restricciones estrictas: es inaplicable cuando $\Omega$ es infinito (dividir entre infinito anula cualquier evento finito) y produce resultados erróneos si existe asimetría física, como suponer que es igual de probable no recibir llamadas en una central telefónica entre la 1:00 a. m. y las 2:00 a. m. que entre las 5:00 p. m. y las 6:00 p. m.

> [!EXAMPLE] **Ejemplo 4:** Extracción en una Urna y Lanzamiento de Dados
> 
> Calcule la probabilidad clásica de los siguientes dos experimentos aleatorios bajo condiciones de simetría física:
> 
> 1. **Esferas en una urna:** Una urna contiene $4$ esferas azules y $5$ rojas, y se extrae una esfera al azar. Determine la probabilidad de extraer una esfera azul ($E_{\text{azul}}$).
> 2. **Suma de dos dados regulares:** Se lanzan dos dados equilibrados de seis caras y se registran sus resultados. Determine la probabilidad de que la suma de las caras sea $7$ ($E$).

Este ejercicio ilustra la aplicación directa del modelo clásico de Laplace en dos experimentos discretos y finitos donde la simetría física de los objetos garantiza que ningún resultado tiene ventaja sobre otro. Se busca determinar la probabilidad de cada evento favorable reduciendo el problema a un conteo exacto de casos.

1. Verificamos la simetría física de ambos experimentos (esferas indistinguibles al tacto y dados no cargados) para legitimar el supuesto de equiprobabilidad $\forall \omega \in \Omega : P(\omega) = 1/\lVert \Omega \rVert$ y establecer la regla de Laplace.

$$P(A) = \frac{\lVert A \rVert}{\lVert \Omega \rVert}$$

2. Para el experimento de la urna, contabilizamos el total de esferas disponibles como el tamaño del espacio muestral y el número de esferas azules como los casos favorables, obteniendo el cociente de probabilidad.

$$\lVert \Omega \rVert = 4 + 5 = 9, \quad \lVert E_{\text{azul}} \rVert = 4 \implies P(E_{\text{azul}}) = \frac{4}{9}$$

3. Para el lanzamiento de los dos dados equilibrados, determinamos la cardinalidad del espacio muestral formado por pares ordenados $(d_1, d_2)$ e identificamos todas las combinaciones cuya suma es igual a $7$.

$$\lVert \Omega \rVert = 6 \times 6 = 36, \qquad E = \{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\} \implies \lVert E \rVert = 6$$

4. Dividimos la cardinalidad del evento favorable entre el total de resultados equiprobables para obtener la probabilidad exacta de sumar $7$.

$$P(E) = \frac{\lVert E \rVert}{\lVert \Omega \rVert} = \frac{6}{36} = \frac{1}{6}$$

## 3.2. Enfoque Frecuentista (Límite de Frecuencias Relativas)

Cuando el fenómeno carece de simetría ideal (por ejemplo, al evaluar una moneda deformada o la proporción de bombillas que duran más de $100\text{ horas}$), no es posible deducir la probabilidad a priori; se recurre a la repetición experimental.

> [!QUOTE] **Definición Formal 5:** Probabilidad Frecuentista (Empírica)
> 
> Si un experimento no determinístico se repite $N$ veces de manera independiente bajo las mismas condiciones y un evento $E \subseteq \Omega$ ocurre en $n_E$ ocasiones, su probabilidad se define como el límite de la frecuencia relativa cuando el número de repeticiones tiende a infinito:
> 
> $$P(E) = \lim_{N \to \infty} \frac{n_E}{N}$$

De manera intuitiva, este enfoque aprovecha la regularidad estadística: aunque en pocos lanzamientos de una moneda las caras y los sellos parezcan alternarse de forma caprichosa, tras repetir el lanzamiento miles de veces la proporción $n_E / N$ se estabiliza en torno a un valor constante.

![[PROBA 2-1 Espacios de Probabilidad y los Axiomas de Kolmogorov - Convergencia Frecuentista de una Moneda.webp]]
  
La limitación estructural del enfoque frecuentista reside en su requisito de repetibilidad bajo condiciones idénticas: resulta inválido para eventos únicos, históricos o irrepetibles, como determinar la probabilidad de que una nueva empresa tenga éxito en su primer año de operaciones.

## 3.3. Enfoque Geométrico (Medidas Continuas)

Cuando el espacio muestral $\Omega$ es continuo e infinito no numerable (un segmento de tiempo, una región plana o un volumen), el conteo de elementos de Laplace falla porque $\lvert \Omega \rvert = \infty$ y la probabilidad de cualquier punto aislado es cero. El enfoque geométrico reemplaza la cardinalidad discreta por medidas continuas de Lebesgue (longitud, área o volumen).

> [!QUOTE] **Definición Formal 6:** Probabilidad Geométrica
> 
> Sea $\Omega \subset \mathbb{R}^n$ una región medible con medida finita y estrictamente positiva ($0 < \text{Medida}(\Omega) < \infty$), y sea $E \subseteq \Omega$ una subregión medible. Si un punto aleatorio se distribuye de forma uniforme sobre $\Omega$, la probabilidad de que pertenezca a $E$ es el cociente entre ambas medidas:
> 
> $$P(E) = \frac{\text{Medida}(E)}{\text{Medida}(\Omega)}$$

Equivale a lanzar un dardo completamente al azar sobre un blanco plano: la probabilidad de acertar dentro de una figura dibujada en su interior depende únicamente de la fracción de área que ocupa esa figura respecto al área total del blanco. Su limitación es que asume densidad uniforme en toda la región; si unas zonas son más probables que otras, el cociente geométrico simple deja de ser válido y requiere integrar una función de densidad no constante.

> [!EXAMPLE] **Ejemplo 5:** Probabilidad Geométrica en un Intervalo Temporal
> 
> Se sabe que un corte en el suministro eléctrico ocurrirá de manera totalmente uniforme entre las 12:00 y las 13:00 horas (un intervalo continuo de $60\text{ minutos}$). Calcule la probabilidad de que el corte ocurra durante los primeros $15\text{ minutos}$ de esa hora (evento $E$).

Al estudiar un fenómeno cuyo resultado se mide sobre el tiempo continuo, el espacio muestral contiene infinitos instantes no numerables, lo cual vuelve inaplicable el conteo de casos de Laplace. La finalidad de este ejercicio es calcular la probabilidad de un suceso temporal utilizando el enfoque geométrico, sustituyendo la cardinalidad discreta por la medida continua de longitud bajo densidad uniforme.

1. Identificamos el espacio muestral continuo $\Omega$ como el intervalo temporal de $60$ minutos y determinamos su medida unidimensional (longitud).

$$\Omega = [0, 60]\text{ min} \implies \text{Longitud}(\Omega) = 60\text{ min}$$

2. Delimitamos el subintervalo correspondiente al evento favorable $E$ (los primeros $15$ minutos de la hora) y calculamos su longitud.

$$E = [0, 15]\text{ min} \implies \text{Longitud}(E) = 15\text{ min}$$

3. Aplicamos la definición de probabilidad geométrica dividiendo la longitud del subintervalo favorable entre la longitud total del espacio muestral.

$$P(E) = \frac{\text{Longitud}(E)}{\text{Longitud}(\Omega)} = \frac{15\text{ min}}{60\text{ min}} = \frac{1}{4} = 0.25$$

## 3.4. Enfoque Subjetivo (Grados de Creencia Racionales)

Ante escenarios irrepetibles la probabilidad subjetiva (o personal) cuantifica el grado de convicción o creencia racional de un observador respecto a una proposición con base en la evidencia disponible.

> [!QUOTE] **Definición Formal 7:** Probabilidad Subjetiva
> 
> Dado un evento único o proposición $E$, la **probabilidad subjetiva** $P(E)$ mide el grado de creencia racional de un observador informado sobre la ocurrencia de $E$. Para que dicha asignación sea matemáticamente válida, debe ser internamente coherente y satisfacer los tres axiomas de la función probabilística.

Este enfoque traduce el juicio experto a una proporción entre $0$ y $1$ que respeta las leyes axiomáticas (por ejemplo, si un analista asigna $P(E) = 0.80$ a un suceso, queda obligado por el Corolario 1 a asignar $P(E^c) = 0.20$ a su negación). Su limitación inherente es la dependencia del sesgo y de la información previa de cada observador.

> [!EXAMPLE] **Ejemplo 6:** Inversores «Toros» y «Osos» en el Mercado Bursátil
> 
> Ante la publicación del reporte trimestral de una empresa tecnológica (un evento único e irrepetible), dos inversores racionales analizan la misma información pública para estimar la probabilidad del evento $E$: «el precio de la acción sube al día siguiente». El inversor optimista (**«toro»**), ponderando la cartera de patentes, asigna $P(E) = 0.85$; mientras que el inversor pesimista (**«oso»**), ponderando el riesgo macroeconómico, asigna $P(E) = 0.20$. Determine el enfoque metodológico adecuado y verifique la coherencia matemática de ambas asignaciones calculando la probabilidad del evento complementario $E^c$ para cada inversor.

Este ejercicio aborda un escenario único e irrepetible donde no es posible realizar ensayos experimentales bajo condiciones idénticas ni establecer simetrías físicas o geométricas. Se busca justificar el uso del enfoque subjetivo de probabilidad y comprobar que, incluso cuando dos observadores discrepan en sus criterios, sus estimaciones siguen siendo matemáticamente válidas si respetan los axiomas de la función probabilística y sus corolarios.

1. Descartamos los enfoques clásico y frecuentista debido a la irrepetibilidad del evento bursátil y adoptamos el enfoque subjetivo para formalizar las creencias racionales de cada inversor sobre el suceso $E$.

$$E = \{\text{el precio de la acción sube al día siguiente}\}, \qquad P_{\text{toro}}(E) = 0.85, \quad P_{\text{oso}}(E) = 0.20$$

2. Verificamos que la asignación del inversor optimista cumple el Axioma 1 al pertenecer al intervalo $[0, 1]$ y aplicamos el Corolario 1 (regla del complemento) para obtener la probabilidad que debe asignar a que la acción no suba ($E^c$).

$$0 \le 0.85 \le 1, \qquad P_{\text{toro}}(E^c) = 1 - P_{\text{toro}}(E) = 1 - 0.85 = 0.15$$

3. Repetimos la verificación del Axioma 1 y aplicamos el Corolario 1 para el inversor pesimista, confirmando que su postura también mantiene plena coherencia axiomática.

$$0 \le 0.20 \le 1, \qquad P_{\text{oso}}(E^c) = 1 - P_{\text{oso}}(E) = 1 - 0.20 = 0.80$$

## 3.5. Síntesis Comparativa de los Enfoques de Asignación

La siguiente tabla resume las condiciones de validez, fórmulas de cálculo y limitaciones de los cuatro enfoques metodológicos:

|**Enfoque Probabilístico**|**Requisito del Espacio Muestral**|**Mecanismo de Asignación**|**Limitación / Falla Estructural**|
|---|---|---|---|
|**Clásico (Laplace)**|Discreto, finito y equiprobable|$\mathbb{P}(A) = \frac{\lVert A \rVert}{\lVert \Omega \rVert}$|Inaplicable a dominios infinitos o procesos con asimetría física.|
|**Frecuentista**|Repetible bajo condiciones idénticas|$\lim_{N \to \infty} \frac{n_A}{N}$|Inválido para eventos únicos, irrepetibles o históricos.|
|**Geométrico**|Continuo, no numerable, uniforme|$\frac{\text{Medida}(A)}{\text{Medida}(\Omega)}$|Asume densidad uniforme; requiere integración si no hay simetría.|
|**Subjetivo**|Cualquier naturaleza (único o repetible)|Juicio experto calibrado|Dependencia del sesgo cognoscitivo del observador.|

# 5. Ejercicios Prácticos Resueltos

## 5.1. Concurrencia Temporal en Sincronización de Tareas

> [!EXAMPLE] **Ejemplo 7:** Probabilidad Geométrica de Colisión de Acceso
> 
> Dos procesos independientes intentan acceder a un recurso compartido entre las 0:00 y las 1:00 h. Cada proceso retiene el recurso exactamente $15\text{ minutos}$. Calcule mediante probabilidad geométrica la probabilidad de que ocurra una colisión de acceso.

En este caso de estudio modelamos un problema de concurrencia temporal en sistemas computacionales donde dos tareas llegan en instantes continuos e independientes dentro de una ventana de una hora. Lo que se busca es representar los pares de tiempos de llegada como puntos uniformes en una región plana bidimensional y calcular la probabilidad exacta de solapamiento.

Para simplificar el cálculo de áreas y evitar particionar la región central en polígonos irregulares, combinaremos la probabilidad geométrica de Lebesgue con el corolario del evento complementario.

1. Representamos los instantes de llegada (en minutos a partir de las 0:00 h) del primer y segundo proceso como variables continuas $X, Y \in [0, 60]$, construyendo el espacio muestral bidimensional $\Omega$ y calculando su área total.

$$\Omega = [0, 60] \times [0, 60], \qquad \text{Área}(\Omega) = 60 \times 60 = 3600\text{ min}^2$$

2. Traducimos el solapamiento temporal a una relación algebraica: dado que cada proceso retiene el recurso durante $15\text{ min}$, los intervalos $[X, X + 15]$ e $[Y, Y + 15]$ colisionan (evento $C$) si y solo si la diferencia absoluta entre sus instantes de inicio es menor o igual a $15\text{ min}$.

$$C = \{(x, y) \in \Omega \mid \lvert x - y \rvert \le 15\}$$

3. Identificamos el evento complementario $C^c$ (ejecución sin conflicto), formado geométricamente por dos triángulos rectángulos congruentes en las esquinas exteriores del cuadrado cuyos catetos miden $60 - 15 = 45\text{ min}$, y calculamos su área combinada.

$$C^c = \{(x, y) \in \Omega \mid \lvert x - y \rvert > 15\} \implies \text{Área}(C^c) = 2 \cdot \left(\frac{45 \times 45}{2}\right) = 45^2 = 2025\text{ min}^2$$

4. Aplicamos el Corolario 1 (regla del complemento) junto con la definición de probabilidad geométrica para hallar la probabilidad exacta de colisión.

$$P(C) = 1 - P(C^c) = 1 - \frac{\text{Área}(C^c)}{\text{Área}(\Omega)} = 1 - \frac{2025}{3600} = \frac{1575}{3600} = \frac{7}{16} = 0.4375 \quad (43.75\%)$$

## 5.2. Generación de Manos en Juegos de Azar Computarizados

> [!EXAMPLE] **Ejemplo 8:** Probabilidad Clásica de un «Full House» en Póker
> 
> Calcule la probabilidad clásica de obtener exactamente un «Full House» (tres cartas de un mismo valor y dos cartas de otro valor distinto) al repartir al azar una mano de $5$ cartas de una baraja estándar de $52$ naipes.

En este ejercicio aplicamos el modelo clásico de Laplace combinado con técnicas de conteo combinatorio en una baraja estándar ($13$ denominaciones con $4$ palos cada una). Dado que al repartir una mano de $5$ cartas el orden de entrega no altera la jugada resultante y todas las combinaciones son igualmente probables, se busca cuantificar con exactitud el número total de manos posibles y las configuraciones favorables que conforman un «Full House».

1. Calculamos el tamaño del espacio muestral equiprobable $\Omega$ mediante combinaciones simples sin repetición de $5$ cartas elegidas entre las $52$ disponibles en la baraja.

$$\lvert \Omega \rvert = C_{52, 5} = \binom{52}{5} = \frac{52!}{5! \cdot 47!} = \frac{52 \times 51 \times 50 \times 49 \times 48}{120} = 2\,598\,960$$

2. Descomponemos la construcción de una mano favorable (evento $E$) en cuatro etapas mediante el Principio de Multiplicación: seleccionamos de forma distinguible el valor del trío entre las $13$ denominaciones y $3$ de sus $4$ palos, y luego escogemos un valor distinto para el par entre las $12$ denominaciones restantes junto con $2$ de sus $4$ palos.

$$\binom{13}{1} = 13, \qquad \binom{4}{3} = 4, \qquad \binom{12}{1} = 12, \qquad \binom{4}{2} = 6$$

3. Multiplicamos el número de opciones de cada etapa para obtener la cardinalidad exacta del evento favorable $E$.

$$\lvert E \rvert = \binom{13}{1} \binom{4}{3} \binom{12}{1} \binom{4}{2} = 13 \times 4 \times 12 \times 6 = 3\,744$$

4. Aplicamos el modelo clásico de Laplace dividiendo los casos favorables entre el total del espacio muestral, concluyendo que en promedio aparece un «Full House» aproximadamente una vez cada $694$ manos repartidas ($4165 / 6 \approx 694.17$).

$$P(E) = \frac{\lvert E \rvert}{\lvert \Omega \rvert} = \frac{3\,744}{2\,598\,960} = \frac{6}{4\,165} \approx 0.00144058 \quad (0.1441\%)$$

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