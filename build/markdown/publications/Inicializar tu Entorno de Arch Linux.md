---
created: 2025-01-09T17:30:00
title: Prontuario para Inicializar tu Entorno de Arch Linux
author: Guillermo Galavís
description: Transformar una instalación base de Arch Linux en un entorno de trabajo funcional requiere ajustes precisos que maximizan el rendimiento y la estabilidad. Desde la optimización de Pacman y la gestión del AUR, hasta la configuración de seguridad, controladores gráficos y renderizado de fuentes, este proceso es el paso definitivo para convertir tu terminal en un sistema operativo profesional, eficiente y totalmente personalizado.
tags:
  - prontuario
  - linux
---

<h1 id="post-title" align="center"> Prontuario para Inicializar tu Entorno de Arch Linux </h1>

Una vez que la instalación base de Arch Linux está lista y reinicias tu equipo, te encuentras frente a una pantalla negra con una terminal parpadeante. El núcleo del sistema ya funciona, pero aún queda convertir esa base mínima en un entorno de trabajo completo.

En este prontuario me enfocaré únicamente en **poner fina esa instalación**. Aquí aprenderás a estabilizar tu conexión de red, acelerar el gestor de paquetes, instalar un asistente para el AUR, asegurar tu equipo con un firewall, optimizar el consumo de batería en laptops o el rendimiento en computadoras de escritorio, y preparar el renderizado visual tanto si decides usar el servidor gráfico tradicional (**X11**) como el protocolo moderno (**Wayland**).

El objetivo de esta guía es ser lo suficientemente general para funcionar tanto en un entorno de escritorio completo como lo puede ser KDE Plasma, un Tiling Window Manager como Hyperland o la pura terminal. Para ello supondré que has leído ya mi [[240322 - Instalar Arch Linux|Prontuario para Instalar Arch Linux]].

# 1. Verificación y Gestión de Conectividad

Al iniciar por primera vez tu nuevo sistema, el demonio `NetworkManager` que dejamos habilitado gestionará tus interfaces de red. Lo primero que debes hacer es verificar si tienes salida a internet:

```sh
ping -c 3 archlinux.org
```

Si conectaste un cable de red (Ethernet), la conexión se habrá establecido sola. Si estás usando Wi-Fi o necesitas conectarte a una red inalámbrica desde la terminal, utilizaremos `nmcli` (_NetworkManager Command Line Interface_).

## 1.1. Escaneo y Conexión a Redes Wi-Fi

Para ver qué redes inalámbricas detecta tu tarjeta de red, ejecuta:

```sh
nmcli dev wifi list
```

Conéctate a tu red sustituyendo `<NombreDeRed>` y `<Contraseña>`:

```sh
nmcli dev wifi connect "<NombreDeRed>" password "<Contraseña>"
```

> [!IMPORTANT] IMPORTANTE
> 
> Si tu red Wi-Fi no emite su nombre públicamente (red oculta), añade el parámetro `hidden yes` al final:
> 
> ```sh
> nmcli dev wifi connect "<NombreDeRed>" password "<Contraseña>" hidden yes
> ```

## 1.2. Configuración de Servidores DNS

Por defecto, tu proveedor de internet (ISP) te asigna sus propios servidores DNS, los cuales suelen ser lentos, poco privados y propensos a bloqueos de dominio. Es una buena práctica configurar servidores DNS públicos de baja latencia como los de **Cloudflare** (`1.1.1.1` y `1.0.0.1`) o **Quad9** (`9.9.9.9` enfocado en seguridad).

1. Identifica el nombre exacto de tu perfil de conexión activo:
    
    ```sh
    nmcli connection show
    ```
    
2. Asigna los servidores DNS de Cloudflare a esa conexión (reemplaza `<NombreConexion>` por el que viste en la columna `NAME`):
    
    ```sh
    nmcli connection modify "<NombreConexion>" ipv4.dns "1.1.1.1 1.0.0.1"
    nmcli connection modify "<NombreConexion>" ipv4.ignore-auto-dns yes
    ```
    
