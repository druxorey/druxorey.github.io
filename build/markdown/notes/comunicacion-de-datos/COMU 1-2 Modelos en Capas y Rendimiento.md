---
created: 2026-04-22T22:18:00
title: Modelos en Capas y Rendimiento
semester: 5
subject:
  - "[[COMU 0-0 Nota Informativa|Comunicación de Datos]]"
unit: 1
status: done
---

<h1 id="main-title"  align="center"> Modelos en Capas y Rendimiento </h1>

> [!TLDR] SÍNTESIS 
> La **arquitectura en capas** organiza la comunicación de datos mediante una **abstracción jerárquica** que descompone procesos complejos en módulos independientes. A través de modelos como **OSI** y la pila **TCP/IP**, se estandariza el **encapsulamiento** de información, garantizando la interoperabilidad entre sistemas heterogéneos. La eficacia de estas redes se evalúa mediante **métricas de rendimiento** y **QoS**, asegurando la entrega, exactitud y oportunidad de los datos transmitidos.

Si una aplicación tuviera que preocuparse al mismo tiempo por calibrar voltajes en el cobre, corregir interferencias del canal, calcular rutas entre miles de cruces intermedios y evitar desbordar la memoria del receptor, construir software distribuido sería sencillamente imposible. Intentar resolver todas estas responsabilidades dentro de un único bloque monolítico genera una rigidez inmanejable, donde modificar el tipo de cableado obligaría a reescribir desde cero cada programa de usuario.

El dilema fundamental de la ingeniería de redes consiste en cómo descomponer el caos en tareas independientes y aisladas, garantizando que cualquier equipo pueda dialogar de forma predecible sin importar su tecnología interna.

# 1. Arquitectura Jerárquica

Para gestionar la enorme complejidad que implica conectar sistemas informáticos, dividimos todo el proceso de comunicación en una secuencia de capas o módulos independientes. Cada nivel se enfoca exclusivamente en resolver una tarea específica del intercambio de datos. Gracias a este aislamiento, las capas superiores pueden desligarse por completo de los detalles técnicos y de la lógica interna con la que operan los niveles inferiores, limitándose a consumir sus servicios mediante una interfaz sencilla y bien definida.

Pensemos en el sistema de producción y envío de una imprenta industrial clásica. En este esquema, cada trabajador ejecuta un conjunto de reglas estricto dentro de su propia estación sin preocuparse por el trabajo de los demás. El empaquetador no necesita entender el idioma en que está escrito el texto ni cómo se calibraron los tipos de tinta en la imprenta, pues su única función es sellar la caja y entregársela al carretero. De la misma forma, si los caminos de tierra se sustituyen por rutas marítimas, únicamente cambia la técnica del transportista, sin obligar al autor a modificar su caligrafía ni al tipógrafo a cambiar sus moldes.

## 1.1. El Modelo de Referencia OSI (7 Capas)

A finales de la década de 1970, la Organización Internacional de Normalización (ISO) formuló el Modelo de Referencia para la Interconexión de Sistemas Abiertos (OSI, ISO/IEC 7498-1) con el objetivo de ofrecer un marco conceptual integral e interoperable para fabricantes de todo el mundo. El modelo descompone la comunicación en siete capas ordenadas:

|**Nivel**|**Capa**|**Función Principal en el Sistema**|**Protocolos / Entidades de Referencia**|
|---|---|---|---|
|**7**|**Aplicación**|Suministra interfaz directa y servicios de red a los procesos y programas del usuario final.|HTTP, DNS, SMTP, FTP|
|**6**|**Presentación**|Resuelve diferencias de sintaxis, aplica transformaciones de formatos de datos, compresión y cifrado.|TLS, JPEG, ASCII, UTF-8|
|**5**|**Sesión**|Establece, coordina, gestiona puntos de control («checkpoints») y finaliza los diálogos entre aplicaciones.|RPC, Sockets API, NetBIOS|
|**4**|**Transporte**|Proporciona transferencia de datos confiable o no confiable de extremo a extremo, control de flujo y multiplexación por puertos.|TCP, UDP, SCTP|
|**3**|**Red**|Gestiona el direccionamiento lógico global y selecciona las rutas de conmutación óptimas a través de subredes heterogéneas.|IPv4, IPv6, ICMP, enrutadores|
|**2**|**Enlace de Datos**|Estructura el flujo de bits en tramas, gestiona el acceso al medio físico compartido y realiza detección de errores por salto.|Ethernet (IEEE 802.3), Wi-Fi, switches|
|**1**|**Física**|Transmite la secuencia bruta de bits no estructurados sobre el canal mediante magnitudes electromagnéticas, lumínicas o mecánicas.|Cables coaxiales, pares trenzados, fibra óptica|

