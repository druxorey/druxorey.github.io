export interface Article {
  id: string;
  title: string;
  slug: string;
  summary: string;
  date: string;
  readingTime: string;
  tags: string[];
  image?: string | null;
}

export const articlesData: Article[] = [
  {
    "id": "buenas-practicas-de-gestion-de-repositorios",
    "title": "Buenas Prácticas de Gestión de Repositorios",
    "slug": "buenas-practicas-de-gestion-de-repositorios.html",
    "summary": "La gestión profesional de repositorios se basa en el uso de Scoped Commits y convenciones de nomenclatura claras para transformar el historial de cambios en una herramienta de navegación intuitiva. Al integrar PRs atómicas, protección de ramas y buenas prácticas de higiene del código, es posible elevar la calidad del desarrollo y simplificar la colaboración en proyectos de cualquier escala.",
    "date": "2026-06-14",
    "readingTime": "10 min de lectura",
    "tags": [
      "investigaciones"
    ],
    "image": "/images/post/buenas-practicas-de-gestion-de-repositorios.avif"
  },
  {
    "id": "crea-un-servidor-dedicado-de-minecraft-en-linux",
    "title": "Prontuario para Instalar un Servidor de Minecraft en Linux",
    "slug": "crea-un-servidor-dedicado-de-minecraft-en-linux.html",
    "summary": "Transformar hardware antiguo en un servidor doméstico es una excelente forma de aprovechar recursos. Esta guía enseña a desplegar un servidor de Minecraft optimizado con Fabric, utilizando Java 21 en modo headless para maximizar el rendimiento. Aprenderás a configurar entornos en Arch Linux o Debian, automatizar servicios en segundo plano y gestionar conexiones seguras sin complicaciones innecesarias en tu red.",
    "date": "2025-12-18",
    "readingTime": "10 min de lectura",
    "tags": [
      "prontuario",
      "linux",
      "juegos"
    ],
    "image": "/images/post/crea-un-servidor-dedicado-de-minecraft-en-linux.avif"
  },
  {
    "id": "inicializar-tu-entorno-de-arch-linux",
    "title": "Prontuario para Inicializar tu Entorno de Arch Linux",
    "slug": "inicializar-tu-entorno-de-arch-linux.html",
    "summary": "Una vez instalado el sistema, la optimización del entorno es clave para maximizar el rendimiento y la autonomía. Esta guía detalla la configuración de redes, la gestión de paquetes mediante Pacman y AUR, y el ajuste de controladores gráficos y gestión energética. Aprenderás a personalizar tu equipo para lograr un sistema estable, seguro y eficiente, adaptado perfectamente a tus necesidades de hardware.",
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
    "summary": "La instalación manual de Arch Linux representa una oportunidad invaluable para comprender a fondo el funcionamiento de un sistema operativo GNU/Linux. Al configurar desde cero el particionado de discos, el gestor de arranque y los servicios esenciales, se adquiere un dominio técnico superior sobre el hardware y el software, transformando un proceso intimidante en una experiencia de aprendizaje fundamental para cualquier usuario avanzado.",
    "date": "2024-03-22",
    "readingTime": "15 min de lectura",
    "tags": [
      "prontuario",
      "linux"
    ],
    "image": "/images/post/instalar-arch-linux.avif"
  }
];
