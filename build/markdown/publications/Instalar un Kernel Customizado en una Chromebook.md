---
created: 2025-12-20 02:25
title: Prontuario para Instalar un Kernel Customizado en una Chromebook
author: Guillermo Galavís
description: Liberar una Chromebook de las restricciones de ChromeOS es posible mediante la instalación de un firmware UEFI personalizado. Al desactivar la protección física contra escritura y flashear Coreboot, transformas un equipo limitado en una computadora x86 estándar. Este proceso te otorga control total sobre el hardware, permitiéndote instalar distribuciones como Arch Linux y optimizar el kernel para un rendimiento absoluto.
tags:
  - prontuario
  - linux
---

<h1 id="post-title" align="center"> Prontuario para Instalar un Kernel Customizado en una Chromebook </h1>

Mi primer acercamiento a la programación de manera seria ocurrió frente a una modesta Dell Chromebook P22T. Aunque el equipo era sumamente portátil y ligero, ChromeOS pronto se convirtió en una jaula: el almacenamiento interno eMMC era diminuto, el sistema impedía acceder a utilidades de desarrollo avanzadas y el kernel compilado por Google venía recortado y bloqueado de fábrica. Para tener un control absoluto sobre los recursos de la máquina y compilar código sin limitaciones, no bastaba con arreglos temporales en espacio de usuario; necesitaba reemplazar el sistema operativo por completo y montar un kernel personalizado optimizado para el hardware sobre una base limpia como Arch Linux.

Lograr esto exigió intervenir el dispositivo desde adentro: desarmar la laptop para desactivar el bloqueo físico de la placa base, sustituir el firmware original por una BIOS UEFI abierta utilizando las utilidades de **MrChromebox** y reconfigurar la gestión de controladores a nivel de kernel. A continuación, encontrarás el procedimiento detallado y actualizado para transformar tu Chromebook en una computadora x86 plenamente libre y estándar.

> [!WARNING] ADVERTENCIA DE SEGURIDAD: Modificación de Firmware
> 
> Este procedimiento implica abrir físicamente el equipo para modificar la placa base y sobrescribir el chip de memoria SPI Flash (*BIOS*). Si interrumpes el proceso de flasheo o cortas la energía, el dispositivo podría quedar brickeado. Realiza una copia de seguridad obligatoria del firmware de fábrica cuando el script te lo solicite y procede bajo tu propia responsabilidad.

> [!IMPORTANT] IMPORTANTE
> 
> Esta guía toma como referencia el procedimiento en una **Dell Chromebook 11 (P22T / modelo *Candy*)**. Aunque el script de MrChromebox es compatible con la mayoría de arquitecturas x86 de ChromeOS, la ubicación física del mecanismo de protección contra escritura varía notablemente según el fabricante y año del modelo.

# 1. Herramientas y Preparativos de Hardware

No es posible realizar este procedimiento únicamente mediante software; necesitarás herramientas manuales y periféricos auxiliares:

