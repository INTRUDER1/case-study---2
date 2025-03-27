import pandas as pd
import os

# Load the featured dataset
file_path = os.path.join("..", "data", "insurance_featured.csv")
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    raise FileNotFoundError(f"File not found: {file_path}")

# 1️⃣ Average Charges per Region
avg_charges_region = data.groupby("region")['charges'].mean().reset_index()
print("\nAverage Charges by Region:")
print(avg_charges_region)

# 2️⃣ Average Charges per Policy Type (if applicable, assuming smoker status as policy impact)
avg_charges_smoker = data.groupby("smoker")['charges'].mean().reset_index()
print("\nAverage Charges by Smoker Status:")
print(avg_charges_smoker)

# 3️⃣ Average Charges by BMI Category
avg_charges_bmi = data.groupby("bmi_category")['charges'].mean().reset_index()
print("\nAverage Charges by BMI Category:")
print(avg_charges_bmi)

# 4️⃣ Count of Customers by Age Group
age_group_counts = data['age_group'].value_counts().reset_index()
age_group_counts.columns = ['Age Group', 'Customer Count']
print("\nCustomer Distribution by Age Group:")
print(age_group_counts)

# 5️⃣ Saving Summary Report to CSV
summary_file_path = os.path.join("..", "data", "summary_report.csv")
summary_data = {
    'Average Charges by Region': avg_charges_region,
    'Average Charges by Smoker Status': avg_charges_smoker,
    'Average Charges by BMI Category': avg_charges_bmi,
    'Customer Distribution by Age Group': age_group_counts
}

with open(summary_file_path, 'w') as file:
    for key, df in summary_data.items():
        file.write(f"\n{key}\n")
        df.to_csv(file, index=False)
        file.write("\n")

print("\nSummary Report Generated: summary_report.csv")
