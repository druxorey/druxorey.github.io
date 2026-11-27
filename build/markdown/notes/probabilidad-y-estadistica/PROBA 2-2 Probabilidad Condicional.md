---
created: 2026-04-22 15:27
title: Probabilidad Condicional
semester: 4
subject:
  - "[[PROBA 0-0 Nota Informativa|Probabilidad y Estadística]]"
unit: 2
status: done
---

<h1 id="main-title"  align="center"> Probabilidad Condicional </h1>

> [!TLDR] SÍNTESIS 
> La **probabilidad condicional** ajusta la medida de incertidumbre de un evento cuando se dispone de evidencia parcial que reduce el espacio muestral original a un subconjunto conocido. Este enfoque métrico, complementado por la **independencia estadística** y la **ley multiplicativa**, permite actualizar estimaciones lógicas, descomponer sistemas complejos de fiabilidad y resolver cadenas de sucesos sucesivos sin reposición.

En cualquier entorno operativo real, la información sobre el estado de un sistema rara vez llega completa de una sola vez. Descartar los datos nuevos para evaluar el riesgo usando únicamente las probabilidades iniciales no solo ignora evidencia valiosa, sino que conduce a estimaciones imprecisas; por el contrario, integrar cualquier información previa disponible mejora drásticamente la toma de decisiones, un principio fundamental que nos obliga a estudiar cómo actualizar formalmente nuestra incertidumbre mediante la probabilidad condicional.

# 1. Probabilidad Condicional y Reducción del Espacio Muestral

El cálculo tradicional de $\mathbb{P}(A)$ evalúa el peso del evento $A$ respecto a la totalidad del espacio muestral $\Omega$. Sin embargo, cuando sabemos con certeza que ya ocurrió un evento $B$, cualquier resultado elemental fuera de $B$ queda descartado. Mantener $\Omega$ como referencia total distorsionaría el cálculo porque asignaría peso a escenarios que ya sabemos que no sucedieron.

## 1.1. Masa Probabilística Positiva

Para integrar la ocurrencia confirmada de $B$, el espacio muestral original se contrae hacia el subconjunto $B$ y las probabilidades de los resultados contenidos dentro de él se reescalan proporcionalmente para que su suma vuelva a ser igual a la unidad.

