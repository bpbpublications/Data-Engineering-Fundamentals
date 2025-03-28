from pyspark.sql import SparkSession
from pyspark.sql.functions import col, randn

# Create Spark session
spark = SparkSession.builder.appName("DataAugmentation").getOrCreate()

# Original dataset
data = [(1.2,), (2.4,), (3.1,), (4.6,), (5.0,)]
df = spark.createDataFrame(data, ["feature"])

# Data Augmentation: Add random noise to the 'feature' column
df = df.withColumn(
    "augmented_feature", col("feature") + randn() * 0.1
)  # Add Gaussian noise with std deviation 0.1

# Show the augmented dataset
df.show()