1. Por último, reactiva la conexión para aplicar los cambios:
    
    ```sh
    nmcli connection up "<NombreConexion>"
    ```

# 2. Optimización de Pacman y Asistente de AUR

Pacman es el corazón de la administración de software en Arch Linux. Con un par de ajustes en su archivo de configuración principal, podemos hacer que descargue mucho más rápido y luzca mejor en terminal.

## 2.1. Ajustes en `/etc/pacman.conf`

Abre el archivo con privilegios de superusuario:

```sh
sudo micro /etc/pacman.conf
```

Dentro de la sección `[options]`, localiza y ajusta las siguientes líneas (elimina el `#` inicial si están comentadas):

- `Color`: Habilita colores en la terminal para distinguir fácilmente paquetes, versiones y alertas.
    
- `VerbosePkgLists`: Muestra una tabla detallada con los nombres, versiones previas y tamaños de descarga antes de confirmar cualquier instalación.
  
- `ParallelDownloads = 5`: Permite que Pacman descargue hasta 5 paquetes en simultáneo, aprovechando al máximo el ancho de banda de tu conexión.
    
- `ILoveCandy`: Escribe esta directiva debajo de `Color` para transformar la barra de carga tradicional en un divertido homenaje visual retro.

Si vas a utilizar aplicaciones de 32 bits (como el cliente de **Steam**, emuladores o **Wine** para ejecutar software de Windows), necesitas el repositorio `multilib`.

En ese mismo archivo `/etc/pacman.conf`, baja hasta el final y descomenta estas dos líneas:

```plaintext
[multilib]
Include = /etc/pacman.d/mirrorlist
```

Guarda el archivo (`Ctrl + S`, `Ctrl + Q`) y sincroniza los repositorios para registrar los cambios:

```sh
sudo pacman -Syu
```

## 2.2. Instalación de un Asistente para AUR (`yay` o `paru`)

El **Arch User Repository (AUR)** es el repositorio comunitario más grande del ecosistema Linux. Para instalar programas del AUR sin tener que compilar y resolver dependencias manualmente con `makepkg`, instalaremos un asistente (_AUR helper_). Uno de los más populares y ligeros es `yay`:

```sh
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/yay-bin.git
cd yay-bin
makepkg -si
cd .. && rm -rf yay-bin
```

A partir de este momento, puedes instalar cualquier paquete de los repositorios oficiales o del AUR usando `yay -S <nombre_paquete>` sin anteponer `sudo` (el propio asistente te pedirá la contraseña cuando sea necesario).

## 2.3. Optimización de Mirrors con `rate-mirrors`

Los repositorios de Arch Linux están distribuidos en servidores espejo (_mirrors_) repartidos por todo el mundo. El archivo `/etc/pacman.d/mirrorlist` define el orden de prioridad en el que Pacman consultará estos servidores. Si los primeros mirrors de tu lista están caídos, saturados o geográficamente lejos de ti, las descargas y actualizaciones del sistema se ralentizarán considerablemente.

Aunque la herramienta tradicional suele ser `reflector`, **`rate-mirrors`** es una alternativa moderna escrita en Rust que destaca por ser significativamente más rápida: comprueba en paralelo no solo la latencia del servidor, sino la velocidad real de transferencia y qué tan sincronizado está con los repositorios oficiales.

1. Aprovechando el asistente de AUR (`yay`) que instalamos en el paso anterior, obtén la versión precompilada en binario para no demorar tiempo compilando:

	```sh
	yay -S rate-mirrors-bin
	```

2. Antes de sobrescribir cualquier archivo crítico del sistema, acostumbra crear un respaldo del estado actual:

	```sh
	sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
	```

3. Ejecuta `rate-mirrors` indicando que evalúe los servidores de Arch Linux y redirige el resultado ordenado directamente a tu archivo `mirrorlist`:

	```sh
	rate-mirrors arch | sudo tee /etc/pacman.d/mirrorlist
	```

