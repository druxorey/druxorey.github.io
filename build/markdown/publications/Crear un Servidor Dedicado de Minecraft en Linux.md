---
created: 2025-12-18 14:19
title: Prontuario para Instalar un Servidor de Minecraft en Linux
author: Guillermo Galavís
description: Convertir hardware antiguo en un servidor dedicado de Minecraft es la forma ideal de aprovechar recursos mientras mantienes un control total sobre tu partida. Al utilizar Fabric junto a mods de optimización, lograrás un rendimiento superior sin alterar la experiencia original. Aprenderás a automatizar el proceso con systemd y gestionar conexiones seguras mediante Playit.gg, garantizando un entorno estable, eficiente y siempre disponible.
tags:
  - prontuario
  - linux
  - juegos
---

<h1 id="post-title" align="center"> Prontuario para Crear un Servidor Dedicado de Minecraft en Linux </h1>

Darle una segunda vida al hardware que dabas por obsoleto es una de las experiencias más gratificantes dentro de la informática. Una laptop con la pantalla dañada o una PC de escritorio arrumbada tienen potencia más que suficiente para convertirse en un servidor doméstico rápido, silencioso y eficiente.

En este prontuario te enseñaré a construir un servidor dedicado de Minecraft basado en **Fabric** (Sé que existen alternativas como PaperMC, pero alteran las mecánicas básicas y son un verdadero dolor de cabeza si eres un jugador técnico), diseñado para exprimir el rendimiento de tu máquina mediante mods de optimización a bajo nivel. Abordando desde la configuración energética para laptops hasta la automatización con servicios de segundo plano y la apertura segura a internet sin necesidad de tocar los puertos de tu router.

> [!IMPORTANT] IMPORTANTE
> 
> Esta guía asume que ya tienes instalado un sistema base limpio (únicamente en modo terminal, sin entornos gráficos pesados que consuman memoria RAM innecesariamente). Si necesitas preparar tu sistema desde cero, puedes consultar previamente el [[240322 - Instalar Arch Linux|Prontuario para Instalar Arch Linux]].

# 1. Preparación del Sistema y Dependencias

Antes de descargar el software del servidor, debemos preparar el sistema operativo con las herramientas necesarias y el entorno de ejecución de Java adecuado.

## 1.1. Actualización e Instalación de Paquetes

Minecraft (versión 1.20.5 en adelante, incluyendo la 1.21+) requiere **Java 21**. Para mantener el servidor lo más ligero posible, utilizaremos las versiones *headless* del OpenJDK; estas eliminan bibliotecas gráficas (como AWT o Swing) que no tienen ninguna utilidad en un servidor por terminal, ahorrando espacio en disco y memoria RAM. Ejecuta los comandos correspondientes a tu distribución:

**En Arch Linux:**

```sh
sudo pacman -Syu
sudo pacman -S jre21-openjdk-headless wget nano git curl
```

**En Debian / Ubuntu:**

```sh
sudo apt update && sudo apt upgrade -y
sudo apt install -y openjdk-21-jre-headless wget nano git curl
```

