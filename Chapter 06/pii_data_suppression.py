import pandas as pd
# Sample dataset with PII
data = {
    'Name': ['John Doe', 'Alice Smith', 'Bob Johnson'],
    'Email': ['john@example.com', 'alice@example.com', 'bob@example.com'],
    'Phone': ['123-456-7890', '987-654-3210', '555-555-5555'],
    'Age': [30, 25, 40],
    'Gender': ['Male', 'Female', 'Male']
}
# Convert data to DataFrame
df = pd.DataFrame(data)
# Dropping PII columns (Name, Email, Phone)
df_dropped_pii = df.drop(columns=['Name', 'Email', 'Phone'])