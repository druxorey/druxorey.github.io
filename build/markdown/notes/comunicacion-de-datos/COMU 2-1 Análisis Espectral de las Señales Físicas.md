---
created: 2026-05-04T23:59:00
title: Análisis Espectral de las Señales Físicas
semester: 5
subject:
  - "[[COMU 0-0 Nota Informativa|Comunicación de Datos]]"
unit: 2
status: done
---

<h1 id="main-title"  align="center"> Análisis Espectral de las Señales Físicas </h1>

> [!TLDR] SÍNTESIS 
> Las **señales físicas** transforman los datos abstractos en perturbaciones electromagnéticas continuas o discretas capaces de viajar a través de un **medio de transmisión**. Su comportamiento se analiza mediante la dualidad entre el **dominio del tiempo** y el **dominio de la frecuencia**, utilizando el **análisis espectral** para descomponer formas de onda complejas. Asimismo, la calidad de la **propagación inalámbrica** depende del despeje geométrico en las **zonas de Fresnel** y de la compensación del **efecto Doppler**.

Los medios de transmisión no son canales ideales; la geometría del espacio, los obstáculos materiales y las pérdidas energéticas imponen fronteras estrictas a la distancia que una onda puede recorrer antes de extinguirse o deformarse. Para diseñar redes capaces de superar estas barreras naturales sin corromper la información es necesario tratar el medio físico como un conducto con irregularidades.

# 1. Naturaleza y Parámetros de las Señales Físicas

En el nivel de la capa física, los datos abstractos dejan de ser bits lógicos para convertirse en perturbaciones electromagnéticas continuas capaces de viajar por un medio de transmisión.

## 1.1. Datos Digitales y Señales Analógicas

Toda transmisión electromagnética involucra la conversión de información en una magnitud física medible que varía en el tiempo.

> [!QUOTE] **Definición 1:** Señal Electromagnética
> 
> Una señal electromagnética es una función temporal continua $s(t)$ que describe la oscilación acoplada de un campo eléctrico $\vec{E}(t)$ y un campo magnético $\vec{B}(t)$, capaz de transferir energía e información a través del espacio libre o de un medio físico guiado.

Para clasificar los elementos de la comunicación, distinguimos formalmente entre la naturaleza de los datos y la forma de la señal:

- **Datos analógicos:** Información continua del mundo real que puede tomar infinitos valores intermedios dentro de un intervalo medible (como la presión acústica de la voz humana, la temperatura ambiental o la intensidad lumínica).

- **Datos digitales:** Información codificada en un conjunto finito y discreto de estados lógicos bien diferenciados (como las cadenas de ceros y unos almacenadas en memoria).

- **Señales analógicas:** Ondas continuas cuya amplitud evoluciona de manera suave en el tiempo, pasando por infinitos niveles intermedios de voltaje o intensidad de campo.

- **Señales digitales:** Formas de onda que alternan de manera escalonada entre un número finito y determinado de niveles discretos de tensión (por ejemplo, $+5\text{ V}$ para representar un «1» binario y $0\text{ V}$ para un «0» binario).

Ambos conceptos se articulan en cuatro combinaciones operativas fundamentales:

1. **Datos analógicos en señales analógicas:** La voz capturada por un micrófono modula directamente la tensión continua de un circuito telefónico convencional.

2. **Datos analógicos en señales digitales:** La señal acústica de voz se muestrea, se cuantifica y se convierte en una secuencia de bits binarios (como en la modulación por impulsos codificados, PCM).

3. **Datos digitales en señales analógicas:** Una computadora transmite paquetes binarios a través del aire modulando la amplitud, la frecuencia o la fase de una onda portadora de radio.

4. **Datos digitales en señales digitales:** Una tarjeta de red transmite tramas binarias directamente sobre un cable de cobre mediante pulsos de tensión discretos (como la codificación Manchester o NRZ en Ethernet).

## 1.2. Parámetros Fundamentales de la Onda Sinusoidal Pura

La onda sinusoidal pura constituye la función periódica elemental en física ondulatoria. Representa la oscilación más simple posible y sirve como base para construir cualquier forma de onda más compleja.

> [!QUOTE] **Definición 2:** Onda Sinusoidal Pura
> 
> Una onda sinusoidal simple se describe en el dominio del tiempo mediante la expresión matemática:
> 
> $$s(t) = A \cdot \sin(2\pi f t + \phi)$$
> 
> donde:
> 
> - $A$ es la amplitud pico de la oscilación ($A \in \mathbb{R}^+$), medida en voltios ($\text{V}$) para señales eléctricas.
> - $f$ es la frecuencia temporal de la señal, medida en hercios ($\text{Hz}$).
> - $t$ es el tiempo continuo, medido en segundos ($\text{s}$).
> - $\phi$ es la fase inicial de la onda en el instante de referencia $t = 0$, medida en radianes o grados.

