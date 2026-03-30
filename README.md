# bigdata-lab

Este repositorio contiene materiales, notebooks y recursos para prácticas y aprendizaje de arquitecturas y fundamentos de Big Data.

## Estructura del proyecto

- **artifacts/**: Archivos generados por procesos o ejecuciones.
  - **output/**: Resultados de procesos, como archivos de éxito (_SUCCESS).
- **data/**: Conjunto de datos de ejemplo para prácticas y ejercicios.
  - `biblia_ntv_.csv`, `clientes.csv`, `ventas.csv`
- **docker/**: Archivos para la configuración y despliegue de entornos con Docker.
  - `docker-compose.yml`, `Dockerfile`
- **notebooks/**: Notebooks y scripts Python para prácticas y experimentos.
  - `01_arquitecturas_big_data.ipynb`, `02_fundamentos_practica.ipynb`, `03_etl_spark.ipynb`, etc.

## Requisitos

- Python 3.x
- Docker
- Apache Spark (opcional, recomendado para notebooks de ETL)

## Uso rápido

1. Clona este repositorio:
   ```bash
   git clone <url-del-repo>
   ```
2. Instala los requisitos necesarios (puedes usar Docker para facilitar la configuración).
3. Abre los notebooks en Jupyter o VS Code para comenzar a trabajar.

## Levantar el servidor con Docker

Desde la carpeta `docker/`, ejecuta:

```bash
# Construir la imagen (solo la primera vez o si hay cambios)
docker compose build

# Levantar el servidor
# (esto inicia Jupyter Notebook en http://localhost:8888)
docker compose up
```

Esto montará los notebooks, datos y artefactos en el contenedor y expondrá los puertos 8888 (Jupyter) y 4040 (Spark UI).

## Créditos

Material de apoyo para cursos y talleres de Big Data.

---

Para dudas o sugerencias, abre un issue o contacta al responsable del curso.