Las capas 1, 2 y 3 conforman el **subgrupo de soporte de red** (intervienen activamente en los nodos y conmutadores intermedios del trayecto). Las capas 5, 6 y 7 constituyen el **subgrupo de soporte de usuario** (operan exclusivamente en el software de los sistemas terminales). La capa 4 enlaza estructuralmente ambos mundos, aislando a las capas superiores de las contingencias de transmisión del hardware subyacente.

## 1.2. Obsolescencia Práctica de OSI frente a la Pila TCP/IP

A pesar de su utilidad teórica como herramienta de diseño pedagógico, los protocolos propios desarrollados para el modelo OSI jamás alcanzaron despliegue masivo en la infraestructura productiva mundial. El análisis académico e industrial atribuye el colapso de OSI frente a TCP/IP a cuatro fallos cardinales:

- **Mal momento:** El comité de la ISO tardó años en consensuar los estándares. Para cuando los protocolos OSI quedaron ratificados formalmente, la pila TCP/IP ya se encontraba plenamente operativa en la red ARPANET, distribuida de forma gratuita en las versiones del sistema operativo BSD UNIX y ampliamente amortizada por las universidades y laboratorios de investigación. Cambiar a OSI suponía un coste prohibitivo sin ventajas prácticas tangibles.

- **Mala tecnología:** La selección de siete niveles respondió a acuerdos administrativos y políticos más que a requerimientos técnicos. Las capas de Sesión y Presentación resultaron prácticamente vacías en la práctica cotidiana, mientras que las capas de Red y Enlace de Datos terminaron saturadas de funciones complejas. A su vez, ciertas responsabilidades críticas como el control de errores y el control de flujo se duplicaban innecesariamente en casi todas las capas.

- **Malas implementaciones:** Dada la complejidad desmedida de las especificaciones de la ISO, las primeras implementaciones de la pila OSI fueron voluminosas, lentas y requerían una cantidad desproporcionada de memoria de cómputo. En contraste, TCP/IP ofrecía un código optimizado, ligero y robusto.

## 1.3. La Pila TCP/IP Híbrida de 5 Capas

El funcionamiento de Internet se estructura en una **pila híbrida de 5 capas**, la cual sintetiza las virtudes conceptuales de OSI con la arquitectura pragmática de TCP/IP, agrupando los niveles de sesión, presentación y aplicación en una única capa superior:

| **Nivel Jerárquico**       | **PDU (Unidad de Datos)**        | **Identificador / Direccionamiento**                                      | **Dispositivo / Entidad Representativa**            |
| -------------------------- | -------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------- |
| **Capa 5: Aplicación**     | Datos / Mensaje ($M$)            | Nombre de Dominio / URL / URI                                             | Navegadores web, demonios de servicio               |
| **Capa 4: Transporte**     | Segmento (TCP) / Datagrama (UDP) | Puerto lógico de $16\text{ bits}$ ($0\text{ a }65535$)                    | Núcleo del sistema operativo, sockets               |
| **Capa 3: Red (Internet)** | Paquete / Datagrama IP           | Dirección lógica IP ($32\text{ bits}$ en IPv4, $128\text{ bits}$ en IPv6) | Enrutador («Router»), conmutador de capa 3          |
| **Capa 2: Enlace**         | Trama (Frame)                    | Dirección física MAC de $48\text{ bits}$                                  | Conmutador («Switch»), tarjeta de interfaz (NIC)    |
| **Capa 1: Física**         | Bit                              | Sincronismo de señal / Nivel de tensión                                   | Medios de cobre, transceptores ópticos, repetidores |

# 2. Mecánica de Encapsulamiento y Desencapsulamiento de Datos

La transmisión de información a través de una arquitectura jerárquica requiere que cada capa añada su propia información de control para coordinar las operaciones con su capa homóloga de destino.

## 2.1. Encapsulamiento Descendente y Formato de las Unidades de Datos

> [!QUOTE] **Definición 1:** Encapsulamiento de Protocolo
> 
> Sea $M$ la Unidad de Datos de Servicio ($\text{SDU}_{n}$) entregada por la capa superior $n+1$ a la capa $n$. El encapsulamiento es la operación mediante la cual la entidad de capa $n$ construye su Unidad de Datos de Protocolo ($\text{PDU}_n$) anteponiendo una cabecera de control $H_n$ y, eventualmente, adjuntando una cola de control $T_n$:
> 
> $$\text{PDU}_n = [H_n \mid \text{SDU}_n \mid T_n] = [H_n \mid \text{PDU}_{n+1} \mid T_n]$$
> 
> Donde $\mid$ denota la concatenación binaria de campos, siendo $T_n = \emptyset$ para todo nivel $n \neq 2$ en las pilas convencionales.