Pensemos en el pedal de una bicicleta que gira a un ritmo perfectamente constante visto desde un lateral. La altura máxima que alcanza el pedal por encima del eje central representa la amplitud pico ($A$). El número de vueltas completas que da el pedal en un segundo corresponde a la frecuencia ($f$). El ángulo exacto en el que se encontraba el pedal en el momento preciso en que encendimos el cronómetro marca la fase inicial ($\phi$).

### 1.2.1. Período, Frecuencia y Longitud de Onda Espacial

La oscilación temporal de la fuente y la extensión geométrica que ocupa la perturbación en el espacio físico están gobernadas por la velocidad de propagación del medio.

> [!QUOTE] **Definición 3:** Período y Longitud de Onda
> 
> El período ($T$) es la duración temporal exacta que tarda una señal periódica en completar un ciclo entero:
> 
> $$T = \frac{1}{f} \iff f = \frac{1}{T}$$
> 
> La longitud de onda espacial ($\lambda$) es la distancia física lineal que recorre el frente de onda a través del medio durante el transcurso de un período completo:
> 
> $$\lambda = \frac{v}{f} = v \cdot T$$
> 
> siendo $v$ la velocidad de propagación de la perturbación en el canal. Para ondas electromagnéticas en el vacío o en el aire, se toma la velocidad de la luz: $c \approx 3 \times 10^8\text{ m/s}$.

### 1.2.2. Amplitud Pico frente a Valor Cuadrático Medio (RMS)

Una señal alterna no entrega su tensión máxima de manera continua, ya que su valor instantáneo varía en cada punto del ciclo y cruza el eje de cero voltios dos veces por cada período completo.
  
> [!QUOTE] **Definición 4:** Valor Cuadrático Medio o Eficaz ($V_{\text{rms}}$)
> 
> El valor cuadrático medio ($V_{\text{rms}}$, _Root Mean Square_) de una señal sinusoidal pura representa la magnitud equivalente de tensión continua ($\text{DC}$) que disipa exactamente la misma potencia térmica sobre una resistencia de carga resistiva pura:
> 
>   
> 
> $$V_{\text{rms}} = \sqrt{\frac{1}{T} \int_{0}^{T} s^2(t)\,dt} = \frac{V_{\text{pico}}}{\sqrt{2}} \approx 0.7071 \cdot V_{\text{pico}}$$
> 
> De forma inversa, la amplitud de pico máxima se relaciona con el valor eficaz mediante:
> 
>   
> 
> $$V_{\text{pico}} = V_{\text{rms}} \cdot \sqrt{2} \approx 1.4142 \cdot V_{\text{rms}}$$

> [!EXAMPLE] **Ejemplo 1:** Tensión Pico y Longitud de Onda en un Enlace de Microondas 
> 
> Un radioenlace inalámbrico opera con una portadora sinusoidal pura a $f = 6\text{ GHz}$ ($6 \times 10^9\text{ Hz}$) y entrega a la entrada del circuito receptor un valor eficaz de $V_{\text{rms}} = 120\text{ mV}$. Calcule la amplitud pico real ($V_{\text{pico}}$) que experimenta el semiconductor y la longitud de onda física ($\lambda$) en el aire.
 
**Paso 1:** Al diseñar los circuitos de entrada del receptor, no basta con proteger los transistores contra los $120\text{ mV}$ eficaces nominales. La onda alcanza crestas de casi $170\text{ mV}$, por lo que calculamos la amplitud pico multiplicando el valor eficaz por el factor $\sqrt{2}$ para fijar la tolerancia dieléctrica real:
     
$$V_{\text{pico}} = V_{\text{rms}} \cdot \sqrt{2} = (120 \times 10^{-3}\text{ V}) \cdot 1.4142 \approx 169.70\text{ mV}$$

**Paso 2:** Expresamos la frecuencia en unidades base del Sistema Internacional ($6\text{ GHz} = 6 \times 10^9\text{ Hz}$) y dividimos la velocidad de la luz ($3 \times 10^8\text{ m/s}$) entre dicho valor para calcular la longitud de onda espacial. Un ciclo espacial de la portadora mide apenas $5\text{ centímetros}$, lo que permite dimensionar antenas muy compactas para captar la señal con eficiencia:
     
$$\lambda = \frac{c}{f} = \frac{3 \times 10^8\text{ m/s}}{6 \times 10^9\text{ Hz}} = 0.05\text{ m} = 5\text{ cm}$$

# 2. Dominio de la Frecuencia y Análisis Espectral

Una sinusoide pura individual no transmite información útilo. Para codificar datos binarios o analógicos, la señal debe experimentar variaciones temporales en amplitud, frecuencia o fase, convirtiéndose en una señal compuesta por múltiples componentes sinusoidales simultáneas.

## 2.1. El Dominio del Tiempo y de la Frecuencia

El comportamiento de una señal física se analiza desde dos perspectivas complementarias y equivalentes.

