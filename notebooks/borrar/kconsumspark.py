from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, LongType, DoubleType

spark = SparkSession.builder \
    .appName("KafkaSparkStreamingOrdenes") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

schema = StructType([
    StructField("tipoEvento", StringType(), True),
    StructField("ordenId", LongType(), True),
    StructField("total", DoubleType(), True),
    StructField("estado", StringType(), True),
    StructField("origen", StringType(), True),
    StructField("timestamp", LongType(), True)
])

df_kafka = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "ec-kafka:9092") \
    .option("subscribe", "orden-eventos") \
    .option("startingOffsets", "earliest") \
    .load()

df_value = df_kafka.selectExpr("CAST(value AS STRING) AS value")

df_parsed = df_value.select(
    from_json(col("value"), schema).alias("data")
).select("data.*")

df_validado = df_parsed.filter(
    col("tipoEvento").isNotNull() &
    col("ordenId").isNotNull()
)

df_transformed = df_validado.filter(col("total") > 100)

query_console = df_transformed.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query_console.awaitTermination()