> [!QUOTE] **Definición Formal 1:** Probabilidad Condicional
> 
> Sean $A$ y $B$ dos eventos pertenecientes a un mismo espacio de probabilidad $(\Omega, \mathcal{F}, \mathbb{P})$ tales que $\mathbb{P}(B) > 0$. La **probabilidad condicional** de que ocurra $A$, dado que ha ocurrido $B$, se denota como $\mathbb{P}(A \mid B)$ y se define mediante el cociente:
> 
> $$\mathbb{P}(A \mid B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$$

Calcular $\mathbb{P}(A \mid B)$ equivale a enfocar exclusivamente la región $B$ del espacio muestral y medir qué fracción de esa región está ocupada por $A$. Como solo nos interesan los resultados donde ocurre $B$, los únicos casos favorables para $A$ son aquellos que pertenecen simultáneamente a ambos conjuntos ($A \cap B$). Dividir entre $\mathbb{P}(B)$ normaliza la medida para que el nuevo espacio muestral reducido $B$ conserve una probabilidad total de $1$.

El requisito de exigir $\mathbb{P}(B) > 0$ evita una indeterminación matemática del tipo $\frac{0}{0}$, pues si $\mathbb{P}(B) = 0$, la monotonía de la probabilidad obliga a que $\mathbb{P}(A \cap B) = 0$ al cumplirse $A \cap B \subseteq B$. Además, condicionar un cálculo sobre un evento de probabilidad nula carece de utilidad práctica porque supone restringir el análisis a un escenario que no ocurre en el experimento.

Asimismo, para un evento condicionante fijo $B$ con $\mathbb{P}(B) > 0$, la aplicación $A \mapsto \mathbb{P}(A \mid B)$ satisface todos los [[PROBA 2-1 Espacios de Probabilidad y los Axiomas de Kolmogorov#2.1. Los Tres Axiomas Fundamentales|axiomas de Kolmogórov]]: es no negativa ($\mathbb{P}(A \mid B) \ge 0$), asigna certeza total al nuevo universo ($\mathbb{P}(B \mid B) = 1$) y es aditiva para eventos mutuamente excluyentes. En consecuencia, todas las propiedades derivadas de los axiomas siguen siendo válidas bajo condicionamiento, como la regla del complemento condicional:

$$\mathbb{P}(A^c \mid B) = 1 - \mathbb{P}(A \mid B)$$

> [!EXAMPLE] **Ejemplo 1:** Control de Calidad en Producción de Listones Textiles
> 
> En un proceso industrial textil se producen listones de tela que pueden presentar defectos en su longitud ($L$) o en su textura ($T$). A partir de registros históricos se sabe que el $10\%$ de los listones no pasan la prueba de longitud, el $5\%$ no pasan la prueba de textura y el $0.8\%$ fallan simultáneamente en ambas pruebas. Si se selecciona un listón al azar y una inspección rápida confirma que no pasa la prueba de longitud, calcule la probabilidad de que su textura también esté defectuosa.

En este ejercicio analizamos un caso de control de calidad industrial donde dos tipos de fallas pueden superponerse sobre un mismo producto. La finalidad es determinar cómo la detección temprana de un defecto de longitud actualiza la probabilidad de encontrar un defecto de textura, restringiendo el espacio muestral al grupo de piezas defectuosas en longitud mediante la definición de probabilidad condicional.

1. Definimos los eventos $L$ («el listón falla la prueba de longitud») y $T$ («el listón falla la prueba de textura»), y traducimos los porcentajes históricos del enunciado a probabilidades marginales y conjuntas.

$$\mathbb{P}(L) = 0.10, \qquad \mathbb{P}(T) = 0.05, \qquad \mathbb{P}(L \cap T) = 0.008$$

2. Verificamos que el evento condicionante tiene probabilidad estrictamente positiva ($\mathbb{P}(L) = 0.10 > 0$) y planteamos la fórmula de probabilidad condicional $\mathbb{P}(T \mid L)$ dividiendo la probabilidad conjunta entre la marginal del evento observado.

$$\mathbb{P}(T \mid L) = \frac{\mathbb{P}(L \cap T)}{\mathbb{P}(L)} = \frac{0.008}{0.10}$$

3. Efectuamos el cociente para obtener la probabilidad actualizada, observando que conocer el fallo en longitud eleva el riesgo de defecto en textura desde el $5\%$ inicial hasta el $8\%$.

$$\mathbb{P}(T \mid L) = 0.08$$

## 1.2. Causalidad Temporal y la Actualización de Información

En el lenguaje cotidiano, la expresión «dado que ocurrió $B$» suele asociarse con una secuencia cronológica en la que $B$ sucede antes que $A$. Sin embargo, la probabilidad condicional $\mathbb{P}(A \mid B)$ no exige orden temporal ni relación física de causa y efecto entre los eventos.

El condicionamiento refleja una actualización lógica basada en la información disponible. Tanto $A$ como $B$ son subconjuntos de un mismo espacio muestral $\Omega$; por lo tanto, es igual de válido evaluar la probabilidad de un desenlace futuro dada una condición inicial ($\mathbb{P}(\text{Efecto} \mid \text{Causa})$) que evaluar la probabilidad de una condición pasada a partir de una observación posterior ($\mathbb{P}(\text{Causa} \mid \text{Efecto})$). Saber qué ocurrió al final del experimento descarta los resultados elementales incompatibles con esa observación y reajusta las probabilidades de las etapas previas.

> [!EXAMPLE] **Ejemplo 2:** Actualización Inversa de Información en Puntualidad de Vuelos
> En una ruta aérea comercial, la probabilidad de que un vuelo salga a tiempo ($D$) es $0.83$, la probabilidad de que llegue a tiempo ($A$) es $0.82$, y la probabilidad de que salga y llegue a tiempo simultáneamente es $0.78$. Calcule:
> 
> 
> 1. La probabilidad de que el vuelo haya salido a tiempo, sabiendo que llegó a tiempo ($\mathbb{P}(D \mid A)$).
> 
> 
> 2. La probabilidad de que el vuelo llegue a tiempo, sabiendo que no salió a tiempo ($\mathbb{P}(A \mid D^c)$).
> 
> 
> 
> 

Este ejercicio ilustra que la probabilidad condicional opera en ambos sentidos temporales: tanto para inferir un evento previo a partir de un resultado posterior como para actualizar el pronóstico de un evento futuro ante un retraso inicial. Lo que se busca es aplicar la definición de probabilidad condicional junto con la descomposición de conjuntos para cuantificar ambos escenarios.

1. Registramos las probabilidades dadas para la salida puntual ($D$), la llegada puntual ($A$) y su ocurrencia simultánea ($D \cap A$).

$$\mathbb{P}(D) = 0.83, \qquad \mathbb{P}(A) = 0.82, \qquad \mathbb{P}(D \cap A) = 0.78$$

2. Calculamos $\mathbb{P}(D \mid A)$ dividiendo la intersección $\mathbb{P}(D \cap A)$ entre $\mathbb{P}(A)$, actualizando la probabilidad de salida puntual a partir de la confirmación posterior de que el avión aterrizó a tiempo.

$$\mathbb{P}(D \mid A) = \frac{\mathbb{P}(D \cap A)}{\mathbb{P}(A)} = \frac{0.78}{0.82} = \frac{39}{41} \approx 0.9512$$

3. Para el segundo inciso, calculamos primero la probabilidad de que el vuelo no salga a tiempo ($\mathbb{P}(D^c)$) mediante la regla del complemento, y la probabilidad de que llegue a tiempo habiendo salido tarde ($\mathbb{P}(A \cap D^c)$) restando la intersección $\mathbb{P}(A \cap D)$ a la probabilidad total de llegada puntual $\mathbb{P}(A)$.

$$\mathbb{P}(D^c) = 1 - \mathbb{P}(D) = 1 - 0.83 = 0.17, \qquad \mathbb{P}(A \cap D^c) = \mathbb{P}(A) - \mathbb{P}(A \cap D) = 0.82 - 0.78 = 0.04$$

4. Dividimos $\mathbb{P}(A \cap D^c)$ entre $\mathbb{P}(D^c)$ para obtener la probabilidad condicionada $\mathbb{P}(A \mid D^c)$, comprobando cómo el retraso en el despegue reduce drásticamente la probabilidad de llegar a tiempo desde el $82\%$ original hasta aproximadamente el $23.53\%$.

$$\mathbb{P}(A \mid D^c) = \frac{\mathbb{P}(A \cap D^c)}{\mathbb{P}(D^c)} = \frac{0.04}{0.17} = \frac{4}{17} \approx 0.2353$$

# 2. Independencia Estadística

Una vez establecido cómo la ocurrencia de un evento $B$ modifica la probabilidad de $A$, surge el caso límite opuesto: ¿qué ocurre cuando saber que sucedió $B$ no aporta ningún dato relevante para predecir $A$? Esa ausencia de influencia mutua define la independencia estadísticas.

## 2.1. Definición Formal y Caracterización Equivalente

Intuitivamente, dos eventos $A$ y $B$ son independientes si la probabilidad condicional de $A$ dado $B$ coincide exactamente con la probabilidad original de $A$, es decir, $\mathbb{P}(A \mid B) = \mathbb{P}(A)$. Sin embargo, escribir esta condición como un cociente exige que $\mathbb{P}(B) > 0$. Para eliminar esa restricción de división y expresar la propiedad de manera simétrica, la definición formal se formula mediante el producto de probabilidades.

> [!QUOTE] **Definición Formal 2:** Independencia Estadística de Dos Eventos
> 
> Dos eventos $A$ y $B$ de un espacio de probabilidad $(\Omega, \mathcal{F}, \mathbb{P})$ son **estadísticamente independientes** si y solo si la probabilidad de su ocurrencia simultánea es igual al producto de sus probabilidades individuales:
> 
> $$\mathbb{P}(A \cap B) = \mathbb{P}(A)\,\mathbb{P}(B)$$
> 
> Cuando $\mathbb{P}(A) > 0$ y $\mathbb{P}(B) > 0$, esta igualdad es equivalente a las relaciones condicionales:
> 
> $$\mathbb{P}(A \mid B) = \mathbb{P}(A) \quad \land \quad \mathbb{P}(B \mid A) = \mathbb{P}(B)$$

La independencia significa observar uno de los eventos no altera las proporciones relativas del otro dentro del espacio muestral. Además, la simetría de la multiplicación ($\mathbb{P}(A)\mathbb{P}(B) = \mathbb{P}(B)\mathbb{P}(A)$) garantiza que la independencia es siempre recíproca: si $A$ es independiente de $B$, entonces $B$ es necesariamente independiente de $A$.

Cuando se analizan tres o más eventos $A_1, A_2, \dots, A_n$, la independencia mutua exige una condición más estricta que la simple independencia por pares: la probabilidad de la intersección de *cualquier* subcolección de $2, 3, \dots, n$ eventos debe factorizarse como el producto de sus probabilidades individuales. Es decir, si tenemos tres eventos $A_1, A_2$ y $A_3$, no basta con que:

$$\mathbb{P}(A_1 \cap A_2) = \mathbb{P}(A_1)\mathbb{P}(A_2) \quad \land \quad \mathbb{P}(A_1 \cap A_3) = \mathbb{P}(A_1)\mathbb{P}(A_3) \quad \land \quad \mathbb{P}(A_2 \cap A_3) = \mathbb{P}(A_2)\mathbb{P}(A_3)$$

Sino que además se debe cumplir estrictamente que:

$$\mathbb{P}(A_1 \cap A_2 \cap A_3) = \mathbb{P}(A_1)\mathbb{P}(A_2)\mathbb{P}(A_3)$$

## 2.2. Incompatibilidad con la Exclusión Mutua e Inclusión de Subconjuntos

Un error conceptual frecuente consiste en confundir eventos mutuamente excluyentes ($A \cap B = \emptyset$) con eventos estadísticamente independientes. Mientras que la exclusión mutua es una propiedad geométrica de conjuntos (no comparten elementos), la independencia es una propiedad métrica de proporciones. De hecho, para eventos con probabilidad positiva, ambas propiedades son lógicamente incompatibles.

> [!QUOTE] **Teorema 1:** Incompatibilidad entre Exclusión Mutua e Independencia
> 
> Sean $A$ y $B$ dos eventos tales que $\mathbb{P}(A) > 0$ y $\mathbb{P}(B) > 0$. Si $A$ y $B$ son mutuamente excluyentes ($A \cap B = \emptyset$), entonces **no pueden ser estadísticamente independientes**.

La demostración es directa a partir de los axiomas. Si $A$ y $B$ son mutuamente excluyentes, entonces $A \cap B = \emptyset$, por lo que $\mathbb{P}(A \cap B) = \mathbb{P}(\emptyset) = 0$. Por otra parte, como $\mathbb{P}(A) > 0$ y $\mathbb{P}(B) > 0$, su producto es estrictamente mayor que cero ($\mathbb{P}(A)\mathbb{P}(B) > 0$). Al cumplirse $\mathbb{P}(A \cap B) = 0 \neq \mathbb{P}(A)\mathbb{P}(B)$, la condición de independencia se viola de inmediato. En la práctica, dos eventos excluyentes presentan la máxima dependencia negativa posible: saber que ocurrió $B$ garantiza con certeza absoluta que $A$ no ocurrió ($\mathbb{P}(A \mid B) = 0 \neq \mathbb{P}(A)$).

De manera análoga, ocurre una dependencia estricta cuando un evento está contenido dentro de otro ($A \subset B$) bajo probabilidades no triviales ($0 < \mathbb{P}(A) < \mathbb{P}(B) < 1$). Al estar $A$ incluido en $B$, su intersección coincide con el conjunto menor ($A \cap B = A$), lo que implica $\mathbb{P}(A \cap B) = \mathbb{P}(A)$. Al evaluar las probabilidades condicionales resulta:

$$\mathbb{P}(B \mid A) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(A)} = \frac{\mathbb{P}(A)}{\mathbb{P}(A)} = 1 \neq \mathbb{P}(B)$$

$$\mathbb{P}(A \mid B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)} = \frac{\mathbb{P}(A)}{\mathbb{P}(B)} > \mathbb{P}(A)$$

Por lo tanto, saber que sucedió el evento más específico $A$ fuerza la certeza absoluta de que también sucedió $B$, descartando la independencia (que solo podría sostenerse en los casos extremos degenerados donde $\mathbb{P}(A) = 0$ o $\mathbb{P}(B) = 1$).

> [!EXAMPLE] **Ejemplo 3:** Contraste entre Independencia y Exclusión Mutua en un Dado
> Se lanza un dado equilibrado de seis caras ($\Omega = \{1, 2, 3, 4, 5, 6\}$) y se definen los eventos: $A = \{2, 4, 6\}$ («obtener un número par»), $B = \{1, 2, 3, 4\}$ («obtener un número menor que $5$») y $C = \{1, 3, 5\}$ («obtener un número impar»). Compruebe analíticamente si $A$ y $B$ son estadísticamente independientes, y verifique por qué $A$ y $C$ no lo son.
> 
> 

En este ejercicio aplicamos el criterio algebraico de independencia sobre un espacio muestral equiprobable sencillo. Se busca contrastar dos parejas de eventos para observar cómo la intersección de conjuntos con proporciones balanceadas preserva la independencia, mientras que la ausencia total de elementos comunes la destruye.

1. Calculamos las probabilidades individuales de los tres eventos bajo el modelo clásico de Laplace sobre el espacio muestral $\Omega$ de $6$ resultados equiprobables.

$$\mathbb{P}(A) = \frac{3}{6} = \frac{1}{2}, \qquad \mathbb{P}(B) = \frac{4}{6} = \frac{2}{3}, \qquad \mathbb{P}(C) = \frac{3}{6} = \frac{1}{2}$$

2. Determinamos la intersección $A \cap B$ («número par menor que $5$»), calculamos su probabilidad y la comparamos con el producto $\mathbb{P}(A)\mathbb{P}(B)$, confirmando que son iguales y que, por tanto, $A$ y $B$ son independientes.

$$A \cap B = \{2, 4\} \implies \mathbb{P}(A \cap B) = \frac{2}{6} = \frac{1}{3}$$
$$\mathbb{P}(A)\,\mathbb{P}(B) = \frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3} \implies \mathbb{P}(A \cap B) = \mathbb{P}(A)\,\mathbb{P}(B)$$