- **Destornillador de precisión (Phillips #0 o #1):** Para retirar la tapa inferior y remover el tornillo de protección de la placa base.

- **Unidad USB con instalador UEFI:** Una memoria USB booteable con tu distribución Linux preferida (por ejemplo, el instalador base de Arch Linux).

- **Segunda memoria USB (Formateada en FAT32):** Para guardar el respaldo (*backup*) del firmware original de Google.

- **Teclado y mouse USB externos:** Durante la primera instalación, muchos kernels genéricos no integran los controladores del bus I2C para el touchpad o el teclado interno de las Chromebooks.

- **Conexión a internet estable:** Indispensable para que el script descargue la imagen de Coreboot correspondiente a tu procesador.

# 2. Desactivación de la Protección Contra Escritura Física (Write-Protect)

Google protege el chip de memoria flash del firmware mediante una línea de voltaje enlazada a un tornillo físico en la placa base (*Hardware Write-Protect*). Mientras este contacto permanezca cerrado, el chip impedirá cualquier operación de sobreescritura en las secciones críticas de la memoria ROM.

1. Apaga la Chromebook por completo, desconecta el cargador y dale la vuelta sobre una superficie suave.

2. Retira todos los tornillos del chasis inferior con tu destornillador y retira la tapa con cuidado.

3. Localiza el **tornillo Write-Protect (WP)**. En la Dell Chromebook 11 P22T, suele ser un tornillo metálico visible cerca del módulo del ventilador/disipador, marcado con una pista circular dividida en la placa base.

4. Desatornilla y retira dicho tornillo por completo; guárdalo en un lugar seguro.

5. Vuelve a colocar la tapa trasera y atorníllala antes de encender el equipo.

# 3. Habilitación del Modo Desarrollador

El mecanismo *Verified Boot* de ChromeOS valida la firma criptográfica del sistema antes de cada arranque. Para abrir una terminal con privilegios de root dentro de ChromeOS, debemos forzar al sistema a ingresar en el modo para desarrolladores.

1. Con el equipo apagado, mantén presionadas las teclas **`Esc` + `Refresh` (tecla de recargar/F3) + `Power`** para iniciar en la pantalla de recuperación (*Recovery Screen*).

2. En la pantalla con el signo de exclamación amarillo, presiona la combinación **`Ctrl + D`**.

3. Presiona **`Enter`** cuando el sistema solicite confirmación para activar el modo desarrollador.

4. La Chromebook ejecutará un formateo de fábrica (*Powerwash*) para borrar todos los datos de usuario locales. Este proceso tomará entre 5 y 10 minutos.

# 4. Descarga y Ejecución del Script de MrChromebox

Una vez que el sistema termine de reiniciar, realiza la configuración inicial mínima de ChromeOS únicamente para conectarte a tu red Wi-Fi (puedes entrar como invitado).

1. Abre la consola de ChromeOS (*Crosh*) presionando **`Ctrl + Alt + T`**.

2. Escribe `shell` y presiona Enter para obtener un intérprete Bash con permisos completos.

3. Descarga y ejecuta el script de utilidades de firmware oficial desarrollado por **MrChromebox**:
    
    ```sh
    cd; curl -LO https://mrchromebox.tech/firmware-util.sh
    sudo bash firmware-util.sh
    ```

El script analizará automáticamente el código de hardware de tu placa (_board name_), comprobará si el tornillo Write-Protect fue retirado correctamente y desplegará un menú interactivo con las opciones disponibles.

# 5. Flasheo del Firmware Full ROM (UEFI Coreboot)

Para convertir la Chromebook en una computadora tradicional capaz de iniciar cualquier kernel o distribución, debemos instalar la opción **Full ROM**. Esta alternativa reemplaza la BIOS propietaria de Google por una implementación abierta de **Coreboot** con el gestor **Tianocore (EDK2)**.

1. En el menú del script, selecciona la opción:
    
    ```console
    Install/Update Full ROM Firmware
    ```
    
1. Escribe `Y` para confirmar que comprendes los riesgos del procedimiento.

2. **Copia de seguridad del Firmware:** Conecta tu memoria USB secundaria cuando el script te lo pregunte. El sistema extraerá el archivo binario del firmware de fábrica (`backup.rom`) y lo guardará en la memoria. Conserva este archivo para poder restaurar ChromeOS en el futuro si alguna vez lo necesitas.
    
3. El script descargará la imagen compilada de UEFI Coreboot para tu modelo específico y la escribirá en la memoria SPI.
    
4. Una vez que la pantalla confirme que el proceso concluyó con éxito, presiona Enter y apaga el equipo (`sudo poweroff`).

# 6. Arranque e Instalación del Sistema Operativo

Tu Chromebook ha dejado de buscar las particiones firmadas de ChromeOS y ahora se comporta como una computadora x86 estándar gobernada por una BIOS UEFI completa.

1. Inserta la memoria USB booteable con el instalador de Arch Linux (o la distribución de tu elección) y conecta el teclado/mouse auxiliar.
    
2. Enciende el equipo. Verás la pantalla de inicio del firmware UEFI de MrChromebox (representada comúnmente por el logotipo de un conejo blanco).
    
3. Presiona la tecla **`Esc`** inmediatamente al encender para abrir el menú de dispositivos de arranque y selecciona tu unidad USB.
    
4. Procede con el particionado e instalación habitual de tu sistema operativo.

> [!TIP] TIP: Ajustes para el Kernel en Chromebooks antiguas
> 
> En plataformas como Intel Bay Trail / Braswell (presentes en la Dell P22T), los controladores de audio y gestión de energía suelen requerir módulos específicos en el kernel de Linux. Asegúrate de instalar paquetes de firmware actualizados (`linux-firmware`) y, de ser necesario, compilar módulos del árbol de sonido ALSA específicos para hardware ChromeOS (`snd_soc_sst_acpi`).

---

> [!RESOURCES] REFERENCIAS
> 
> - **MrChromebox.tech (Sitio Oficial):** Documentación técnica, matriz de compatibilidad de hardware y guías de firmware en [mrchromebox.tech](https://mrchromebox.tech/).
>     
> - **Proyecto Coreboot:** Documentación del proyecto de firmware de código abierto para arquitecturas x86 en [coreboot.org](https://www.coreboot.org/).
>     
> - **TianoCore EDK2:** Implementación de referencia abierta de la especificación Unified Extensible Firmware Interface (UEFI) en [tianocore.org](https://www.tianocore.org/).
>     
> - **Arch Wiki - ChromeOS devices:** Guía detallada para la configuración de controladores, audio y teclado en hardware Chromebook dentro de [wiki.archlinux.org/title/ChromeOS_devices](https://www.google.com/search?q=https://wiki.archlinux.org/title/ChromeOS_devices).
>     
> - **Flashrom:** Utilidad universal de código abierto para identificación y flasheo de memorias ROM/Flash en [flashrom.org](https://www.flashrom.org/).
>     
> - **The Linux Kernel - ChromeOS hardware platform:** Documentación de controladores del kernel dedicados al subsistema de hardware de ChromeOS en [kernel.org/doc/html/latest/driver-api/chromeos.html](https://www.google.com/search?q=https://www.kernel.org/doc/html/latest/driver-api/chromeos.html).