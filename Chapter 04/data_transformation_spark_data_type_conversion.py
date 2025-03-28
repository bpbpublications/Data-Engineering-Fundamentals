from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import IntegerType, FloatType, StringType, DateType

# Initialize Spark Session
spark = SparkSession.builder.appName("DataFrameExample").getOrCreate()

# Sample Data
data = [
    ("Alice", 25, "50000", "2022-01-10"),
    ("Bob", 30, "60000", "2021-05-15"),
    ("Charlie", 28, "75000", "2023-06-20"),
    ("David", 35, "45000", "2020-12-05"),
    ("Eve", 40, "70000", "2019-07-30"),
]

# Define Schema
schema = ["name", "age", "salary", "joined"]

# Create Spark DataFrame
df = spark.createDataFrame(data, schema=schema)

# Convert 'joined' to DateType and 'salary' to FloatType
df = df.withColumn("joined", to_date(col("joined"), "yyyy-MM-dd")).withColumn(
    "salary", col("salary").cast(FloatType())
)

# Show DataFrame
df.printSchema()
df.show()
