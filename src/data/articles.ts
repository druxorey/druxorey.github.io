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
    "id": "instalar-arch-linux",
    "title": "Prontuario para Instalar Arch Linux",
    "slug": "instalar-arch-linux.html",
    "summary": "Guía práctica y comprensible para instalar Arch Linux paso a paso en sistemas UEFI/GPT, explicando el propósito de cada comando, partición y paquete base para entender el sistema a fondo.",
    "date": "2024-03-22",
    "readingTime": "15 min de lectura",
    "tags": [
      "prontuario"
    ],
    "image": "/images/post/instalar-arch-linux.avif"
  }
];
