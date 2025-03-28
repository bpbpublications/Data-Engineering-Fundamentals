from pyspark.sql import SparkSession
from pyspark.sql.functions import col, last
from pyspark.sql.window import Window

# Create Spark session
spark = SparkSession.builder.appName("DataAugmentation").getOrCreate()
# Sample DataFrame with missing values
data = [(1, 10), (2, None), (3, 15), (4, None), (5, 20)]
df = spark.createDataFrame(data, ["time", "value"])

# Data Interpolation: Filling missing values using forward fill (last observed value)
window = Window.orderBy("time")
df_interpolated = df.withColumn(
    "interpolated_value", last(col("value"), True).over(window)
)

# Show the dataset with interpolated values
df_interpolated.show()
