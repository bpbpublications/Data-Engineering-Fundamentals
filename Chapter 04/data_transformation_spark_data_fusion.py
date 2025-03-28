from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("DataAugmentation").getOrCreate()
# Sample DataFrames
data_transactions = [(1, 100), (2, 200), (3, 150)]
data_social_media = [(1, 0.8), (2, 0.6), (3, 0.9)]

df_transactions = spark.createDataFrame(
    data_transactions, ["customer_id", "transaction_amount"]
)
df_social_media = spark.createDataFrame(
    data_social_media, ["customer_id", "sentiment_score"]
)

# Data Fusion: Perform an inner join on customer_id
df_fused = df_transactions.join(df_social_media, "customer_id")

# Show the fused dataset
df_fused.show()