> [!QUESTION] ¿Qué hace este comando?
> 
> - `rate-mirrors arch`: Descarga la lista global de mirrors activos de Arch, evalúa su velocidad de respuesta simultáneamente y los ordena del más rápido al más lento.
>     
> - `| sudo tee /etc/pacman.d/mirrorlist`: Recibe la salida filtrada a través de la tubería (_pipe_) y la escribe con permisos administrativos en el archivo de mirrors, mostrándote el resultado en pantalla en tiempo real.

4. Al cambiar por completo el orden y origen de los servidores espejo, es necesario forzar a Pacman a reconstruir sus bases de datos locales contra el nuevo mirror principal:

	```sh
	sudo pacman -Syyu
	```

> [!TIP] TIP: El parámetro `-yy` obliga a renovar todas las listas de paquetes aunque el sistema crea que ya están al día.

# 3. Seguridad y Mantenimiento del Sistema

## 3.1. Configuración del Firewall con UFW

Un firewall es indispensable para controlar el tráfico de red y evitar accesos no autorizados a puertos abiertos en tu sistema. `ufw` (_Uncomplicated Firewall_) simplifica la administración de las reglas del kernel.

1. Instala el paquete:
    
    ```sh
    sudo pacman -S ufw
    ```
    
2. Establece una política estricta por defecto (bloquear todo lo entrante, permitir todo lo saliente):
    
    ```sh
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    ```
    
3. Si utilizas conexiones remotas por SSH, limita los intentos de conexión en el puerto 22 para mitigar ataques de fuerza bruta:
    
    ```sh
    sudo ufw limit 22/tcp
    ```
    
4. Habilita el servicio para que inicie siempre con el sistema:
    
    ```sh
    sudo systemctl enable --now ufw.service
    ```

## 3.2. Mantenimiento de Unidades de Estado Sólido (SSD / NVMe)

Si instalaste Arch en un disco SSD o NVMe, es vital activar el comando **TRIM**. Esta función le comunica al controlador del disco qué bloques de memoria ya no contienen datos válidos para que pueda limpiarlos en segundo plano, prolongando la vida útil y la velocidad de la unidad:

```sh
sudo systemctl enable --now fstrim.timer
```

Este temporizador de systemd ejecutará TRIM una vez por semana de forma automática sin afectar el rendimiento mientras usas tu equipo.

## 3.3. Optimización del Tiempo de Arranque (GRUB)

Si Arch Linux es el único sistema operativo instalado en tu computadora, la cuenta regresiva de 5 segundos del menú de GRUB solo retrasa el inicio del equipo.

1. Edita la configuración de GRUB:
    
    ```sh
    sudo micro /etc/default/grub
    ```
    
2. Localiza las siguientes directivas y ajústalas así:
    
    ```plaintext
    GRUB_TIMEOUT=0
    GRUB_TIMEOUT_STYLE=hidden
    ```
    
3. Regenera el archivo de configuración de arranque:
    
    ```sh
    sudo grub-mkconfig -o /boot/grub/grub.cfg
    ```

# 4. Controladores de Hardware y Gestión de Energía

El soporte de hardware varía dependiendo de si estás configurando una laptop o una estación de trabajo de escritorio.

## 4.1. Controladores Gráficos (GPU)

Para que tu interfaz gráfica funcione con aceleración por hardware, debes instalar los controladores correspondientes a tu tarjeta de video:

- **Tarjetas gráficas Intel (integradas):**
    
    ```sh
    sudo pacman -S mesa vulkan-intel
    ```
    
- **Tarjetas gráficas AMD (Radeon):**
    
    ```sh
    sudo pacman -S mesa vulkan-radeon xf86-video-amdgpu
    ```
    
- **Tarjetas gráficas NVIDIA (GPUs modernas Turing / Ampere / Ada Lovelace):**
    
    ```sh
    sudo pacman -S nvidia-open nvidia-utils
    ```
    
Si tienes una tarjeta NVIDIA más antigua o prefieres los controladores privativos cerrados tradicionales, instala `nvidia` en lugar de `nvidia-open`.

## 4.2. Ajustes Específicos para Laptops

