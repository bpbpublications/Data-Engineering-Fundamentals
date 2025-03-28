from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("SparkPartitioningExample").getOrCreate()

# Sample DataFrame
data = [
    ("John", 25, "New York"),
    ("Alice", 30, "San Francisco"),
    ("Bob", 35, "New York"),
    ("David", 40, "Los Angeles"),
    ("Eva", 28, "San Francisco"),
]
columns = ["name", "age", "city"]
df = spark.createDataFrame(data, columns)

# Write the DataFrame partitioned by the 'city' column
df.write.mode("overwrite").partitionBy("city").parquet("/tmp/partitioned_data")

# Display the DataFrame
df.show()

# Stop the Spark session
spark.stop()
