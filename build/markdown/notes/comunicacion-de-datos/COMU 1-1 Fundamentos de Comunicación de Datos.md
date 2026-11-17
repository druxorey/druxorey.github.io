---
created: 2026-04-20 06:57
title: Fundamentos de Comunicación y Topologías de Red
semester: 5
subject:
  - "[[COMU 0-0 Nota Informativa|Comunicación de Datos]]"
unit: 1
status: done
---

<h1 id="main-title"  align="center"> Fundamentos de Comunicación y Topologías de Red </h1>

> [!TLDR] SÍNTESIS 
> La **comunicación de datos** constituye el intercambio estructurado de información digital mediante la transformación de bits en señales físicas, regido por **protocolos** que aseguran la sintaxis, semántica y temporización. Este proceso integra **emisor, receptor, mensaje, medio y protocolo**, organizándose bajo diversas **topologías físicas** y arquitecturas lógicas como **cliente-servidor** o **SDN**, optimizando la conectividad y gestión eficiente de recursos en redes de distinta cobertura.

Mover información entre dos puntos distantes no ocurre por arte de magia dentro de las computadoras. Cualquier intercambio exige transformar datos digitales en energía física; sin embargo, el mundo real impone barreras inevitables: la señal pierde fuerza con la distancia, el espectro electromagnético es un recurso limitado, la infraestructura física exige grandes costos de energía y el ruido ambiental distorsiona las señales en tránsito. Resulta imposible conectar equipos enviando señales a ciegas sin un acuerdo estricto sobre cómo interpretar esa energía. De esta necesidad elemental surge la arquitectura fundamental que rige a todo sistema de transmisión.

# 1. Axiomas de la Comunicación de Datos

La comunicación humana parte de la necesidad de transferir ideas entre dos entidades que comparten un canal físico y un código de representación acordado. Si dos personas intentan dialogar a través de idiomas incompatibles o bajo un nivel de ruido acústico intolerable en el aire, el intercambio se degrada o colapsa.

La comunicación de datos traslada este principio al ámbito digital. En este entorno, los mensajes se descomponen en secuencias discretas de bits (ceros y unos). Los dispositivos conectados actúan como transductores que transforman representaciones numéricas en perturbaciones físicas mensurables (pulsos de voltaje en cobre, variaciones lumínicas en fibra óptica u ondas electromagnéticas en el espacio libre). Para que esta interacción sea comprensible y reproducible, los sistemas requieren protocolos estandarizados que dicten la organización, validación y sincronización de las tramas de información.

> [!QUOTE] **Definición 1:** Protocolo de Comunicación
> 
> Un protocolo es un conjunto formal de normas, convenciones y especificaciones que gobiernan el intercambio de información entre dos o más entidades dentro de un sistema de comunicación. Define las reglas de sintaxis (formato y ordenamiento de bits), semántica (significado de los patrones binarios) y temporización (sincronización y velocidad de transferencia), asegurando una interacción determinista y la gestión estructurada de fallos en el canal.

## 1.1. Los Cinco Componentes Sistémicos

Todo sistema elemental de transferencia de datos está constituido por cinco elementos indispensables:

- **Emisor:** Dispositivo o nodo de origen que genera la información bruta y la acondiciona en forma de señales físicas aptas para viajar a través del canal.

- **Receptor:** Dispositivo de destino que captura la señal electromagnética u óptica del canal, la decodifica y reconstruye el mensaje original.

- **Mensaje (Payload):** La carga útil o información neta que se desea transferir entre los extremos (texto, datos numéricos, imágenes, audio o bloques binarios ejecutables).

- **Medio de transmisión:** El soporte físico por el cual viaja la energía de la señal desde el emisor hacia el receptor. Se divide en dos clases:

    - **Medios guiados:** Confinan las ondas a lo largo de un camino material específico (pares trenzados de cobre, cable coaxial y cables de fibra óptica).

    - **Medios no guiados:** Permiten la propagación de ondas electromagnéticas a través del aire, el agua o el vacío sin confinamiento físico (radiofrecuencia, microondas y radiación infrarroja).

- **Protocolo:** Conjunto de reglas algorítmicas adoptadas por emisor y receptor que regulan la transferencia. Sin su aplicación previa, ambos extremos pueden estar conectados físicamente pero ser incapaces de comunicarse.

## 1.2. Elementos Formales de un Protocolo

El diseño riguroso de cualquier protocolo informático se descompone en tres componentes estructurales:

- **Sintaxis:** Refiere a la estructura formal y a la distribución espacial de los datos dentro del bloque transmitido. Define el orden, la longitud en bits y el propósito de cada campo (por ejemplo, especificar que los primeros 16 bits representan la dirección del emisor, los 16 bits siguientes la del receptor y el remanente el cuerpo de datos útiles).