> [!QUOTE] **Definición 5:** Dominios de Representación Temporal y Espectral
> 
> El **dominio del tiempo** describe una señal mediante la función $s(t)$, representando su amplitud instantánea a lo largo del eje temporal continuo $t$.
> 
> El **dominio de la frecuencia** o espectro $S(f)$ representa la distribución de amplitudes y fases de las sinusoides puras constitutivas que integran la señal frente al eje continuo o discreto de frecuencias $f$.

Imagina que un amigo te manda una nota de voz hablando. 

- **El dominio del tiempo** es la forma en que ves el archivo de audio al abrirlo en WhatsApp: una línea ondulada (onda) que muestra cómo sube y baja el volumen del sonido segundo a segundo.

- **El dominio de la frecuencia** es como un ecualizador gráfico (las barritas que suben y bajan en Spotify): te muestra exactamente cuántos graves, medios y agudos componen esa voz en ese mismo instante. 

Ambos son exactamente el mismo audio, pero mientras el primero te muestra *cómo evoluciona en el tiempo*, el segundo te muestra *qué notas o frecuencias lo forman*. La instrumentación de laboratorio y las características del espectro se organizan según dos criterios operativos:

- **Osciloscopio frente a Analizador de Espectro:** El **osciloscopio** captura y dibuja directamente la función temporal $s(t)$ en un plano de tensión frente a tiempo ($V$ vs. $t$). El **analizador de espectro** procesa la señal mediante filtros sintonizados o algoritmos FFT para graficar la potencia o la amplitud en función de la frecuencia ($V$ vs. $f$), permitiendo medir con exactitud armónicos e interferencias parásitas.

- **Espectro discreto (de líneas) frente a Espectro continuo:**

    - Las **señales periódicas** generan un espectro discreto compuesto exclusivamente por líneas verticales delgadas (deltas ponderadas) situadas en la frecuencia fundamental $f_0$ y en múltiplos enteros exactos $n f_0$. Entre dos armónicos sucesivos, la potencia espectral es idénticamente nula.

    - Las **señales aperiódicas** (como un pulso rectangular aislado o un tren aleatorio de datos) no se repiten en un período finito ($T_0 \to \infty$). En este caso, la separación entre armónicos infinitesimales se anula ($\Delta f = 1/T_0 \to 0$), provocando que las líneas discretas se fusionen en un espectro continuo distribuido a lo largo del eje frecuencial.

## 2.2. Series de Fourier y Descomposición Armónica

Cualquier forma de onda periódica puede sintetizarse sumando un conjunto determinado de ondas sinusoidales elementales.

> [!QUOTE] **Definición 6:** Serie Trigonométrica de Fourier
> 
> Toda señal periódica real $x(t)$ de período fundamental $T_0$ y frecuencia fundamental $f_0 = 1/T_0$ que satisfaga las condiciones de Dirichlet puede descomponerse de forma unívoca en la serie infinita:
> 
> $$x(t) = a_0 + \sum_{n=1}^{\infty} \left[ a_n \cos(2\pi n f_0 t) + b_n \sin(2\pi n f_0 t) \right]$$
> 
> donde los coeficientes reales vienen dados por:
> 
> $$a_0 = \frac{1}{T_0} \int_{0}^{T_0} x(t)\,dt$$
> 
> $$a_n = \frac{2}{T_0} \int_{0}^{T_0} x(t) \cos(2\pi n f_0 t)\,dt, \qquad b_n = \frac{2}{T_0} \int_{0}^{T_0} x(t) \sin(2\pi n f_0 t)\,dt$$

A partir de esta formulación matemática, se definen los parámetros de análisis espectral:

- **Componente continua ($a_0$):** Valor promedio en el tiempo de la señal a lo largo de un período completo (corresponde a la frecuencia cero o $\text{DC}$).

- **Frecuencia fundamental ($f_0$):** La componente oscilatoria más lenta presente en la descomposición ($n = 1$), cuyo valor coincide con la inversa del período de repetición de la onda compuesta ($f_0 = 1/T_0$).

- **Armónicos de orden superior ($n \cdot f_0$):** Componentes sinusoidales cuyas frecuencias corresponden a múltiplos enteros estrictos de la fundamental ($2f_0, 3f_0, 4f_0, \dots$).

- **Ancho de banda espectral ($B$):** La diferencia cuantitativa entre la frecuencia más alta ($f_{\text{máx}}$) y la frecuencia más baja ($f_{\text{mín}}$) con potencia significativa dentro del espectro compuesto:

$$B = f_{\text{máx}} - f_{\text{mín}}$$

> [!EXAMPLE] **Ejemplo 2:** Armónicos y Ancho de Banda de una Señal Compuesta
> 
> Se inyecta en una línea de transmisión una señal periódica formada por un nivel de continua de $2\text{ V}$, una fundamental de $f_0 = 2.5\text{ kHz}$, su tercer armónico ($n=3$) y su quinto armónico ($n=5$). Calcule las frecuencias presentes en el medio y el ancho de banda espectral activo ($B$).