3. Evaluamos la intersección $A \cap C$: al ser eventos mutuamente excluyentes su probabilidad conjunta es cero, valor que difiere del producto $\mathbb{P}(A)\mathbb{P}(C) = \frac{1}{4}$, demostrando que $A$ y $C$ son dependientes.

$$A \cap C = \emptyset \implies \mathbb{P}(A \cap C) = 0 \neq \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$$

# 3. Ley Multiplicativa de la Probabilidad

Despejar el numerador en la definición de probabilidad condicional produce la identidad $\mathbb{P}(A \cap B) = \mathbb{P}(A)\,\mathbb{P}(B \mid A)$. Esta expresión resulta indispensable cuando se desea calcular la probabilidad de que ocurran varios sucesos en secuencia y el resultado de cada etapa altera las condiciones de las etapas posteriores.

## 3.1. Regla Multiplicativa Generalizada

Al extender este encadenamiento desde dos eventos hasta una colección finita de $n$ eventos sucesivos, se obtiene la ley multiplicativa generalizada.

> [!QUOTE] **Teorema 2:** Ley Multiplicativa (Regla de la Cadena para $n$ Eventos)
> 
> Sean $A_1, A_2, \dots, A_n \in \mathcal{F}$ eventos tales que $\mathbb{P}\left(\bigcap_{j=1}^{n-1} A_j\right) > 0$. La probabilidad de que ocurran simultáneamente todos los $n$ eventos está dada por:
> 
> $$\mathbb{P}\left(\bigcap_{i=1}^n A_i\right) = \mathbb{P}(A_1)\,\mathbb{P}(A_2 \mid A_1)\,\mathbb{P}(A_3 \mid A_1 \cap A_2)\cdots \mathbb{P}\left(A_n \mid \bigcap_{j=1}^{n-1} A_j\right)$$

