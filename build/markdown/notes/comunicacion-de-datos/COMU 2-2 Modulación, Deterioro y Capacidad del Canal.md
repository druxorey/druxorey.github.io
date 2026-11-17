---
created: 2026-06-01T23:59:00
title: Modulación, Deterioro y Capacidad del Canal
semester: 5
subject:
  - "[[COMU 0-0 Nota Informativa|Comunicación de Datos]]"
unit: 2
status: done
---

<h1 id="main-title"  align="center"> Modulación, Deterioro y Capacidad del Canal </h1>

> [!TLDR] SÍNTESIS 
> La **modulación digital** adapta flujos de bits binarios a ondas portadoras analógicas de alta frecuencia para superar los límites físicos de los canales de transmisión. Mediante técnicas como **ASK**, **FSK**, **PSK** y **QAM**, junto con arquitecturas avanzadas como **OFDM**, se optimiza la eficiencia espectral frente a factores de deterioro como la atenuación y el ruido térmico, cuyos límites teóricos son gobernados por los teoremas de **Nyquist** y **Shannon-Hartley**.

El mundo físico transporta magnitudes continuas como voltajes, pulsos de luz u ondas electromagnéticas que sufren la resistencia del medio, pierden energía y conviven con perturbaciones del entorno. El dilema fundamental aparece cuando intentamos enviar esos pulsos digitales directos por medios inalámbricos o de larga distancia: los canales reales no admiten corrientes continuas ni cambios de voltaje abruptos sin deformar la señal hasta volverla irreconocible a los pocos metros. Para lograr que los bits crucen el espacio libre o un medio guiado de forma eficiente, es indispensable encontrar una manera de adaptar esa información discreta y «montarla» sobre una onda continua de alta frecuencia capaz de viajar con estabilidad a través del canal.

# 1. Técnicas de Señalización Pasabanda

En los medios de transmisión físicos no siempre es factible inyectar señales en banda base desde $0\text{ Hz}$. Cuando transmitimos por el aire, por cable coaxial o a través de enlaces satelitales, los canales se comportan como medios pasabanda. Para superar esta barrera física, trasladamos la información binaria hacia frecuencias elevadas alterando los parámetros de una oscilación sinusoidal denominada portadora.

## 1.1. Principios de la Conversión Digital a Analógica

Modular digitalmente consiste en mapear combinaciones de bits lógicos en estados analógicos discretos de una onda portadora continua durante intervalos regulares de tiempo.

> [!QUOTE] **Definición 1:** Onda Portadora Pasabanda
> 
> Una señal portadora analógica pura se modela en el dominio del tiempo mediante la función continua:
> 
> $$s(t) = A \cdot \cos(2\pi f_c t + \phi)$$
> 
> Donde:
> 
> - $A$ es la amplitud pico de la onda (medida en voltios, $\text{V}$).
> - $f_c$ es la frecuencia central de la portadora (en Hertz, $\text{Hz}$).
> - $\phi$ es el desfase angular inicial en $t = 0$ (en radianes o grados).

Para cuantificar la velocidad de transmisión, diferenciamos la tasa a nivel lógico de la velocidad de conmutación física del medio:

- **Tasa de bits ($N$):** Cantidad de dígitos binarios que el transmisor despacha por segundo, expresada en bits por segundo ($\text{bps}$).

- **Tasa de baudios ($S$):** Cantidad de cambios de estado físico (símbolos) que el circuito genera sobre el canal en cada segundo, expresada en baudios ($\text{Baud}$).

- **Factor de empaquetamiento ($r$):** Cantidad de bits lógicos representados por cada símbolo físico ($r = \log_2 L$).

> [!QUOTE] **Definición 2:** Relación entre Tasa de Bits y Tasa de Baudios
> 
> La velocidad de conmutación de símbolos sobre el canal ($S$) es inversamente proporcional al número de bits codificados en cada elemento de señal ($r$):
> 
> $$S = \frac{N}{r} = \frac{N}{\log_2(L)}$$
> 
> Donde $L$ es el número de niveles o estados discretos distinguibles del modulador.

Imaginemos camiones que salen de un centro logístico hacia una autopista. La tasa de bits ($N$) representa el total de cajas que debemos mover por hora. La tasa de baudios ($S$) es la cantidad de camiones que transitan por la calzada por hora. Si cada camión transporta una sola caja ($L = 2 \implies r = 1$), necesitamos que pasen tantos camiones como cajas tengamos ($S = N$). Si cargamos camiones más grandes que llevan 4 cajas apiladas cada uno ($L = 16 \implies r = 4$), la carretera solo debe soportar la cuarta parte de camiones físicos para entregar la misma cantidad de carga ($S = N/4$).