En el envío de una pieza mecánica de precisión mediante cajas de seguridad postales el fabricante envuelve la pieza y le pega una etiqueta que dice para qué departamento de la fábrica de destino sirve (mensaje de aplicación). Luego mete ese conjunto dentro de un maletín, con un candado que solo el encargado de mantenimiento de la otra fábrica puede abrir (segmento de transporte). A continuación, el maletín se introduce dentro de un cajón de madera donde se pinta con pintura blanca la ciudad y la calle del destinatario (paquete de red). Por último, ese cajón se coloca dentro de un contenedor de carga metálico con un sello numerado que certifica que las bisagras no se abrieron en el camino (trama de enlace con su cola de verificación). Los marineros del buque de carga solo ven y mueven el contenedor metálico por su matrícula exterior, desconociendo por completo qué tipo de pieza viaja en el centro.

El flujo descendente en el nodo emisor se descompone operativamente de la siguiente forma:

1. **Capa de Aplicación:** El proceso de usuario produce un mensaje en bruto $M$ estructurado según la sintaxis del protocolo aplicativo (ej. una solicitud HTTP).

2. **Capa de Transporte:** Recibe $M$, lo fragmenta si excede el tamaño máximo permitido y le antepone la cabecera de transporte $H_t$. Esta cabecera incorpora el puerto de origen y puerto de destino, números de secuencia y códigos de verificación. El resultado es el **segmento**:
	
$$S = [H_t \mid M]$$
    
2. **Capa de Red:** Toma el segmento $S$ en calidad de carga útil («payload») y añade la cabecera de red $H_n$, que incluye las direcciones IP de origen y destino, el tiempo de vida ($\text{TTL}$) y directivas de fragmentación. El bloque resultante es el **paquete** o datagrama:
    
$$P = [H_n \mid S] = [H_n \mid H_t \mid M]$$
    
2. **Capa de Enlace:** Agrega una cabecera de enlace $H_l$ con las direcciones físicas MAC del salto inmediato y añade al final una cola de control $T_l$, conformada por una secuencia de verificación de trama (FCS, «Frame Check Sequence») calculada típicamente mediante comprobación de redundancia cíclica ($\text{CRC}-32$). El bloque resultante es la **trama** («frame»):

$$F = [H_l \mid P \mid T_l] = [H_l \mid H_n \mid H_t \mid M \mid T_l]$$

2. **Capa Física:** Toma la secuencia de bits de $F$ y modula las magnitudes físicas del medio (pulsos de tensión en cobre, modulaciones de luz en fibra o fases de onda portadora en el aire).

## 2.2. Desencapsulamiento Ascendente y Verificación de Integridad

En el nodo receptor se ejecuta el proceso inverso de desencapsulamiento ascendente:

1. **Recepción física:** El transceptor digitaliza la señal y reconstruye la secuencia discreta de bits.

2. **Verificación de capa 2:** La tarjeta de red evalúa la cola $T_l$ aplicando el polinomio generador del $\text{CRC}$. Si detecta alteraciones binarias causadas por ruido en el canal, descarta la trama en el acto. Si la trama es íntegra, contrasta la dirección MAC de destino de la cabecera $H_l$ con la suya propia; si coincide, retira $H_l$ y $T_l$, y despacha el paquete $P$ a la capa de red.

3. **Inspección de capa 3:** El sistema operativo examina la cabecera $H_n$, decrementa el $\text{TTL}$, valida la dirección IP de destino, retira $H_n$ y pasa el segmento $S$ al protocolo de transporte especificado.

4. **Despacho de capa 4:** La capa de transporte inspecciona $H_t$, comprueba el checksum de extremo a extremo, reordena los segmentos si llegaron permutados y lee el número de puerto de destino para entregar la carga útil limpia $M$ al proceso o socket exacto en la capa de aplicación.

**Operación en Nodos Intermedios:**

- Un conmutador de capa 2 (switch) solo desencapsula hasta la cabecera de enlace $H_l$ para conmutar la trama hacia el puerto físico correspondiente, sin alterar $H_n$ ni $H_t$.

