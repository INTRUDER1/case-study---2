# import pandas as pd
# import os

# # Define file path
# file_path = os.path.join("..", "data", "insurance.csv")

# # Load the dataset
# df = pd.read_csv(file_path)

# # Display dataset info
# print("Dataset Info:")
# print(df.info())

# # Display first 5 rows
# print("\nFirst 5 Rows:")
# print(df.head())

# # Check for missing values
# print("\nMissing Values:")
# print(df.isnull().sum())

# # Check for duplicate records
# print("\nDuplicate Records:", df.duplicated().sum())

# # Display basic statistics
# print("\nSummary Statistics:")
# print(df.describe(include='all'))


#  Modifying - remove Duplicates
#              Standardize Categorical Data (Sex, smoker, region)
#              Handle Outliers in bmi & charges
#              Save the Cleaned Dataset for Further Analysis


import pandas as pd
import os

# Define file path
file_path = os.path.join("..", "data", "insurance.csv")

# Load the dataset
df = pd.read_csv(file_path)

# Remove Duplicate Records
df.drop_duplicates(inplace=True)

# Standardize Categorical Columns
df['sex'] = df['sex'].str.lower().str.strip()
df['smoker'] = df['smoker'].str.lower().str.strip()
df['region'] = df['region'].str.lower().str.strip()

# Handle Outliers (Using IQR Method for bmi & charges)
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df

df = remove_outliers(df, 'bmi')
df = remove_outliers(df, 'charges')

# Save Cleaned Dataset
cleaned_file_path = os.path.join("..", "data", "insurance_cleaned.csv")
df.to_csv(cleaned_file_path, index=False)

# Display summary after cleaning
print("\nCleaned Dataset Info:")
print(df.info())
print("\nFinal Duplicate Records:", df.duplicated().sum())
print("\nFinal Dataset Shape:", df.shape)