La regla de la cadena equivale a recorrer una rama específica de un árbol de probabilidad desde la raíz hasta una hoja terminal. Para que la secuencia completa tenga éxito, primero debe ocurrir $A_1$; luego debe ocurrir $A_2$ sabiendo que ya pasó $A_1$; a continuación debe ocurrir $A_3$ bajo la condición de que ya sucedieron tanto $A_1$ como $A_2$, y así sucesivamente hasta el paso $n$. Multiplicar las probabilidades condicionales a lo largo de esa trayectoria entrega la probabilidad conjunta exacta. Cuando los $n$ eventos son mutuamente independientes, cada término condicional colapsa a su probabilidad marginal $\mathbb{P}(A_i)$ y la fórmula se reduce a $\prod_{i=1}^n \mathbb{P}(A_i)$.

### 3.1.1. Demostración por Inducción Matemática

Para validar la regla de la cadena para cualquier entero $n \ge 2$, procedemos por inducción matemática sobre el número de eventos:

**Caso base ($n = 2$):** Dados dos eventos $A_1$ y $A_2$ con $\mathbb{P}(A_1) > 0$, partimos de la Definición Formal 1:

$$\mathbb{P}(A_2 \mid A_1) = \frac{\mathbb{P}(A_1 \cap A_2)}{\mathbb{P}(A_1)}$$