- Un enrutador de capa 3 (router) desencapsula hasta la cabecera de red $H_n$ para consultar su tabla de reenvío; al saltar al siguiente enlace, descarta la cabecera $H_l$ y la cola $T_l$ viejas, actualiza el $\text{TTL}$ en $H_n$ y genera una nueva cabecera $H_l'$ y una nueva cola $T_l'$ adaptadas a la tecnología del nuevo medio de enlace.

# 3. Métricas de Rendimiento y Criterios de Eficacia en el Canal

## 3.1. Ancho de Banda Espectral frente a Tasa Binaria

Existe confusión por el uso del término «ancho de banda». En ciencias de la computación e ingeniería de telecomunicaciones es obligatorio distinguir rigurosamente la magnitud analógica de la digital:

> [!QUOTE] **Definición 2:** Ancho de Banda Espectral y Capacidad Binaria
> 
> - El **Ancho de Banda Espectral** ($B$), medido en Hertz ($\text{Hz}$), es el rango continuo de frecuencias que delimita el espectro de una señal o el intervalo frecuencial que una línea física puede dejar pasar sin atenuación inaceptable:
>     
> $$B = f_{\text{máx}} - f_{\text{mín}}$$
>     
> - La **Tasa Binaria o Ancho de Banda Digital** ($R$), medida en bits por segundo ($\text{bps}$), representa el número de dígitos binarios discretos que un canal puede transportar por unidad de tiempo.
>     
> La cota teórica entre ambas magnitudes en un canal con ruido gaussiano blanco viene fijada por el Teorema de Shannon-Hartley:
> 
> $$C = B \cdot \log_2\left(1 + \text{SNR}\right)$$
> 
> Donde $\text{SNR} = \frac{S}{N}$ representa la relación señal-ruido en escala lineal.

En un puente vehicular el ancho de banda espectral ($B$) equivale al ancho físico del puente medido con una cinta métrica (cuántos metros de calzada tiene la estructura).

La tasa binaria ($R$) representa la cantidad máxima de toneladas que pueden pasar rodando por minuto sobre él. El espacio físico disponible ($B$) condiciona directamente el volumen de carga que podemos mover por segundo ($R$), pero la velocidad a la que circulan los vehículos y la rugosidad de los tablones (el nivel de ruido del camino) limitan el flujo neto de mercancía.

## 3.2. Rendimiento Real frente a Caudal Útil

La capacidad nominal del hardware establece una cota superior teórica, pero las aplicaciones rara vez experimentan esa velocidad de transferencia:

- **Capacidad Nominal ($R$):** Máxima velocidad física a la que los circuitos pueden inyectar bits en el medio.

- **Rendimiento Real («Throughput», $T$):** Tasa efectiva de bits totales (incluyendo cabeceras, bits de sincronismo y tramas de control) que cruzan exitosamente una sección de la red por unidad de tiempo. Se ve degradado por contención en el canal, cuellos de botella y pérdidas de paquetes.

- **Caudal Útil («Goodput», $G$):** Tasa neta de bits de datos útiles de la aplicación ($M$) entregados al receptor por segundo, excluyendo todas las cabeceras de protocolo ($H_l, H_n, H_t$), las colas ($T_l$), los paquetes de control de sesión y los bloques retransmitidos debido a pérdidas:
    
$$G = \frac{\text{Bits de datos útiles recibidos sin error}}{t_{\text{total}}} \le T \le R$$

## 3.3. Los Cuatro Criterios de Evaluación del Canal

La eficacia y calidad operativa de un sistema de comunicación de datos se fundamenta en cuatro pilares elementales:

1. **Entrega (Delivery):** El sistema debe encaminar y entregar la información al destinatario correcto y únicamente a él. Si los datos alcanzan un nodo equivocado o se pierden en el trayecto, el enlace carece de utilidad funcional.

2. **Exactitud (Accuracy):** Los datos recibidos deben ser idénticos a los transmitidos. La alteración de bits provocada por interferencias que no sea detectada ni corregida en destino invalida la información (un error de un solo bit en un registro financiero altera por completo su valor).

3. **Oportunidad (Timeliness):** La información debe entregarse dentro de una ventana de tiempo admisible. En flujos interactivos de voz y video en tiempo real, un paquete que llega demorado es inservible y se descarta.

4. **Fluctuación de Fase (Jitter):** Los paquetes pertenecientes a un mismo flujo deben arribar con retardos temporales predecibles y uniformes. Una variación desordenada en los tiempos de tránsito deteriora la calidad perceptiva de los flujos continuos.

## 3.4. Calidad de Servicio (QoS) y Mecanismos de Provisión

