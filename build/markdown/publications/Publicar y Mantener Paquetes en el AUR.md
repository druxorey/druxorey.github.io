---
created: 2026-04-02 19:00
title: Prontuario para Publicar y Mantener Paquetes en el AUR
author: Guillermo Galavís
description: Publicar tus propios paquetes en el Arch User Repository (AUR) es la mejor forma de contribuir a la comunidad y mantener tus herramientas siempre al día. Dominar la estructura de un PKGBUILD te permite empaquetar desde binarios cerrados hasta versiones VCS dinámicas. Aprenderás a gestionar tu entorno con SSH, automatizar metadatos y seguir las normativas de empaquetado para asegurar que tu software sea impecable, reproducible y profesional.
tags:
  - prontuario
  - linux
---

<h1 id="post-title" align="center"> Prontuario para Publicar y Mantener Paquetes en el AUR </h1>

El **Arch User Repository (AUR)** es, sin duda, la joya de la corona de Arch Linux. Gran parte de la magia de esta distribución se debe a que casi cualquier programa existente en el mundo Linux ya fue empaquetado por alguien de la comunidad y está listo para instalar. Sin embargo, llega un momento en el que una herramienta que necesitas no está disponible, o el paquete existente quedó abandonado en el tiempo.

Empaquetar para el AUR no es física cuántica: solo necesitas entender la estructura declarativa de un archivo `PKGBUILD` y seguir las normativas de empaquetado de Arch. En este prontuario explicaré desde la configuración criptográfica de tu entorno con SSH, hasta cómo redactar recetas limpias para binarios precompilados (`-bin`) y compilaciones dinámicas desde repositorios Git (`-git`), evitando errores comunes y manteniendo el ecosistema impecable.