Multiplicando ambos miembros por $\mathbb{P}(A_1)$ obtenemos directamente la identidad para dos eventos:

$$\mathbb{P}(A_1 \cap A_2) = \mathbb{P}(A_1)\,\mathbb{P}(A_2 \mid A_1)$$

**Hipótesis inductiva:** Supongamos que la fórmula es válida para cualquier colección de $n - 1$ eventos cuya intersección hasta el término $n - 2$ tenga probabilidad positiva:

$$\mathbb{P}\left(\bigcap_{i=1}^{n-1} A_i\right) = \mathbb{P}(A_1)\,\mathbb{P}(A_2 \mid A_1)\,\mathbb{P}(A_3 \mid A_1 \cap A_2)\cdots \mathbb{P}\left(A_{n-1} \mid \bigcap_{j=1}^{n-2} A_j\right)$$

**Paso inductivo:** Definimos el evento compuesto $E = \bigcap_{j=1}^{n-1} A_j$, el cual cumple $\mathbb{P}(E) > 0$ por hipótesis. Asociando los primeros $n - 1$ eventos dentro de $E$, aplicamos el caso base ($n = 2$) al par de eventos $E$ y $A_n$:

$$\mathbb{P}\left(\bigcap_{i=1}^n A_i\right) = \mathbb{P}\left(\left(\bigcap_{j=1}^{n-1} A_j\right) \cap A_n\right) = \mathbb{P}(E \cap A_n) = \mathbb{P}(E)\,\mathbb{P}(A_n \mid E)$$

