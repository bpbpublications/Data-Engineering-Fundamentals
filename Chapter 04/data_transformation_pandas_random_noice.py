import pandas as pd
import numpy as np

# Original dataset
df = pd.DataFrame({"feature": [1.2, 2.4, 3.1, 4.6, 5.0]})

# Data Augmentation: Add random noise to the original feature
# Generate random noise with mean 0 and std deviation 0.1
noise = np.random.normal(0, 0.1, size=len(df))
# Create an augmented feature by adding noise
df["augmented_feature"] = df["feature"] + noise

# Display the augmented dataset
print(df)
