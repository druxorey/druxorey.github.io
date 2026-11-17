---
created: 2026-06-14 18:25
title: Buenas Prácticas de Gestión de Repositorios
author: Guillermo Galavís
description: Gestionar un repositorio de forma profesional requiere abandonar el caos en favor de una arquitectura de control de versiones predecible y eficiente. Al implementar Scoped Commits, ramas basadas en módulos y una gobernanza automatizada mediante plantillas, eliminas el ruido administrativo y potencias la trazabilidad. Aprenderás a mantener un historial lineal, realizar rebase interactivo y aplicar estrategias de fusión que garantizan un código limpio, atómico y listo para producción.
tags:
  - investigaciones
---

<h1 id="main-title" align="center"> Buenas Prácticas de Gestión de Repositorios </h1>

# 1. Fundamentos de Scoped Commits frente a Conventional Commits

## 1.1. Limitaciones de Conventional Commits

Conventional Commits clasifica los cambios anteponiendo el tipo de acción administrativa (`feat`, `fix`, `chore`, `refactor`). En el día a día de proyectos medianos y grandes, este esquema presenta fricciones:

- **Ruido visual en el historial:** Al revisar `git log`, la columna izquierda se satura con las mismas cuatro palabras repetidas, ocultando qué parte del sistema se modificó.

- **Pérdida de tiempo en categorizaciones:** La diferencia práctica entre un `refactor`, un `perf` y un `fix` interno suele ser subjetiva. Debatir la etiqueta distrae del objetivo del cambio.

- **Falta de ubicación espacial:** Para depurar o entender la evolución de un archivo, la información crítica no es la intención administrativa, sino el componente o módulo exacto que fue alterado.

## 1.2. Filosofía y Estructura de Scoped Commits

Un Scoped Commit es un formato de mensaje de confirmación que elimina el prefijo de acción administrativa y coloca como sujeto principal el componente, módulo o directorio modificado: `<scope>: <descripción>`.

Para entender la diferencia, piensa en un taller mecánico: si guardas repuestos en cajas etiquetadas como «adición» o «arreglo», nadie sabe qué hay adentro. En cambio, si las cajas dicen «frenos: pastillas delanteras» o «motor: filtro de aceite», cualquier mecánico ubica la pieza de inmediato.

### 1.2.1. Anatomía y Reglas de Redacción

La estructura básica se mapea directamente con la arquitectura del proyecto:

