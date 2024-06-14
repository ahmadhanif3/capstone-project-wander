import os
import pandas as pd

# Specify the folder containing CSV files
folder_path = r'//folder to merge'

# Ensure the output directory exists
output_folder = r'//where you gonna put the merged files'
output_filename = 'merged_output.csv'
output_path = os.path.join(output_folder, output_filename)

# List all files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Initialize an empty list to hold dataframes
df_list = []

# Loop through the CSV files and read them into dataframes
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    df_list.append(df)

# Concatenate all dataframes into one
merged_df = pd.concat(df_list, ignore_index=True)

# Save the merged dataframe to a CSV file
merged_df.to_csv(output_path, index=False)

print(f'Merged CSV saved to {output_path}') 