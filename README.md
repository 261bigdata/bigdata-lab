# bigdata-lab

Repositorio de laboratorio para trabajar con notebooks, PySpark, datos de ejemplo y prácticas de procesamiento Big Data.

Su papel es servir como entorno de trabajo para ejercicios de fundamentos, ETL y streaming, tanto de forma independiente como integrado con Kafka cuando la práctica lo requiera.

## Estructura del proyecto

- `artifacts/`: archivos generados por procesos o ejecuciones
- `data/`: datos de ejemplo para prácticas y ejercicios
- `docker/`: archivos para levantar el entorno con Docker
- `notebooks/`: notebooks y scripts Python para prácticas y experimentos

## Requisitos

- Docker
- Python local es opcional
- Apache Spark local es opcional si no usas Docker, porque el contenedor ya incluye `pyspark`

## Uso rápido

Ubícate en:

```powershell
cd C:\261bigdata\bigdata-lab\docker
```

Levanta el laboratorio base:

```bash
docker compose up --build
```

Luego accede a:

- Jupyter: `http://localhost:8888`
- Spark UI: `http://localhost:4040`

## Levantar el laboratorio con Docker

Desde la carpeta `docker/`, ejecuta:

```bash
docker compose up --build
```

Esto monta en el contenedor:

- notebooks en `/opt/notebooks`
- datos en `/opt/data`
- artefactos en `/opt/artifacts`

Y expone los puertos:

- `8888`: Jupyter
- `4040`: Spark UI

## Modos de uso

### Modo 1. Laboratorio independiente

Usa:

```bash
docker compose up --build
```

Este modo sirve para:

- notebooks de fundamentos
- ETL con Spark
- ejercicios con archivos locales
- pruebas sin depender de Kafka

### Modo 2. Laboratorio integrado con Kafka

Si quieres conectar `bigdata-lab` al Kafka de `dev`, primero asegúrate de que exista la red externa `ec-kafka-dev-net` y luego ejecuta:

```bash
docker compose -f docker-compose.yml -f docker-compose.kafka.yml up --build
```

Este modo sirve para:

- consumir eventos Kafka desde Spark
- probar flujos de streaming
- trabajar con el broker interno:

```text
ec-kafka:9092
```

## Notebooks principales

En `notebooks/` encontrarás, entre otros:

- `01_arquitecturas_big_data.ipynb`
- `02_fundamentos_practica.ipynb`
- `03_etl_spark.ipynb`
- `04_hdfs_formatos.ipynb`
- `07_spark_streaming_consumer_ordenes.ipynb`

## Archivos Docker

En la carpeta `docker/` se usan estos archivos:

- `docker-compose.yml`: compose base para levantar `bigdata-lab` de forma independiente
- `docker-compose.kafka.yml`: override opcional para conectar `bigdata-lab` al Kafka de `dev`
- `Dockerfile`: imagen base del contenedor

## Créditos

Material de apoyo para cursos y talleres de Big Data.

Para dudas o sugerencias, abre un issue o contacta al responsable del curso o con Angel Sullon
