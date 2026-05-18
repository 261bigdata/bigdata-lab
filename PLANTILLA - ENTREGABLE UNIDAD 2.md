# PLANTILLA - ENTREGABLE UNIDAD 2

## Unidad 2: Sistema Big Data en tiempo real

**Producto de la unidad:** Pipeline streaming en Spark para ML/BI a escala y en tiempo real.

**Alcance de esta plantilla:** La Unidad 2 abarca únicamente las sesiones 6, 7 y 8.  
Las sesiones 9, 10 y 11 se reservan para la Unidad 3.

---

## Datos generales

**Curso:** Big Data  
**Unidad:** 2  
**Estudiante / equipo:** ______________________________  
**Fecha:** ____ / ____ / ______  
**Docente:** ______________________________  

---

## Entregable esperado

El estudiante/equipo debe presentar un pipeline streaming funcional basado en Kafka y Spark Structured Streaming, acompañado de evidencias técnicas, métricas operativas y una propuesta básica de observabilidad, costos y escalado.

---

## Sesiones de la Unidad 2

| Sesión | Tema | Contenido | Actividad práctica de sesión | Actividad de aprendizaje autónomo | Evidencia esperada |
|---|---|---|---|---|---|
| S6 | Kafka para ingesta en tiempo real | Apache Kafka: tópicos, productores, consumidores y patrones de ingesta en tiempo real. | Crear un tópico y ejecutar productor/consumidor. Definir el esquema de evento y el patrón de ingesta para el caso. | Documentar el contrato de evento: campos, tipos, ejemplos y estrategia de particionado del tópico. | Capturas o logs del tópico, productor, consumidor y ejemplo de mensaje. |
| S7 | Procesamiento en Streaming con Spark | Spark Structured Streaming: micro-batch, ventanas, watermarking y semántica de entrega. | Implementar un stream con ventanas y watermarking. Medir comportamiento del pipeline: latencia y throughput. | Ajustar parámetros como trigger y watermark. Registrar efectos en latencia/throughput mediante una tabla comparativa. | Notebook, script o evidencia de ejecución del stream con resultados medidos. |
| S8 | Observabilidad, costos y escalado | Métricas de operación, logging estructurado, alertas, estimación de recursos, costos y buenas prácticas de escalado. | Instrumentar el pipeline con métricas de latencia, throughput y errores. Definir alertas, umbrales y estimación de recursos/costos. | Proponer un tablero mínimo de operación y redactar una nota operativa con riesgos, backpressure y plan de escalado/optimización. | Métricas, logs, propuesta de dashboard, alertas, estimación de costos y plan operativo. |

---

## Estructura sugerida del informe

### 1. Resumen ejecutivo

Describir brevemente el objetivo del pipeline streaming, el problema abordado y el resultado obtenido.

### 2. Arquitectura del pipeline

Incluir una explicación de los componentes principales:

- Fuente de datos.
- Kafka como sistema de ingesta.
- Spark Structured Streaming como motor de procesamiento.
- Salida del pipeline para BI, monitoreo o almacenamiento.
- Supuestos técnicos de ejecución.

### 3. Ingesta en tiempo real con Kafka

Documentar:

- Nombre del tópico.
- Número de particiones.
- Estrategia de particionado.
- Productor utilizado.
- Consumidor utilizado.
- Ejemplo de evento generado.

#### Contrato de evento

| Campo | Tipo de dato | Descripción | Ejemplo |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### 4. Procesamiento en streaming con Spark

Documentar:

- Fuente de lectura desde Kafka.
- Transformaciones aplicadas.
- Uso de ventanas.
- Uso de watermarking.
- Configuración de trigger.
- Salida del stream.

#### Parámetros utilizados

| Parámetro | Valor | Justificación |
|---|---|---|
| Trigger | | |
| Watermark | | |
| Ventana | | |
| Output mode | | |
| Checkpoint | | |

### 5. Métricas de rendimiento

Registrar resultados de pruebas controladas.

| Prueba | Trigger | Watermark | Throughput | Latencia | Observaciones |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### 6. Observabilidad del pipeline

Describir cómo se monitorea el pipeline.

Incluir:

- Métricas clave.
- Logs generados.
- Errores identificados.
- Umbrales de alerta.
- Propuesta de dashboard mínimo.

#### Dashboard mínimo propuesto

| Métrica | Descripción | Umbral sugerido | Frecuencia de revisión |
|---|---|---|---|
| Latencia | | | |
| Throughput | | | |
| Errores | | | |
| Backpressure | | | |

### 7. Costos y escalado

Estimar los recursos necesarios para operar el pipeline.

Considerar:

- CPU.
- Memoria.
- Número de particiones Kafka.
- Número de ejecutores Spark.
- Volumen de datos esperado.
- Riesgos de backpressure.
- Estrategia de escalado.

#### Estimación de recursos

| Recurso | Estimación | Justificación |
|---|---|---|
| CPU | | |
| Memoria | | |
| Particiones Kafka | | |
| Ejecutores Spark | | |
| Almacenamiento | | |

### 8. Evidencias

Adjuntar o referenciar evidencias como:

- Capturas de ejecución.
- Logs.
- Salidas de consola.
- Fragmentos de código.
- Resultados de pruebas.
- Tablas de métricas.

### 9. Conclusiones

Resumir:

- Qué se logró implementar.
- Qué limitaciones se encontraron.
- Qué mejoras se proponen.
- Cómo se podría preparar el pipeline para una siguiente etapa con ML distribuido.

---

## Checklist de entrega

| Criterio | Cumple | Observaciones |
|---|---|---|
| Se creó y probó un tópico Kafka. | [ ] | |
| Se ejecutó productor y consumidor. | [ ] | |
| Se documentó el contrato de evento. | [ ] | |
| Se implementó un pipeline con Spark Structured Streaming. | [ ] | |
| Se usaron ventanas y watermarking. | [ ] | |
| Se midió latencia y throughput. | [ ] | |
| Se propuso una estrategia de observabilidad. | [ ] | |
| Se definieron métricas, alertas y umbrales. | [ ] | |
| Se estimaron costos o recursos de operación. | [ ] | |
| Se propuso una estrategia de escalado. | [ ] | |
| Se adjuntaron evidencias técnicas. | [ ] | |

---

## Producto final de Unidad 2

Pipeline streaming Kafka + Spark con métricas de rendimiento, documentación operativa, propuesta de observabilidad y estimación básica de costos/escalado.
