export interface Publication {
  id: string;
  title: string;
  slug: string;
  summary: string;
  date: string;
  readingTime: string;
  tags: string[];
  image?: string | null;
}

export const publicationsData: Publication[] = [
  {
    "id": "buenas-practicas-de-gestion-de-repositorios",
    "title": "Buenas Prácticas de Gestión de Repositorios",
    "slug": "buenas-practicas-de-gestion-de-repositorios.html",
    "summary": "Gestionar un repositorio de forma profesional requiere abandonar el caos en favor de una arquitectura de control de versiones predecible y eficiente. Al implementar Scoped Commits, ramas basadas en módulos y una gobernanza automatizada mediante plantillas, eliminas el ruido administrativo y potencias la trazabilidad. Aprenderás a mantener un historial lineal, realizar rebase interactivo y aplicar estrategias de fusión que garantizan un código limpio, atómico y listo para producción.",
    "date": "2026-06-14",
    "readingTime": "10 min de lectura",
    "tags": [
      "investigaciones"
    ],
    "image": "/images/post/buenas-practicas-de-gestion-de-repositorios.avif"
  },
  {
    "id": "publicar-y-mantener-paquetes-en-el-aur",
    "title": "Prontuario para Publicar y Mantener Paquetes en el AUR",
    "slug": "publicar-y-mantener-paquetes-en-el-aur.html",
    "summary": "Publicar tus propios paquetes en el Arch User Repository (AUR) es la mejor forma de contribuir a la comunidad y mantener tus herramientas siempre al día. Dominar la estructura de un PKGBUILD te permite empaquetar desde binarios cerrados hasta versiones VCS dinámicas. Aprenderás a gestionar tu entorno con SSH, automatizar metadatos y seguir las normativas de empaquetado para asegurar que tu software sea impecable, reproducible y profesional.",
    "date": "2026-04-02",
    "readingTime": "14 min de lectura",
    "tags": [
      "prontuario",
      "linux"
    ],
    "image": "/images/post/publicar-y-mantener-paquetes-en-el-aur.avif"
  },
  {
    "id": "instalar-un-kernel-customizado-en-una-chromebook",
    "title": "Prontuario para Instalar un Kernel Customizado en una Chromebook",
    "slug": "instalar-un-kernel-customizado-en-una-chromebook.html",
    "summary": "Liberar una Chromebook de las restricciones de ChromeOS es posible mediante la instalación de un firmware UEFI personalizado. Al desactivar la protección física contra escritura y flashear Coreboot, transformas un equipo limitado en una computadora x86 estándar. Este proceso te otorga control total sobre el hardware, permitiéndote instalar distribuciones como Arch Linux y optimizar el kernel para un rendimiento absoluto.",
    "date": "2025-12-20",
    "readingTime": "7 min de lectura",
    "tags": [
      "prontuario",
      "linux"
    ],
    "image": "/images/post/instalar-un-kernel-customizado-en-una-chromebook.avif"
  },
  {
    "id": "crear-un-servidor-dedicado-de-minecraft-en-linux",
    "title": "Prontuario para Instalar un Servidor de Minecraft en Linux",
    "slug": "crear-un-servidor-dedicado-de-minecraft-en-linux.html",
    "summary": "Convertir hardware antiguo en un servidor dedicado de Minecraft es la forma ideal de aprovechar recursos mientras mantienes un control total sobre tu partida. Al utilizar Fabric junto a mods de optimización, lograrás un rendimiento superior sin alterar la experiencia original. Aprenderás a automatizar el proceso con systemd y gestionar conexiones seguras mediante Playit.gg, garantizando un entorno estable, eficiente y siempre disponible.",
    "date": "2025-12-18",
    "readingTime": "10 min de lectura",
    "tags": [
      "prontuario",
      "linux",
      "juegos"
    ],
    "image": "/images/post/crear-un-servidor-dedicado-de-minecraft-en-linux.avif"
  },
  {
    "id": "inicializar-tu-entorno-de-arch-linux",
    "title": "Prontuario para Inicializar tu Entorno de Arch Linux",
    "slug": "inicializar-tu-entorno-de-arch-linux.html",
    "summary": "Transformar una instalación base de Arch Linux en un entorno de trabajo funcional requiere ajustes precisos que maximizan el rendimiento y la estabilidad. Desde la optimización de Pacman y la gestión del AUR, hasta la configuración de seguridad, controladores gráficos y renderizado de fuentes, este proceso es el paso definitivo para convertir tu terminal en un sistema operativo profesional, eficiente y totalmente personalizado.",
    "date": "2025-01-09",
    "readingTime": "17 min de lectura",
    "tags": [
      "prontuario",
      "linux"
    ],
    "image": "/images/post/inicializar-tu-entorno-de-arch-linux.avif"
  },
  {
    "id": "instalar-arch-linux",
    "title": "Prontuario para Instalar Arch Linux",
    "slug": "instalar-arch-linux.html",
    "summary": "Instalar Arch Linux es el desafío definitivo para quienes buscan un sistema operativo a medida, eficiente y minimalista. Al prescindir de automatizaciones, obtienes un control total sobre cada componente, desde el particionado manual hasta la configuración del kernel. Es la oportunidad perfecta para dominar la arquitectura de tu equipo y construir un entorno de trabajo optimizado, estable y diseñado exclusivamente bajo tus necesidades.",
    "date": "2024-03-22",
    "readingTime": "15 min de lectura",
    "tags": [
      "prontuario",
      "linux"
    ],
    "image": "/images/post/instalar-arch-linux.avif"
  }
];