**Paso 1:** Al ser una señal estrictamente periódica, los armónicos solo pueden aparecer en múltiplos enteros de la fundamental $f_0 = 2.5\text{ kHz}$. Calculamos sus frecuencias multiplicando el orden por la fundamental:

$$f_1 = f_0 = 2.5\text{ kHz}$$
$$f_3 = 3 \cdot f_0 = 3 \cdot (2.5\text{ kHz}) = 7.5\text{ kHz}$$
$$f_5 = 5 \cdot f_0 = 5 \cdot (2.5\text{ kHz}) = 12.5\text{ kHz}$$

**Paso 2:** La componente de corriente continua se sitúa en $0\text{ Hz}$. Calculamos el ancho de banda espectral restando la componente alterna más alta de la más baja, obteniendo el rango entre la frecuencia oscilatoria inferior ($2.5\text{ kHz}$) y la superior ($12.5\text{ kHz}$):

$$B = f_{\text{máx}} - f_{\text{mín}} = 12.5\text{ kHz} - 2.5\text{ kHz} = 10.0\text{ kHz}$$

Cualquier canal que transporte esta señal debe disponer de un ancho de banda útil de al menos $10.0\text{ kHz}$ para no mutilar dichos armónicos.

## 2.3. Espectro Armónico de la Onda Cuadrada Digital Ideal

Las señales binarias que circulan por los circuitos de procesamiento digital adoptan la forma de pulsos rectangulares o cuadrados. El análisis de Fourier de esta forma de onda revela una limitación física fundamental de los canales de telecomunicación.

Consideremos una onda cuadrada simétrica con valor medio nulo, amplitud pico $A$, período $T_0$ y frecuencia fundamental $f_0$. Por simetría de media onda impar, los coeficientes pares y los cosenos se anulan ($a_0 = 0$, $a_n = 0$, $b_{2k} = 0$), quedando únicamente los senos de orden impar:

$$x_{\text{cuadrada}}(t) = \frac{4A}{\pi} \sum_{k=1,3,5,\dots}^{\infty} \frac{1}{k} \sin(2\pi k f_0 t) = \frac{4A}{\pi} \left[ \sin(2\pi f_0 t) + \frac{1}{3}\sin(6\pi f_0 t) + \frac{1}{5}\sin(10\pi f_0 t) + \dots \right]$$

Esta serie matemática arroja tres conclusiones estructurales:

1. **Ausencia de armónicos pares:** La señal está compuesta exclusivamente por la fundamental ($f_0$) y los armónicos impares ($3f_0, 5f_0, 7f_0, \dots$).

2. **Decaimiento hiperbólico de amplitud:** La amplitud de cada armónico decae de forma proporcional a la inversa de su orden ($1/k$). El tercer armónico tiene un tercio de la amplitud fundamental; el quinto armónico, un quinto; y así sucesivamente.

3. **Exigencia de ancho de banda infinito:** Para generar esquinas rectas perfectas y transiciones verticales instantáneas (tiempo de subida $t_r = 0$), se requiere sumar una cantidad infinita de armónicos impares. Por tanto, una onda cuadrada digital ideal requiere un ancho de banda teórico estrictamente infinito:


$$B_{\text{ideal}} = \lim_{k \to \infty} (k \cdot f_0) - f_0 = \infty$$

Dado que todo medio físico de transmisión real presenta un ancho de banda finito, las componentes de alta frecuencia resultan atenuadas o filtradas por completo. Cuando un canal elimina los armónicos superiores, los flancos verticales de los pulsos pierden pendiente y se redondean. En la práctica ingenieril, permitir el paso de la fundamental junto al tercer y quinto armónico retiene más del 90% de la energía de la señal, preservando una forma de onda suficientemente definida para que el circuito receptor tome muestras lógicas sin cometer errores de decisión de bit.


## 2.4. Canales Paso-Bajo frente a Paso-Banda y Modos de Transmisión

La respuesta en frecuencia del medio físico condiciona la técnica de transmisión que debe emplearse para inyectar la señal.

> [!QUOTE] **Definición 7:** Canal Paso-Bajo y Canal Paso-Banda
> 
> Un **canal paso-bajo** (_low-pass_) es un medio de transmisión cuya respuesta en frecuencia admite el paso de señales desde $0\text{ Hz}$ hasta una frecuencia de corte superior finita $f_c$, presentando un ancho de banda $B = f_c$.
> 
> Un **canal paso-banda** (_bandpass_) es un medio de transmisión que solo permite la propagación de frecuencias situadas dentro de un intervalo acotado $[f_1, f_2]$, con $0 < f_1 < f_2$, bloqueando tanto las frecuencias cercanas a continua como las muy elevadas, con un ancho de banda $B = f_2 - f_1$.

