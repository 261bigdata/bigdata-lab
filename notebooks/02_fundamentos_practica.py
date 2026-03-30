# Fundamentos Spark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Fundamentos").getOrCreate()

df = spark.read.csv("/opt/data/ventas.csv", header=True, inferSchema=True)
df.show()

df2 = df.filter(df["monto"] > 100)
df2.show()

df2.explain(True)
