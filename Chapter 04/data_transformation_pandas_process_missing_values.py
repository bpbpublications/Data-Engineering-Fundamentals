import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    "age": [25, np.nan, 35, 45, 22, 150],
    "salary": [50000, 60000, np.nan, 80000, 75000, 120000],
    "joined": [
        "2010-01-01",
        "2012-05-16",
        "NaN",
        "2014-08-19",
        "2015-03-25",
        "2016-07-13",
    ],
}
df = pd.DataFrame(data)

# Handling Missing Values

# Option 1: Fill missing values
df["age"].fillna(df["age"].mean(), inplace=True)  # Fill missing age with mean
df["salary"].fillna(
    df["salary"].median(), inplace=True
)  # Fill missing salary with median

# Option 2: Drop rows with missing values in specific columns
df.dropna(subset=["joined"], inplace=True)  # Drop rows where 'joined' is NaN

# Display the updated DataFrame
print(df)
