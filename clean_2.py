import pandas as pd
import warnings

warnings.filterwarnings("ignore")

print("🚀 Starting Data Cleaning Process...")

# Load dataset (same folder as script)
df = pd.read_csv("Messy_Employee_dataset.csv")

print("\n📊 Initial Data Info:")
print(df.info())

print("\n🔍 Missing Values:")
print(df.isnull().sum())

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Convert Age to integer
df['Age'] = df['Age'].round().astype(int)

# Format date
df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')
df['Join_Date'] = df['Join_Date'].dt.strftime('%d-%m-%Y')

# Create full name
df['Full_name'] = df['First_Name'] + ' ' + df['Last_Name']

# Drop old columns
df = df.drop(columns=['First_Name', 'Last_Name'])

# Reorder columns (Full_name at 2nd position)
cols = list(df.columns)
cols.remove('Full_name')
cols.insert(1, 'Full_name')
df = df[cols]

# Clean phone numbers
df['Phone'] = df['Phone'].astype(str).str.replace('-', '')

# Save output
df.to_csv("cleaned_employee_data.csv", index=False)

print("\n✅ Data Cleaning Completed Successfully!")