De esta clasificación electromagnética surgen las dos modalidades operativas de transmisión:

- **Transmisión en Banda Base (_Baseband_):** La señal eléctrica digital o analógica se inyecta directamente sobre el medio de transmisión sin modular ninguna portadora sinusoidal de alta frecuencia. Debido a que los pulsos digitales contienen componentes frecuenciales concentradas cerca de continua ($0\text{ Hz}$), la transmisión en banda base exige obligatoriamente un **canal paso-bajo**. Es la técnica universal en redes de área local guiadas (cable de par trenzado en Ethernet) y buses entre circuitos integrados.

- **Transmisión en Banda Ancha (_Broadband_):** La señal de datos original modula en amplitud, frecuencia o fase una portadora sinusoidal de frecuencia central $f_c \gg 0$, desplazando el espectro hacia una banda superior apta para el medio. Opera invariablemente sobre **canales paso-banda**. Permite transmitir a través de medios no guiados (antenas de radio, telefonía celular, Wi-Fi) o canalizar múltiples canales independientes mediante multiplexación por división de frecuencia (FDM) dentro de un único cable coaxial o fibra óptica.
  
# 3. Propagación Inalámbrica

Cuando las ondas electromagnéticas se propagan por el espacio libre sin confinamiento metálico o dieléctrico, la calidad de la comunicación depende de la geometría espacial tridimensional del trayecto y de la cinemática de los terminales.

## 3.1. Zonas de Fresnel y Despeje Geométrico de Enlaces

En enlaces inalámbricos con visibilidad directa (LOS, _Line-of-Sight_), la energía radiada por las antenas no viaja restringida a una línea delgada unidimensional. La radiación se expande por el espacio formando una familia de elipsoides de revolución concéntricos cuyos focos se ubican en la antena transmisora y en la antena receptora.

> [!QUOTE] **Definición 8:** Radio de la Enésima Zona de Fresnel
> 
> El radio transversal $F_n$ de la frontera circular de la zona de Fresnel de orden $n \in \mathbb{Z}^+$ en un punto intermedio situado a distancias de visión $d_1$ y $d_2$ de los extremos del enlace se define como:
> 
> $$F_n = \sqrt{\frac{n \cdot \lambda \cdot d_1 \cdot d_2}{d_1 + d_2}}$$
> 
> donde $\lambda$ es la longitud de onda de la señal, y $d_1, d_2$ son las distancias lineales desde el obstáculo hacia el transmisor y el receptor, respectivamente (todas las variables en metros).

La interferencia entre los rayos difractados y el rayo directo determina el comportamiento ondulatorio:

- **Primera Zona de Fresnel ($n = 1$, Elipsoide Constructivo):** Representa el volumen envolvente donde la diferencia de camino óptico entre una trayectoria reflejada en el borde y la trayectoria directa central es menor o igual a media longitud de onda ($\Delta d \le \lambda/2$). Esto se traduce en un desfase de llegada al receptor menor a $180^\circ$ ($\Delta\phi \le \pi$), provocando que las ondas se sumen constructivamente con la señal principal. Alberga la mayor concentración de potencia del enlace.

- **Segunda Zona de Fresnel ($n = 2$, Elipsoide Destructivo):** Comprende el volumen anular donde la diferencia de camino óptico se sitúa entre media longitud de onda y una longitud de onda completa ($\lambda/2 < \Delta d \le \lambda$). El desfase de llegada se encuentra entre $180^\circ$ y $360^\circ$, generando interferencia destructiva que sustrae potencia neta al rayo directo en la antena receptora.

### 3.1.1. Ecuación Simplificada en el Punto Medio y Margen Normativo

En el diseño práctico de radioenlaces terrestres, el punto crítico de máximo abultamiento ocurre en el centro exacto de la trayectoria ($d_1 = d_2 = d_{\text{total}}/2$).

> [!QUOTE] **Definición 8:** Radio Central de Fresnel y Regla del 60%
> 
> En el punto medio de un enlace simétrico, el radio de la primera zona de Fresnel ($F_{1,\text{centro}}$) se expresa en unidades prácticas de ingeniería como:
> 
> $$F_{1,\text{centro}} = 8.65 \cdot \sqrt{\frac{d_{\text{total}}\text{ (km)}}{f\text{ (GHz)}}}$$
> 
> con $F_1$ en metros ($\text{m}$), la distancia total $d_{\text{total}}$ en kilómetros ($\text{km}$), y la frecuencia de portadora $f$ en gigahercios ($\text{GHz}$).
> 
> **Criterio normativo de despeje:** Para que las pérdidas por difracción de borde de cuchillo sean despreciables ($< 1\text{ dB}$), el perfil topográfico exige mantener libre de cualquier obstrucción física al menos el **60% del radio de la primera zona de Fresnel** ($0.6 \cdot F_1$) en cualquier punto del trayecto.

