---
created: 2026-04-23 14:33
title: Ley de Probabilidad Total y Teorema de Bayes
semester: 4
subject:
  - "[[PROBA 0-0 Nota Informativa|Probabilidad y Estadística]]"
unit: 2
status: done
---

<h1 id="main-title"  align="center"> Ley de Probabilidad Total y Teorema de Bayes </h1>

> [!TLDR] SÍNTESIS 
> La **Ley de Probabilidad Total** permite calcular la probabilidad global de un evento complejo fragmentando el espacio muestral en una **partición exhaustiva** de escenarios disjuntos. Complementariamente, el **Teorema de Bayes** facilita la inferencia retrospectiva para actualizar creencias iniciales ante nueva evidencia empírica, fundando la base matemática de los **clasificadores probabilísticos** y modelos de aprendizaje automatizado como **Naïve Bayes**.

En múltiples situaciones cotidianas la causa real de un fenómeno permanece oculta en el momento en que ocurre. Un médico no observa directamente si un paciente porta un virus específico, sino síntomas visibles como fiebre, es decir que existe una distancia entre las causas ocultas que originan el suceso y los efectos superficiales que logramos observar. Resolver este problema plantea dos retos complementarios:

1) Cuando un evento observable puede ocurrir por distintas vías con diferentes frecuencias, calcular su probabilidad global de forma directa resulta difícil si no se divide el conjunto de posibilidades en escenarios aislados y manejables.

2) Una vez que se observa un síntoma concreto, hace falta recorrer el razonamiento en sentido inverso (desde el efecto observado hacia la causa probable) sin dejarse engañar por falsas alarmas cuando el evento buscado es poco frecuente.

# 1. Particiones del Espacio Muestral