### 4.2.1. Autonomía y Eficiencia Energética con TLP

En una laptop, optimizar el uso de energía es crítico para que la batería no se agote en un par de horas. **TLP** ajusta automáticamente el consumo del procesador, discos y puertos USB según el equipo esté conectado a la corriente o usando la batería.

```sh
sudo pacman -S tlp tlp-rdw
sudo systemctl enable tlp.service
```

> [!WARNING] ADVERTENCIA
> 
> No utilices TLP junto con `power-profiles-daemon` (que suele venir instalado en escritorios como GNOME o KDE), ya que ambos servicios entrarán en conflicto intentando gestionar el mismo hardware.

### 4.2.2. Desactivación del Auto-Arranque de Bluetooth

El adaptador de Bluetooth realiza búsquedas pasivas constantes que drenan energía silenciosamente. Si no usas dispositivos Bluetooth todo el tiempo, puedes configurar el sistema para que no lo encienda de manera automática al arrancar:

```sh
sudo pacman -S bluez bluez-utils
sudo systemctl enable bluetooth.service
```

Edita su archivo de configuración:

```sh
sudo micro /etc/bluetooth/main.conf
```

En la sección `[Policy]`, cambia el parámetro a `false`:

```plaintext
AutoEnable = false
```

Cuando necesites conectar unos audífonos o un mouse, puedes activar el adaptador abriendo `bluetoothctl` en la terminal o mediante utilidades gráficas como `blueman`.

### 4.2.3. Soporte para Gestos en el Touchpad

Para que tu touchpad admita gestos multitáctiles, toques para hacer clic (_tap-to-click_) y desplazamiento natural con dos dedos:

```sh
sudo pacman -S libinput
```

# 5. Servidor Gráfico: Diferencias entre X11 y Wayland

Linux cuenta con dos formas de renderizar y gestionar ventanas en pantalla: **X11** (el protocolo clásico con más de 30 años de compatibilidad) y **Wayland** (el protocolo moderno, más seguro, fluido y con mejor manejo de pantallas de alta resolución o refresco mixto).

Dependiendo del entorno de escritorio o gestor de ventanas que decidas instalar después, necesitarás herramientas base diferentes:

|**Componente**|**En X11 (ej. BSPWM, i3, XFCE)**|**En Wayland (ej. Hyprland, Sway, KDE Wayland)**|
|---|---|---|
|**Servidor / Compositor**|`xorg-server`, `xorg-xinit`|Integrado en el propio compositor|
|**Gestión del Portapapeles**|`xclip`, `xsel`|`wl-clipboard`|
|**Capturas de pantalla**|`maim`, `scrot`|`grim`, `slurp`|
|**Integración con apps y pantalla compartida**|Nativo mediante X11|`xdg-desktop-portal` + `xdg-desktop-portal-wlr` (o hyprland)|
|**Ajuste de Monitores**|`xrandr`, `arandr`|`wlr-randr` o configuración directa en el compositor|

Instala las utilidades correspondientes al tipo de sesión que vayas a construir. Si vas a usar **Wayland**, asegúrate además de instalar las capas de compatibilidad para aplicaciones Qt:

```sh
sudo pacman -S qt5-wayland qt6-wayland
```

# 6. Audio y Servidor Multimedia (PipeWire)

Durante la instalación base instalamos `pipewire`. Ahora debemos asegurar que el enrutamiento de audio y el gestor de sesiones estén completamente listos para reproducir sonido sin problemas de latencia:

1. Instala el gestor de sesiones y las capas de compatibilidad con ALSA y Jack:
    
    ```sh
    sudo pacman -S wireplumber pipewire-alsa pipewire-jack pavucontrol
    ```
    
2. Habilita los servicios a nivel de usuario (no uses `sudo` para este comando):
    
    ```sh
    systemctl --user enable --now pipewire.socket pipewire-pulse.socket wireplumber.service
    ```

`pavucontrol` es una interfaz gráfica liviana que te permitirá ajustar volúmenes, seleccionar salidas de audio (auriculares, HDMI, altavoces) y cambiar entradas de micrófono fácilmente.