> [!QUOTE] **Definición 3:** Calidad de Servicio (QoS)
> 
> La Calidad de Servicio es la capacidad cuantitativa de una red para otorgar un trato diferenciado a flujos específicos de tráfico, asegurando contractualmente cotas delimitadas de ancho de banda, retardo máximo, jitter y tasa de pérdida de paquetes en función de los requerimientos de la aplicación.

Para garantizar niveles de servicio, los proveedores formulan Acuerdos de Nivel de Servicio (SLA, «Service Level Agreement») con sus clientes. A nivel arquitectónico existen dos paradigmas para implantar QoS en redes conmutadas:

- **Servicios Integrados (IntServ - RFC 1633):** Enfoque de grano fino basado en reserva de recursos previa flujo por flujo mediante protocolos de señalización (como RSVP). Exige que cada enrutador intermedio almacene y mantenga tablas de estado por cada sesión activa, lo que introduce problemas severos de escalabilidad en el núcleo de Internet.

- **Servicios Diferenciados (DiffServ - RFC 2475):** Enfoque de grano grueso basado en clases de servicio. Los paquetes se marcan en el borde de la red asignando un código en la cabecera IP (campo DSCP de 6 bits). Los enrutadores del núcleo no memorizan sesiones individuales; se limitan a clasificar el tráfico y aplicar comportamientos por salto (PHB, «Per-Hop Behavior») priorizando las colas correspondientes.

# 4. Formulación del Retardo y Fluctuación de Fase

## 4.1. Ecuación Analítica del Retardo Total Unidireccional

El tiempo total que le toma a una unidad de datos viajar desde el nodo emisor hasta ser recibida íntegramente por el nodo de destino no es instantáneo. Viene determinado por cuatro factores acumulativos:

> [!QUOTE] **Definición 4:** Retardo Total de Extremo a Extremo
> 
> Para un enlace punto a punto, el retardo total unidireccional $L$ experimentado por un paquete de longitud $D$ bits es la suma algebraica de cuatro componentes disjuntas:
> 
> $$L = t_{\text{trans}} + t_{\text{prop}} + t_{\text{queue}} + t_{\text{proc}} = \frac{D}{R} + \frac{d}{v} + t_{\text{queue}} + t_{\text{proc}}$$
> 
> Donde:
> 
> - $D$: Tamaño total del paquete transmitido (en bits).
>     
> - $R$: Capacidad de transmisión de la interfaz de red (en bits por segundo, $\text{bps}$).
>     
> - $d$: Distancia física del enlace entre emisor y receptor (en metros, $\text{m}$).
>     
> - $v$: Velocidad de propagación de la señal en el medio material (en metros por segundo, $\text{m/s}$). En par trenzado de cobre $v \approx 2.3 \times 10^8\text{ m/s}$, y en fibra óptica $v \approx 2.0 \times 10^8\text{ m/s}$ (aproximadamente $\frac{2}{3} c$, donde $c = 3 \times 10^8\text{ m/s}$).
>     
> - $t_{\text{queue}}$: Tiempo de permanencia del paquete en las colas de memoria del conmutador esperando turno de salida (en segundos, $\text{s}$).
>     
> - $t_{\text{proc}}$: Tiempo consumido por el procesador del nodo para verificar cabeceras, recalcular códigos de comprobación y determinar la interfaz de reenvío (en segundos, $\text{s}$).

El retardo de transmisión ($t_{\text{trans}} = \frac{D}{R}$) es el tiempo necesario para colocar todos los bits que componen un paquete de datos en el medio físico, determinado directamente por el tamaño del paquete en bits y la capacidad de transferencia del enlace.

El retardo de propagación ($t_{\text{prop}} = \frac{d}{v}$) es el tiempo que tardan las señales físicas en recorrer la distancia geográfica entre el emisor y el receptor a través del medio de transmisión, dependiendo exclusivamente de dicha distancia y de la velocidad de propagación de la onda en el material.

El retardo de procesamiento ($t_{\text{proc}}$) es el tiempo requerido por los nodos de red para examinar las cabeceras de los paquetes, verificar la integridad de los datos y calcular la ruta o interfaz de salida correspondiente.

El retardo de encolamiento ($t_{\text{queue}}$) es el tiempo variable que un paquete permanece almacenado en las memorias intermedias o búferes de un dispositivo de red mientras espera su turno para ser transmitido, debido a la congestión o saturación temporal del canal.

## 4.2. Modelado de la Fluctuación de Fase («Jitter»)