```git
<scope>: <descripcion_en_imperativo>
````

Para cambios dentro de submódulos o directorios anidados:

```git
<scope>/<sub-scope>: <descripcion_en_imperativo>
```

**Reglas de estilo:**

- **Ámbitos base (`scope`):** Nombres de módulos reales del repositorio (`auth`, `api`, `ui`, `db`, `deps`, `infra`, `docs`).
    
- **Verbo en presente imperativo:** La descripción responde a: «Al aplicar este commit, el código...».
    
- **Formato:** Todo en minúsculas (salvo nombres propios o constantes), sin punto final y manteniendo la primera línea en menos de $72$ caracteres.

> [!EXAMPLE] **Ejemplo 1:** Comparación de Convenciones en el Log
> 
> **Conventional Commits:**
> 
> ```git
> fix(auth): resolve memory leak on token refresh
> feat(ui/button): add loading spinner state
> chore(deps): bump postgresql driver to v4.2
> ```
> 
> **Scoped Commits:**
> 
> ```git
> auth: resolve memory leak on token refresh
> ui/button: add loading spinner state
> deps: bump postgresql driver to v4.2
> ```

En Scoped Commits, el lector identifica el módulo de inmediato (`auth`, `ui/button`, `deps`). La naturaleza del cambio (si es corrección, ajuste o mejora) se entiende directamente al leer la acción o el diff del código.

# 2. Convenciones de Nombres para Repositorios y Ramas

## 2.1. Nomenclatura de Repositorios

Un buen nombre de repositorio debe ser autoexplicativo, predecible y fácil de escribir en terminal.

- **Uso estricto de kebab-case:** Todo en minúsculas y separado por guiones medios (ej. `payment-gateway`). Nunca usar mayúsculas, espacios ni guiones bajos.
    
- **Prefijos por tipo de componente:** En organizaciones con varios repositorios, ayuda clasificar el rol del proyecto:
   
    - `app-`: Aplicaciones de usuario final o clientes web/móvil (ej. `app-admin-portal`).
    - `svc-`: Servicios o APIs backend (ej. `svc-orders`).
    - `lib-`: Librerías o utilidades compartidas (ej. `lib-logger`).
    - `infra-`: Automatización, contenedores o scripts de despliegue (ej. `infra-k8s-configs`).

- **Sin sufijos temporales:** Prohibido usar `-v2`, `-new` o `-final`. El control de versiones ya gestiona la evolución temporal.

## 2.2. Nomenclatura de Ramas Basada en Ámbitos

Las ramas deben seguir el mismo principio que los Scoped Commits, eliminando prefijos como `feature/` o `bugfix/`.

```git
<scope>/<accion-breve>[-<ticket>]
```

- **Mapeo directo:** El primer segmento indica el módulo sobre el que se trabajará.
- **Acción en kebab-case:** Resumen corto de $2$ a $4$ palabras.
- **ID de tarea:** Si se usa un gestor de tareas (Jira, Linear, GitHub Issues), se incluye el código al final para mantener trazabilidad.

> [!EXAMPLE] **Ejemplo 2:** Declaración de Ramas de Trabajo
> 
> Para trabajar en la autenticación con Google (Tarea SEC-45):
> 
> ```git
> git checkout -b auth/google-oauth-login-SEC-45
> ```
> 
> Para ajustar la tabla de usuarios en la interfaz (Tarea UI-12):
> 
> ```git
> git checkout -b ui/virtualized-table-UI-12
> ```

## 2.3. Tipos y Ciclo de Vida de las Ramas

- **Rama principal (`main`):** Refleja el código listo para producción. No se envían commits directamente a ella.
    
- **Ramas de trabajo (`<scope>/...`):** Ramas cortas creadas para resolver una tarea puntual. Su ciclo de vida ideal es de $1$ a $3$ días y deben eliminarse del servidor remoto tras ser integradas.

# 3. Gobernanza y Gestión del Proyecto en GitHub

## 3.1. Archivos Clave en el Directorio `.github/`

Configurar buenas herramientas dentro de `.github/` automatiza el orden del equipo sin necesidad de reuniones de coordinación constantes:

- **`CODEOWNERS`:** Asigna de forma automática a los revisores responsables según los archivos modificados en una Pull Request.
    
- **`PULL_REQUEST_TEMPLATE.md`:** Formulario predeterminado que guía al autor a describir qué cambió, por qué y cómo probarlo.
    
- **`ISSUE_TEMPLATE/`:** Plantillas para que los reportes de errores y solicitudes de funciones incluyan datos mínimos (pasos para reproducir, capturas, logs).

> [!EXAMPLE] **Ejemplo 3:** Configuración de `CODEOWNERS`
> 
> ```plain text
> Por defecto, todo el repositorio requiere revisión del equipo general:
> *                   @equipo-core
> 
> Módulos específicos asignados a sus especialistas:
> /src/auth/          @seguridad-backend
> /src/ui/            @frontend-lead
> /infra/             @devops
> ```

## 3.2. Reglas de Protección de Ramas (Branch Protection)

Para evitar accidentes en la rama `main`, se deben activar las siguientes restricciones en GitHub:

- **Aprobaciones obligatorias:** Exigir al menos $1$ o $2$ revisiones aprobadas por pares antes de habilitar el merge.

- **Status Checks requeridos:** La PR no se puede integrar si los tests automáticos, linters o compilaciones de CI fallan.
    
- **Historial lineal obligatorio:** Bloquea la creación de merge commits desordenados forzando rebase o squash.
    
- **Bloqueo de `push --force`:** Impide que alguien sobreescriba accidentalmente el historial compartido de `main`.

## 3.3. Gestión y Tamaño de Pull Requests

Un error común es acumular dos semanas de trabajo en una sola PR de $2000$ líneas. Esto hace que las revisiones sean superficiales y los bugs pasen inadvertidos.

- **PRs atómicas y pequeñas:** Cada PR debe abarcar un único cambio funcional, manteniéndose idealmente por debajo de $300$ - $400$ líneas.
    
- **Draft PRs (Borradores):** Abre la PR como borrador desde el primer commit. Esto permite que el CI valide el código temprano y el equipo pueda ver en qué estás trabajando sin pedir una revisión formal todavía.

# 4. Operaciones de Higiene, Diagnóstico y Recuperación

## 4.1. Higiene del Historial Local

Antes de pedir revisión en una PR, el historial local debe quedar limpio y estructurado.

### 4.1.1. Enmienda Silenciosa (`git commit --amend`)

Si acabas de hacer un commit y olvidaste guardar un archivo o dejaste un error tipográfico, no crees un commit extra tipo «oops» o «fix typo»:

```bash
# 1. Agrega el archivo corregido al stage
git add src/auth/jwt.go

