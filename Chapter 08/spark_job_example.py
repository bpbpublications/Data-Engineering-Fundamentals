from pyspark.sql import SparkSession

# Create a Spark Session
spark = SparkSession.builder.appName("Spark Job Stage Task Example").getOrCreate()
# Read a CSV file - this is a transformation and doesn't trigger a job
data = spark.read.option("header", "true").csv("path/to/your/file.csv")
# Perform a transformation to create a new DataFrame with an added column
transformed_data = data.withColumn("new_column", data["existing_column"] * 2)
# Now, call an action - this triggers a Spark job
result = transformed_data.count()
print(result)
spark.stop()