(Si planeas ejecutar versiones antiguas del juego, como Minecraft 1.17 a 1.20.4, instala `jre17-openjdk-headless` en su lugar

## 1.2. Gestión de Energía en Laptops (Ignorar la Tapa Cerrada)

> [!IMPORTANT] IMPORTANTE
> 
> Si usas una pc de escritorio o un servidor, puedes saltar directamente a la siguiente sección. Este paso es exclusivo para evitar que una laptop se apague o suspenda al cerrarla.

Por defecto, Linux entra en modo de suspensión (_sleep_) cuando detectas que la tapa de la laptop se ha cerrado. Para que puedas colocar tu laptop en una repisa o rincón con la pantalla cerrada y el servidor funcionando las 24 horas del día, debemos indicarle a `systemd-logind` que ignore este evento:

1. Abre el archivo de configuración del gestor de sesiones:
    
    ```sh
    sudo nano /etc/systemd/logind.conf
    ```
    
2. Localiza las siguientes directivas, elimina el `#` inicial y asigna el valor `ignore`:
    
    ```plaintext
    HandleLidSwitch=ignore
    HandleLidSwitchExternalPower=ignore
    HandleLidSwitchDocked=ignore
    ```
    
3. Guarda los cambios (`Ctrl + O`, Enter, `Ctrl + X`) y reinicia el servicio para que surtan efecto:
    
    ```sh
    sudo systemctl restart systemd-logind
    ```

# 2. Despliegue y Optimización del Servidor con Fabric

Existen múltiples tipos de servidores para Minecraft. Aunque alternativas como Paper o Purpur son populares, a menudo alteran las mecánicas internas del juego. **Fabric** mantiene el comportamiento 100 % idéntico al juego vanilla y permite instalar mods de rendimiento que multiplican los FPS del servidor.

## 2.1. Creación del Espacio de Trabajo

Crearemos un directorio exclusivo para mantener aislados todos los mundos y configuraciones:

```sh
mkdir -p ~/mc_server && cd ~/mc_server
```

## 2.2. Descarga y Ejecución del Instalador de Fabric

Descargaremos el instalador oficial en formato `.jar` desde el repositorio Maven de Fabric:

```sh
wget https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.1.0/fabric-installer-1.1.0.jar -O fabric-installer.jar
```

Ejecuta el instalador indicando la versión exacta de Minecraft que deseas utilizar (en este ejemplo, 1.21.1) y el parámetro `-downloadMinecraft` para que descargue automáticamente el ejecutable oficial de Mojang:

```sh
java -jar fabric-installer.jar server -mcversion 1.21.1 -downloadMinecraft
```

## 2.3. Aceptación del Acuerdo de Licencia (EULA)

Minecraft no arrancará hasta que aceptes expresamente los términos de uso de Mojang. Realiza un primer arranque para generar la estructura básica de archivos:

```sh
java -jar fabric-server-launch.jar nogui
```

El proceso se detendrá inmediatamente generando el archivo `eula.txt`. Ábrelo y cambia su valor a verdadero:

```sh
micro eula.txt
```

Modifica la línea para que quede así:

```plaintext
eula=true
```

Guarda y sal del editor.

## 2.4. Instalación de Mods de Optimización

En un servidor con hardware modesto, estos tres mods del lado del servidor son indispensables:

- **Lithium:** Reescribe los algoritmos de física, inteligencia artificial de entidades y carga de chunks sin romper mecánicas _vanilla_.
    
- **FerriteCore:** Reduce drásticamente el uso de memoria RAM optimizando el almacenamiento de estados de bloques en memoria.
    
- **Krypton:** Optimiza la pila de red y el tráfico de paquetes de Minecraft, reduciendo el uso de CPU con muchos jugadores conectados.

Descárgalos dentro de la carpeta `mods`:

```sh
mkdir -p mods && cd mods

# Lithium
wget https://cdn.modrinth.com/data/gvQqBUqZ/versions/N08Z8wog/lithium-fabric-0.15.4%2Bmc1.21.1.jar

# FerriteCore
wget https://cdn.modrinth.com/data/u6SJDs6g/versions/y993XfGf/ferritecore-7.0.0-fabric.jar

# Krypton
wget https://cdn.modrinth.com/data/fQEb0iXm/versions/Acz3ttTp/krypton-0.2.8.jar

cd ..
```

# 3. Configuración de Red Local y Dirección IP Estática

Para que los dispositivos dentro de tu hogar siempre encuentren el servidor, su dirección IP interna (ej. `192.168.1.50`) no debe cambiar cada vez que se reinicie el router.

## 3.1. Obtención de la Dirección Física (MAC Address)

Identifica la interfaz de red activa y su dirección MAC mediante el comando `ip link`:

```sh
ip link
```

Identifica tu interfaz (por ejemplo `enp3s0` / `eth0` para cable Ethernet o `wlan0` / `wlp2s0` para Wi-Fi). La dirección física es la cadena hexadecimal de 6 pares ubicada tras `link/ether` (ejemplo: `a1:b2:c3:d4:e5:f6`).

## 3.2. Reserva DHCP en el Router

La forma más limpia y robusta de asignar una IP fija es mediante una **reserva DHCP** desde el propio router:

1. Entra al panel de administración de tu router desde un navegador (usualmente `192.168.1.1` o `192.168.0.1`).
    
2. Dirígete al apartado de **DHCP Server**, **LAN Setup** o **Address Reservation**.
    
3. Añade una nueva regla ingresando la **dirección MAC** de tu servidor y asignándole la IP que desees fijar (por ejemplo `192.168.1.100`).
    
4. Guarda los cambios. A partir de este momento, el router siempre entregará la misma dirección IP a tu servidor.

## 3.3. Configuración del Firewall (UFW)

Si tienes un firewall activo en tu máquina como **UFW**, debes abrir el puerto predeterminado del juego (25565 por TCP):

```sh
sudo ufw allow 25565/tcp
```

# 4. Script de Inicio y Banderas de Rendimiento

Crearemos un script que inicie el servidor con parámetros avanzados para la máquina virtual de Java (JVM), asegurando una recolección de basura (_Garbage Collection_) eficiente para mitigar tirones de lag (_lag spikes_).

1. Crea el script de arranque:
    
    ```sh
    nano start.sh
    ```
    
2. Añade la siguiente configuración:
    
    ```bash
    #!/usr/bin/env bash
    
    # Ajusta la RAM según la memoria de tu equipo (ej. 4G para un equipo con 8GB)
    MEMORIA="4G"
    
    exec java -Xms${MEMORIA} -Xmx${MEMORIA} \
       -XX:+UseG1GC \
       -XX:+ParallelRefProcEnabled \
       -XX:MaxGCPauseMillis=200 \
       -XX:+UnlockExperimentalVMOptions \
       -XX:+DisableExplicitGC \
       -XX:+AlwaysPreTouch \
       -XX:G1NewSizePercent=30 \
       -XX:G1MaxNewSizePercent=40 \
       -XX:G1ReservePercent=20 \
       -XX:G1HeapWastePercent=5 \
       -XX:G1MixedGCCountTarget=4 \
       -XX:InitiatingHeapOccupancyPercent=15 \
       -XX:G1MixedGCLiveThresholdPercent=90 \
       -XX:G1RSetUpdatingPauseTimePercent=5 \
       -XX:SurvivorRatio=32 \
       -XX:+PerfDisableSharedMem \
       -XX:MaxTenuringThreshold=1 \
       -jar fabric-server-launch.jar nogui
    ```
    
3. Otorga permisos de ejecución al script:
	
    ```sh
    chmod +x start.sh
    ```
    

> [!QUESTION] ¿Por qué fijar `-Xms` y `-Xmx` con el mismo valor?
> 
> Al igualar la memoria mínima (`-Xms`) y máxima (`-Xmx`), la JVM reserva todo el bloque de memoria desde el inicio, evitando pausas en el juego causadas por el redimensionamiento dinámico de la memoria en el sistema operativo.

# 5. Automatización como Servicio con Systemd

Si ejecutas el servidor directamente desde tu terminal por SSH, el proceso se cerrará en cuanto cierres la conexión. Crearemos un servicio de `systemd` para que Minecraft se ejecute en segundo plano y se inicie automáticamente cada vez que la computadora encienda.

1. Crea el archivo de servicio con permisos de superusuario:
    
    ```sh
    sudo nano /etc/systemd/system/minecraft.service
    ```
    
2. Pega la siguiente definición (reemplaza `tu_usuario` por tu nombre de usuario real en Linux):
    
    ```toml
    [Unit]
    Description=Servidor Dedicado de Minecraft (Fabric)
    After=network.target
    
    [Service]
    Type=simple
    User=tu_usuario
    WorkingDirectory=/home/tu_usuario/mc_server
    ExecStart=/bin/bash /home/tu_usuario/mc_server/start.sh
    Restart=on-failure
    RestartSec=20s
    
    [Install]
    WantedBy=multi-user.target
    ```
    
3. Recarga los demonios de systemd y activa el servicio:
    
    ```sh
    sudo systemctl daemon-reload
    sudo systemctl enable --now minecraft.service
    ```

A partir de ahora, puedes controlar tu servidor con los comandos estándar:

- **Ver el estado y logs en vivo:** `sudo journalctl -u minecraft.service -f`
- **Detener el servidor:** `sudo systemctl stop minecraft.service`
- **Reiniciar el servidor:** `sudo systemctl restart minecraft.service`

# 6. Acceso Público Seguro con Playit.gg 

Para jugar con amigos fuera de tu red local solía ser obligatorio abrir puertos (_Port Forwarding_) en el router. Sin embargo, si estás detrás de un **CGNAT** (donde tu proveedor no te da una IP pública real) o no deseas exponer la dirección IP privada de tu casa a internet, **Playit.gg** es la solución ideal.

Playit crea un túnel cifrado inverso mediante un proxy seguro: tus amigos se conectan a un dominio público de Playit y el tráfico se reenvía directamente a tu servidor local.

## 6.1. Instalación del Agente de Playit

Descarga el ejecutable para Linux (arquitectura x86_64 / amd64):

```sh
cd ~
wget https://github.com/playit-cloud/playit-agent/releases/latest/download/playit-linux-amd64 -O playit
chmod +x playit
```

## 6.2. Vinculación y Creación del Túnel

1. Inicia el agente en tu servidor:
    
    ```sh
    ./playit
    ```
    
2. La terminal imprimirá un enlace de reclamo (_Claim URL_) con un formato como `https://playit.gg/claim/xxxx-xxxx`.
    
3. Copia el enlace y ábrelo en el navegador de tu computadora personal.
    
4. Inicia sesión o crea una cuenta en Playit.
    
5. En el panel de control, haz clic en **«Add Tunnel»**, selecciona el tipo **Minecraft Java** y confirma que el puerto local apunte al **25565**.
    
6. El panel te entregará una dirección única (por ejemplo: `mi-servidor.playit.gg`). Esta es la dirección pública que compartirás con tus amigos para que se unan a la partida.

---
> [!RESOURCES] REFERENCIAS
> 
> - **FabricMC.** *Documentación Oficial*. Recuperado de [fabricmc.net](https://fabricmc.net/)
>   
> - **Modrinth.** *Repositorio de Mods*. Recuperado de [modrinth.com](https://modrinth.com/)
>   
> - **PaperMC.** *Optimización de Banderas JVM (Aikar's Flags)*. Recuperado de [docs.papermc.io/paper/aikars-flags](https://docs.papermc.io/paper/aikars-flags)
>   
> - **Playit.gg.** *Documentación y Soporte*. Recuperado de [playit.gg/support](https://playit.gg/support/)
>   
> - **Debian Wiki.** *Gestión de Servicios con Systemd*. Recuperado de [wiki.debian.org/systemd](https://wiki.debian.org/systemd)
>   
> - **Arch Wiki.** *Administración de Servidores de Minecraft*. Recuperado de [wiki.archlinux.org/title/Minecraft](https://wiki.archlinux.org/title/Minecraft)