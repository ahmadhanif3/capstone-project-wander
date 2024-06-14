import pandas as pd

# Load the CSV file
file_path = 'cleaned_output.csv'
df = pd.read_csv(file_path)

# Check for duplicates
duplicates = df.duplicated()

# Print the number of duplicate rows
print(f"Number of duplicate rows: {duplicates.sum()}")

# Remove duplicates
df_cleaned = df.drop_duplicates()

# Save the cleaned data to a new CSV file
cleaned_file_path = 'cleaned_output.csv'
df_cleaned.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
