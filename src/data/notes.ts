export interface AcademicNote {
  id: string;
  title: string;
  rawTitle: string;
  slug: string;
  subject: string;
  order: number;
  orderBadge: string;
  summary: string;
  tags: string[];
}

export const notesData: AcademicNote[] = [
  {
    "id": "fundamentos-de-comunicacion-y-topologias-de-red",
    "title": "#01 - Fundamentos de Comunicación y Topologías de Red",
    "rawTitle": "Fundamentos de Comunicación y Topologías de Red",
    "slug": "fundamentos-de-comunicacion-y-topologias-de-red.html",
    "subject": "Comunicación de datos",
    "order": 1,
    "orderBadge": "#01",
    "summary": "La comunicación de datos permite el intercambio de información digital mediante protocolos normalizados que gestionan la transmisión, el enrutamiento y la integridad de los paquetes. Mediante el uso de conmutación de paquetes, diversas topologías de red y una jerarquía de ISP, los sistemas garantizan la conectividad global, optimizando el rendimiento a través de métricas críticas como latencia, ancho de banda y QoS.",
    "tags": [
      "académico"
    ]
  },
  {
    "id": "modelos-en-capas-y-protocolos-de-red",
    "title": "#02 - Modelos en Capas y Protocolos de Red",
    "rawTitle": "Modelos en Capas y Protocolos de Red",
    "slug": "modelos-en-capas-y-protocolos-de-red.html",
    "subject": "Comunicación de datos",
    "order": 2,
    "orderBadge": "#02",
    "summary": "Los modelos en capas estructuran la comunicación de red mediante jerarquías funcionales que facilitan la interoperabilidad y escalabilidad de sistemas heterogéneos. Mientras el modelo OSI actúa como marco conceptual, la pila TCP/IP constituye la arquitectura práctica de Internet, gestionando el encapsulamiento de datos, el direccionamiento IP y los mecanismos de transporte confiable o eficiente, optimizados actualmente mediante protocolos modernos como QUIC.",
    "tags": [
      "académico"
    ]
  },
  {
    "id": "senales-y-analisis-espectral",
    "title": "#03 - Señales y Análisis Espectral",
    "rawTitle": "Señales y Análisis Espectral",
    "slug": "senales-y-analisis-espectral.html",
    "subject": "Comunicación de datos",
    "order": 3,
    "orderBadge": "#03",
    "summary": "Las señales electromagnéticas constituyen la base física de la comunicación, permitiendo la transmisión de información mediante variaciones en el dominio del tiempo y la frecuencia. El análisis espectral, fundamentado en la serie de Fourier, facilita la gestión del ancho de banda y la propagación en el espacio, considerando factores críticos como las zonas de Fresnel y el efecto Doppler en sistemas inalámbricos.",
    "tags": [
      "académico"
    ]
  }
];
