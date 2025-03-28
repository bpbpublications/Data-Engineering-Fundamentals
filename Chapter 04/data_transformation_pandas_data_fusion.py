import pandas as pd

# Example DataFrames
df_transactions = pd.DataFrame(
    {"customer_id": [1, 2, 3], "transaction_amount": [100, 200, 150]}
)

df_social_media = pd.DataFrame(
    {"customer_id": [1, 2, 3], "sentiment_score": [0.8, 0.6, 0.9]}
)

# Data Fusion: Merging the two DataFrames on customer_id
df_fused = pd.merge(df_transactions, df_social_media, on="customer_id")

# Display the fused dataset
print(df_fused)