> [!QUOTE] **Definición 5:** Fluctuación de Fase o Jitter
> 
> La fluctuación de fase instantánea ($J$) se define como la diferencia absoluta entre los retardos de extremo a extremo experimentados por dos paquetes sucesivos de un mismo flujo:
> 
> $$J = \vert L_i - L_{i-1} \vert$$
> 
> En protocolos de transporte en tiempo real (RTP, RFC 3550), la estimación estadística del retardo relativo acumulado se modela evaluando la variación en la separación de llegada frente a la de partida:
> 
> $$D(i) = \left( R_i - R_{i-1} \right) - \left( S_i - S_{i-1} \right)$$
> 
> Calculando el jitter medio estimado $J(i)$ mediante una media móvil exponencial con factor de amortiguamiento $\alpha = \frac{1}{16}$:
> 
> $$J(i) = \frac{15}{16} J(i-1) + \frac{1}{16} \vert D(i) \vert$$
> 
> Donde $S_k$ es la marca temporal de transmisión del paquete $k$ y $R_k$ es su marca temporal de recepción en destino.

Imaginemos una videollamada en la que dos amigos se turnan para hablar enviando frases cortas cada pocos segundos. Si la conexión es completamente estable, cada frase llega en el momento exacto y la conversación fluye de forma natural y continua ($J = 0$).

Pero si una de las frases se retrasa porque la red se congestionó momentáneamente, y la siguiente llega volando porque el canal se despejó, ambas frases se amontonarán en la recepción o llegarán de golpe. Esa irregularidad y variación constante en el tiempo que tardan en llegar los mensajes es el jitter.

## 4.3. Resolución de Problemas de Rendimiento y Retardo

> [!EXAMPLE] **Ejemplo 1:** Cálculo de Retardo Total y Fluctuación Instantánea en Fibra Óptica
> 
> **Enunciado:** Dos enrutadores distantes $d = 400\text{ km}$ se interconectan mediante un enlace punto a punto de fibra óptica monomodo donde las ondas electromagnéticas se propagan a $v = 2 \times 10^8\text{ m/s}$. El enlace opera a una tasa de $R = 100\text{ Mbps}$ ($100 \times 10^6\text{ bps}$). El emisor transmite consecutivamente dos paquetes idénticos de longitud $D = 1500\text{ bytes}$ ($12000\text{ bits}$).
> 
> Durante la emisión del paquete 1, la red presenta baja carga: su tiempo en cola es $t_{\text{queue}, 1} = 1.20\text{ ms}$ y su tiempo de procesamiento es $t_{\text{proc}, 1} = 0.05\text{ ms}$.
> 
> Justo después, ocurre una ráfaga de tráfico entrante de otros flujos que satura temporalmente el búfer: el paquete 2 experimenta un tiempo en cola de $t_{\text{queue}, 2} = 4.80\text{ ms}$, manteniéndose su tiempo de procesamiento en $t_{\text{proc}, 2} = 0.05\text{ ms}$.
> 
> Calcule:
> 
> 1. El retardo de transmisión ($t_{\text{trans}}$) y de propagación ($t_{\text{prop}}$) del canal.
>     
> 2. El retardo total de cada paquete ($L_1$ y $L_2$).
>     
> 3. El jitter instantáneo ($J$) experimentado entre ambas muestras.
     
**Paso 1:** Convertimos las dimensiones a unidades fundamentales del Sistema Internacional y calculamos las componentes deterministas del enlace: multiplicamos los $1500\text{ bytes}$ por $8$ para obtener $12000\text{ bits}$ y dividimos entre la capacidad de transmisión del enlace ($100 \times 10^6\text{ bps}$) para determinar el tiempo de transmisión ($t_{\text{trans}}$), que es el tiempo que el hardware tarda en modular todos los bits hacia la línea:

$$t_{\text{trans}} = \frac{D}{R} = \frac{12000\text{ bits}}{100 \times 10^6\text{ bps}} = 0.00012\text{ s} = 0.12\text{ ms}$$

**Paso 2:** Calculamos el tiempo de viaje físico de la luz a lo largo de los $400\text{ km}$ ($400000\text{ m}$) dividiendo entre la velocidad de la luz en el núcleo de sílice ($2 \times 10^8\text{ m/s}$), obteniendo el retardo de propagación ($t_{\text{prop}}$). Notamos que tanto $t_{\text{trans}}$ como $t_{\text{prop}}$ son valores constantes e invariantes entre paquetes idénticos en la misma línea:

$$t_{\text{prop}} = \frac{d}{v} = \frac{400 \times 10^3\text{ m}}{2 \times 10^8\text{ m/s}} = 0.002\text{ s} = 2.00\text{ ms}$$

**Paso 3:** Sumamos las cuatro componentes del retardo ($t_{\text{trans}}$, $t_{\text{prop}}$, $t_{\text{queue}}$ y $t_{\text{proc}}$) para cada datagrama. Vemos que el primer paquete llega a destino a los $3.37\text{ ms}$, pero el segundo se retrasa hasta los $6.97\text{ ms}$ debido exclusivamente al encolamiento provocado por la congestión del conmutador intermedio:

$$L_1 = t_{\text{trans}} + t_{\text{prop}} + t_{\text{queue}, 1} + t_{\text{proc}, 1} = 0.12\text{ ms} + 2.00\text{ ms} + 1.20\text{ ms} + 0.05\text{ ms} = 3.37\text{ ms}$$
$$L_2 = t_{\text{trans}} + t_{\text{prop}} + t_{\text{queue}, 2} + t_{\text{proc}, 2} = 0.12\text{ ms} + 2.00\text{ ms} + 4.80\text{ ms} + 0.05\text{ ms} = 6.97\text{ ms}$$

**Paso 4:** Evaluamos la diferencia absoluta entre ambas latencias para determinar la fluctuación instantánea o *jitter* ($J$). El receptor experimenta una variación de llegada de $3.60\text{ ms}$. Si este flujo transportara audio en tiempo real sin un búfer de compensación (*jitter buffer*) en la aplicación receptora, la reproducción sufriría un salto audible o congelamiento:

$$J = \vert L_2 - L_1 \vert = \vert 6.97\text{ ms} - 3.37\text{ ms} \vert = 3.60\text{ ms}$$

# 5. Organismos Internacionales de Normalización

Para que equipos diseñados por compañías competidoras puedan dialogar de forma determinista, las especificaciones de hardware y software deben estandarizarse formalmente.

## 5.1. IEEE (Institute of Electrical and Electronics Engineers)

El Instituto de Ingenieros Eléctricos y Electrónicos es la mayor asociación profesional de ingeniería del mundo. Su labor en telecomunicaciones se concentra de forma preponderante en las dos capas más bajas de la pila arquitectónica: la Capa Física y la Capa de Enlace de Datos.

En 1980, la entidad constituyó el **Comité de Estandarización IEEE 802** para normalizar las redes de área local (LAN) y metropolitana (MAN). Para resolver la diversidad de medios de comunicación físicos, el IEEE dividió la Capa de Enlace de Datos de OSI en dos subcapas funcionales:

- **Subcapa de Control de Enlace Lógico (LLC, IEEE 802.2):** Proporciona una interfaz de servicio homogénea e independiente hacia la capa de red superior, gestionando control de errores y direccionamiento lógico entre procesos.

- **Subcapa de Control de Acceso al Medio (MAC):** Gestiona los protocolos de contención y acceso al canal físico específico, estructurando las tramas y manipulando las direcciones físicas de hardware.

Los grupos de trabajo más influyentes del comité IEEE 802 comprenden:

- **IEEE 802.3:** Redes locales por cable bajo la tecnología Ethernet (con variantes desde $10\text{ Mbps}$ hasta $400\text{ Gbps}$).

- **IEEE 802.11:** Redes inalámbricas de área local (WLAN), conocidas comercialmente como Wi-Fi.

- **IEEE 802.15:** Redes de área personal inalámbricas (WPAN), incluyendo estándares para Bluetooth (802.15.1) y Zigbee (802.15.4).

## 5.2. IETF (Internet Engineering Task Force)

La Fuerza de Tarea de Ingeniería de Internet es el organismo técnico abierto responsable del diseño y evolución de los protocolos centrales de Internet (concentrado en las capas de red, transporte y aplicación). Depende administrativamente de la Internet Society (ISOC) y del Consejo de Arquitectura de Internet (IAB).

La filosofía organizativa del IETF rechaza la burocracia jerárquica tradicional, rigiéndose por el principio rector articulado por David Clark: _«Rechazamos a los reyes, a los presidentes y a las votaciones; creemos en el consenso aproximado y en el código que funciona»_ («rough consensus and running code»).

Las especificaciones técnicas de Internet se publican bajo la denominación de **Peticiones de Comentarios** (RFC, «Request for Comments»). A diferencia de los borradores, los documentos RFC, una vez publicados con su número formal asignado, son inmutables de por vida; si un estándar necesita una mejora, se redacta un nuevo RFC que declara explícitamente actualizar o dejar obsoleto («obsoletes») al documento anterior.