- **Semántica:** Establece el significado interpretativo de cada sección de control y los cursos de acción asociados. Determina qué acción operativa debe ejecutar el receptor al descifrar un patrón concreto (por ejemplo, reconocer si un patrón de bits indica una confirmación positiva de recepción, una solicitud de retransmisión por suma de comprobación inválida o una petición de cierre de enlace).

- **Temporización («Timing» y Secuenciación):** Regula la escala temporal del enlace, cubriendo la velocidad de transmisión y el ordenamiento secuencial de los intercambios. Resuelve la adaptación de velocidades para evitar que un emisor rápido desborde la capacidad de absorción de un receptor lento y define los intervalos máximos de espera antes de declarar la pérdida de un paquete.

## 1.3. Modos de Transmisión según Direccionalidad

La orientación vectorial del flujo de datos a través del canal establece tres modos de operación:

- **Símplex:** Transferencia estrictamente unidireccional. La asignación de funciones es estática: un extremo opera exclusivamente como transmisor y el otro únicamente como receptor, sin que estos roles puedan alternarse.

> [!EXAMPLE] **Ejemplo 1:** Transmisión Símplex 
> 
> La señalización luminosa de un faro hacia los barcos en altamar o la transferencia de pulsos desde un teclado convencional hacia la placa base. Todo el ancho de banda del medio se reserva de forma permanente para un único sentido.

- **Half-Duplex:** Transferencia bidireccional no simultánea. Ambos nodos tienen la capacidad de emitir y recibir información, pero deben alternar el uso del canal en el dominio temporal.
    
> [!EXAMPLE] **Ejemplo 2:** Transmisión Half-Duplex
> 
> Un tramo de vía férrea de un solo carril donde los trenes pueden avanzar en ambos sentidos, pero exige que un convoy espere en la estación lateral mientras el otro cruza para evitar un choque frontal (análogo al uso de radiocomunicadores portátiles con botón de alternancia).

- **Full-Duplex:** Transferencia bidireccional y simultánea. Ambos extremos pueden emitir y capturar señales concurrentemente sin riesgo de interferencia mutua. Se logra aislando dos caminos físicos independientes (como dos hilos de cobre o dos fibras ópticas paralelas) o dividiendo el espectro del canal en bandas de frecuencia disjuntas.
        
> [!EXAMPLE] **Ejemplo 3: Transmisión Full-Duplex**
> 
> Una carretera de dos canales independientes donde los vehículos circulan en sentidos opuestos de forma continua y sin interrupciones cruzadas.

# 2. Clasificación de Redes por Cobertura Física

El alcance geográfico condiciona de manera directa el retardo de propagación electromagnética, las tecnologías de modulación admisibles, la tasa de errores esperada y el régimen administrativo de la infraestructura.

> [!QUOTE] **Definición 2:** Cobertura Física de Red
> 
> Es la delimitación del alcance espacial dentro del cual una arquitectura de comunicación mantiene la integridad física de sus señales y cotas operativas de latencia, clasificando las redes según la distancia métrica ($d$) entre sus nodos extremos y la naturaleza de sus medios de transporte.

Las redes se clasifican formalmente según los siguientes rangos de cobertura física:

- **PAN (Personal Area Network):** Cobertura confinada al entorno operativo inmediato de una persona, con un límite nominal de $d \le 10\text{ m}$. Emplea enlaces inalámbricos de muy bajo consumo energético y corto alcance (como Bluetooth o Zigbee) para interconectar sensores corporales y dispositivos periféricos.

- **LAN (Local Area Network):** Cobertura circunscrita a un área arquitectónica delimitada, como una oficina, laboratorio o edificio corporativo ($d \le 1\text{ km}$). Presenta altas tasas de transmisión (de $1\text{ Gbps}$ a $100\text{ Gbps}$), medios de transmisión privados y tasas de error extremadamente reducidas (ej. tecnologías Ethernet o Wi-Fi).

- **CAN (Campus Area Network):** Interconecta varias redes LAN geográficamente adyacentes dentro de un predio delimitado, cubriendo un radio de $1\text{ km} < d \le 5\text{ km}$. Utiliza canalizaciones y cableado de alta capacidad de propiedad privada institucional (universidades, bases militares o complejos industriales) sin arrendar infraestructura pública de telecomunicaciones.

- **MAN (Metropolitan Area Network):** Cobertura que abarca una ciudad o aglomeración urbana ($5\text{ km} < d \le 50\text{ km}$). Suele sustentarse sobre anillos metropolitanos de fibra óptica operados por empresas de telecomunicaciones para interconectar sedes dispersas de entidades bancarias o suministrar acceso corporativo.

