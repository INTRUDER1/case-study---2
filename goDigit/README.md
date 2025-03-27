# Insurance Customer Data Analysis & Predictive Modeling

## Project Overview
This project focuses on analyzing and preparing insurance customer data to derive actionable insights. The key aspects of the project include:
- **Data Quality Assessment & Cleaning**
- **Data Transformation & Preparation**
- **Exploratory Data Analysis (EDA)**
- **Feature Engineering**
- **Predictive Modeling**
- **Reporting & Insights Communication**

The objective is to enhance data-driven decision-making for an insurance company by identifying patterns, customer segments, and risk factors.

## Folder Structure
```
📂 GoDigit_Case_Study/
│── 📂 data/            # Contains the dataset files
│   ├── insurance.csv  # Raw dataset
│   ├── insurance_cleaned.csv  # Cleaned dataset
│   ├── insurance_featured.csv  # Feature engineered dataset
│
│── 📂 notebooks/        # Jupyter Notebooks for step-by-step execution
│   ├── 01_data_cleaning.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   ├── 04_modeling.ipynb
│   ├── 05_summary_report.ipynb
│
│── 📂 scripts/          # Python scripts for each stage
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── eda.py
│   ├── modeling.py
│   ├── summary_report.py
│
│── 📂 reports/          # Final reporting materials
│   ├── findings.docx    # Detailed case study documentation
│   ├── findings.pptx    # Presentation for non-technical audience
│
│── requirements.txt     # List of required Python packages
│── README.md            # Project documentation and instructions
```

## Installation & Setup
To run this project on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/INTRUDER1/case-study---2.git
   cd GoDigit_Case_Study
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Scripts or Jupyter Notebooks:**
   - For step-by-step execution, open Jupyter notebooks:
     ```bash
     jupyter notebook
     ```
   - Alternatively, run Python scripts directly:
     ```bash
     python scripts/data_cleaning.py
     python scripts/feature_engineering.py
     python scripts/eda.py
     python scripts/modeling.py
     ```

## Key Steps & Methodology
### 1. Data Quality Assessment & Cleaning
- Identified missing values, duplicates, and outliers.
- Standardized categorical variables.
- Saved the cleaned data as `insurance_cleaned.csv`.

### 2. Data Transformation & Feature Engineering
- Extracted new features like `age groups`, `smoker categories`, and `BMI categories`.
- Standardized and encoded categorical variables.
- Created `insurance_featured.csv` for modeling.

### 3. Exploratory Data Analysis (EDA)
- Analyzed data distributions and relationships.
- Visualized trends such as **Age vs Charges**, **BMI vs Charges**, and **Smoker vs Non-Smoker Charges**.

### 4. Predictive Modeling
- Built a **Linear Regression** model to predict insurance charges.
- Evaluated performance using **MAE, MSE, RMSE, and R² score**.

### 5. Reporting & Insights
- Summarized findings in `findings.docx` and `findings.pptx`.
- Provided recommendations for improving insurance pricing strategies.

## Results & Key Findings
- **Smoking significantly impacts insurance charges** (Smokers pay much higher premiums).
- **BMI and Age show a correlation with insurance costs**.
- **The predictive model achieved an R² score of ~0.56**, indicating moderate accuracy.
- **Recommendations for the insurance company**:
  - Improve pricing models with more advanced ML techniques.
  - Focus marketing on non-smokers and healthier individuals.
  - Introduce targeted premium discounts for young customers.

## Contribution & Contact
- **Author:** [Your Name]
- **Contact:** [Your Email]
- **GitHub:** [Your GitHub Profile]
- **LinkedIn:** [Your LinkedIn Profile]

Feel free to contribute by raising issues or submitting pull requests!

---
*Thank you for checking out this project! Happy coding!* 🚀

