---
created: 2024-03-22T17:30:00
title: Prontuario para Instalar Arch Linux
author: Guillermo Galavís
description: Instalar Arch Linux es el desafío definitivo para quienes buscan un sistema operativo a medida, eficiente y minimalista. Al prescindir de automatizaciones, obtienes un control total sobre cada componente, desde el particionado manual hasta la configuración del kernel. Es la oportunidad perfecta para dominar la arquitectura de tu equipo y construir un entorno de trabajo optimizado, estable y diseñado exclusivamente bajo tus necesidades.
tags:
  - prontuario
  - linux
---

<h1 id="post-title" align="center"> Prontuario para Instalar Arch Linux </h1>

Arch Linux ha arrastrado históricamente un aura de elitismo, lo que ha llevado a considerar su instalación como una tarea reservada exclusivamente para usuarios expertos. Sin embargo, la realidad es mucho más sencilla: el proceso solo requiere capacidad de lectura y un poco de sentido común (el cual curiosamente parece ser el sentido menos común). Mi primer contacto con esta distribución fue a finales de 2020, armado únicamente con una laptop y mi teléfono para consultar la [Arch Linux Wiki](https://wiki.archlinux.org/).

La Arch Wiki es, probablemente, la fuente de información sobre Linux más completa y mejor estructurada de internet, siendo un recurso indispensable para resolver problemas en casi cualquier distribución. No obstante, considero que su guía de instalación oficial puede resultar intimidante para los recién llegados, ya que da por sentados ciertos conocimientos técnicos.

Por esa razón, tras haber instalado Arch decenas de veces en diferentes entornos, preparé este prontuario. Mi objetivo es guiarte de forma directa para que no solo copies y pegues comandos en la terminal, sino que entiendas qué hace cada herramienta, por qué la ejecutamos y cómo encaja en tu nuevo sistema operativo.

> [!WARNING] ADVERTENCIA DE SEGURIDAD: Proceso Destructivo
> 
> Este proceso formateará y reparticionará la unidad de almacenamiento que elijas, lo que significa que **se borrarán todos los datos existentes de forma definitiva e irreversible**. Antes de continuar, respalda cualquier archivo personal importante en una memoria externa o en la nube. Revisa siempre con mucha atención las rutas de disco (`/dev/...`) antes de presionar Enter.

Esta guía se enfoca en una instalación manual limpia sobre equipos modernos con arquitectura **UEFI y tabla de particiones GPT**. Si en algún momento prefieres un método asistido por menús automatizados, Arch incluye el script oficial `archinstall`, cuya guía puedes revisar en la [documentación oficial de Archinstall](https://wiki.archlinux.org/title/Archinstall "null").

Ten presente que aquí dejaremos listo el **sistema base por línea de comandos**, con red y privilegios de usuario configurados. Para añadir una interfaz gráfica después, puedes apoyarte en la wiki oficial sobre los [Entornos de Escritorio en la Arch Wiki](https://wiki.archlinux.org/title/Desktop_environment "null")

# 1. Pre-Instalación

> [!IMPORTANT] IMPORTANTE
> 
> En esta primera etapa nada de lo que hagas modificará tu disco duro. El instalador de Arch se ejecuta completamente en la memoria RAM dentro de un entorno temporal conocido como _Live Environment_.

## 1.1. Preparación del Medio de Instalación

1. **Descarga de la imagen:** Obtén el archivo `.iso` oficial y verificado desde la página de [Descargas de Arch Linux](https://archlinux.org/download/ "null").
    
2. **Creación del USB Booteable:**
    
    - Si estás en Linux o buscas la herramienta más versátil, te recomiendo [Ventoy](https://www.ventoy.net/en/index.html "null"), que te permite arrastrar imágenes ISO a la memoria sin formatearla cada vez.
    
    - Si preparas la USB desde Windows, [Rufus](https://rufus.ie/en/ "null") en modo _DD_ o _ISO_ es la opción más sólida y confiable.
     
3. **Ajustes en la BIOS/UEFI:** Inserta la memoria USB en tu equipo, enciéndelo y presiona la tecla de acceso a la BIOS o al menú de arranque (_Boot Menu_, usualmente `F12`, `F11`, `F8` o `Supr`).

> [!IMPORTANT] DESACTIVA SECURE BOOT EN TU BIOS
> 
> Por defecto, el kernel y los módulos estándar de la ISO de Arch no cuentan con las firmas criptográficas de Microsoft, por lo que Secure Boot bloqueará el arranque del instalador si permanece encendido.

Al arrancar la USB, verás el menú de bienvenida y en pocos segundos tendrás una consola interactiva con privilegios de superusuario (`root@archiso ~ #`).

## 1.2. Configuración de Red

Arch Linux es una distribución rolling release minimalista: la ISO apenas contiene los instaladores esenciales y descarga los paquetes más actualizados directamente desde los repositorios durante la instalación. Por ello, contar con conexión a internet es indispensable.

### 1.2.1. Cable de red (Ethernet)

Si tu equipo está conectado por cable, el protocolo DHCP negociará automáticamente tu dirección IP. Solo debes verificar la conexión:

```sh
ping -c 3 archlinux.org
```

### 1.2.2. Red Inalámbrica (Wi-Fi)

Para redes Wi-Fi utilizaremos la utilidad interactiva `iwctl`:

1. Abre el intérprete de iwd:

	```sh
	iwctl
	```

2. Consulta el nombre de tu tarjeta inalámbrica (normalmente aparece como `wlan0`):

	```sh
	device list
	```

3. Escanea las redes disponibles y conéctate sustituyendo `<interfaz>` por tu dispositivo (ej. `wlan0`) y `<NombreDeRed>` por tu red Wi-Fi:

	```sh
	station <interfaz> scan
	station <interfaz> get-networks
	station <interfaz> connect "<NombreDeRed>"
	```

>[!TIP] TIP: Si tu red está oculta, utiliza `station <interfaz> connect-hidden "<NombreDeRed>"`

4. Introduce tu contraseña cuando te la solicite y escribe `exit` para volver a la terminal principal.

5. Comprueba el enlace:

	```sh
	ping -c 3 archlinux.org
	```

## 1.3. Sincronización del Reloj del Sistema

Antes de descargar paquetes o generar certificados de seguridad, es necesario sincronizar el reloj interno de la computadora a través de internet mediante NTP (*Network Time Protocol*):

```sh
timedatectl set-ntp true
```

# 2. Preparación de la Unidad de Almacenamiento

Aquí definiremos el esquema de particiones donde residirá tu nuevo sistema.

## 2.1. Identificación y Particionado del Disco

Primero, identifica cómo nombra el kernel a tus discos de almacenamiento:

```sh
fdisk -l
```

Verás unidades identificadas según su tecnología:

* Discos NVMe: `/dev/nvme0n1`
* Discos SATA / SSD / USB: `/dev/sda`, `/dev/sdb`

Identifica la unidad por su tamaño y capacidad. En este prontuario utilizaremos como ejemplo `/dev/nvme0n1`. Inicia la herramienta visual `cfdisk` indicando la ruta de tu disco:

```sh
cfdisk /dev/nvme0n1
```

1. **Tabla de Particiones:** Si el disco está vacío o nuevo, selecciona la etiqueta **`gpt`** (el estándar obligatorio para UEFI).

2. **Eliminar particiones viejas:** Si tienes particiones de instalaciones anteriores que ya no necesitas, selecciónalas y pulsa **`Delete`**.

3. **Estructura recomendada de particiones:**

| Partición | Tamaño sugerido | Tipo en `cfdisk` | Propósito |
| --- | --- | --- | --- |
| **Boot / EFI (ESP)** | `512M` a `1G` | `EFI System` | Aloja el gestor de arranque (GRUB) y los archivos de inicio de la placa base. |
| **Swap** | `4G` a `8G` | `Linux swap` | Memoria de intercambio virtual cuando la RAM física se satura o para hibernación. |
| **Root (`/`)** | Resto del disco | `Linux filesystem` | Contiene el sistema operativo, programas, librerías y tus carpetas personales. |

4. **Guardar cambios:** Dirígete con las flechas a **`[ Write ]`**, escribe `yes` para confirmar la escritura en el disco y sal con **`[ Quit ]`**.

Verifica el resultado ejecutando:

```sh
lsblk
```

Tu salida mostrará una estructura similar a esta:

```console
NAME         MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
nvme0n1      259:0    0 476.9G  0 disk 
├─nvme0n1p1  259:1    0     1G  0 part 
├─nvme0n1p2  259:2    0     8G  0 part 
└─nvme0n1p3  259:3    0 467.9G  0 part 
```

## 2.2. Formateo de los Sistemas de Archivos

Una partición es solo un contenedor; para almacenar datos necesita una estructura organizada de archivos.

1. **Partición Boot / EFI (FAT32):** La especificación UEFI exige obligatoriamente un sistema de archivos FAT32 para que la placa base pueda leer el gestor de arranque:

	```sh
	mkfs.fat -F 32 /dev/nvme0n1p1
	```

2. **Partición Swap:** La inicializamos como espacio de intercambio:

	```sh
	mkswap /dev/nvme0n1p2
	```

3. **Partición Root (ext4):** Formateamos la partición principal en `ext4`, un sistema de archivos sumamente estable, rápido y con journaling para evitar corrupción de datos:

	```sh
	mkfs.ext4 /dev/nvme0n1p3
	```

## 2.3. Montaje de las Unidades

Montar una partición significa enlazar ese bloque de almacenamiento a un directorio dentro del árbol de archivos de Linux, haciéndolo accesible.

1. **Montar la raíz (`/`)** en el directorio temporal `/mnt`:

	```sh
	mount /dev/nvme0n1p3 /mnt
	```

2. **Crear el punto de montaje EFI y montar la partición Boot:**

	```sh
	mkdir -p /mnt/boot/efi
	mount /dev/nvme0n1p1 /mnt/boot/efi
	```

3. **Activar la partición Swap:**

	```sh
	swapon /dev/nvme0n1p2
	```

# 3. Instalación del Sistema Base

Ahora que el disco está formateado y montado, volcaremos los paquetes esenciales de Arch Linux dentro de `/mnt`.

## 3.1. Instalación de Paquetes Básicos

El comando `pacstrap` es un script especial que descarga e instala paquetes en una jerarquía de directorios externa. Instalaremos los siguientes componentes indispensables:

- `base`: El núcleo mínimo de herramientas Unix de Arch Linux.
- `linux` y `linux-firmware`: El kernel de Linux y los controladores binarios para soporte de hardware (tarjetas gráficas, wifi, bluetooth, etc.).
- `base-devel`: Herramientas esenciales para compilar software (incluye `gcc`, `make`, `sudo`, `fakeroot`, necesarias para usar el AUR más adelante).
- `grub` y `efibootmgr`: El gestor de arranque y la utilidad para registrar entradas de inicio en la memoria NVRAM de tu placa UEFI.
- `micro`: Un editor de texto sencillo para terminal.
- `networkmanager`: Demonio completo para gestionar conexiones de red (cable, wifi, VPNs) de forma automática.
- `git`: Control de versiones fundamental para clonar programas y repositorios.
- `pipewire` y `pipewire-pulse`: El servidor de audio moderno y eficiente para Linux.
- `intel-ucode` o `amd-ucode`: Parches de microcódigo del procesador para mitigar fallas de seguridad a nivel de silicio y mejorar la estabilidad del CPU.

> [!IMPORTANT] IMPORTANTE
> 
> Si tu procesador es **AMD**, cambia `intel-ucode` por `amd-ucode` en el siguiente comando:

```sh
pacstrap /mnt base linux linux-firmware base-devel grub efibootmgr micro networkmanager git pipewire pipewire-pulse intel-ucode
```

## 3.2. Generación del Archivo `fstab`

El archivo `fstab` (*File Systems Table*) contiene el mapa que le dice al sistema qué particiones montar automáticamente cada vez que la computadora enciende. Generaremos este archivo utilizando identificadores únicos universales (**UUIDs**) con el parámetro `-U`. Esto evita problemas si los nombres de los discos cambian de orden al conectar otros dispositivos USB:

```sh
genfstab -U /mnt >> /mnt/etc/fstab
```

Comprueba que la información se haya generado correctamente inspeccionando su contenido:

```sh
cat /mnt/etc/fstab
```

Deberías ver listadas tus tres particiones (`/`, `/boot/efi` y `swap`) con sus respectivos UUIDs.

## 3.3. Entorno de Trabajo Interno con `arch-chroot`

Hasta este momento, estábamos operando desde la memoria USB. Con el comando `arch-chroot`, cambiamos la raíz del sistema operativo a `/mnt`. A partir de este instante, cualquier comando que ejecutes afectará directamente al sistema instalado en tu disco duro:

```sh
arch-chroot /mnt
```

Notarás que el prompt de tu terminal cambia a `[root@archiso /]#`. Ya estás dentro de tu nueva instalación.

# 4. Configuración del Sistema Operativo

Estando dentro de la jaula `chroot`, configuraremos la identidad, zona horaria, usuarios y arranque del sistema.

## 4.1. Zona Horaria y Reloj de Hardware

1. Crea un enlace simbólico entre la base de datos de zonas horarias y el archivo de hora local. Sustituye `Region` y `Ciudad` por tu ubicación geográfica (por ejemplo: `America/Caracas`, `America/Mexico_City`, `America/Argentina/Buenos_Aires`, `Europe/Madrid`):

	```sh
	ln -sf /usr/share/zoneinfo/America/Caracas /etc/localtime
	```

2. Sincroniza el reloj del hardware interno de la placa base (RTC) con la hora del sistema:

	```sh
	hwclock --systohc
	```

## 4.2. Localización e Idioma del Sistema

La localización define el idioma, codificación de caracteres y formatos numéricos de tus aplicaciones.

1. Abre el archivo de generación de idiomas:

	```sh
	micro /etc/locale.gen
	```

2. Busca tu idioma eliminando el símbolo `#` al inicio de la línea correspondiente. Se recomienda descomentar siempre la versión UTF-8 en inglés y la de tu país y luego guarda en micro con `Ctrl + S`, presiona Enter y sal con `Ctrl + Q`):

	```console
	en_US.UTF-8 UTF-8
	es_ES.UTF-8 UTF-8
	es_VE.UTF-8 UTF-8
	```

3. Genera las tablas de idioma en el sistema:

	```sh
	locale-gen
	```

4. Define el idioma predeterminado del sistema creando el archivo `locale.conf`:

	```sh
	echo LANG=en_US.UTF-8 > /etc/locale.conf
	```

## 4.3. Distribución del Teclado en Consola

Si tu teclado físico tiene distribución en español o latinoamericano, configura la consola de texto para que reconozca los caracteres especiales (como la `ñ` o tildes):

* Para teclado en **Español (España)**:

	```sh
	echo "KEYMAP=es" > /etc/vconsole.conf
	```

* Para teclado **Latinoamericano**:

	```sh
	echo "KEYMAP=la-latin1" > /etc/vconsole.conf
	```

- Para teclado **Inglés** pero con soporte a caractéres **Internacionales**:

	```sh
	echo KEYMAP=us-acentos > /etc/vconsole.conf
	```

## 4.4. Nombre del Equipo (*Hostname*)

El hostname es el nombre de red que identifica a tu computadora en tu red local y en la terminal.

1. Asigna el nombre que desees (ejemplo: `arch-workstation`):

	```sh
	echo "arch-workstation" > /etc/hostname
	```

2. Configura la tabla local de resolución de nombres editando `/etc/hosts`:

	```sh
	micro /etc/hosts
	```

Añade las siguientes líneas reemplazando `arch-workstation` por el nombre que elegiste:

```plaintext
127.0.0.1   localhost
::1         localhost
127.0.1.1   arch-workstation.localdomain arch-workstation
```

## 4.5. Contraseña del Administrador (*root*)

Asigna una contraseña para el usuario root ejecutando el comando:

```sh
passwd
```

Escribe tu contraseña (por seguridad, no se mostrarán caracteres en pantalla mientras escribes) y presiona Enter para confirmarla.

## 4.6. Creación de tu Usuario Personal con Privilegios `sudo`

Utilizar la cuenta `root` para tareas cotidianas es un riesgo de seguridad. Crearemos tu usuario normal y lo añadiremos al grupo `wheel` para otorgarle acceso a tareas administrativas mediante `sudo`.

1. Crea el nuevo usuario (sustituye `user` por tu nombre de usuario deseado):

	```sh
	useradd -m -G wheel -s /bin/bash user
	```

El parámetro `-m` crea la carpeta personal `/home/usuario` y `-s /bin/bash` establece Bash como tu shell predeterminado.

2. Asígnale una contraseña a tu nuevo usuario:

	```sh
	passwd user
	```

3. Habilita los permisos de superusuario para el grupo `wheel` abriendo el archivo de configuración con `visudo`:

	```sh
	EDITOR=micro visudo
	```

Busca la línea que dice:

```text
# %wheel ALL=(ALL:ALL) ALL
```

Borra el `#` al principio para descomentarla y que quede exactamente así:

```text
%wheel ALL=(ALL:ALL) ALL
```

Guarda y sal del editor (`Ctrl + S`, Enter, `Ctrl + Q`).

## 4.7. Habilitar Servicios Esenciales

Para que el sistema tenga conectividad de red de forma automática al encender sin necesidad de configurarla manualmente en cada sesión, habilita el servicio de NetworkManager:

```sh
systemctl enable NetworkManager.service
```

## 4.8. Instalación y Configuración del Bootloader (GRUB en UEFI)

El bootloader es el programa que la placa base ejecuta al encender para cargar el kernel de Linux en la memoria RAM.

> [!IMPORTANT] IMPORTANTE
> 
> En sistemas **UEFI/GPT**, `grub-install` no debe apuntar a la raíz del disco físico (como se hacía antiguamente en BIOS/MBR), sino a la partición EFI que montamos en `/boot/efi`.

1. Instala los binarios de GRUB en la partición EFI del sistema:

	```sh
	grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
	```

2. Genera el archivo de configuración de arranque (`grub.cfg`), el cual detectará automáticamente el kernel, el microcódigo y los parámetros de inicio:

	```sh
	grub-mkconfig -o /boot/grub/grub.cfg
	```

# 5. Primer Arranque

¡Felicidades! Has instalado y configurado con éxito la base completa de Arch Linux desde cero. Solo resta salir de la jaula chroot, desmontar las particiones de forma segura para asegurar que todos los datos en caché se escriban en el disco y reiniciar el equipo:

1. Sal del entorno chroot:

	```sh
	exit
	```

2. Desmonta recursivamente todas las particiones:

	```sh
	umount -R /mnt
	```

3. Reinicia la computadora:

	```sh
	reboot
	```
   
Retira la memoria USB durante el reinicio para que tu computadora arranque directamente desde el disco duro. Al iniciar, verás el menú de GRUB, seguido de la pantalla de bienvenida de Arch Linux pidiéndote tu usuario y contraseña. A partir de aquí, tienes un sistema limpio, rápido y preparado para que construyas tu entorno visual y flujo de trabajo preferido.

---

> [!RESOURCES] REFERENCIAS
> 
> - **Arch Wiki.** *Arch User Repository*. Recuperado de [wiki.archlinux.org/title/Arch_User_Repository](https://wiki.archlinux.org/title/Arch_User_Repository)
>   
> - **Arch Wiki.** *GRUB*. Recuperado de [wiki.archlinux.org/title/GRUB](https://wiki.archlinux.org/title/GRUB)
>   
> - **Arch Wiki.** *Desktop environment*. Recuperado de [wiki.archlinux.org/title/Desktop_environment](https://wiki.archlinux.org/title/Desktop_environment)
>   
> - **The Linux Kernel.** *Documentation*. Recuperado de [kernel.org/doc/html/latest/](https://www.kernel.org/doc/html/latest/)
>
> - **YouTube.** *Arch Linux: A ℂ𝕠𝕞𝕗𝕪 Install Guide*. Recuperado de [youtu.be/68z11VAYMS8](https://youtu.be/68z11VAYMS8)
>
> - **GitHub Gist.** *A modern, updated installation guide for Arch Linux with BTRFS on an UEFI system*. Recuperado de [gist.github.com/mjkstra/96ce7a5689d753e7a6bdd92cdc169bae](https://gist.github.com/mjkstra/96ce7a5689d753e7a6bdd92cdc169bae)
>
> - **Linuxiac.** *How to Install Arch Linux: A Beginner’s Practical Guide*. Recuperado de [linuxiac.com/arch-linux-install/](https://linuxiac.com/arch-linux-install/)
>
> - **Arch Wiki.** *Installation guide*. Recuperado de [wiki.archlinux.org/title/Installation_guide](https://wiki.archlinux.org/title/Installation_guide)