- **WAN (Wide Area Network):** Cobertura geográfica masiva que cruza fronteras regionales, nacionales o continentales ($d > 50\text{ km}$). Depende de infraestructuras de transporte público operadas por compañías de telecomunicaciones, enlaces satelitales y cables submarinos. Internet es el ejemplo canónico de WAN interconectada.

- **SAN (Storage Area Network):** Red de alta velocidad concebida específicamente para el transporte de datos masivos a nivel de bloques entre servidores de procesamiento y bancos de almacenamiento secundario. Opera desacoplada de la red LAN general mediante protocolos dedicados (como Fibre Channel o iSCSI), asegurando transferencias continuas y latencias mínimas.

# 3. Topologías Físicas y Análisis Combinatorio

La topología física define la distribución geométrica y el trazado del cableado y de los nodos dentro del sistema de interconexión.

## 3.1. Topologías Fundamentales

### 3.1.1. Topología en Bus

Todos los dispositivos se conectan a un cable troncal compartido continuo mediante conectores o derivaciones de derivación pasiva («taps»). Es una topología multipunto. La señal introducida por cualquier nodo viaja en ambas direcciones a lo largo del medio físico, alcanzando a todos los demás terminales del enlace.

En cada uno de los dos extremos del cable coaxial troncal es obligatorio instalar una resistencia de terminación (típicamente de $50\ \Omega$). El terminador absorbe la energía de la onda incidente; si faltara, la señal electromagnética chocaría con el extremo abierto, rebotando en sentido opuesto en forma de eco parásito y corrompiendo las tramas legítimas que circulan por el bus. Un corte material en cualquier punto del cable troncal divide el bus y altera la impedancia del circuito, lo que deja inoperativa la totalidad de la red.

### 3.1.2. Topología en Anillo

Los nodos se interconectan secuencialmente hasta formar una trayectoria física cerrada en circuito. Cada dispositivo dispone únicamente de una conexión punto a punto con su vecino previo y con su vecino posterior. La información fluye en un sentido predefinido y unidireccional a lo largo del lazo. Cada nodo incorpora un repetidor activo: cuando recibe una trama destinada a otra estación, regenera la forma de onda eléctrica de los bits y la reinyecta hacia el segmento siguiente con su potencia nominal original.

La ruptura de un único segmento de cable o la desconexión imprevista de un nodo intermedio interrumpe el lazo de circulación y colapsa la conectividad global del sistema, salvo que se añada un anillo redundante de contra-rotación.

### 3.1.3. Topología en Estrella

Cada nodo terminal establece un enlace dedicado punto a punto con un conmutador o concentrador central (switch). Los equipos terminales no dialogan directamente entre sí a nivel de cable. El conmutador central recibe las tramas entrantes, analiza sus direcciones de control y reenvía el flujo exclusivamente por el puerto físico donde reside el destinatario.

Si un cable periférico sufre un daño o una máquina se apaga, solo ese nodo específico queda desconectado. Sin embargo, el dispositivo central representa un **punto único de fallo**: una avería eléctrica o de control en el conmutador inutiliza de inmediato toda la red.

### 3.1.4. Topología en Malla Completa

Cada nodo del sistema cuenta con un enlace físico dedicado, directo e independiente con cada uno de los demás nodos que integran la red. Ofrece la máxima redundancia estructural e inmunidad ante fallos de enlaces. El tráfico circula de forma aislada por líneas privadas, eliminando las colisiones y garantizando privacidad física entre pares. El volumen total de cables e interfaces requeridos crece drásticamente con cada nuevo nodo incorporado.

# 4. Arquitecturas de Red y Paradigmas de Gestión

La arquitectura lógica describe la distribución de las funciones de cómputo, las jerarquías de servicio y la toma de decisiones sobre el tráfico entre los nodos.

## 4.1. Cliente-Servidor

Es una arquitectura marcadamente jerárquica y asimétrica basada en la centralización de recursos. El **servidor** es un proceso que se ejecuta de forma ininterrumpida en una máquina dedicada, manteniendo puertos abiertos a la escucha de peticiones entrantes. El **cliente** es un proceso de ejecución transitoria que inicia activamente el contacto bajo demanda del usuario, solicita un recurso, procesa la respuesta devuelta y finaliza su ejecución.

Dado que todas las solicitudes convergen hacia el mismo punto, la máquina servidora o su enlace local de acceso a la red pueden convertirse rápidamente en un cuello de botella («bottleneck») y en un punto central de fallo operativo.