> [!IMPORTANT] IMPORTANTE
> 
> Para seguir esta guía debes tener instalado en tu sistema el metapaquete base de compilación (`base-devel`) y `git`, además de contar con una cuenta registrada en el portal oficial de [aur.archlinux.org](https://aur.archlinux.org/).

# 1. Configuración del Entorno y Conexión SSH

El AUR opera internamente como una gran colección de repositorios Git independientes que se gestionan exclusivamente a través del protocolo seguro SSH. Para poder pushear cambios, necesitas autenticar tu máquina frente a los servidores de Arch.

## 1.1. Generación de una Llave SSH Moderna

Utilizaremos el algoritmo **Ed25519**, que ofrece firmas criptográficas mucho más seguras, ligeras y rápidas que el estándar clásico RSA:

```sh
ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"
````

El asistente te preguntará dónde guardar la llave; presiona Enter para aceptar la ruta por defecto (`~/.ssh/id_ed25519`). Si le colocas una contraseña (_passphrase_) (lo cual es muy recomendable por seguridad), puedes integrarla al agente SSH de tu terminal para no tener que escribirla a cada rato:

```sh
# Añade esto al final de tu ~/.bashrc o ~/.zshrc
eval "$(ssh-agent -s)" > /dev/null
ssh-add ~/.ssh/id_ed25519 2> /dev/null
```

## 1.2. Vincular tu Llave Pública en el Portal del AUR

1. Imprime en pantalla y copia tu llave pública:
    
    ```sh
    cat ~/.ssh/id_ed25519.pub
    ```
    
2. Inicia sesión en [aur.archlinux.org](https://aur.archlinux.org/) y entra en la sección **«Mi cuenta»** (_My Account_).
    
3. Pega la clave copiada en el campo **«SSH Public Key»** y guarda los cambios.

## 1.3. Probar la Autenticación

Verifica que el servidor reconozca tu identidad ejecutando:

```sh
ssh -T aur@aur.archlinux.org
```

Si todo está fino, recibirás un mensaje de bienvenida similar a este:

```plaintext
Welcome to AUR, druxorey! Interactive shell is disabled.
```

# 2. Los Tres Sabores de Paquetes en el AUR

En el Arch User Repository no existe un único molde para empaquetar. Para mantener el ecosistema ordenado, la comunidad de Arch Linux definió un estándar estricto de nomenclatura según el origen del código y la forma en que se distribuye.

## 2.1. Diferencias y Propósito del Estándar

| **Tipo de paquete** | **Sufijo**                            | **Origen del software**                                                                | **Proceso de instalación**                                                                                    | **Caso de uso ideal**                                                                                                                                            |
| ------------------- | ------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Estándar**        | _Ninguno_ (`paquete`)                 | Código fuente comprimido de una versión estable (ej. `v1.2.0.tar.gz`).                 | Descarga el tarball del release, lo compila en la máquina del usuario y lo empaqueta.                         | La opción por defecto para proyectos de código abierto con versiones estables publicadas.                                                                        |
| **Binario**         | `-bin` (`paquete-bin`)                | Ejecutable precompilado por el autor original (o binarios extraídos de `.deb`/`.rpm`). | Descarga directamente el binario empaquetado, omite la compilación y lo ubica en `/usr/bin/`.                 | Software privativo/cerrado o programas gigantescos que tardarían horas en compilar en una laptop modesta (como navegadores o paquetes pesados de Rust/Electron). |
| **VCS / Dinámico**  | `-git`, `-hg`, `-svn` (`paquete-git`) | La rama principal del repositorio de control de versiones (`git clone`).               | Clona el repositorio en vivo, autocalcula la versión según el último commit y compila el código más reciente. | Probar funciones en desarrollo (_bleeding-edge_), parches recientes o cuando el autor no publica _releases_ formales.                                            |

## 2.2. ¿Cómo Determinar qué Tipo de Paquete Crear?

Antes de crear un repositorio en el AUR, pregúntate lo siguiente para elegir el nombre adecuado:

- **¿El software es de código cerrado o comercial?** Entonces debe ser obligatoriamente **`paquete-bin`**, ya que no existe código fuente para compilar.
    
- **¿Es un programa ligero o mediano de código abierto con versiones numeradas (Tags/Releases)?** En ese caso crea el paquete estándar **`paquete`**. Es el formato preferido por las directrices de Arch.
    
- **¿Es un programa abierto pero compilarlo le exige al usuario 32 GB de RAM y dos horas de procesador?** Puedes publicar **`paquete-bin`** (usando los binarios de los releases oficiales) para ahorrarle ese trabajo al usuario, o bien mantener ambos: `paquete` (fuente) y `paquete-bin` (binario).
    
- **¿Quieres ofrecer la versión más fresca del repositorio de desarrollo sin esperar a que saquen versión oficial?** Crea **`paquete-git`**.

# 3. Base Común del Empaquetado: Estructura y Archivos

Sin importar si estás haciendo un paquete normal, `-bin` o `-git`, todos comparten la misma base estructural y las mismas reglas de convivencia en el sistema.

## 3.1. Clonación del Repositorio y Blindaje con `.gitignore`

Cada paquete en el AUR es un repositorio de Git independiente. Clónalo según el nombre que hayas definido:

```sh
git clone ssh://aur@aur.archlinux.org/nombre-paquete.git
cd nombre-paquete
```

> [!WARNING] ADVERTENCIA: Cuidado con los archivos basura en el repositorio
> 
> Los servidores del AUR solo aceptan archivos de texto plano que contengan las instrucciones (`PKGBUILD`, `.SRCINFO`, parches o accesos directos `.desktop`). Subir archivos comprimidos (`.tar.gz`), binarios o carpetas temporales de compilación es una falta grave a las normativas de Arch.

Crea de inmediato un archivo `.gitignore` para no subir artefactos por error:

```sh
cat << 'EOF' > .gitignore
pkg/
src/
*.tar.*
*.zip
*.deb
*.rpm
EOF
```

## 3.2. Variables y Reglas de Convivencia

Todo archivo `PKGBUILD` cuenta con variables estructurales que debes declarar al inicio:

- **`_pkgname`**: Variable auxiliar para guardar el nombre base del programa y evitar escribirlo repetidas veces.
    
- **`pkgname`**: El nombre oficial del paquete en el AUR (`${_pkgname}`, `${_pkgname}-bin` o `${_pkgname}-git`).
    
- **`pkgdesc`, `url`, `license`, `arch`**: Metadatos descriptivos, página oficial, licencia legal (ej. `MIT`, `GPL-3.0-or-later`) y arquitecturas compatibles (`'x86_64'`, `'aarch64'`).
    
- **`provides=("${_pkgname}")`**: Le avisa a pacman que, aunque el paquete se llame `nombre-bin` o `nombre-git`, provee la herramienta real `nombre`.
    
- **`conflicts=("${_pkgname}")`**: Evita que dos variantes del mismo programa se instalen al mismo tiempo y armen un arroz con mango en las rutas de tu disco.

## 3.3. La Función de Instalación (`package`) y el Directorio Ficticio

Arch Linux utiliza una técnica llamada _fakeroot_: durante la instalación crea un directorio temporal llamado `${pkgdir}` que simula ser la raíz (`/`) de tu sistema.

```sh
package() {
    cd "${srcdir}"
    # Crea las carpetas intermedias y da permisos de ejecución (para binarios)
    install -Dm755 "${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
    # Asigna permisos de lectura (para licencias y documentación)
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
```

Todo archivo que deposites dentro de `${pkgdir}/usr/bin/` terminará instalado exactamente en `/usr/bin/` cuando el usuario lo instale con `pacman`.

# 4. Implementación del `PKGBUILD` según el Tipo de Paquete

Para facilitarte la vida, no necesitas inventar la rueda desde cero ni ponerte a adivinar qué variables o banderas de compilación requiere cada lenguaje. La propia comunidad de Arch Linux mantiene prototipos y guías oficiales de empaquetado (_package guidelines_) diseñadas para asegurar que el software compile de forma limpia, reproducible y optimizada para el sistema.

Si la herramienta que quieres publicar está escrita en un lenguaje o entorno particular, puedes consultar y apoyarte directamente en su normativa técnica correspondiente en la Arch Wiki:

- **Proyectos en Go (Golang):** [Go package guidelines](https://wiki.archlinux.org/title/Go_package_guidelines)
- **Proyectos en Rust (Cargo):** [Rust package guidelines](https://wiki.archlinux.org/title/Rust_package_guidelines)
- **Proyectos en Python:** [Python package guidelines](https://wiki.archlinux.org/title/Python_package_guidelines)
- **Proyectos en C / C++ (CMake o Meson):** [CMake package guidelines](https://wiki.archlinux.org/title/CMake_package_guidelines) y [Meson package guidelines](https://wiki.archlinux.org/title/Meson_package_guidelines)
- **Proyectos en Node.js / JavaScript:** [Node.js package guidelines](https://wiki.archlinux.org/title/Node.js_package_guidelines)
- **Paquetes de control de versiones (Git / VCS):** [VCS package guidelines](https://wiki.archlinux.org/title/VCS_package_guidelines)

A continuación, revisaremos las tres plantillas base fundamentales para que elijas la que mejor se adapte a tu caso:

## 4.1. Caso A: Paquete Estándar (Desde Código Fuente Estable)

Descarga el código fuente de un release específico, lo compila de forma reproducible y lo empaqueta.

```sh
# Maintainer: Tu Nombre <tu_email@ejemplo.com>

_pkgname=herramienta
pkgname=${_pkgname}
pkgver=1.0.0
pkgrel=1
pkgdesc="Herramienta compilada desde código fuente estable"
arch=('x86_64' 'aarch64')
url="https://github.com/autor/herramienta"
license=('MIT')
depends=('glibc')
makedepends=('make' 'gcc')
provides=("${_pkgname}")
conflicts=("${_pkgname}-bin" "${_pkgname}-git")

source=("${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('SKIP')

build() {
    cd "${_pkgname}-${pkgver}"
    make
}

package() {
    cd "${_pkgname}-${pkgver}"
    install -Dm755 "${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
```

## 4.2. Caso B: Paquete Precompilado (`-bin`)

Descarga directamente el ejecutable ya compilado por los desarrolladores desde sus _Releases_. Observa que **no lleva función `build()`**, ya que el binario viene listo de fábrica.

```sh
# Maintainer: Tu Nombre <tu_email@ejemplo.com>

_pkgname=herramienta
pkgname=${_pkgname}-bin
pkgver=1.0.0
pkgrel=1
pkgdesc="Herramienta distribuida como binario precompilado"
arch=('x86_64' 'aarch64')
url="https://github.com/autor/herramienta"
license=('MIT')
provides=("${_pkgname}")
conflicts=("${_pkgname}" "${_pkgname}-git")

# Enlaces de descarga dinámicos según la arquitectura del procesador
source_x86_64=("${url}/releases/download/v${pkgver}/${_pkgname}-v${pkgver}-linux-amd64.tar.gz")
source_aarch64=("${url}/releases/download/v${pkgver}/${_pkgname}-v${pkgver}-linux-arm64.tar.gz")
sha256sums_x86_64=('SKIP')
sha256sums_aarch64=('SKIP')

package() {
    cd "${srcdir}"
    install -Dm755 "${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
```

## 4.3. Caso C: Paquete Dinámico (`-git`)

Clona el repositorio en vivo. Utiliza una función `pkgver()` que cuenta la cantidad de commits e inyecta la versión en tiempo real.

```sh
# Maintainer: Tu Nombre <tu_email@ejemplo.com>

_pkgname=herramienta
pkgname=${_pkgname}-git
pkgver=r142.a1b2c3d
pkgrel=1
pkgdesc="Herramienta compilada desde el último commit de desarrollo"
arch=('x86_64' 'aarch64')
url="https://github.com/autor/herramienta"
license=('MIT')
provides=("${_pkgname}")
conflicts=("${_pkgname}" "${_pkgname}-bin")
makedepends=('git' 'gcc' 'make')

source=("git+${url}.git")
sha256sums=('SKIP')

pkgver() {
    cd "${_pkgname}"
    # Formato estándar: r<número_commits>.<hash_corto>
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}

build() {
    cd "${_pkgname}"
    make
}

package() {
    cd "${_pkgname}"
    install -Dm755 "${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
```

### Directivas de compilación comunes según el lenguaje en `build()`:

- **Proyectos en Go:**
    
    ```sh
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
    go build -o "${_pkgname}" .
    ```
    
- **Proyectos en Rust:**
    
    ```sh
    cargo build --release --locked --all-features --target-dir=target
    # El binario se instala desde: target/release/${_pkgname}
    ```
    
- **Proyectos en C/C++ con CMake:**
    
    ```sh
    cmake -B build -S . -G Ninja -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release
    cmake --build build
    # En package(): DESTDIR="${pkgdir}" cmake --install build
    ```

# 5. Flujo Común de Verificación, Metadatos y Publicación

Una vez redactado el `PKGBUILD`, sigue este procedimiento secuencial para dejar el paquete al pelo y subirlo a los servidores.

## 5.1. Calcular Hashes Automáticamente

Reemplaza los marcadores temporales `SKIP` por las firmas criptográficas reales calculadas por el sistema:

```sh
updpkgsums
```

En los paquetes `-git`, como el repositorio cambia con cada commit, `sha256sums` permanece como `'SKIP'` y este paso se omite.

## 5.2. Prueba de Compilación e Instalación Local

Prueba que el paquete resuelva dependencias, compile e instale limpiamente en tu máquina:

```sh
makepkg -si
```

Verifica de inmediato en tu terminal que el comando principal funcione y responda:

```sh
nombre-herramienta --version
```

## 5.3. Generación Obligatoria del `.SRCINFO`

La plataforma web del AUR no lee archivos `PKGBUILD` por motivos de rendimiento y seguridad; utiliza exclusivamente el archivo estático `.SRCINFO` para indexar el paquete y mostrar su información en el buscador web.

```sh
makepkg --printsrcinfo > .SRCINFO
```

> [!IMPORTANT] IMPORTANTE
> 
> Cada vez que modifiques cualquier variable en el `PKGBUILD` (subir versión, cambiar descripción o agregar dependencias), debes volver a ejecutar `makepkg --printsrcinfo > .SRCINFO` antes de hacer commit.

## 5.4. Publicar en el Servidor del AUR

Sube los cambios a la plataforma usando Git:

```sh
git add PKGBUILD .SRCINFO .gitignore
git commit -m "feat: publicar version 1.0.0"
git push origin master
```

Si todo está en orden, tu paquete aparecerá disponible públicamente en la web del AUR en cuestión de segundos.

# 6. Mantenimiento, Adopción y Co-mantenimiento

## 6.1. Actualización de Versiones de un Paquete Existente

Cuando el autor publique una nueva versión:

1. Edita el `PKGBUILD` y actualiza la variable `pkgver` (y reinicia `pkgrel=1`).
2. Ejecuta `updpkgsums` para actualizar las sumas de verificación.
3. Compila localmente con `makepkg -si` para comprobar que nada se rompa.
4. Regenera los metadatos con `makepkg --printsrcinfo > .SRCINFO`.
5. Haz `git commit -m "chore: bump version to X.Y.Z"` y `git push origin master`.

## 6.2. Adopción de Paquetes Huérfanos (_Orphans_)

Si encuentras un paquete cuyo mantenedor aparece como **«None»**, significa que está libre para que cualquier usuario asuma la responsabilidad de mantenerlo:

- **Vía Web:** Haz clic en **«Adopt Package»** en el menú lateral derecho.
- **Vía Terminal (SSH):**
    
    ```sh
    ssh aur@aur.archlinux.org adopt nombre-paquete
    ```

Una vez adoptado, clona el repositorio, coloca tu nombre en el encabezado `# Maintainer:`, actualiza el código y sube los cambios.

## 6.3. Paquetes Abandonados con Mantenedor Inactivo (Regla de los 14 Días)

Si un paquete lleva meses sin actualizarse o está roto, pero aún tiene a un mantenedor asignado, no puedes quitárselo de la nada. Hay un protocolo comunitario que debes respetar:

1. **Deja un comentario público** en la página del paquete avisando que la versión actual está rota o desactualizada y ofrece tu ayuda.
    
2. **Espera un período de cortesía de catorce (14) días continuos**.
    
3. Si tras dos semanas el mantenedor no da señales de vida, entra en el menú web del paquete y haz clic en **«Submit Request»** > **«Orphan Request»**.
    
4. Explica con claridad que el paquete está desactualizado, que se le notificó formalmente en comentarios y que venció el plazo de 14 días sin respuesta.
    
5. Un Moderador de Confianza (_Trusted User_) revisará la solicitud, pasará el paquete a estado huérfano y podrás adoptarlo formalmente.

## 6.4. Co-mantenimiento

Para colaborar con otros desarrolladores sin transferir la propiedad del paquete, el mantenedor principal puede agregar colaboradores desde el enlace **«Manage Co-Maintainers»** en la web del AUR. Los co-mantenedores tienen permisos completos para empujar commits con `git push` y moderar comentarios destacados, pero el dueño principal conserva el control sobre la eliminación o transferencia definitiva del proyecto.

---

> [!RESOURCES] REFERENCIAS
> 
> - **Arch Wiki.** _Arch User Repository (Guía general del AUR)_. Recuperado de [wiki.archlinux.org/title/Arch_User_Repository](https://wiki.archlinux.org/title/Arch_User_Repository)
>     
> - **Arch Wiki.** _PKGBUILD (Especificación técnica de variables y funciones)_. Recuperado de [wiki.archlinux.org/title/PKGBUILD](https://wiki.archlinux.org/title/PKGBUILD)
>     
> - **Arch Wiki.** _AUR submission guidelines (Reglas y políticas de publicación)_. Recuperado de [wiki.archlinux.org/title/AUR_submission_guidelines](https://wiki.archlinux.org/title/AUR_submission_guidelines)
>     
> - **Arch Wiki.** _VCS package guidelines (Reglas para paquetes dinámicos -git)_. Recuperado de [wiki.archlinux.org/title/VCS_package_guidelines](https://wiki.archlinux.org/title/VCS_package_guidelines)