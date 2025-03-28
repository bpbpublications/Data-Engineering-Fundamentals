import pandas as pd
import numpy as np

# Dataset with missing values
df = pd.DataFrame({"time": [1, 2, 3, 4, 5], "value": [
                  10, np.nan, 15, np.nan, 20]})

# Data Interpolation: Filling missing values using linear interpolation
df["interpolated_value"] = df["value"].interpolate()

# Display the dataset with interpolated values
print(df)