Si un obstáculo físico (vegetación, colinas o construcciones urbanas) invade esa zona de guarda del 60%, la difracción introduce una atenuación severa que puede degradar o interrumpir el enlace, aun cuando exista una línea visual directa sin obstrucción aparente entre los extremos.

> [!EXAMPLE] **Ejemplo 3:** Despeje y Altura Mínima de Torres en un Enlace Rural
> 
> Un enlace inalámbrico punto a punto se proyecta sobre una distancia total de $d_{\text{total}} = 16\text{ km}$ a una frecuencia de portadora de $f = 5.8\text{ GHz}$. En el punto medio del trayecto ($d_1 = d_2 = 8\text{ km}$), una arboleda tiene una altura de $h_{\text{obs}} = 12\text{ m}$ sobre el suelo plano. Calcule el radio de la primera zona de Fresnel en el centro, el margen normativo de despeje y la altura estructural mínima requerida para las torres en los extremos.
 

**Paso 1:** Al encontrarse la arboleda en el centro exacto de la trayectoria ($8\text{ km}$ hacia cada antena), aplicamos la fórmula simplificada introduciendo la distancia en kilómetros ($16$) y la frecuencia en gigahercios ($5.8$), obteniendo el radio de la primera zona de Fresnel:

$$F_{1,\text{centro}} = 8.65 \cdot \sqrt{\frac{16\text{ km}}{5.8\text{ GHz}}} \approx 8.65 \cdot \sqrt{2.7586} \approx 8.65 \cdot 1.6609 \approx 14.37\text{ m}$$

**Paso 2:** Calculamos el 60% de dicho radio para determinar el despeje vertical estricto que debe permanecer libre de obstáculos y así evitar pérdidas de potencia por difracción:

$$r_{\text{despeje}} = 0.60 \cdot F_{1,\text{centro}} = 0.60 \cdot (14.37\text{ m}) \approx 8.62\text{ m}$$

**Paso 3:** Sumamos la altura del obstáculo ($12\text{ m}$) y el radio de guarda obligatorio para determinar la altura estructural mínima que deben tener las torres en los extremos:

$$h_{\text{torre}} = h_{\text{obs}} + r_{\text{despeje}} = 12\text{ m} + 8.62\text{ m} = 20.62\text{ m}$$
  

> [!EXAMPLE] **Ejemplo 4:** Comparativa de Zonas de Fresnel en Bandas Sub-1 GHz frente a Ondas Milimétricas
> 
> Compare el radio de la primera zona de Fresnel en el centro de un enlace de $d_{\text{total}} = 10\text{ km}$ para dos frecuencias operativas distintas: un sistema rural en banda ISM de $f_A = 900\text{ MHz}$ ($0.9\text{ GHz}$) frente a un enlace troncal 5G en ondas milimétricas de $f_B = 28\text{ GHz}$.

**Paso 1:** Para la banda de $900\text{ MHz}$ ($0.9\text{ GHz}$) sustituimos los valores en la ecuación simplificada de punto medio:

$$F_{1,900\text{MHz}} = 8.65 \cdot \sqrt{\frac{10\text{ km}}{0.9\text{ GHz}}} \approx 8.65 \cdot \sqrt{11.111} \approx 8.65 \cdot 3.333 \approx 28.83\text{ m}$$

A $900\text{ MHz}$, la longitud de onda larga ($\lambda \approx 33.3\text{ cm}$) expande el elipsoide de Fresnel hasta un radio de casi $29\text{ metros}$, exigiendo torres muy elevadas para no chocar con el suelo o las edificaciones intermedias.

**Paso 2:** Para la banda de ondas milimétricas de $28\text{ GHz}$ sustituimos los valores en la ecuación simplificada de punto medio:

$$F_{1,28\text{GHz}} = 8.65 \cdot \sqrt{\frac{10\text{ km}}{28\text{ GHz}}} \approx 8.65 \cdot \sqrt{0.3571} \approx 8.65 \cdot 0.5976 \approx 5.17\text{ m}$$

Al subir la frecuencia a $28\text{ GHz}$ ($\lambda \approx 1.07\text{ cm}$), el elipsoide se contrae drásticamente hasta un radio de apenas $5.17\text{ metros}$. Esto demuestra una regla clásica de planificación de radio: las frecuencias altas confinan la energía en volúmenes espaciales mucho más estrechos, requiriendo menos despeje físico respecto a los obstáculos del terreno.

## 3.2. Efecto Doppler en Comunicaciones Electromagnéticas

Cuando existe movimiento cinemático relativo entre el emisor y el receptor, la frecuencia aparente con la que la onda incide sobre la antena receptora difiere de la frecuencia nominal emitida por el transmisor.