El ciclo formal de maduración técnica comprende los siguientes estadios:

1. **Borrador de Internet («Internet Draft»):** Documento de trabajo provisional en constante discusión, sin valor de estándar y con una vigencia máxima de 6 meses tras la cual se renueva o desaparece.

2. **Estándar Propuesto («Proposed Standard»):** Si el borrador demuestra madurez y el IESG lo aprueba, se publica como RFC formal. Especifica una solución estable y bien resuelta técnicamente.

3. **Estándar en Borrador («Draft Standard»):** Exige demostrar la existencia de al menos dos implementaciones independientes, completas e interoperables probadas en entornos productivos durante meses.

4. **Estándar de Internet («Internet Standard»):** Nivel superior de ratificación técnica. Recibe frecuentemente un identificador suplementario (STD) y constituye una norma obligatoria de la arquitectura de Internet.

## 5.3. ITU-T (International Telecommunication Union - Telecommunication Standardization Sector)

La Unión Internacional de Telecomunicaciones (UIT) es el organismo especializado de las Naciones Unidas en el ámbito de las tecnologías de la información y la comunicación. Su sector de normalización, el **ITU-T** (denominado formalmente CCITT hasta 1993), coordina las normas y tratados internacionales entre gobiernos soberanos y corporaciones de telecomunicaciones autorizadas.

A diferencia del IETF, la ITU-T opera mediante conferencias diplomáticas y grupos de estudio formales divididos por áreas temáticas (como el Estudio de Grupo 15 para infraestructuras de transporte óptico). Sus documentos normativos se denominan **Recomendaciones** («Recommendations»). Aunque formalmente se definen como sugerencias técnicas, en la práctica son de cumplimiento obligatorio para posibilitar el tránsito fronterizo entre operadoras nacionales de telecomunicaciones.

Aportes fundamentales ratificados por ITU-T:

- **Series V y X:** Estándares históricos de modulación para transmisión de datos sobre telefonía conmutada (ej. V.90 a $56\text{ kbps}$) y redes públicas de datos (ej. X.25 y el estándar de certificados criptográficos X.509).

- **Series G y H:** Sistemas de transmisión digital, jerarquías digitales síncronas (SDH), estándares de fibra óptica y algoritmos mundiales de compresión de video digital (tales como H.264 / AVC y H.265 / HEVC, desarrollados conjuntamente con ISO/IEC).

- **Series G.992 (ADSL / VDSL):** Estándares mundiales que permitieron transformar las líneas tradicionales de pares de cobre telefónicas en enlaces de acceso a Internet de alta velocidad.

---

> [!RESOURCES] REFERENCIAS 
> 
> - **Cerf, V. & Kahn, R.** (1974). *A Protocol for Packet Network Interconnection*. IEEE Transactions on Communications, COM-22(5), 637–648.
>   
> - **Comer, D. E.** *Internetworking with TCP/IP, Volume I: Principles, Protocols, and Architecture*. 6.ª ed., Prentice Hall.
>   
> - **Day, J. D. & Zimmermann, H.** (1983). *The OSI Reference Model*. Proceedings of the IEEE, 71(12), 1334–1340.
>   
> - **Forouzan, B. A.** *Data Communications and Networking*. 5.ª ed., McGraw-Hill.
>   
> - **IEEE 802 LAN/MAN Standards Committee.** *IEEE 802 Standards for Local and Metropolitan Area Networks*. Disponible en [ieee802.org](https://www.ieee802.org/).
>   
> - **IETF (Internet Engineering Task Force).** *Official Internet Protocol Specifications and RFC Database*. Disponible en [ietf.org](https://www.ietf.org/).
>   
> - **ISO (International Organization for Standardization).** *ISO/IEC 7498-1: Information Technology — Open Systems Interconnection — Basic Reference Model*. Disponible en [iso.org](https://www.iso.org/standard/20269.html).
>   
> - **ITU-T (International Telecommunication Union - Telecommunication Standardization Sector).** *ITU-T Recommendations and Standards*. Disponible en [itu.int](https://www.itu.int/itu-t/).
>   
> - **Peterson, L. L. & Davie, B. S.** *Computer Networks: A Systems Approach*. 5.ª ed., Morgan Kaufmann.
>   
> - **Stallings, W.** *Data and Computer Communications*. 10.ª ed., Pearson / Prentice Hall.
>   
> - **Tanenbaum, A. S. & Wetherall, D.** *Computer Networks*. 5.ª ed., Prentice Hall.