> [!EXAMPLE] **Ejemplo 1:** Cálculo de Tasa de Modulación en Transmisión Binaria y Multinivel
> 
> Un transmisor genera un flujo continuo de datos a $N = 9600\text{ bps}$. Calculamos la velocidad física de conmutación ($S$) si empleamos señalización binaria ($L = 2$) y señalización multinivel de 16 estados ($L = 16$).
 
**Paso 1:** Para señalización binaria ($L = 2$) identificamos que en el esquema binario cada cambio de señal transporta un único bit ($r = 1$), de modo que la tasa física en baudios coincide con la tasa de bits.

$$r = \log_2(2) = 1\text{ bit/símbolo} \implies S = \frac{9600\text{ bps}}{1} = 9600\text{ Baud}$$

**Paso 2:** Para señalización multinivel ($L = 16$), en el caso de 16 niveles, calculamos $r = \log_2(16) = 4\text{ bits}$. Al dividir la tasa de bits entre 4, vemos que el hardware solo conmuta 2400 veces por segundo, reduciendo el ancho de banda necesario en el canal.

$$r = \log_2(16) = 4\text{ bits/símbolo} \implies S = \frac{9600\text{ bps}}{4} = 2400\text{ Baud}$$

## 1.2. Esquemas Modulatorios Clásicos (ASK, FSK y PSK)

Las modulaciones elementales varían únicamente una propiedad de la portadora, manteniendo constantes las otras dos.

### 1.2.1. Modulación por Desplazamiento de Amplitud (ASK)

En ASK, los bits determinan el nivel de amplitud pico de la portadora. El caso binario básico es **OOK** (_On-Off Keying_), donde el bit «1» se representa con la portadora activa a amplitud completa y el bit «0» con la portadora apagada ($0\text{ V}$).

- **Sensibilidad al ruido:** Muy alta. Las fuentes de ruido e interferencia electromagnética alteran la amplitud de las ondas de manera directa, lo que induce al receptor a confundir pulsos atenuados con ceros.

- **Ancho de banda requerido ($B_{\text{ASK}}$):** Depende de la tasa de baudios y del factor de exceso de banda del filtro conformado ($d \in [0, 1]$):
    
$$B_{\text{ASK}} = (1 + d) \cdot S$$

### 1.2.2. Modulación por Desplazamiento de Frecuencia (FSK)

En FSK, la amplitud y la fase permanecen invariables, mientras que la frecuencia salta entre dos valores: una frecuencia de marca ($f_1 = f_c + \Delta f$) para el bit «1» y una de espacio ($f_2 = f_c - \Delta f$) para el «0».

- **Sensibilidad al ruido:** Media. Al no basarse en la amplitud, las fluctuaciones de tensión no alteran el ritmo de oscilación de la onda.

- **Ancho de banda requerido ($B_{\text{FSK}}$):** Como exige dos frecuencias portadoras separadas por una guarda mínima ($2\Delta f$), consume más espectro que los demás esquemas:
    
$$B_{\text{FSK}} = (1 + d) \cdot S + 2\Delta f$$

### 1.2.3. Modulación por Desplazamiento de Fase (PSK)

En PSK, la amplitud y la frecuencia son constantes, y el flujo de bits modula la fase inicial de la onda. En **BPSK** (_Binary PSK_), el bit «0» tiene fase $0^\circ$ y el «1» tiene fase $180^\circ$. En **QPSK** (_Quadrature PSK_), agrupamos los bits de a pares ($r = 2$) sobre cuatro fases ($45^\circ, 135^\circ, 225^\circ, 315^\circ$), duplicando la tasa de bits para la misma tasa de baudios.

- **Sensibilidad al ruido:** Baja. Ofrece alta robustez ante variaciones de nivel de potencia.

- **Ancho de banda requerido ($B_{\text{PSK}}$):** Es equivalente al de ASK:

$$B_{\text{PSK}} = (1 + d) \cdot S$$

|**Técnica**|**Parámetro modulado**|**Bits/símbolo (rrr)**|**Ancho de banda (BBB)**|**Robustez al ruido**|**Eficiencia espectral**|**Aplicaciones típicas**|
|---|---|---|---|---|---|---|
|**ASK / OOK**|Amplitud|$1$|$(1 + d) \cdot S$|Muy baja|Baja|RFID pasivo, enlaces infrarrojos|
|**FSK (BFSK)**|Frecuencia|$1$|$(1 + d) \cdot S + 2\Delta f$|Media|Muy baja|Bluetooth clásico, telemetría|
|**BPSK**|Fase (2 estados)|$1$|$(1 + d) \cdot S$|Alta|Media|Wi-Fi base (802.11b), GPS|
|**QPSK**|Fase (4 estados)|$2$|$(1 + d) \cdot S$|Alta|Buena ($2\text{ bps/Hz}$)|Satélite DVB-S, 3G|
|**QAM**|Amplitud y fase|$2\text{ a }12+$|$(1 + d) \cdot S$|Variable (cae al subir $M$)|Muy alta|Wi-Fi 6/7, 4G LTE, 5G NR|

