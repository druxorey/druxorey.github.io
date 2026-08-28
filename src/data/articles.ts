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
  }
];