Sustituimos ahora $\mathbb{P}(E)$ por la expresión de la hipótesis inductiva y reescribimos $E = \bigcap_{j=1}^{n-1} A_j$ en el último factor condicional:

$$\mathbb{P}\left(\bigcap_{i=1}^n A_i\right) = \mathbb{P}(A_1)\,\mathbb{P}(A_2 \mid A_1)\,\mathbb{P}(A_3 \mid A_1 \cap A_2)\cdots \mathbb{P}\left(A_{n-1} \mid \bigcap_{j=1}^{n-2} A_j\right)\,\mathbb{P}\left(A_n \mid \bigcap_{j=1}^{n-1} A_j\right) \quad \blacksquare$$

# 4. Ejercicios Prácticos Resueltos

## 4.1. Auditoría de Consistencia de Datos sin Reemplazo

> [!EXAMPLE] **Ejemplo 4:** Auditoría de Integridad en una Base de Datos sin Reemplazo
> En una base de datos con $100$ registros, $6$ contienen campos corruptos y los $94$ restantes son íntegros. Si un script de auditoría inspecciona aleatoriamente $4$ registros sin reemplazo, calcule la probabilidad de que todos los registros inspeccionados sean íntegros aplicando la ley multiplicativa de la probabilidad.
> 
> 

En este ejercicio modelamos un procedimiento de muestreo aleatorio sin reposición sobre un lote finito de registros. Dado que cada registro revisado se retira del conjunto candidato antes de la siguiente selección, el resultado de una inspección modifica tanto el total de registros disponibles como la proporción de registros íntegros restantes, invalidando el supuesto de independencia.

Lo que se busca es encadenar las probabilidades condicionales de cada extracción sucesiva mediante la regla de la cadena para determinar la probabilidad exacta de superar las cuatro inspecciones sin detectar ningún dato corrupto.

1. Definimos los eventos $I_k$ («el $k$-ésimo registro inspeccionado es íntegro») para $k \in \{1, 2, 3, 4\}$ y expresamos la probabilidad de que los cuatro sean íntegros mediante la ley multiplicativa para $n = 4$ eventos.

$$\mathbb{P}(I_1 \cap I_2 \cap I_3 \cap I_4) = \mathbb{P}(I_1)\,\mathbb{P}(I_2 \mid I_1)\,\mathbb{P}(I_3 \mid I_1 \cap I_2)\,\mathbb{P}(I_4 \mid I_1 \cap I_2 \cap I_3)$$