> [!EXAMPLE] **Ejemplo 2:** Comparación de Ancho de Banda entre BFSK y BPSK 
> 
> Deseamos transmitir un flujo de datos a $N = 10\text{ Mbps}$ con un factor de filtrado $d = 0.2$. Para BFSK utilizamos una separación entre portadoras con desviación $\Delta f = 2.5\text{ MHz}$. Calculamos el ancho de banda ocupado por cada modulación.
 
**Paso 1:** Para BPSK ($r = 1 \implies S = 10\text{ MBaud}$). Al ser una modulación binaria, requiere una tasa de símbolos de $S = N / 1 = 10\text{ MBaud}$.

**Paso 2:** Calculamos el espectro de BPSK multiplicando la tasa de símbolos por el factor $(1 + d)$:

$$B_{\text{BPSK}} = (1 + 0.2) \cdot 10\text{ MHz} = 12.0\text{ MHz}$$

**Paso 3:** Para BFSK ($r = 1 \implies S = 10\text{ MBaud}$). Al ser una modulación binaria, requiere la misma tasa de símbolos: $S = N / 1 = 10\text{ MBaud}$.

**Paso 4:** Calculamos el ancho de banda sumando el espectro base y la separación entre las dos portadoras ($2\Delta f = 5.0\text{ MHz}$):

$$B_{\text{BFSK}} = (1 + 0.2) \cdot 10\text{ MHz} + 2 \cdot (2.5\text{ MHz}) = 12.0\text{ MHz} + 5.0\text{ MHz} = 17.0\text{ MHz}$$

BFSK requiere un $41.7\%$ más de espectro que BPSK para la misma tasa de bits.

## 1.3. Modulación de Amplitud en Cuadratura (QAM)

A medida que intentamos meter más fases en un círculo de PSK puro (como en 8-PSK o 16-PSK), los puntos quedan demasiado juntos en ángulo. QAM resuelve esta limitación combinando cambios de amplitud y fase simultáneos mediante dos portadoras desfasadas $90^\circ$ entre sí.

> [!QUOTE] **Definición 3:** Señal Modulada en QAM
> 
> La forma de onda de una señal QAM se obtiene mediante la suma lineal de dos componentes ortogonales:
> 
> $$s(t) = A_I \cdot \cos(2\pi f_c t) - A_Q \cdot \sin(2\pi f_c t)$$
> 
> Donde $A_I$ representa la amplitud del canal en fase (eje I) y $A_Q$ la del canal en cuadratura (eje Q). Cada combinación $(A_I, A_Q)$ define un punto en el **diagrama de constelación**.

Pensemos en una cuadrícula sobre el piso de un almacén. Si solo camináramos sobre una línea recta hacia adelante o hacia atrás, tendríamos una sola dimensión física. En cambio, si usamos filas y columnas identificadas con letras y números, cada baldosa representa un casillero único en dos dimensiones. Al encender una luz sobre una baldosa específica, indicamos sus coordenadas $(x, y)$ a la vez. En QAM, el modulador transmite un punto $(I, Q)$ del plano en cada instante de símbolo.

Propiedades fundamentales de las constelaciones QAM:

- **Empaquetamiento de bits:** Una constelación de $M$ símbolos transporta $r = \log_2(M)$ bits por símbolo. Así, 16-QAM transporta $4\text{ bits}$, 64-QAM transporta $6\text{ bits}$, 256-QAM transporta $8\text{ bits}$ y 1024-QAM transporta $10\text{ bits}$.

- **Degradación de la distancia mínima ($d_{\text{mín}}$):** Si mantenemos constante la potencia promedio de transmisión, al densificar el número de puntos la distancia euclidiana entre estados vecinos se reduce:
    
$$d_{\text{mín}} \propto \frac{1}{\sqrt{M}}$$

Si en una cuadrícula amplia colocamos 16 marcas separadas, una sacudida mecánica leve no impedirá ver en qué celda está cada objeto. Si en ese mismo suelo dibujamos 1024 casillas diminutas, una vibración pequeña desplazará la posición percibida hacia la casilla contigua, provocando errores en la decisión del receptor.

## 1.4. Multiplexación por División de Frecuencias Ortogonales (OFDM)

Transmitir un único flujo de datos de alta velocidad sobre una sola portadora ensancha su espectro, volviéndolo muy vulnerable a desvanecimientos selectivos en frecuencia y a ecos de señal. OFDM aborda este reto repartiendo el caudal entre múltiples subportadoras ortogonales de banda estrecha en paralelo.

