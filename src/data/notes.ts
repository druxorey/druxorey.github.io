export interface AcademicNote {
  id: string;
  title: string;
  rawTitle: string;
  slug: string;
  subject: string;
  semester: number;
  unit: number;
  order: number;
  orderBadge: string;
  summary: string;
  tags: string[];
}

export const notesData: AcademicNote[] = [
  {
    "id": "signos-vitales",
    "title": "Signos Vitales",
    "rawTitle": "Signos Vitales",
    "slug": "signos-vitales.html",
    "subject": "Primeros Auxilios",
    "semester": 6,
    "unit": 1,
    "order": 1,
    "orderBadge": "1.1",
    "summary": "Los signos vitales son mediciones fisiológicas objetivas, distintas de los síntomas subjetivos, que evalúan el estado básico del organismo regulado por los sistemas nervioso y endocrino. Abarcan signos primarios (pulso, presión arterial, ventilación y temperatura) y signos secundarios (coloración, llenado capilar, oximetría, respuesta ocular y glicemia) para detectar oportunamente alteraciones críticas y orientar la atención en primeros auxilios.",
    "tags": []
  },
  {
    "id": "fundamentos-de-comunicacion-y-topologias-de-red",
    "title": "Fundamentos de Comunicación y Topologías de Red",
    "rawTitle": "Fundamentos de Comunicación y Topologías de Red",
    "slug": "fundamentos-de-comunicacion-y-topologias-de-red.html",
    "subject": "Comunicacion de Datos",
    "semester": 5,
    "unit": 1,
    "order": 1,
    "orderBadge": "1.1",
    "summary": "La comunicación de datos constituye el intercambio estructurado de información digital mediante la transformación de bits en señales físicas, regido por protocolos que aseguran la sintaxis, semántica y temporización. Este proceso integra emisor, receptor, mensaje, medio y protocolo, organizándose bajo diversas topologías físicas y arquitecturas lógicas como cliente-servidor o SDN, optimizando la conectividad y gestión eficiente de recursos en redes de distinta cobertura.",
    "tags": []
  },
  {
    "id": "modelos-en-capas-y-rendimiento",
    "title": "Modelos en Capas y Rendimiento",
    "rawTitle": "Modelos en Capas y Rendimiento",
    "slug": "modelos-en-capas-y-rendimiento.html",
    "subject": "Comunicacion de Datos",
    "semester": 5,
    "unit": 1,
    "order": 2,
    "orderBadge": "1.2",
    "summary": "La arquitectura en capas organiza la comunicación de datos mediante una abstracción jerárquica que descompone procesos complejos en módulos independientes. A través de modelos como OSI y la pila TCP/IP, se estandariza el encapsulamiento de información, garantizando la interoperabilidad entre sistemas heterogéneos. La eficacia de estas redes se evalúa mediante métricas de rendimiento y QoS, asegurando la entrega, exactitud y oportunidad de los datos transmitidos.",
    "tags": []
  },
  {
    "id": "analisis-espectral-de-las-senales-fisicas",
    "title": "Análisis Espectral de las Señales Físicas",
    "rawTitle": "Análisis Espectral de las Señales Físicas",
    "slug": "analisis-espectral-de-las-senales-fisicas.html",
    "subject": "Comunicacion de Datos",
    "semester": 5,
    "unit": 2,
    "order": 1,
    "orderBadge": "2.1",
    "summary": "Las señales físicas transforman los datos abstractos en perturbaciones electromagnéticas continuas o discretas capaces de viajar a través de un medio de transmisión. Su comportamiento se analiza mediante la dualidad entre el dominio del tiempo y el dominio de la frecuencia, utilizando el análisis espectral para descomponer formas de onda complejas. Asimismo, la calidad de la propagación inalámbrica depende del despeje geométrico en las zonas de Fresnel y de la compensación del efecto Doppler.",
    "tags": []
  },
  {
    "id": "modulacion-deterioro-y-capacidad-del-canal",
    "title": "Modulación, Deterioro y Capacidad del Canal",
    "rawTitle": "Modulación, Deterioro y Capacidad del Canal",
    "slug": "modulacion-deterioro-y-capacidad-del-canal.html",
    "subject": "Comunicacion de Datos",
    "semester": 5,
    "unit": 2,
    "order": 2,
    "orderBadge": "2.2",
    "summary": "La modulación digital adapta flujos de bits binarios a ondas portadoras analógicas de alta frecuencia para superar los límites físicos de los canales de transmisión. Mediante técnicas como ASK, FSK, PSK y QAM, junto con arquitecturas avanzadas como OFDM, se optimiza la eficiencia espectral frente a factores de deterioro como la atenuación y el ruido térmico, cuyos límites teóricos son gobernados por los teoremas de Nyquist y Shannon-Hartley.",
    "tags": []
  },
  {
    "id": "principios-del-conteo-y-palomar",
    "title": "Principios del Conteo y Palomar",
    "rawTitle": "Principios del Conteo y Palomar",
    "slug": "principios-del-conteo-y-palomar.html",
    "subject": "Probabilidad y Estadistica",
    "semester": 4,
    "unit": 1,
    "order": 1,
    "orderBadge": "1.1",
    "summary": "Los principios del conteo determinan analíticamente la cardinalidad de un espacio muestral discreto evitando la búsqueda exhaustiva. Mediante las reglas de la suma, del producto y de la división, junto con el principio de inclusión-exclusión y el principio del palomar, estas herramientas fundamentan el modelo clásico de probabilidad, dimensionan espacios de estados y establecen cotas de colisión en sistemas computacionales.",
    "tags": []
  }
];