> [!QUOTE] **Definición 9:** Desplazamiento Doppler Electromagnético
> 
> Para una onda electromagnética que se propaga a la velocidad de la luz $c$, el corrimiento de frecuencia ($\Delta f = f_{\text{recibida}} - f$) causado por una velocidad axial relativa $v_{\text{rel}}$ entre emisor y receptor en trayectos unidireccionales directos se calcula mediante:
> 
> $$\Delta f_{\text{móvil}} = \pm f \cdot \left(\frac{v_{\text{rel}}}{c}\right)$$
> 
> donde el signo positivo ($+$) indica acercamiento mutuo (compresión espectral) y el signo negativo ($-$) indica alejamiento mutuo (dilatación espectral).
> 
> En un sistema de **radar activo por eco continuo**, donde la onda realiza un trayecto doble (viaje de ida hacia el blanco y retorno reflejado), el corrimiento se duplica:
> 
> $$\Delta f_{\text{radar}} = 2 \cdot f \cdot \left(\frac{v_{\text{rel}}}{c}\right)$$

Este fenómeno se manifiesta en tres escenarios de ingeniería de telecomunicaciones:
  
1. **Terminales móviles terrestres:** La compresión y dilatación de la portadora desalinea los filtros de recepción en automóviles o trenes de alta velocidad.

2. **Radar de eco continuo:** Al chocar contra un objetivo en movimiento, la superficie actúa sucesivamente como un receptor en movimiento (primer corrimiento Doppler) y luego como un retransmisor en movimiento (segundo corrimiento Doppler), justificando el factor 2 en la ecuación.

3. **Satélites LEO frente a Satélites GEO:**

    - **Satélites Geoestacionarios (GEO):** Orbitan a una altitud de $35786\text{ km}$ sobre el ecuador terrestre con un período orbital de 24 horas. Al desplazarse a la misma velocidad angular que la rotación de la Tierra, su posición relativa respecto a una estación terrena fija permanece inmóvil ($v_{\text{rel}} \approx 0$), lo que produce un corrimiento Doppler prácticamente nulo ($\Delta f \approx 0$).

    - **Satélites de Órbita Baja (LEO):** Orbitan a altitudes reducidas (entre $500\text{ km}$ y $1200\text{ km}$) para reducir la latencia de propagación. Para contrarrestar la atracción gravitatoria, deben desplazarse a velocidades orbitales de $v_{\text{orb}} \approx 7.5\text{ km/s}$ ($27000\text{ km/h}$). Al sobrevolar la estación de tierra, un satélite LEO introduce desplazamientos Doppler de cientos de kilohercios que varían dinámicamente en cuestión de minutos, exigiendo que el módem implemente algoritmos de sincronización de portadora en tiempo real.
	
> [!EXAMPLE] **Ejemplo 5:** Desplazamiento Doppler en Tren de Alta Velocidad (4G frente a 5G)
> 
> Un tren de pasajeros de alta velocidad se desplaza a $v = 360\text{ km/h}$ en aproximación frontal directa hacia una radiobase celular instalada junto a la vía. Compare el corrimiento Doppler en una banda celular 4G de $f_1 = 2.0\text{ GHz}$ frente a una banda milimétrica 5G NR de $f_2 = 26\text{ GHz}$.
 
**Paso 1:** Convertimos la velocidad del tren al Sistema Internacional: dividimos los $360\text{ km/h}$ entre el factor de conversión $3.6$ para obtener la velocidad lineal de avance en metros por segundo ($100\text{ m/s}$).
     
$$v_{\text{rel}} = \frac{360\text{ km/h}}{3.6} = 100\text{ m/s}$$

**Paso 2:** Calculamos el corrimiento en la banda 4G ($2.0\text{ GHz}$). Evaluamos la relación adimensional entre la velocidad del móvil y la velocidad de la luz ($\frac{100}{3 \times 10^8} \approx 3.333 \times 10^{-7}$) y la multiplicamos por la frecuencia operativa:
     
$$\Delta f_{\text{4G}} = (2.0 \times 10^9\text{ Hz}) \cdot \left(\frac{100\text{ m/s}}{3 \times 10^8\text{ m/s}}\right) = 666.67\text{ Hz}$$
 
El corrimiento de $666.67\text{ Hz}$ es absorbido fácilmente por los lazos de seguimiento de fase (PLL) habituales.

**Paso 3:** Calculamos el corrimiento en la banda 5G ($26\text{ GHz}$) multiplicando el factor de velocidad por la frecuencia correspondiente:
     
$$\Delta f_{\text{5G}} = (26.0 \times 10^9\text{ Hz}) \cdot \left(\frac{100\text{ m/s}}{3 \times 10^8\text{ m/s}}\right) \approx 8666.67\text{ Hz} \approx 8.67\text{ kHz}$$

En 5G milimétrico, el corrimiento escala hasta $8.67\text{ kHz}$ (13 veces mayor), exigiendo algoritmos avanzados de compensación Doppler en el procesador de banda base para evitar desfasajes entre subportadoras OFDM.