> [!QUOTE] **Definición 4:** Condición Matemática de Ortogonalidad en Frecuencia
> 
> Dos subportadoras sinusoidales continuas de frecuencias $f_n$ y $f_m$ son mutuamente ortogonales en un intervalo de símbolo $T_s$ si su producto interno satisface:
> 
> $$\frac{1}{T_s} \int_0^{T_s} e^{j 2\pi f_n t} \cdot e^{-j 2\pi f_m t} \, dt = \begin{cases} 1 & \text{si } n = m \\ 0 & \text{si } n \neq m \end{cases} \iff \Delta f = \frac{1}{T_s}$$
> 
> Donde $\Delta f = |f_n - f_m|$ es la separación mínima de frecuencia entre subportadoras.

Aspectos de diseño de OFDM:

- **Solapamiento espectral:** Como $\Delta f = 1/T_s$, la cresta espectral de cada subportadora coincide de forma exacta con los cruces por cero de todas las demás. Esto permite comprimir las subportadoras sin necesidad de bandas de guarda intermedias.

- **Implementación por IFFT/FFT en banda base:** En lugar de construir cientos de circuitos osciladores independientes por hardware, el transmisor calcula la **Transformada Rápida de Fourier Inversa (IFFT)** sobre los símbolos de entrada para generar la señal en el dominio temporal. En recepción, la **FFT** descompone la señal y extrae cada subportadora de inmediato.

- **Prefijo Cíclico (CP):** Copiamos una fracción del tramo final del símbolo útil y la anteponemos como guarda al inicio. Esto absorbe los retardos provocados por rebotes en edificios y obstáculos (multitrayecto), evitando la interferencia intersimbólica.

> [!EXAMPLE] **Ejemplo 3:** Análisis de Parámetros OFDM en Wi-Fi 6
> 
> Un canal de Wi-Fi 6 (802.11ax) posee un ancho de banda de $B = 20\text{ MHz}$ y define un período de símbolo útil $T_s = 12.8\text{ }\mu\text{s}$. Calculamos la separación de subportadoras, el número total de subportadoras y la tasa bruta usando 1024-QAM sobre 234 subportadoras asignadas a datos.
 
 
**Paso 1:** Calculamos la separación ortogonal ($\Delta f$). Invertimos la duración del símbolo para obtener la separación ortogonal exacta de $78.125\text{ kHz}$.
 
$$\Delta f = \frac{1}{T_s} = \frac{1}{12.8 \times 10^{-6}\text{ s}} = 78.125\text{ kHz}$$
 
Calculamos el total de subportadoras teóricas del canal:
 
 $$N_{\text{sub}} = \frac{B}{\Delta f} = \frac{20 \times 10^6\text{ Hz}}{78.125 \times 10^3\text{ Hz}} = 256\text{ subportadoras}$$

**Paso 2:** Dividimos el ancho de banda del canal ($20\text{ MHz}$) entre dicha separación para determinar que el canal aloja 256 subportadoras.
 
Calculamos la tasa bruta con 1024-QAM ($r = \log_2 1024 = 10\text{ bits}$):
 
$$R_{\text{bruta}} = 234 \cdot \left( \frac{10\text{ bits}}{12.8\text{ }\mu\text{s}} \right) = \frac{2340\text{ bits}}{12.8 \times 10^{-6}\text{ s}} \approx 182.81\text{ Mbps}$$
 
**Paso 3:** Multiplicamos las 234 subportadoras útiles de datos por los $10\text{ bits}$ aportados por cada símbolo de 1024-QAM y dividimos entre el tiempo de símbolo para deducir la velocidad bruta de $182.81\text{ Mbps}$.

# 2. Factores de Deterioro en la Transmisión de Señales

Durante su propagación a través de conductores metálicos, fibras ópticas o el espacio libre, toda señal sufre deterioros causados por tres factores: atenuación, distorsión y ruido.

## 2.1. Atenuación y Escalas Logarítmicas en Decibelios (dB, dBm y dBW)

La atenuación describe la pérdida de energía que experimenta la onda debido a efectos resistivos en cables o a la dispersión geométrica y absorción en el espacio.

> [!QUOTE] **Definición 5:** Atenuación y Niveles Absolutos de Potencia
> 
> La variación logarítmica de potencia entre la salida ($P_2$) y la entrada ($P_1$) de un enlace se calcula en decibelios ($\text{dB}$):
> 
> $$\text{dB} = 10 \log_{10}\left( \frac{P_2}{P_1} \right)$$
> 
> Los niveles absolutos de potencia referenciados se calculan como:
> 
> $$P_{\text{dBm}} = 10 \log_{10}\left( \frac{P_{\text{lineal}}}{1\text{ mW}} \right), \qquad P_{\text{dBW}} = 10 \log_{10}\left( \frac{P_{\text{lineal}}}{1\text{ W}} \right)$$
> 
> Con la relación directa de conversión: $P_{\text{dBm}} = P_{\text{dBW}} + 30\text{ dB}$.

