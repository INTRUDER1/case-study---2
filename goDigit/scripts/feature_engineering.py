# import pandas as pd
# import os

# # Load dataset

# file_path = os.path.join("..", "data", "insurance_cleaned.csv")  # Adjust path if needed
# if os.path.exists(file_path):
#     data = pd.read_csv(file_path)
# else:
#     raise FileNotFoundError(f"File not found: {file_path}")

# # Load the dataset
# df = pd.read_csv(file_path)

# # 1️⃣ Categorize BMI into Health Groups
# def categorize_bmi(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi < 25:
#         return "Normal"
#     elif 25 <= bmi < 30:
#         return "Overweight"
#     else:
#         return "Obese"

# data["bmi_category"] = data["bmi"].apply(categorize_bmi)

# # 2️⃣ Categorize Age into Groups
# def categorize_age(age):
#     if age < 31:
#         return "Young"
#     elif 31 <= age < 51:
#         return "Middle-Aged"
#     else:
#         return "Senior"

# data["age_group"] = data["age"].apply(categorize_age)

# # 3️⃣ Interaction Features
# data["bmi_smoker_interaction"] = data["bmi"] * data["smoker"].apply(lambda x: 1 if x == "yes" else 0)
# data["age_smoker_interaction"] = data["age"] * data["smoker"].apply(lambda x: 1 if x == "yes" else 0)

# # Save the enhanced dataset
# featured_file_path = os.path.join("..", "data", "insurance_featured.csv")
# df.to_csv(featured_file_path, index=False)

# # Display summary after cleaning
# print("\nCleaned Dataset Info:")
# print(df.info())
# print("\nFinal Duplicate Records:", df.duplicated().sum())
# print("\nFinal Dataset Shape:", df.shape)

# =================================== Modification - 1 ==================================================

import pandas as pd
import os

# Define file path
file_path = os.path.join("..", "data", "insurance_cleaned.csv")
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    raise FileNotFoundError(f"File not found: {file_path}")

# 1️⃣ Categorize BMI into Health Groups
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

data["bmi_category"] = data["bmi"].apply(categorize_bmi)

# 2️⃣ Categorize Age into Groups
def categorize_age(age):
    if age < 31:
        return "Young"
    elif 31 <= age < 51:
        return "Middle-Aged"
    else:
        return "Senior"

data["age_group"] = data["age"].apply(categorize_age)

# 3️⃣ Interaction Features
data["bmi_smoker_interaction"] = data["bmi"] * data["smoker"].apply(lambda x: 1 if x == "yes" else 0)
data["age_smoker_interaction"] = data["age"] * data["smoker"].apply(lambda x: 1 if x == "yes" else 0)

# Save the enhanced dataset
featured_file_path = os.path.join("..", "data", "insurance_featured.csv")
data.to_csv(featured_file_path, index=False)

# Display updated dataset preview
print("Feature Engineering Completed. Updated dataset saved as insurance_featured.csv")
print(data.head())
