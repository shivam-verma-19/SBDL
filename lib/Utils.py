import os
from pyspark.sql import SparkSession

def get_spark_session(env):
    # Force-disable Spark Connect
    os.environ["PYSPARK_ENABLE_CONNECT"] = "0"

    builder = (
        SparkSession.builder
        .appName("SBDL")
        .enableHiveSupport()
    )

    if env.upper() == "LOCAL":
        builder = builder \
            .master("local[2]") \
            .config("spark.driver.extraJavaOptions", "-Dlog4j.configuration=file:log4j.properties")

    spark = builder.getOrCreate()
    return spark