Pensemos en el flujo de agua a través de una tubería larga con asperezas internas. La bomba aplica una presión de entrada alta. A medida que el fluido avanza kilómetros contra el rozamiento de las paredes, la presión cae continuamente. La ventaja de medir las pérdidas en decibelios es que, en vez de multiplicar fracciones decimales para cada tramo de tubería, sumamos y restamos valores directamente.

Reglas de referencia rápida:

- Una caída de $-3\text{ dB}$ equivale a perder el $50\%$ de la potencia original ($P_2 \approx 0.5 \cdot P_1$).
- Una caída de $-10\text{ dB}$ reduce la potencia al $10\%$ inicial ($P_2 = 0.1 \cdot P_1$).
- Una caída de $-20\text{ dB}$ deja solo el $1\%$ de la potencia original ($P_2 = 0.01 \cdot P_1$).

> [!EXAMPLE] **Ejemplo 4:** Atenuación en un Tendido de Fibra Óptica
> 
> Un transmisor inyecta una potencia óptica de $P_1 = 40\text{ mW}$ sobre una fibra de $d = 60\text{ km}$ con una atenuación nominal de $\alpha = 0.3\text{ dB/km}$. Calculamos la potencia recibida en $\text{dBm}$ y en milivatios lineales.
 
 **Paso 1:** Convertimos la potencia inicial a $\text{dBm}$. Convertimos la potencia lineal de entrada ($40\text{ mW}$) a escala logarítmica relativa a $1\text{ mW}$ sumando $16.02\text{ dBm}$.

$$P_{1,\text{dBm}} = 10 \log_{10}\left( \frac{40\text{ mW}}{1\text{ mW}} \right) \approx 10 \cdot 1.602 = 16.02\text{ dBm}$$
 
Calculamos la pérdida total acumulada:
 
$$A_{\text{total}} = 0.3\text{ dB/km} \cdot 60\text{ km} = 18.0\text{ dB}$$
 
**Paso 2:** Calculamos la atenuación total multiplicando la tasa de pérdida unitaria por la longitud: $0.3 \times 60 = 18.0\text{ dB}$.

Restamos la pérdida para obtener la potencia recibida:
 
$$P_{2,\text{dBm}} = 16.02\text{ dBm} - 18.0\text{ dB} = -1.98\text{ dBm}$$
 
**Paso 3:** Restamos las pérdidas: $16.02 - 18.0 = -1.98\text{ dBm}$.

Pasamos el valor a milivatios:
 
$$P_{2,\text{mW}} = 1\text{ mW} \cdot 10^{\frac{-1.98}{10}} \approx 0.634\text{ mW}$$

**Paso 4:** Despejamos el valor lineal elevando 10 a la potencia de $-0.198$, obteniendo $0.634\text{ mW}$ útiles en el extremo receptor.

## 2.2. Distorsión por Retardo, Dispersión e Interferencia Intersimbólica (ISI)

La distorsión es la alteración de la forma geométrica que sufre una señal compuesta al cruzar un medio físico:

- **Distorsión de amplitud:** Ocurre cuando el canal atenúa unas frecuencias con mayor intensidad que otras.

- **Distorsión por retardo:** La velocidad de fase de una onda electromagnética varía según la frecuencia en medios guiados. Las componentes de alta frecuencia viajan a distinta velocidad que las de baja frecuencia.

- **Dispersión cromática:** En fibras ópticas, las distintas longitudes de onda del pulso de luz viajan a velocidades ligeramente diferentes por el núcleo de vidrio, ensanchando temporalmente los pulsos a lo largo de la distancia.

> [!QUOTE] **Definición 6:** Interferencia Intersimbólica (ISI)
> 
> Si la respuesta al impulso temporal del canal $h(t)$ se ensancha más allá del intervalo de símbolo $T_s$, la señal recibida en el instante de muestreo del símbolo $k$-ésimo contiene energía residual de los símbolos anteriores y posteriores:
> 
> $$y(k T_s) = a_k \cdot h(0) + \sum_{n \neq k} a_n \cdot h((k - n)T_s) + w(k T_s)$$
> 
> Donde el término de sumatoria representa la **Interferencia Intersimbólica (ISI)** que contamina la detección del dato útil $a_k$.

Pensemos en corredores de relevos dentro de una pista atlética. Si parten espaciados por cinco metros, pero unos corren a zancadas más largas y otros a paso corto, con el paso de las vueltas el pelotón se desordena. Las colas de unos corredores chocan con las cabezas de los que vienen detrás, haciendo imposible distinguir la posición de cada competidor. Eso mismo le sucede a los pulsos de señal cuando se ensanchan y se solapan entre sí.

## 2.3. Clasificación del Ruido Físico y Relación Señal a Ruido (SNR)