## 4.2. Redes Punto a Punto (Peer-to-Peer o P2P)

Es un esquema descentralizado donde no existen servidores exclusivos ni dependencias jerárquicas permanentes. Cada nodo (peer) actúa simultáneamente como cliente y como servidor. Al mismo tiempo que un nodo descarga fragmentos de información desde otros miembros de la red, comparte sus propios bloques almacenados y su ancho de banda de subida con los demás pares.

Conforme ingresan nuevos usuarios al enjambre, la capacidad global de entrega y almacenamiento del sistema crece de forma proporcional a la demanda, diluyendo la carga en lugar de saturar un servidor centralizado.

## 4.3. Redes Definidas por Software (SDN)

En la conmutación tradicional, cada enrutador o conmutador físico integra de forma monolítica dos responsabilidades distintas: resolver las rutas óptimas del sistema y transferir físicamente los paquetes bit a bit. El paradigma SDN se trata de una arquitectura de red donde las funciones de decisión de encaminamiento (**plano de control**) se separan físicamente de la maquinaria de reenvío de paquetes (**plano de datos**), centralizando la lógica de control en una entidad lógica programable por software y reduciendo los dispositivos de conmutación a ejecutores deterministas de instrucciones de flujo de la siguiente forma:

- **Plano de Control (Control Plane):** Representa el cerebro lógico del sistema. Se extrae del hardware individual y se ejecuta en un controlador centralizado (o clúster distribuido) mediante software. Este plano recopila la topología completa de la red, ejecuta algoritmos para determinar los caminos óptimos, aplica políticas de seguridad y genera las tablas de flujo que rigen el comportamiento del tráfico.

- **Plano de Datos (Data Plane o Plano de Reenvío):** Representa la estructura de ejecución mecánica que permanece en los conmutadores físicos. Su única labor consiste en recibir paquetes por una interfaz, consultar las tablas de reglas inyectadas previamente por el controlador y despachar los paquetes hacia la interfaz de salida correspondiente a velocidad de cable. Emplea hardware de alta velocidad basado en circuitos integrados específicos (ASIC) y memorias asociativas (TCAM) para resolver las coincidencias en microsegundos.

Pensemos en la gestión del tráfico aéreo mediante una torre de control centralizada. Los aviones (plano de datos) transportan físicamente a los pasajeros a alta velocidad y ejecutan de manera mecánica las maniobras de propulsión y viraje; sin embargo, los pilotos no calculan de forma aislada las trayectorias globales para esquivar a los demás vuelos. La torre de control (plano de control) supervisa el mapa del espacio aéreo completo, calcula los corredores seguros y emite instrucciones coordinadas a cada cabina; los aviones se limitan a seguir de inmediato las rutas asignadas. 

Permite a los administradores programar y reconfigurar el comportamiento de toda la red global mediante código e interfaces API, eliminando la necesidad de configurar manualmente y de forma individual cada enrutador de la infraestructura.

---

> [!RESOURCES] REFERENCIAS
> 
> - **Balaguz, R.** (2026). *Medios de Transmisión y Redes Modernas*. Comunicación de Datos, Escuela de Computación, Facultad de Ciencias, Universidad Central de Venezuela (UCV).
>   
> - **Baran, P.** (1964). *On Distributed Communications: I. Introduction to Distributed Communications Networks* (RM-3420-PR). RAND Corporation. Recuperado de [rand.org](https://www.rand.org/pubs/research_memoranda/RM3420.html)
>   
> - **Forouzan, B. A.** (2022). *Data Communications and Networking* (6th ed.). New York: McGraw-Hill Education.
>   
> - **International Organization for Standardization.** *ISO/IEC 7498-1: Information technology — Open Systems Interconnection — Basic Reference Model*. Recuperado de [iso.org](https://www.iso.org/standard/20269.html)
>   
> - **Internet Engineering Task Force (IETF).** *RFC Editor & Official Protocol Specifications*. Recuperado de [ietf.org](https://www.ietf.org)
>   
> - **Institute of Electrical and Electronics Engineers (IEEE).** *IEEE 802 Local and Metropolitan Area Network Standards Committee*. Recuperado de [ieee802.org](https://www.ieee802.org)
>   
> - **Stallings, W.** (2014). *Data and Computer Communications* (10th ed.). Upper Saddle River, NJ: Pearson Education.
> 
> - **Open Networking Foundation.** *Software-Defined Networking: The New Norm for Networks* [White Paper]. Recuperado de [opennetworking.org](https://opennetworking.org)
>   
> - **Tanenbaum, A. S., & Wetherall, D. J.** (2011). *Computer Networks* (5th ed.). Upper Saddle River, NJ: Prentice Hall.