# 2. Únelo al último commit sin cambiar el mensaje
git commit --amend --no-edit
```

### 4.1.2. Rebase Interactivo (`git rebase -i`)

Permite reordenar, fusionar o renombrar commits locales antes de enviarlos al repositorio remoto.

```bash
# Modifica los últimos 3 commits
git rebase -i HEAD~3
```

El editor muestra la lista de commits. Los comandos más usados son:

- `pick`: Mantiene el commit.
- `reword`: Pausa el proceso para corregir el mensaje.
- `squash`: Une el commit con el anterior y combina los mensajes.
- `fixup`: Une el commit con el anterior y descarta el mensaje secundario (ideal para ajustes menores).

> [!EXAMPLE] **Ejemplo 4:** Limpieza de Historial con `fixup`
> 
> **Editor interactivo inicial:**
> 
> ```git
> pick 4b1a2c3 ui/button: add loading state
> pick 8f3d1e2 ui/button: fix spinner alignment
> pick 9c2a7b1 ui/button: remove console log
> ```
> 
> **Configuración ordenada:**
> 
> ```git
> pick 4b1a2c3 ui/button: add loading state
> fixup 8f3d1e2 ui/button: fix spinner alignment
> fixup 9c2a7b1 ui/button: remove console log
> ```
> 
> Al guardar, los tres commits se consolidan en uno solo (`ui/button: add loading state`), borrando los pasos intermedios de prueba.

## 4.2. Diagnóstico y Depuración

### 4.2.1. Git Reflog: La Red de Seguridad

El `reflog` es un registro local que guarda cronológicamente cada movimiento del puntero `HEAD` (cambios de rama, rebases, commits modificados o resets).

Si ejecutas un `git reset --hard` por error y parece que perdiste tus cambios, `reflog` guarda el historial de dónde estuvo tu puntero:

```bash
# 1. Inspecciona el registro de movimientos
git reflog

# 2. Regresa la rama al estado previo al error (ejemplo: HEAD@{2})
git reset --hard HEAD@{2}
```

### 4.2.2. Depuración con Git Bisect

Cuando aparece un bug y no sabes qué commit lo causó, `git bisect` aplica búsqueda binaria sobre el historial para hallar la confirmación exacta en tiempo $\mathcal{O}(\log n)$.

**Paso 1: Iniciar la sesión de búsqueda**

```bash
git bisect start
git bisect bad                 # La versión actual tiene el bug
git bisect good v1.4.0         # El tag o commit donde todo funcionaba bien
```

**Paso 2: Evaluar los puntos medios**

Git moverá el código automáticamente al punto medio del historial. Pruebas la aplicación y marcas:

- Si el bug está presente: `git bisect bad`
- Si el código funciona bien: `git bisect good`

**Paso 3: Cerrar la sesión**

Al terminar, Git te dirá el hash y autor exacto del commit que introdujo el error. Para volver a tu rama normal:

```bash
git bisect reset
```

### 4.2.3. Búsqueda por Contenido con Pickaxe (`-S`)

Para encontrar en qué commit se introdujo o eliminó una función, variable o texto específico en todo el historial del proyecto:

```bash
git log -S "AUTH_SECRET_KEY" --oneline
```

# 5. Estrategias de Fusión y Sincronización

## 5.1. Comparación de Estrategias de Integración

Al cerrar una Pull Request, existen tres métodos principales para incorporar los cambios a `main`:

- **Merge Commit clásico (`--no-ff`):** Crea un commit explícito con dos ramas padre. Conserva exactamente la historia de la rama, pero si el equipo es grande puede generar un grafo enredado lleno de bifurcaciones cruzadas.
    
- **Rebase and Merge (Fast-Forward):** Aplica los commits de la rama uno por uno sobre la punta de `main`. Deja un historial totalmente lineal, pero requiere que cada commit individual de la rama sea atómico y estable.
    
- **Squash and Merge:** Toma todos los commits de la rama y los compacta en un único commit directo sobre `main`. Es la mejor opción cuando la rama de trabajo contiene muchos commits de prueba o desordenados.

## 5.2. Sincronización Local sin Ruido

Para evitar que `git pull` genere commits de fusión automáticos innecesarios (`Merge branch 'main' of...`), configura tu entorno para sincronizar siempre mediante rebase:

```bash
# Rebasar cambios locales sobre los remotos al hacer pull
git config --global pull.rebase true

# Limpiar automáticamente referencias a ramas que ya fueron borradas en remoto
git config --global fetch.prune true
```

---

> [!RESOURCES] REFERENCIAS
> - **Scoped Commits Initiative.** _A simplified alternative to Conventional Commits_. Recuperado de [scopedcommits.com](https://scopedcommits.com/ "null")
> - **Scott Chacon & Ben Straub.** _Pro Git Book_. Recuperado de [git-scm.com](https://git-scm.com/book/en/v2 "null")
> - **Git Documentation.** _Git Reference Manual_. Recuperado de [git-scm.com](https://git-scm.com/doc "null")