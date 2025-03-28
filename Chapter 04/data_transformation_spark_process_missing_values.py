from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, when

# Create Spark session
spark = SparkSession.builder.appName("DataCleaning").getOrCreate()

# Sample DataFrame
data = [
    (25, 50000, "2010-01-01"),
    (None, 60000, "2012-05-16"),
    (35, None, None),
    (45, 80000, "2014-08-19"),
    (22, 75000, "2015-03-25"),
    (150, 120000, "2016-07-13"),
]  # 150 is an outlier

columns = ["age", "salary", "joined"]
df = spark.createDataFrame(data, columns)

# Handling Missing Values

# Option 1: Fill missing values
mean_age = df.select(mean(col("age"))).collect()[0][0]
median_salary = df.approxQuantile("salary", [0.5], 0)[0]  # Approx median for salary

df = df.withColumn("age", when(col("age").isNull(), mean_age).otherwise(col("age")))
df = df.withColumn(
    "salary", when(col("salary").isNull(), median_salary).otherwise(col("salary"))
)

# Option 2: Drop rows with missing values in specific columns
df = df.na.drop(subset=["joined"])  # Drop rows where 'joined' is NULL

# Show the updated DataFrame
df.show()