2. Evaluamos cada factor condicional de forma secuencial: en la primera extracción hay $94$ registros íntegros de $100$; si el primero resulta íntegro, quedan $93$ íntegros de $99$, y así sucesivamente hasta la cuarta inspección.

$$\mathbb{P}(I_1) = \frac{94}{100}, \quad \mathbb{P}(I_2 \mid I_1) = \frac{93}{99}, \quad \mathbb{P}(I_3 \mid I_1 \cap I_2) = \frac{92}{98}, \quad \mathbb{P}(I_4 \mid I_1 \cap I_2 \cap I_3) = \frac{91}{97}$$

3. Multiplicamos las cuatro probabilidades condicionales y simplificamos la fracción resultante para obtener la probabilidad exacta de que la muestra completa esté libre de corrupción.

$$\mathbb{P}(I_1 \cap I_2 \cap I_3 \cap I_4) = \frac{94}{100} \cdot \frac{93}{99} \cdot \frac{92}{98} \cdot \frac{91}{97} = \frac{73\,188\,024}{94\,109\,400} = \frac{435\,643}{560\,175} \approx 0.7777$$

## 4.2. La Paradoja de los Cumpleaños 

> [!EXAMPLE] **Ejemplo 5:** La Paradoja de los Cumpleaños y Colisiones en Funciones Hash
> Considere un calendario uniforme de $365$ días al año (ignorando años bisiestos) y fechas de nacimiento independientes entre personas. Utilizando la ley multiplicativa de la probabilidad y la regla del complemento, derive la expresión general para la probabilidad de que al menos dos personas en un grupo de $n$ compartan fecha de nacimiento (modelo base para calcular colisiones en funciones hash con $365$ salidas equiprobables), y determine el valor mínimo de $n$ para el cual dicho riesgo supera el $50\%$.
> 
> 

En seguridad informática y diseño de estructuras de datos, el «ataque de cumpleaños» analiza qué tan rápido aparece una colisión cuando se asignan identificadores aleatorios dentro de un espacio de salida finito. Calcular directamente la probabilidad de que haya *al menos una* coincidencia exigiría sumar múltiples escenarios solapados (parejas, tríos, múltiples pares distintos).

La finalidad de este ejercicio es evitar esa complejidad combinatoria aplicando la regla del complemento: calcularemos primero la probabilidad de que *todas* las $n$ fechas sean distintas entre sí mediante la regla de la cadena, y luego restaremos ese valor de la unidad para hallar el umbral crítico donde el riesgo de colisión supera el $50\%$.

1. Definimos el evento $C_n$ («al menos dos personas entre las $n$ comparten fecha de nacimiento») para $1 \le n \le 365$, y expresamos su probabilidad en términos del evento complementario $C_n^c$ («las $n$ personas tienen fechas de nacimiento todas distintas entre sí»).

$$\mathbb{P}(C_n) = 1 - \mathbb{P}(C_n^c)$$

2. Descomponemos $C_n^c$ como la intersección de $n$ eventos secuenciales $D_1 \cap D_2 \cap \dots \cap D_n$, donde $D_k$ indica que la $k$-ésima persona no coincide con ninguna de las $k - 1$ anteriores, y aplicamos la regla de la cadena: la primera persona dispone de los $365$ días libres, la segunda de $364$, y la $n$-ésima de $365 - (n - 1) = 365 - n + 1$ días disponibles.

$$\mathbb{P}(C_n^c) = \frac{365}{365} \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{365 - n + 1}{365} = \frac{365!}{(365 - n)!\,365^n}$$

3. Sustituimos la expresión de $\mathbb{P}(C_n^c)$ en la regla del complemento para obtener la fórmula general cerrada de la probabilidad de colisión en función del tamaño del grupo $n$.

$$\mathbb{P}(C_n) = 1 - \frac{365!}{(365 - n)!\,365^n}$$

4. Evaluamos la fórmula para valores crecientes de $n$ hasta cruzar el umbral del $50\%$: para $n = 22$ el riesgo aún es inferior a la mitad, pero al incorporar a la persona número $23$ la probabilidad de coincidencia supera el $50\%$, fijando en $n = 23$ el valor crítico buscado.

$$\mathbb{P}(C_{22}) = 1 - \frac{365!}{343!\,365^{22}} \approx 0.4757$$
$$\mathbb{P}(C_{23}) = 1 - \frac{365!}{342!\,365^{23}} \approx 0.5073 $$

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