El ruido agrupa todas aquellas perturbaciones eléctricas no deseadas que se superponen a la señal que viaja por el canal:

- **Ruido térmico (Johnson-Nyquist):** Se genera por la agitación térmica natural de los electrones libres dentro de cualquier medio conductor por encima del cero absoluto ($0\text{ K}$). Es ruido blanco uniforme presente en todo el espectro.

- **Ruido de intermodulación:** Aparece cuando circuitos no lineales mezclan frecuencias distintas $f_1$ y $f_2$, produciendo armónicos espurios ($f_1 \pm f_2$) que interfieren en bandas contiguas.

- **Diafonía (_Crosstalk_):** Acoplamiento inductivo o capacitivo entre pares de cables contiguos que transcurren en paralelo.

- **Ruido impulsivo:** Perturbaciones electromagnéticas transitorias de gran amplitud y corta duración provocadas por relámpagos, conmutaciones industriales o chispas.

> [!QUOTE] **Definición 7:** Potencia de Ruido Térmico y Relación Señal a Ruido
> 
> La potencia de ruido térmico ($P_N$) en un receptor de ancho de banda $B$ se modela mediante la ley de Johnson-Nyquist:
> 
> $$P_N = k \cdot T \cdot B$$
> 
> Donde:
> 
> - $k$ es la constante de Boltzmann ($k \approx 1.3806 \times 10^{-23}\text{ J/K}$).
>     
> - $T$ es la temperatura absoluta del receptor en Kelvin ($K = ^\circ\text{C} + 273.15$).
>     
> - $B$ es el ancho de banda efectivo del receptor en Hertz ($\text{Hz}$).
> 
> La **Relación Señal a Ruido (SNR)** compara la potencia de la señal útil ($P_S$) respecto a la potencia del ruido ($P_N$):
> 
> $$\text{SNR}_{\text{lineal}} = \frac{P_S}{P_N} \iff \text{SNR}_{\text{dB}} = 10 \log_{10}\left( \frac{P_S}{P_N} \right)$$

Pensemos en dos personas conversando en una habitación. La potencia de la señal útil ($P_S$) es el volumen con el que habla el emisor. La potencia de ruido ($P_N$) es el bullicio ambiental de la gente congregada alrededor. Si la sala está en silencio, la SNR es alta y alcanza con un susurro para entender cada palabra. Si el gentío grita, la SNR cae y el emisor debe elevar su voz al máximo o hablar despacio para que sus palabras no queden sepultadas por el ruido de fondo.

# 3. Capacidad Límite de los Canales de Datos y Eficiencia Espectral

La teoría matemática de la información establece los límites superiores de transmisión sin error sobre cualquier canal físico, diferenciando entre canales sin ruido y canales con ruido térmico.

## 3.1. Teorema de Capacidad de Nyquist para Canales sin Ruido

A principios del siglo XX, Harry Nyquist dedujo la velocidad máxima de señalización asumiendo un canal físico ideal exento de perturbaciones de ruido.

> [!QUOTE] **Definición 8:** Límite de Capacidad de Nyquist
> 
> Para un canal analógico de ancho de banda $B$ completamente libre de ruido, la capacidad máxima teórica ($C_{\text{Nyquist}}$) en bits por segundo está delimitada por:
>
> $$C_{\text{Nyquist}} = 2 \cdot B \cdot \log_2(M)$$
> 
> Donde $B$ es el ancho de banda del canal en $\text{Hz}$ y $M$ es el número de estados discretos de señalización.

Pensemos en un péndulo o mecanismo de escape en un reloj de pared. Para evitar que las piezas mecánicas choquen y se traben entre sí, el péndulo solo puede oscilar a un ritmo máximo de $2B$ golpes por segundo. Si en cada golpe el mecanismo pudiera ajustar una aguja sobre infinitas muescas microscópicas sin que nada vibre, podríamos registrar una cantidad ilimitada de información en cada segundo. Sin embargo, en el mundo real, cualquier perturbación desvía la aguja e introduce errores de lectura.

> [!EXAMPLE] **Ejemplo 5:** Capacidad de Nyquist en Canal Telefónico Analógico
> 
> Un canal telefónico tradicional asigna un ancho de banda de voz de $B = 3000\text{ Hz}$ ($3\text{ kHz}$). Calculamos su capacidad teórica ideal sin ruido para señalización binaria ($M = 2$) y para una modulación multinivel de 64 estados ($M = 64$).
  
**Paso 1:** Para señalización binaria ($M = 2$) sustituimos $M = 2$ en la ecuación; como $\log_2(2) = 1$, la tasa límite es:

$$C_{\text{binaria}} = 2 \cdot (3000\text{ Hz}) \cdot \log_2(2) = 6000 \cdot 1 = 6000\text{ bps} = 6\text{ kbps}$$

