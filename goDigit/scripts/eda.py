# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os

# # Load cleaned dataset
# file_path = os.path.join("..", "data", "insurance_cleaned.csv")
# df = pd.read_csv(file_path)

# # 1. Distribution of Age, BMI, and Charges
# plt.figure(figsize=(12, 4))
# plt.subplot(1, 3, 1)
# sns.histplot(df['age'], bins=20, kde=True, color='blue')
# plt.title("Age Distribution")

# plt.subplot(1, 3, 2)
# sns.histplot(df['bmi'], bins=20, kde=True, color='green')
# plt.title("BMI Distribution")

# plt.subplot(1, 3, 3)
# sns.histplot(df['charges'], bins=20, kde=True, color='red')
# plt.title("Charges Distribution")

# plt.tight_layout()
# plt.show()

# # 2️. Correlation Heatmap
# plt.figure(figsize=(6, 4))
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
# plt.title("Correlation Heatmap")
# plt.show()

# # 3️. Average Charges by Smoker Status
# plt.figure(figsize=(6, 4))
# sns.barplot(x="smoker", y="charges", data=df, palette="pastel")
# plt.title("Average Charges by Smoking Status")
# plt.show()

# # 4️. Average Charges by Region
# plt.figure(figsize=(6, 4))
# sns.barplot(x="region", y="charges", data=df, palette="muted")
# plt.title("Average Charges by Region")
# plt.show()

#=========================== Modification in the code - 1 =================================

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import os

# # Load the cleaned dataset

# file_path = os.path.join("..", "data", "insurance_cleaned.csv") 
# if os.path.exists(file_path):
#     data = pd.read_csv(file_path)
# else:
#     raise FileNotFoundError("The file does not exist: {file_path}")


# # Check dataset information
# print("Dataset Info:")
# print(data.info())

# # Statistical Summary
# print("\nSummary Statistics:")
# print(data.describe())

# # Checking for duplicates
# duplicate_count = data.duplicated().sum()
# print(f"\nDuplicate Records: {duplicate_count}")

# # Drop any remaining duplicates if present
# data = data.drop_duplicates()

# # ========== VISUALIZATIONS ==========

# # 1️⃣ Distribution of Charges, Age, and BMI
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# # Age Distribution
# sns.histplot(data['age'], bins=20, kde=True, color='blue', ax=axes[0])
# axes[0].set_title("Age Distribution")
# axes[0].set_ylabel("Count")

# # BMI Distribution
# sns.histplot(data['bmi'], bins=20, kde=True, color='green', ax=axes[1])
# axes[1].set_title("BMI Distribution")

# # Charges Distribution
# sns.histplot(data['charges'], bins=20, kde=True, color='red', ax=axes[2])
# axes[2].set_title("Charges Distribution")

# plt.tight_layout()
# plt.show()

# # 2️⃣ Impact of Smoking on Charges
# plt.figure(figsize=(6, 4))
# sns.boxplot(x=data['smoker'], y=data['charges'], palette=['blue', 'red'])
# plt.title("Insurance Charges: Smokers vs. Non-Smokers")
# plt.xlabel("Smoker")
# plt.ylabel("Charges")
# plt.show()

# # 3️⃣ BMI vs. Charges (Colored by Smoking Status)
# plt.figure(figsize=(6, 4))
# sns.scatterplot(x=data['bmi'], y=data['charges'], hue=data['smoker'], alpha=0.7)
# plt.title("BMI vs. Insurance Charges")
# plt.xlabel("BMI")
# plt.ylabel("Charges")
# plt.legend(title="Smoker")
# plt.show()

# # 4️⃣ Age vs. Charges (Colored by Smoking Status)
# plt.figure(figsize=(6, 4))
# sns.scatterplot(x=data['age'], y=data['charges'], hue=data['smoker'], alpha=0.7)
# plt.title("Age vs. Insurance Charges")
# plt.xlabel("Age")
# plt.ylabel("Charges")
# plt.legend(title="Smoker")
# plt.show()

# # 5️⃣ Charges Comparison by Gender & Region
# plt.figure(figsize=(10, 4))

# # Gender comparison
# plt.subplot(1, 2, 1)
# sns.boxplot(x=data['sex'], y=data['charges'], palette='coolwarm')
# plt.title("Insurance Charges by Gender")

# # Region comparison
# plt.subplot(1, 2, 2)
# sns.boxplot(x=data['region'], y=data['charges'], palette='viridis')
# plt.title("Insurance Charges by Region")

# plt.tight_layout()
# plt.show()

# # ========== CORRELATION ANALYSIS ==========
# plt.figure(figsize=(8, 5))
# sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
# plt.title("Correlation Matrix")
# plt.show()

# ============================= Modification - 2 ==================================

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import os

# # Load the cleaned dataset
# file_path = os.path.join("..", "data", "insurance_cleaned.csv")  # Adjust path if needed
# if os.path.exists(file_path):
#     data = pd.read_csv(file_path)
# else:
#     raise FileNotFoundError(f"File not found: {file_path}")

# # Checking dataset information
# print("Dataset Info:")
# print(data.info())

# # Convert categorical variables to numerical for correlation analysis
# data_numeric = data.copy()
# data_numeric['sex'] = data_numeric['sex'].map({'male': 0, 'female': 1})
# data_numeric['smoker'] = data_numeric['smoker'].map({'no': 0, 'yes': 1})
# data_numeric = pd.get_dummies(data_numeric, columns=['region'])  # One-hot encode region