# 7. Refinamiento y Renderizado de Fuentes Tipográficas

Para que los textos en el navegador, la terminal y los editores de código se vean perfectamente nítidos y sin bordes aserrados (_pixelados_), debemos instalar un catálogo de tipografías base y configurar el motor de renderizado **FreeType** y **Fontconfig**.

## 7.1. Instalación de Paquetes de Fuentes Recomendados

Arch Linux no incluye tipografías por defecto. Instala este conjunto de fuentes de alta legibilidad métrica, símbolos para programadores y soporte internacional:

```sh
sudo pacman -S ttf-liberation noto-fonts noto-fonts-cjk noto-fonts-emoji ttf-jetbrains-mono-nerd
```

## 7.2. Configuración Global con Fontconfig

Fontconfig es la librería universal que le indica al sistema cómo suavizar y ordenar los píxeles de cada letra. Crea o edita el archivo de configuración global:

```sh
sudo micro /etc/fonts/local.conf
```

Pega la siguiente estructura XML que activa el antialiasing, el ajuste de contorno ligero (_hinting_), el patrón de subpíxeles RGB y el filtro LCD estándar:

```xml
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <match target="font">
    <edit name="antialias" mode="assign">
      <bool>true</bool>
    </edit>
    <edit name="hinting" mode="assign">
      <bool>true</bool>
    </edit>
    <edit mode="assign" name="hintstyle">
      <const>hintslight</const>
    </edit>
    <edit mode="assign" name="rgba">
      <const>rgb</const>
    </edit>
    <edit mode="assign" name="lcdfilter">
      <const>lcddefault</const>
    </edit>
  </match>
</fontconfig>
```

Activa los ajustes predefinidos del sistema mediante enlaces simbólicos:

```sh
sudo ln -sf /usr/share/fontconfig/conf.avail/10-sub-pixel-rgb.conf /etc/fonts/conf.d/
sudo ln -sf /usr/share/fontconfig/conf.avail/10-hinting-slight.conf /etc/fonts/conf.d/
sudo ln -sf /usr/share/fontconfig/conf.avail/11-lcdfilter-default.conf /etc/fonts/conf.d/
```

## 7.3. Ajuste Exclusivo para X11 (`~/.Xresources`)

> [!IMPORTANT] X11 VS WAYLAND
> 
> La configuración de `~/.Xresources` **solo aplica para aplicaciones bajo el servidor X11** o programas que corren a través de la capa de compatibilidad XWayland. Si utilizas un entorno 100% nativo de Wayland, este paso no es obligatorio, ya que los compositores leen directamente las reglas de Fontconfig.

Si utilizas X11, define las propiedades de recursos de X creando tu archivo de configuración:

```sh
micro ~/.Xresources
```

Añade las siguientes líneas:

```plaintext
Xft.antialias: 1
Xft.hinting: 1
Xft.rgba: rgb
Xft.hintstyle: hintslight
Xft.lcdfilter: lcddefault
```

Carga los cambios en la memoria del servidor gráfico ejecutando:

```sh
xrdb -merge ~/.Xresources
```

## 7.4. Regenerar la Caché de Fuentes

Por último, limpia y regenera la caché del sistema para que todas tus aplicaciones reconozcan de inmediato las nuevas fuentes y directrices de renderizado:

```sh
sudo fc-cache -fv
```

# 8. Optimizaciones para Gaming

## 8.1. Controladores Gráficos de 32 bits y Soporte Vulkan

La inmensa mayoría de los videojuegos de Windows que se ejecutan mediante capas de compatibilidad requieren librerías gráficas y de Vulkan de 32 bits (_multilib_). Si no las instalas, muchos juegos no arrancarán o se cerrarán con pantallas en negro. Instala las librerías de 32 bits correspondientes a tu tarjeta gráfica:

- **Para GPUs Intel:**
    
    ```sh
    sudo pacman -S lib32-mesa lib32-vulkan-intel
    ```
    
