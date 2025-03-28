import pandas as pd
# Sample dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Income': [40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Numerical binning for Age column
bins = [20, 30, 40, 50, 60, 70, 80]
labels = ['20-29', '30-39', '40-49', '50-59', '60-69', '70+']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# Display DataFrame after binning
print("DataFrame after binning:")
print(df)