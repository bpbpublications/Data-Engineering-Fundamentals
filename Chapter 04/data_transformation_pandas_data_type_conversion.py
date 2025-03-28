import pandas as pd
import numpy as np

# Sample Data
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 28, 35, 40],
    # Initially as string
    "salary": ["50000", "60000", "75000", "45000", "70000"],
    # Initially as string
    "joined": ["2022-01-10", "2021-05-15", "2023-06-20", "2020-12-05", "2019-07-30"],
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'joined' to datetime
df["joined"] = pd.to_datetime(df["joined"])

# Convert 'salary' to float
df["salary"] = df["salary"].astype("float64")

# Display the updated DataFrame
print(df.dtypes)
print(df)