- **Para GPUs AMD:**
    
    ```sh
    sudo pacman -S lib32-mesa lib32-vulkan-radeon
    ```
    
- **Para GPUs NVIDIA:**
    
    ```sh
    sudo pacman -S lib32-nvidia-utils
    ```

## 8.2. Instalación de Steam y Activación de Proton

Steam en Arch Linux se distribuye en los repositorios oficiales mediante el paquete del repositorio `multilib`:

```sh
sudo pacman -S steam
```

Proton es la capa de compatibilidad de Valve integrada en Steam. Combina **Wine** con implementaciones de alto rendimiento como **DXVK** (que traduce DirectX 9/10/11 a Vulkan en tiempo real) y **VKD3D** (que traduce DirectX 12 a Vulkan), permitiendo ejecutar juegos nativos de Windows en Linux con un rendimiento prácticamente idéntico al original. Para activar Proton en todos tus juegos de Steam:

1. Abre Steam y dirígete a **Steam > Parámetros > Compatibilidad**.
2. Marca la casilla **«Habilitar Steam Play para todos los demás títulos»**.
3. En el menú desplegable, selecciona **Proton Experimental** (o la versión estable más reciente).

## 8.3. Instalación y Uso de GameMode

GameMode optimiza dinámicamente tu CPU, GPU y prioridades de procesos mientras juegas.

1. Instala GameMode junto con su biblioteca de compatibilidad de 32 bits:
    
    ```sh
    sudo pacman -S gamemode lib32-gamemode
    ```
    
2. Agrega tu usuario al grupo de GameMode si es necesario o comprueba su estado:
    
    ```sh
    gamemoded -t
    ```
    
3. **Cómo usar GameMode en Steam:**
    
    Haz clic derecho sobre cualquier juego en tu biblioteca de Steam, ve a **Propiedades > General > Parámetros de lanzamiento** y escribe:
    
    ```sh
    gamemoderun %command%
    ```

---
> [!RESOURCES] REFERENCIAS 
> 
> - **Arch Wiki.** _General recommendations (Recomendaciones generales post-instalación)_. Recuperado de [wiki.archlinux.org/title/General_recommendations](https://wiki.archlinux.org/title/General_recommendations)
> 
> - **Arch Wiki.** _Uncomplicated Firewall (UFW)_. Recuperado de [wiki.archlinux.org/title/Uncomplicated_Firewall](https://wiki.archlinux.org/title/Uncomplicated_Firewall)
> 
> - **Arch Wiki.** _TLP - Gestión de energía para Linux_. Recuperado de [wiki.archlinux.org/title/TLP](https://wiki.archlinux.org/title/TLP)
> 
> - **Arch Wiki.** _Solid state drive (Buenas prácticas para unidades SSD y NVMe)_. Recuperado de [wiki.archlinux.org/title/Solid_state_drive](https://wiki.archlinux.org/title/Solid_state_drive)
> 
> - **Manjaro Wiki.** _Improve Font Rendering_. Recuperado de [wiki.manjaro.org/index.php?title=Improve_Font_Rendering](https://wiki.manjaro.org/index.php?title=Improve_Font_Rendering)
> 
> - **Linuxiac.** _Arch Linux Post-Installation Essential Steps_. Recuperado de [linuxiac.com/arch-linux-post-installation-steps/](https://linuxiac.com/arch-linux-post-installation-steps/)
> 
> - **Reddit.** _Things to do after installing Arch Linux_. Recuperado de [reddit.com/r/archlinux/comments/wdry0v/things_to_do_after_installing_arch_linux/](https://www.reddit.com/r/archlinux/comments/wdry0v/things_to_do_after_installing_arch_linux/)
> 
> - **YouTube.** _What to do AFTER you've installed ARCH LINUX - beginner friendly post-install guide_. Recuperado de [youtu.be/-puvglgx6Qs](https://youtu.be/-puvglgx6Qs)
> 
> - **YouTube.** _Arch Linux post install Guide_. Recuperado de [youtu.be/YPrhIfm3VJs](https://youtu.be/YPrhIfm3VJs)