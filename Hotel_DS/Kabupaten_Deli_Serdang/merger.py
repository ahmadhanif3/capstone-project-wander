import os
import pandas as pd

# Specify the folder containing the CSV files
folder_path = os.path.dirname(os.path.abspath(__file__))

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv') ]

# Initialize an empty DataFrame
combined_df = pd.DataFrame()

# Loop through the list of CSV files and append them to the combined DataFrame
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path)
    combined_df = pd.concat([combined_df, df], ignore_index=True)


# Save the combined DataFrame to a new CSV file
combined_df.to_csv(os.path.join(folder_path, 'Merged.csv'), index=False)

print(f'Merged {len(csv_files)} files ')