> [!EXAMPLE] **Ejemplo 6:** Medición de Velocidad en un Cinemómetro Radar Vial
> 
> Un radar de tráfico de control vial emite una portadora de microondas a $f = 24.125\text{ GHz}$. Al rebotar en un vehículo que se aproxima frontalmente, el receptor detecta una señal de eco con un corrimiento positivo de $\Delta f_{\text{radar}} = 2.8\text{ kHz}$ ($2800\text{ Hz}$). Calcule la velocidad del vehículo en $\text{km/h}$.
 
**Paso 1:** Despejamos la velocidad relativa a partir de la ecuación del radar activo. Dado que la onda viaja hacia el vehículo y luego se refleja de vuelta al radar, el corrimiento Doppler ocurre dos veces, por lo que el factor 2 divide en el denominador:
     
$$\Delta f_{\text{radar}} = 2 \cdot f \cdot \left(\frac{v_{\text{rel}}}{c}\right) \implies v_{\text{rel}} = \frac{\Delta f_{\text{radar}} \cdot c}{2 \cdot f}$$

**Paso 2:** Sustituimos los valores numéricos expresados en unidades básicas del Sistema Internacional y calculamos el cociente, obteniendo una velocidad de aproximación de $17.41\text{ m/s}$:
     
$$v_{\text{rel}} = \frac{2800\text{ Hz} \cdot (3 \times 10^8\text{ m/s})}{2 \cdot (24.125 \times 10^9\text{ Hz})} = \frac{8.4 \times 10^{11}}{4.825 \times 10^{10}} \approx 17.41\text{ m/s}$$

**Paso 3:** Convertimos la velocidad resultante a kilómetros por hora multiplicando por $3.6$, concluyendo que el automóvil circula a $62.67\text{ km/h}$:
     
$$v_{\text{km/h}} = 17.41\text{ m/s} \cdot 3.6 \approx 62.67\text{ km/h}$$

> [!EXAMPLE] **Ejemplo 7:** Excursión Doppler en Satélites LEO
> 
> Un terminal terrena recibe la señal portadora en banda Ku ($f = 12\text{ GHz}$) emitida por un satélite de órbita baja (LEO) que viaja a una velocidad orbital de $v_{\text{orb}} = 7.6\text{ km/s}$ ($7600\text{ m/s}$). Calcule el corrimiento Doppler máximo cuando el satélite aparece en el horizonte y la excursión espectral total durante el pase.

**Paso 1:** Calculamos el corrimiento Doppler máximo en el horizonte (máxima velocidad radial). Al asomar por el horizonte en dirección a la estación, el vector de velocidad del satélite se alinea casi frontalmente con la antena receptora, sufriendo un incremento positivo de $+304\text{ kHz}$:
     
$$\Delta f_{\text{máx}} = (12 \times 10^9\text{ Hz}) \cdot \left(\frac{7600\text{ m/s}}{3 \times 10^8\text{ m/s}}\right) = (12 \times 10^9) \cdot (2.5333 \times 10^{-5}) \approx 304000\text{ Hz} = 304\text{ kHz}$$

**Paso 2:** Calculamos el ancho de banda total del barrido Doppler de horizonte a horizonte. Cuando el satélite pasa por el cenit, la velocidad radial relativa se anula momentáneamente ($\Delta f = 0\text{ Hz}$) y al alejarse hacia el horizonte opuesto la frecuencia cae a $-304\text{ kHz}$:
     
$$\Delta f_{\text{barrido}} = 2 \cdot \Delta f_{\text{máx}} = 2 \cdot (304\text{ kHz}) = 608\text{ kHz}$$

En una ventana de paso de apenas 8 a 10 minutos, el receptor experimenta un desplazamiento dinámico continuo de $608\text{ kHz}$, lo que obliga a los receptores satelitales modernos a ajustar la frecuencia de sus osciladores locales de forma permanente para no perder el enlace de datos.

---

> [!RESOURCES] REFERENCIAS
> 
> - **3GPP.** *Technical Specification TS 38.101: 5G NR; User Equipment (UE) Radio Transmission and Reception*. 3rd Generation Partnership Project. Recuperado de [3gpp.org](https://www.3gpp.org)
>   
> - **Bhatia, R.** *Fourier Series*. Mathematical Association of America.
>   
> - **Couch, L. W.** *Digital and Analog Communication Systems* (8.ª ed.). Pearson.
>   
> - **Forouzan, B. A.** *Data Communications and Networking* (4.ª ed.). McGraw-Hill.
>   
> - **OpenStax.** *University Physics Volume 1: Waves, Acoustics and Doppler Effect*. Rice University. Recuperado de [openstax.org](https://openstax.org)
>   
> - **Stallings, W.** *Data and Computer Communications* (10.ª ed.). Pearson Education.
>   
> - **Tanenbaum, A. S., & Wetherall, D. J.** *Computer Networks* (5.ª ed.). Pearson.