**Paso 2:** Para señalización de 64 niveles ($M = 64$) calculamos $\log_2(64) = 6\text{ bits por símbolo}$. Multiplicamos los 6000 baudios máximos por 6 para alcanzar la tasa límite:

$$C_{\text{64-niveles}} = 2 \cdot (3000\text{ Hz}) \cdot \log_2(64) = 6000 \cdot 6 = 36000\text{ bps} = 36\text{ kbps}$$

## 3.2. Teorema de Shannon-Hartley para Canales con Ruido Gaussiano

Claude Shannon demostró que la potencia del ruido térmico impone un techo físico infranqueable a la tasa de transferencia que puede lograrse con una probabilidad de error arbitrariamente baja.

> [!QUOTE] **Definición Formal 9:** Ley de Capacidad de Shannon-Hartley
> 
> La capacidad teórica máxima ($C_{\text{Shannon}}$) de un canal físico sometido a ruido blanco gaussiano de densidad uniforme depende de su ancho de banda y de su relación señal a ruido lineal:
> 
> $$C_{\text{Shannon}} = B \cdot \log_2\left( 1 + \text{SNR}_{\text{lineal}} \right)$$
> 
> Expresada en bits por segundo ($\text{bps}$), donde $\text{SNR}_{\text{lineal}} = P_S / P_N$.

Pensemos en el llenado de recipientes mediante una balanza mecánica en un taller donde el piso tiembla constantemente. La fuerza con la que colocamos el peso es la señal, mientras que las vibraciones del suelo son el ruido. Si el temblor es fuerte, no podemos usar pesas pequeñas porque la aguja oscilará de manera impredecible; solo podremos distinguir con precisión pesas grandes y pesadas. La ley de Shannon establece exactamente cuántas marcas de peso distintas es capaz de discriminar la balanza en presencia de esa vibración.

> [!EXAMPLE] **Ejemplo 6:** Capacidad Límite de Shannon en un Radioenlace de Microondas
> 
> Un radioenlace de comunicaciones dispone de un ancho de banda de $B = 2\text{ MHz}$ y registra en el receptor una relación señal a ruido de $\text{SNR}_{\text{dB}} = 20\text{ dB}$. Calculamos la capacidad límite absoluta que permite la física del canal.

**Paso 1:** Pasamos los $20\text{ dB}$ a escala lineal elevando 10 a la $2.0$, lo que indica que la señal útil supera 100 veces la potencia del ruido.

$$\text{SNR}_{\text{lineal}} = 10^{\frac{20}{10}} = 10^2 = 100$$

**Paso 2:** Sumamos la unidad al cociente lineal ($101$) y calculamos su logaritmo en base 2 mediante el cociente de logaritmos naturales, aplicando la formulación de Shannon-Hartley.

$$C_{\text{Shannon}} = 2 \times 10^6\text{ Hz} \cdot \log_2(1 + 100) = 2 \times 10^6 \cdot \log_2(101)$$

$$\log_2(101) = \frac{\ln(101)}{\ln(2)} \approx \frac{4.6151}{0.6931} \approx 6.6582\text{ bits}$$

**Paso 3:** Multiplicamos el resultado por los $2\text{ MHz}$ de ancho de banda, determinando la capacidad máxima y obteniendo un límite superior de $13.32\text{ Mbps}$ que ningún esquema de transmisión podrá rebasar sin cometer errores.

$$C_{\text{Shannon}} = 2 \times 10^6 \cdot 6.6582 \approx 13.32\text{ Mbps}$$

## 3.3. Eficiencia Espectral y Modulación y Codificación Adaptativa (AMC)

La relación entre los modelos de Nyquist y Shannon gobierna la ingeniería de comunicaciones móviles contemporáneas:

- **Nyquist define la exigencia de diseño ($M$):** Indica cuántos estados de modulación requiere el circuito para alcanzar una tasa dada en un ancho de banda fijo ($C = 2B \log_2 M$).

- **Shannon define la tolerancia física del canal:** Dicta si el nivel de ruido del entorno permite distinguir esos $M$ niveles sin confusiones. Si se fuerza una tasa donde $C_{\text{Nyquist}} > C_{\text{Shannon}}$, la separación entre símbolos resulta menor que la dispersión del ruido, elevando drásticamente los errores.

> [!QUOTE] **Definición Formal 10:** Eficiencia Espectral Máxima
> 
> La eficiencia espectral ($\eta$) normaliza la tasa de información respecto al ancho de banda empleado:
> 
> $$\eta = \frac{C}{B} = \log_2\left( 1 + \text{SNR}_{\text{lineal}} \right) \quad \left[ \frac{\text{bps}}{\text{Hz}} \right]$$

