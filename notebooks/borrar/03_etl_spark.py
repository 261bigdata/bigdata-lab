# ETL Spark
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, sum

spark = SparkSession.builder.appName("ETL").getOrCreate()

ventas = spark.read.csv("/opt/data/ventas.csv", header=True, inferSchema=True)
clientes = spark.read.csv("/opt/data/clientes.csv", header=True, inferSchema=True)

df = ventas.join(clientes, "cliente_id")

window = Window.partitionBy("cliente_id").orderBy("fecha")

df = df.withColumn("rank", row_number().over(window))
df = df.withColumn("acum", sum("monto").over(window))

df.show()

df.write.mode("overwrite").parquet("/opt/artifacts/output")