# # 1️⃣ Distribution of Charges, Age, and BMI
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# sns.histplot(data['age'], bins=20, kde=True, ax=axes[0])
# axes[0].set_title("Age Distribution")

# sns.histplot(data['bmi'], bins=20, kde=True, ax=axes[1])
# axes[1].set_title("BMI Distribution")

# sns.histplot(data['charges'], bins=20, kde=True, ax=axes[2])
# axes[2].set_title("Charges Distribution")

# plt.tight_layout()
# plt.show()

# # 2️⃣ Impact of Smoking on Charges
# plt.figure(figsize=(6, 4))
# sns.boxplot(x="smoker", y="charges", hue="smoker", data=data, palette=['blue', 'red'], legend=False)
# plt.title("Insurance Charges: Smokers vs. Non-Smokers")
# plt.xlabel("Smoker")
# plt.ylabel("Charges")
# plt.show()

# # 3️⃣ BMI vs. Charges (Colored by Smoking Status)
# plt.figure(figsize=(6, 4))
# sns.scatterplot(x=data['bmi'], y=data['charges'], hue=data['smoker'], alpha=0.7)
# plt.title("BMI vs. Insurance Charges")
# plt.xlabel("BMI")
# plt.ylabel("Charges")
# plt.legend(title="Smoker")
# plt.show()

# # 4️⃣ Age vs. Charges (Colored by Smoking Status)
# plt.figure(figsize=(6, 4))
# sns.scatterplot(x=data['age'], y=data['charges'], hue=data['smoker'], alpha=0.7)
# plt.title("Age vs. Insurance Charges")
# plt.xlabel("Age")
# plt.ylabel("Charges")
# plt.legend(title="Smoker")
# plt.show()

# # 5️⃣ Charges Comparison by Gender & Region
# plt.figure(figsize=(10, 4))

# # Gender comparison
# plt.subplot(1, 2, 1)
# sns.boxplot(x="sex", y="charges", hue="sex", data=data, palette="coolwarm", legend=False)
# plt.title("Insurance Charges by Gender")

# # Region comparison
# plt.subplot(1, 2, 2)
# sns.boxplot(x="region", y="charges", hue="region", data=data, palette="viridis", legend=False)
# plt.title("Insurance Charges by Region")

# plt.tight_layout()
# plt.show()

# # 6️⃣ Correlation Analysis (Using Numeric Data)
# plt.figure(figsize=(8, 5))
# sns.heatmap(data_numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
# plt.title("Correlation Matrix")
# plt.show()


# =============================================== Modification - 3 ===========================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the featured dataset
file_path = os.path.join("..", "data", "insurance_featured.csv")
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    raise FileNotFoundError(f"File not found: {file_path}")

# Checking dataset information
print("Dataset Info:")
print(data.info())

# Convert categorical variables to numerical for correlation analysis
data_numeric = data.copy()
data_numeric['sex'] = data_numeric['sex'].map({'male': 0, 'female': 1})
data_numeric['smoker'] = data_numeric['smoker'].map({'no': 0, 'yes': 1})
data_numeric = pd.get_dummies(data_numeric, columns=['region', 'bmi_category', 'age_group'])

# 1️⃣ Distribution of Charges, Age, and BMI
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.histplot(data['age'], bins=20, kde=True, ax=axes[0])
axes[0].set_title("Age Distribution")

sns.histplot(data['bmi'], bins=20, kde=True, ax=axes[1])
axes[1].set_title("BMI Distribution")

sns.histplot(data['charges'], bins=20, kde=True, ax=axes[2])
axes[2].set_title("Charges Distribution")

plt.tight_layout()
plt.show()

# 2️⃣ Impact of Smoking on Charges
plt.figure(figsize=(6, 4))
sns.boxplot(x="smoker", y="charges", hue="smoker", data=data, palette=['blue', 'red'], legend=False)
plt.title("Insurance Charges: Smokers vs. Non-Smokers")
plt.xlabel("Smoker")
plt.ylabel("Charges")
plt.show()

# 3️⃣ BMI vs. Charges (Colored by Smoking Status)
plt.figure(figsize=(6, 4))
sns.scatterplot(x=data['bmi'], y=data['charges'], hue=data['smoker'], alpha=0.7)
plt.title("BMI vs. Insurance Charges")
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.legend(title="Smoker")
plt.show()

# 4️⃣ Age vs. Charges (Colored by Smoking Status)
plt.figure(figsize=(6, 4))
sns.scatterplot(x=data['age'], y=data['charges'], hue=data['smoker'], alpha=0.7)
plt.title("Age vs. Insurance Charges")
plt.xlabel("Age")
plt.ylabel("Charges")
plt.legend(title="Smoker")
plt.show()

# 5️⃣ Charges Comparison by Gender & Region
plt.figure(figsize=(10, 4))

# Gender comparison
plt.subplot(1, 2, 1)
sns.boxplot(x="sex", y="charges", hue="sex", data=data, palette="coolwarm", legend=False)
plt.title("Insurance Charges by Gender")

# Region comparison
plt.subplot(1, 2, 2)
sns.boxplot(x="region", y="charges", hue="region", data=data, palette="viridis", legend=False)
plt.title("Insurance Charges by Region")

plt.tight_layout()
plt.show()

# 6️⃣ Correlation Analysis (Using Numeric Data)
plt.figure(figsize=(8, 5))
sns.heatmap(data_numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()