Pensemos en regular la carga de camiones según las condiciones del camino. En una carretera seca y despejada, un camión puede circular con carga completa y remolques acoplados a velocidad crucero. Si cae una tormenta que vuelve resbaladizo el asfalto, intentar mantener esa misma carga provocará derrapes y accidentes; el conductor debe desacoplar el remolque y reducir la carga a un nivel seguro para no volcar. La modulación adaptativa aplica exactamente este ajuste ante fluctuaciones del canal inalámbrico.

> [!EXAMPLE] **Ejemplo 7:** Selección Adaptativa de Modulación en Celda 5G NR
> 
> Una celda 5G New Radio asigna a un usuario un canal de $B = 100\text{ MHz}$. Las mediciones en el terminal móvil reportan una $\text{SNR} = 25\text{ dB}$. Se evalúa si es viable operar con 256-QAM ($M = 256$) o si el enlace debe descender a 64-QAM ($M = 64$).

**Paso 1:** Convertimos la relación señal a ruido de $25\text{ dB}$ a escala lineal y calculamos la cota física de Shannon:

$$\text{SNR}_{\text{lineal}} = 10^{\frac{25}{10}} \approx 316.23$$
$$C_{\text{Shannon}} = 100 \times 10^6 \cdot \log_2(1 + 316.23) = 100 \times 10^6 \cdot \log_2(317.23) \approx 831\text{ Mbps}$$

Esto establece una eficiencia espectral máxima admisible de $\eta_{\text{máx}} \approx 8.31\text{ bps/Hz}$.

**Paso 2:** Evaluamos el requerimiento de Nyquist con 256-QAM ($r = \log_2 256 = 8\text{ bits}$):

$$C_{\text{Nyquist}} = 2 \cdot (100\text{ MHz}) \cdot 8 = 1600\text{ Mbps} \quad (\eta = 16\text{ bps/Hz})$$

Incluso con filtrado de Nyquist estricto ($S = B = 100\text{ MBaud}$):

$$R_{\text{256-QAM}} = 100\text{ MBaud} \cdot 8\text{ bits/símbolo} = 800\text{ Mbps} \quad (\eta = 8.0\text{ bps/Hz})$$

La tasa de Nyquist ideal duplica la capacidad del canal, superando el límite de Shannon. Al operar a $8.0\text{ bps/Hz}$ al borde del techo físico de $8.31\text{ bps/Hz}$, el margen de protección ante el ruido es de apenas $0.31\text{ bps/Hz}$, lo que provoca pérdidas masivas e inviabilidad en un canal con desvanecimientos.

**Paso 3:** La estación base aplica Modulación y Codificación Adaptativa (AMC) y evalúa el esquema alternativo 64-QAM ($r = \log_2 64 = 6\text{ bits}$):

$$R_{\text{64-QAM}} = 100\text{ MBaud} \cdot 6\text{ bits/símbolo} = 600\text{ Mbps} \quad (\eta = 6.0\text{ bps/Hz})$$

Al conmutar a 64-QAM y fijar la tasa en $600\text{ Mbps}$ con $\eta = 6.0\text{ bps/Hz}$, el sistema opera con holgura por debajo del techo de Shannon y la tasa de errores de trama se estabiliza. Si el usuario se aproxima a la estación base y la SNR supera los $30\text{ dB}$, el sistema restablecerá 256-QAM de forma automática.

---

> [!RESOURCES] REFERENCIAS
> 
> - **3GPP.** _3rd Generation Partnership Project Specification TS 38.101: 5G NR; User Equipment (UE) Radio Transmission and Reception_. Recuperado de [3gpp.org](https://www.3gpp.org/)
>   
> - **Balaguz, R.** (2026). _Material docente y diapositivas de la asignatura Comunicación de Datos_. Escuela de Computación, Facultad de Ciencias, Universidad Central de Venezuela (UCV).
>   
> - **Forouzan, B. A.** (2022). _Data Communications and Networking_ (6.ª ed.). McGraw-Hill Education.
>   
> - **IEEE Standards Association.** _IEEE Std 802.11ax-2021: Enhancements for High Efficiency WLAN_. Recuperado de [standards.ieee.org](https://standards.ieee.org/)
>   
> - **IETF.** _RFC Editor: Request for Comments Repository_ (RFCs para comunicaciones digitales y protocolos de transporte). Recuperado de [rfc-editor.org](https://www.rfc-editor.org/).
>   
> - **ITU-T.** _ITU-T Recommendations: Series G.984 (GPON) & G.9807.1 (XGS-PON)_. Unión Internacional de Telecomunicaciones. Recuperado de [itu.int](https://www.itu.int/)
>   
> - **Proakis, J. G., & Salehi, M.** (2008). _Digital Communications_ (5.ª ed.). McGraw-Hill.
>   
> - **Stallings, W.** (2014). _Data and Computer Communications_ (10.ª ed.). Pearson Education.