El cálculo directo de la probabilidad $\mathbb{P}(A)$ de un evento complejo $A$ suele complicarse cuando el fenómeno que lo produce opera bajo distintos escenarios o grupos poblacionales. La estrategia matemática para simplificarlo consiste en fragmentar el [[PROBA 2-1 Espacios de Probabilidad y los Axiomas de Kolmogorov#1.2. El Espacio Muestral y los Eventos|espacio muestral]] $\Omega$ en subconjuntos que no se solapen entre sí y que cubran todas las alternativas posibles sin dejar huecos.

## 1.1. Concepto Axiomático de Partición Exhaustiva

Para que dividir un problema en subcasos no introduzca errores de doble conteo ni deje por fuera escenarios válidos, los subconjuntos empleados deben satisfacer tres condiciones conjuntistas estrictas.

> [!QUOTE] **Definición Formal 1:** Partición del Espacio Muestral
> 
> Sea $(\Omega, \mathcal{F}, \mathbb{P})$ un espacio de probabilidad. Una colección finita (o numerable) de eventos $\{B_1, B_2, \dots, B_n\} \subseteq \mathcal{F}$ constituye una **partición exhaustiva** del espacio muestral $\Omega$ si cumple simultáneamente:
> 
> 1. **Exclusión mutua dos a dos:** $B_i \cap B_j = \emptyset \quad \forall i \neq j$.
> 2. **Exhaustividad colectiva:** $\bigcup_{i=1}^n B_i = \Omega$.
> 3. **Probabilidad positiva:** $\mathbb{P}(B_i) > 0 \quad \forall i \in \{1, 2, \dots, n\}$.

Una partición equivale a cortar un pastel completo en rebanadas limpias sin que sobre ni una migaja y sin que ningún trozo quede montado encima de otro. Al realizar el experimento, cualquier resultado elemental $\omega \in \Omega$ caerá obligatoriamente dentro de una (y exactamente una) de las regiones $B_i$.

La tercera condición ($\mathbb{P}(B_i) > 0$) asegura que cada escenario tenga una probabilidad real de ocurrir. Este requisito evita divisiones entre cero cuando más adelante se calculen probabilidades condicionadas sobre cada subconjunto $B_i$.

> [!EXAMPLE] **Ejemplo 1:** Validación de una Partición por Turnos Académicos
> 
> En una facultad universitaria, cada estudiante está inscrito exclusivamente en uno de tres turnos de estudio: mañana ($M$), tarde ($T$) o noche ($N$). Los registros de matrícula indican que el $55\%$ de los alumnos estudia en la mañana, el $30\%$ en la tarde y el $15\%$ en la noche. Verifique si la colección $\{M, T, N\}$ constituye una partición válida del espacio muestral $\Omega$.

En este ejercicio analizamos la clasificación de una población estudiantil en tres categorías horarias. Lo que se busca es comprobar de forma ordenada las tres condiciones formales que definen una partición exhaustiva del espacio muestral antes de utilizar estas categorías para cálculos de probabilidad posteriores.

1. Verificamos la exclusión mutua comprobando que ningún estudiante puede pertenecer a dos turnos simultáneamente, por lo que las intersecciones por pares son vacías.

$$M \cap T = \emptyset, \qquad M \cap N = \emptyset, \qquad T \cap N = \emptyset$$

2. Comprobamos la exhaustividad colectiva sumando las proporciones de los tres turnos para confirmar que cubren el $100\%$ de la población estudiantil ($\mathbb{P}(\Omega) = 1$).

$$\mathbb{P}(M \cup T \cup N) = \mathbb{P}(M) + \mathbb{P}(T) + \mathbb{P}(N) = 0.55 + 0.30 + 0.15 = 1.00 = \mathbb{P}(\Omega)$$

3. Verificamos que cada turno posee una probabilidad estrictamente positiva, validando así las tres condiciones de la definición formal.

$$\mathbb{P}(M) = 0.55 > 0, \qquad \mathbb{P}(T) = 0.30 > 0, \qquad \mathbb{P}(N) = 0.15 > 0$$

## 1.2. La Ley de Probabilidad Total

Una vez establecida una partición $\{B_1, B_2, \dots, B_n\}$ sobre $\Omega$, cualquier evento transversal $A \subseteq \Omega$ queda dividido automáticamente en $n$ fragmentos disjuntos $A \cap B_i$. Si conocemos qué tan probable es cada escenario $B_i$ y cuál es la [[PROBA 2-2 Probabilidad Condicional#1. Probabilidad Condicional y Reducción del Espacio Muestral|probabilidad condicional]] de $A$ dentro de cada escenario $\mathbb{P}(A \mid B_i)$, podemos reconstruir la probabilidad global $\mathbb{P}(A)$ sumando los aportes ponderados de todas las ramas.

> [!QUOTE] **Teorema 1:** Ley de Probabilidad Total
> 
> Sea $\{B_1, B_2, \dots, B_n\}$ una partición exhaustiva del espacio muestral $\Omega$ con $\mathbb{P}(B_i) > 0$ para todo $i \in \{1, \dots, n\}$. Para cualquier evento $A \in \mathcal{F}$, su probabilidad total está dada por la suma ponderada:
> $$\mathbb{P}(A) = \sum_{i=1}^n \mathbb{P}(A \cap B_i) = \sum_{i=1}^n \mathbb{P}(A \mid B_i)\,\mathbb{P}(B_i)$$

La Ley de Probabilidad Total funciona como un promedio ponderado de escenarios. Imagina una fábrica con tres máquinas de distinta capacidad: la probabilidad global de que un artículo elegido al azar del almacén salga defectuoso no es el promedio simple de los porcentajes de fallo de cada máquina, sino la suma de la tasa de fallo de cada máquina multiplicada por la fracción de artículos que produce cada una.

Para demostrar formalmente el Teorema, combinamos la propiedad distributiva de la teoría de conjuntos con los [[PROBA 2-1 Espacios de Probabilidad y los Axiomas de Kolmogorov#2.1. Los Tres Axiomas Fundamentales|axiomas de Kolmogórov]] y la [[PROBA 2-2 Probabilidad Condicional#3. Ley Multiplicativa de la Probabilidad|ley multiplicativa]]:

1. **Identidad de intersección universal:** Dado que todo evento $A$ es subconjunto del espacio muestral $\Omega$ ($A \subseteq \Omega$), intersectar $A$ con el universo deja al conjunto inalterado:

$$A = A \cap \Omega$$

2. **Sustitución por la partición exhaustiva:** Reemplazamos $\Omega$ por la unión disjunta de los $n$ eventos que conforman la partición:

$$A = A \cap \left(\bigcup_{i=1}^n B_i\right)$$

3. **Propiedad distributiva de la intersección sobre la unión:** Distribuimos la intersección con $A$ a través de cada término de la unión:

$$A = \bigcup_{i=1}^n (A \cap B_i)$$

4. **Aditividad finita de Kolmogórov:** Como los conjuntos originales $B_i$ son mutuamente excluyentes dos a dos ($B_i \cap B_j = \emptyset$ para $i \neq j$), sus fragmentos recortados también son disjuntos: $(A \cap B_i) \cap (A \cap B_j) = A \cap (B_i \cap B_j) = A \cap \emptyset = \emptyset$. Aplicando el tercer axioma de Kolmogórov:

$$\mathbb{P}(A) = \mathbb{P}\left(\bigcup_{i=1}^n (A \cap B_i)\right) = \sum_{i=1}^n \mathbb{P}(A \cap B_i)$$

5. **Expansión mediante la ley multiplicativa:** Dado que $\mathbb{P}(B_i) > 0$ para todo $i$, sustituimos cada intersección $\mathbb{P}(A \cap B_i) = \mathbb{P}(A \mid B_i)\,\mathbb{P}(B_i)$:

$$\mathbb{P}(A) = \sum_{i=1}^n \mathbb{P}(A \mid B_i)\,\mathbb{P}(B_i) \quad \blacksquare$$

> [!EXAMPLE] **Ejemplo 2:** Proporción de Estudiantes Fumadores en una Universidad
> 
> De todos los estudiantes de una universidad, el $70\%$ son mujeres y el $30\%$ son hombres. Suponga que el $20\%$ de las mujeres y el $25\%$ de los hombres fuman cigarrillos. Si se selecciona un estudiante al azar, calcule la probabilidad de que sea:
> 
> 1. Una mujer fumadora.
> 2. Un hombre fumador.
> 3. Una persona fumadora (sin importar el sexo).

En este ejercicio partimos de una población universitaria dividida naturalmente en dos grupos mutuamente excluyentes y exhaustivos (mujeres y hombres), donde cada grupo presenta un hábito de consumo distinto. Lo que se busca es calcular primero las probabilidades conjuntas de cada subgrupo mediante la ley multiplicativa y luego reunir ambos aportes usando la Ley de Probabilidad Total para hallar la proporción global de fumadores.

1. Definimos los eventos $M$ («el estudiante es mujer»), $H$ («el estudiante es hombre») y $F$ («el estudiante fuma cigarrillos»), y expresamos los porcentajes del enunciado como probabilidades marginales y condicionales.

$$\mathbb{P}(M) = 0.70, \quad \mathbb{P}(H) = 0.30, \qquad \mathbb{P}(F \mid M) = 0.20, \quad \mathbb{P}(F \mid H) = 0.25$$

2. Calculamos la probabilidad de seleccionar una mujer fumadora ($M \cap F$) multiplicando la proporción de mujeres en la universidad por la tasa condicional de fumadoras dentro de ese grupo.

$$\mathbb{P}(M \cap F) = \mathbb{P}(F \mid M)\,\mathbb{P}(M) = (0.20)(0.70) = 0.14 \quad (14\%)$$

3. Calculamos la probabilidad de seleccionar un hombre fumador ($H \cap F$) aplicando el mismo producto sobre la rama correspondiente a los hombres.

$$\mathbb{P}(H \cap F) = \mathbb{P}(F \mid H)\,\mathbb{P}(H) = (0.25)(0.30) = 0.075 \quad (7.5\%)$$

4. Aplicamos la Ley de Probabilidad Total sumando las dos intersecciones disjuntas para obtener la probabilidad global de que el estudiante elegido al azar sea fumador.

$$\mathbb{P}(F) = \mathbb{P}(F \mid M)\,\mathbb{P}(M) + \mathbb{P}(F \mid H)\,\mathbb{P}(H) = 0.14 + 0.075 = 0.215 \quad (21.5\%)$$

# 2. Teorema de Bayes

La Ley de Probabilidad Total proyecta el comportamiento de un experimento hacia adelante: conocidas las causas $B_i$ y sus probabilidades de producir el efecto $A$, determina la frecuencia global del efecto. Sin embargo, en la práctica el problema suele plantearse al revés: el efecto $A$ ya ocurrió y fue observado, y lo que necesitamos averiguar es cuál de las causas $B_k$ lo produjo.

## 2.1. Inversión de Probabilidades Condicionales

Para invertir el sentido del condicionamiento (pasando de $\mathbb{P}(A \mid B_k)$ a $\mathbb{P}(B_k \mid A)$) combinamos la definición de probabilidad condicional con la Ley de Probabilidad Total.

> [!QUOTE] **Teorema 2:** Teorema de Bayes (Forma Generalizada)
> 
> Sea $\{B_1, B_2, \dots, B_n\}$ una partición exhaustiva del espacio muestral $\Omega$ con $\mathbb{P}(B_i) > 0$ para todo $i \in \{1, \dots, n\}$, y sea $A \in \mathcal{F}$ un evento observable tal que $\mathbb{P}(A) > 0$. Para cualquier causa específica $B_k$ ($1 \le k \le n$), la probabilidad condicional inversa está dada por:
> 
> $$\mathbb{P}(B_k \mid A) = \frac{\mathbb{P}(A \cap B_k)}{\mathbb{P}(A)} = \frac{\mathbb{P}(A \mid B_k)\,\mathbb{P}(B_k)}{\sum_{i=1}^n \mathbb{P}(A \mid B_i)\,\mathbb{P}(B_i)}$$

En el caso particular de dos escenarios donde la partición se reduce a una hipótesis $H$ y su complemento $H^c$ ($\Omega = H \cup H^c$), la expresión toma su forma binaria:

$$\mathbb{P}(H \mid A) = \frac{\mathbb{P}(A \mid H)\,\mathbb{P}(H)}{\mathbb{P}(A \mid H)\,\mathbb{P}(H) + \mathbb{P}(A \mid H^c)\,\mathbb{P}(H^c)}$$

El Teorema de Bayes es una regla matemática para actualizar nuestras estimaciones cuando aparece nueva información. Antes de observar ningún síntoma, partimos de una estimación inicial llamada probabilidad a priori $\mathbb{P}(B_k)$. Cuando ocurre la evidencia $A$, cada causa posible $B_i$ compite por explicar ese resultado según su verosimilitud $\mathbb{P}(A \mid B_i)$ (qué tan probable es ver el síntoma bajo esa causa). El numerador $\mathbb{P}(A \mid B_k)\mathbb{P}(B_k)$ mide el peso conjunto de la causa $k$ generando el síntoma, mientras que el denominador $\mathbb{P}(A)$ suma todas las maneras posibles en que el síntoma pudo aparecer, entregando la probabilidad a posteriori $\mathbb{P}(B_k \mid A)$.

> [!EXAMPLE] **Ejemplo 3:** Control de Fecha de Caducidad en una Fábrica de Películas
> 
> Cuatro inspectores de una fábrica de películas colocan la fecha de caducidad en cada paquete al final de la línea de montaje. Javier, quien revisa el $20\%$ de los paquetes, omite la fecha una vez cada $200$ paquetes; Alberto, que revisa el $60\%$, la omite una vez cada $100$ paquetes; Oscar, que revisa el $15\%$, la omite una vez cada $90$ paquetes; y Gustavo, que revisa el $5\%$, la omite una vez cada $200$ paquetes. Si un consumidor se queja de que su paquete no muestra la fecha de caducidad, ¿cuál es la probabilidad de que haya sido inspeccionado por Javier?

En este ejercicio de control de calidad industrial, la producción total se reparte entre cuatro inspectores con diferentes volúmenes de trabajo y distintas tasas de error humano. Lo que se busca es recorrer el proceso en sentido inverso: dado que se detectó un paquete sin fecha de caducidad, aplicaremos primero la Ley de Probabilidad Total para hallar la tasa global de omisión y luego el Teorema de Bayes para determinar qué proporción de esos fallos corresponde a Javier.

1. Definimos los eventos de la partición según el inspector asignado: $J$ (Javier), $A$ (Alberto), $O$ (Oscar) y $G$ (Gustavo), junto con el evento observado $S$ («el paquete no tiene fecha de caducidad»), verificando que las probabilidades a priori suman $1$.

$$\mathbb{P}(J) = 0.20, \quad \mathbb{P}(A) = 0.60, \quad \mathbb{P}(O) = 0.15, \quad \mathbb{P}(G) = 0.05$$

2. Traducimos la frecuencia de error de cada inspector en probabilidades condicionales $\mathbb{P}(S \mid B_i)$.

$$\mathbb{P}(S \mid J) = \frac{1}{200}, \quad \mathbb{P}(S \mid A) = \frac{1}{100}, \quad \mathbb{P}(S \mid O) = \frac{1}{90}, \quad \mathbb{P}(S \mid G) = \frac{1}{200}$$

3. Calculamos la probabilidad total $\mathbb{P}(S)$ de que un paquete salga sin fecha de caducidad ponderando el error de cada inspector por su fracción de trabajo, expresando las fracciones sobre un denominador común de $12\,000$ para evitar errores de redondeo.

$$\mathbb{P}(S) = (0.20)\left(\frac{1}{200}\right) + (0.60)\left(\frac{1}{100}\right) + (0.15)\left(\frac{1}{90}\right) + (0.05)\left(\frac{1}{200}\right)$$

$$\mathbb{P}(S) = \frac{1}{1000} + \frac{3}{500} + \frac{1}{600} + \frac{1}{4000} = \frac{12 + 72 + 20 + 3}{12\,000} = \frac{107}{12\,000} \approx 0.008917$$

4. Aplicamos el Teorema de Bayes dividiendo la contribución específica de Javier ($\mathbb{P}(S \mid J)\mathbb{P}(J) = \frac{1}{1000} = \frac{12}{12\,000}$) entre la probabilidad total $\mathbb{P}(S)$, concluyendo que existe aproximadamente un $11.21\%$ de probabilidad de que Javier haya revisado el paquete defectuoso.

$$\mathbb{P}(J \mid S) = \frac{\mathbb{P}(S \mid J)\,\mathbb{P}(J)}{\mathbb{P}(S)} = \frac{\frac{12}{12\,000}}{\frac{107}{12\,000}} = \frac{12}{107} \approx 0.1121 \quad (11.21\%)$$

## 2.2. Impacto de la Baja Prevalencia

Uno de los resultados más sorprendentes del Teorema de Bayes aparece cuando se aplican pruebas de diagnóstico masivo (como exámenes médicos de detección temprana, controles antidopaje o pruebas detectoras de mentiras) sobre grupos donde la condición buscada tiene una prevalencia inicial muy baja ($\mathbb{P}(C) \ll 1$). Este fenómeno se conoce como la paradoja del falso positivo o «falacia de la tasa base».

Cuando el $99\%$ o el $99.9\%$ de las personas evaluadas son sanas o inocentes ($\mathbb{P}(C^c) \approx 1$), incluso una tasa de error muy pequeña en personas sanas ($\mathbb{P}(E \mid C^c) = \alpha \ll 1$) se multiplica por una población enorme en el denominador de Bayes:

$$\mathbb{P}(C \mid E) = \frac{\mathbb{P}(E \mid C)\,\mathbb{P}(C)}{\mathbb{P}(E \mid C)\,\mathbb{P}(C) + \mathbb{P}(E \mid C^c)\,\mathbb{P}(C^c)}$$

Si la proporción inicial $\mathbb{P}(C)$ es parecida o menor que la tasa de falsos positivos $\mathbb{P}(E \mid C^c)$, el segundo término del denominador domina el cociente y desploma la probabilidad real $\mathbb{P}(C \mid E)$. Por esta razón, cuando una enfermedad afecta apenas a $1$ de cada $1000$ personas, incluso una prueba con $99\%$ de precisión arroja una mayoría de falsos positivos, obligando a los médicos a realizar un segundo examen confirmatorio antes de iniciar tratamientos agresivos.

![[PROBA 2-3 Ley de Probabilidad Total y Teorema de Bayes - La Paradoja del Falso Positivo de Bayes.webp]]

La siguiente tabla resume el significado de cada componente del Teorema de Bayes y su papel en problemas de diagnóstico y control de calidad:

| **Componente Bayesiano** | **Símbolo / Expresión** | **Significado Estadístico** | **Rol en Diagnóstico y Control** |
| --- | --- | --- | --- |
| **Probabilidad a Priori** | $\mathbb{P}(C_i)$ | Estimación base antes de observar evidencia | Proporción histórica de enfermos o piezas defectuosas. |
| **Verosimilitud** | $\mathbb{P}(E \mid C_i)$ | Probabilidad del síntoma dado el estado | Sensibilidad de la prueba médica o tasa de error de un operario. |
| **Probabilidad Total (Evidencia)** | $\mathbb{P}(E) = \sum \mathbb{P}(E \mid C_j)\mathbb{P}(C_j)$ | Frecuencia global del síntoma en toda la población | Proporción total de exámenes positivos o quejas recibidas. |
| **Probabilidad a Posteriori** | $\mathbb{P}(C_i \mid E)$ | Probabilidad actualizada tras observar $E$ | Certeza final de que el paciente esté enfermo tras dar positivo. |

> [!EXAMPLE] **Ejemplo 4:** Evaluación de Confiabilidad de un Suero de la Verdad
> 
> Un suero de la verdad es suministrado a un sospechoso. Se sabe que este suero es $90\%$ confiable cuando la persona es culpable y $99\%$ confiable si la persona es inocente. Si el sospechoso fue seleccionado de un grupo de sujetos de los cuales solo el $5\%$ han cometido un crimen y el suero indica que es culpable, ¿cuál es la probabilidad de que sea inocente?

En este problema se evalúa una prueba forense aplicada sobre un grupo donde la gran mayoría de las personas son inocentes. Lo que se busca es calcular la probabilidad inversa de que el sospechoso sea inocente a pesar de que el suero lo señale como culpable, demostrando cómo una baja proporción inicial de culpables genera una fracción significativa de falsos positivos.

1. Definimos los eventos $C$ («la persona es culpable»), $C^c$ («la persona es inocente») y $P$ («el suero indica que es culpable»), asignando las probabilidades iniciales del grupo.

$$\mathbb{P}(C) = 0.05, \qquad \mathbb{P}(C^c) = 1 - 0.05 = 0.95$$

2. Traducimos la confiabilidad del suero en probabilidades condicionales: si es $90\%$ confiable en culpables, acierta indicando culpabilidad con probabilidad $0.90$; si es $99\%$ confiable en inocentes, acierta indicando inocencia con probabilidad $0.99$, por lo que se equivoca señalando culpabilidad (falso positivo) con probabilidad $0.01$.

$$\mathbb{P}(P \mid C) = 0.90, \qquad \mathbb{P}(P^c \mid C^c) = 0.99 \implies \mathbb{P}(P \mid C^c) = 1 - 0.99 = 0.01$$

3. Aplicamos la Ley de Probabilidad Total para calcular la probabilidad global $\mathbb{P}(P)$ de que el suero indique que el sospechoso es culpable.

$$\mathbb{P}(P) = \mathbb{P}(P \mid C)\,\mathbb{P}(C) + \mathbb{P}(P \mid C^c)\,\mathbb{P}(C^c) = (0.90)(0.05) + (0.01)(0.95) = 0.045 + 0.0095 = 0.0545$$

4. Aplicamos el Teorema de Bayes para hallar la probabilidad a posteriori $\mathbb{P}(C^c \mid P)$ de que el sospechoso sea inocente dado el resultado positivo del suero, comprobando que casi $1$ de cada $6$ personas señaladas por la prueba ($17.43\%$) es realmente inocente.

$$\mathbb{P}(C^c \mid P) = \frac{\mathbb{P}(P \mid C^c)\,\mathbb{P}(C^c)}{\mathbb{P}(P)} = \frac{0.0095}{0.0545} = \frac{19}{109} \approx 0.1743 \quad (17.43\%)$$

# 3. Clasificación Bayesiana con Múltiples Evidencias (Modelo Naïve Bayes)

En muchas decisiones reales no contamos con un único síntoma aislado, sino con un conjunto simultáneo de $d$ observaciones o pistas $E = \{w_1, w_2, \dots, w_d\}$ (por ejemplo, varios síntomas clínicos en un paciente o distintas características físicas en una muestra). Evaluar la probabilidad de que el caso pertenezca a una categoría $C_k$ exige extender el Teorema de Bayes para combinar todas esas evidencias a la vez.

## 3.1. Asunción de Independencia Condicional y Razón de Verosimilitud

Cuando se observan $d$ síntomas simultáneamente, aplicar el Teorema de Bayes requiere conocer la probabilidad conjunta $\mathbb{P}(w_1, w_2, \dots, w_d \mid C_k)$. Sin embargo, estimar directamente todas las combinaciones posibles de $d$ síntomas a partir de registros históricos exige una cantidad gigantesca de casos observados, ya que muchas combinaciones particulares nunca habrán ocurrido juntas en el pasado.

Para resolver esta limitación surge el modelo **Naïve Bayes** (Bayes Ingenuo), que simplifica el cálculo asumiendo [[PROBA 2-2 Probabilidad Condicional#2. Independencia Estadística|independencia estadística]] condicional entre los síntomas una vez que se conoce la categoría real $C_k$:

$$\mathbb{P}(w_1, w_2, \dots, w_d \mid C_k) = \prod_{j=1}^d \mathbb{P}(w_j \mid C_k)$$

> [!QUOTE] **Definición Formal 2:** Clasificador Binario Naïve Bayes
> 
> Dadas dos categorías mutuamente excluyentes y exhaustivas $C_1$ y $C_2$ y un conjunto de $d$ evidencias observadas $w_1, \dots, w_d$ condicionalmente independientes dada cada categoría, la probabilidad a posteriori de pertenecer a la categoría $C_1$ está dada por la razón de verosimilitud:
> 
> $$r(w_1, \dots, w_d) = \mathbb{P}(C_1 \mid w_1, \dots, w_d) = \frac{\mathbb{P}(C_1) \prod_{j=1}^d \mathbb{P}(w_j \mid C_1)}{\mathbb{P}(C_1) \prod_{j=1}^d \mathbb{P}(w_j \mid C_1) + \mathbb{P}(C_2) \prod_{j=1}^d \mathbb{P}(w_j \mid C_2)}$$

Esta fórmula multiplica la probabilidad inicial de cada categoría por las probabilidades individuales de observar cada síntoma dentro de esa categoría. De este modo, cada síntoma aporta su propio peso a favor o en contra de la hipótesis sin necesidad de haber observado exactamente la misma combinación de síntomas en el historial previo.

## 3.2. Ventajas y Limitaciones del Supuesto de Independencia Condicional

Utilizar la hipótesis de independencia condicional implica un equilibrio claro entre simplicidad de cálculo y realismo del modelo:

- **Reducción drástica de datos necesarios:** Si se tienen $d$ síntomas binarios (presente o ausente), calcular todas sus combinaciones conjuntas sin suponer independencia requeriría estimar $2^d - 1$ probabilidades distintas por categoría (por ejemplo, para $d = 10$ síntomas harían falta $1023$ combinaciones). Al asumir independencia condicional, basta con estimar únicamente $d$ probabilidades individuales $\mathbb{P}(w_j \mid C_k)$, pasando de un crecimiento exponencial $O(2^d)$ a uno lineal $O(d)$.

- **Pérdida de relación entre síntomas:** El precio de esta simplicidad es que el modelo trata cada síntoma por separado e ignora si dos síntomas suelen aparecer vinculados entre sí (por ejemplo, en diagnóstico médico la fiebre alta y los escalofríos suelen presentarse juntos por un mismo mecanismo fisiológico). A pesar de esta simplificación, el modelo suele acertar en la clasificación final porque basta con que la categoría correcta acumule mayor probabilidad relativa que su alternativa.

> [!EXAMPLE] **Ejemplo 5:** Diagnóstico Clínico Diferencial con Dos Síntomas Simultáneos
> En una clínica se revisa un historial de $3000$ consultas respiratorias compuestas por $2000$ casos confirmados de gripe ($G$) y $1000$ casos de alergia estacional ($A$). En los pacientes con gripe, el síntoma «fiebre alta» ($w_1$) aparece en $500$ casos y «dolor muscular» ($w_2$) en $600$ casos; en los pacientes con alergia, «fiebre alta» aparece en $20$ casos y «dolor muscular» en $50$ casos. Calcule la probabilidad de que un paciente que acude a consulta con ambos síntomas simultáneamente tenga gripe, asumiendo independencia condicional entre síntomas.

En este ejercicio aplicamos el clasificador binario Naïve Bayes a una situación cotidiana de diagnóstico médico con dos categorías posibles y dos síntomas observados al mismo tiempo. La finalidad es combinar las proporciones iniciales de cada afección en la clínica con las frecuencias individuales de cada síntoma para calcular la probabilidad actualizada de gripe.

1. Calculamos las probabilidades a priori de gripe y alergia estacional a partir de las frecuencias totales del historial clínico de $N = 3000$ pacientes.

$$\mathbb{P}(G) = \frac{2000}{3000} = \frac{2}{3}, \qquad \mathbb{P}(A) = \frac{1000}{3000} = \frac{1}{3}$$

2. Estimamos las probabilidades condicionales (verosimilitudes) de observar «fiebre alta» ($w_1$) y «dolor muscular» ($w_2$) dentro de cada grupo clínico.

$$\mathbb{P}(w_1 \mid G) = \frac{500}{2000} = 0.25, \qquad \mathbb{P}(w_2 \mid G) = \frac{600}{2000} = 0.30$$

$$\mathbb{P}(w_1 \mid A) = \frac{20}{1000} = 0.02, \qquad \mathbb{P}(w_2 \mid A) = \frac{50}{1000} = 0.05$$

3. Aplicamos la hipótesis de independencia condicional multiplicando las verosimilitudes de ambos síntomas dentro de cada diagnóstico, observando que la combinación es $75$ veces más probable bajo gripe ($0.075$) que bajo alergia ($0.001$).

$$\mathbb{P}(w_1, w_2 \mid G) = (0.25)(0.30) = 0.075, \qquad \mathbb{P}(w_1, w_2 \mid A) = (0.02)(0.05) = 0.001$$

4. Sustituimos las probabilidades a priori y las verosimilitudes conjuntas en la fórmula de Bayes para dos categorías, obteniendo una probabilidad del $99.34\%$ de que el paciente tenga gripe.

$$\mathbb{P}(G \mid w_1, w_2) = \frac{\frac{2}{3}(0.075)}{\frac{2}{3}(0.075) + \frac{1}{3}(0.001)} = \frac{0.05}{0.05 + \frac{0.001}{3}} = \frac{0.15}{0.151} = \frac{150}{151} \approx 0.9934 \quad (99.34\%)$$

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