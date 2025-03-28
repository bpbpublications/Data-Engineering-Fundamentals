import pandas as pd

# Input DataFrame
data = {"Age": [25, 30, 28, 35, 35], "Salary": [
    50000, 60000, 500000, 45000, 70000]}
df = pd.DataFrame(data)


# Function to remove outliers using IQR
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)  # First quartile (25th percentile)
    Q3 = df[column].quantile(0.75)  # Third quartile (75th percentile)
    IQR = Q3 - Q1  # Interquartile range
    lower_bound = Q1 - 1.5 * IQR  # Lower bound for outliers
    upper_bound = Q3 + 1.5 * IQR  # Upper bound for outliers
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


# Remove outliers for Salary
df_no_outliers = remove_outliers_iqr(df, "Salary")

print("Original DataFrame:")
print(df)
print("\nDataFrame after removing outliers:")
print(df_no_outliers)
