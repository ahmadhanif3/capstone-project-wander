import os
import pandas as pd

# Define the path to the main folder
main_folder_path = 'C:\\Users\\ACER\\Documents\\Capstone\\Hotel_DS'

# Get a list of all folders within the main folder
folders = [f for f in os.listdir(main_folder_path) if os.path.isdir(os.path.join(main_folder_path, f))]

# Iterate through each folder
for folder in folders:
    folder_path = os.path.join(main_folder_path, folder)
    
    # Get a list of all CSV files in the current folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    # List to hold dataframes
    dfs = []
    
    # Read each CSV file and append it to the list of dataframes
    for csv_file in csv_files:
        csv_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(csv_path)
        dfs.append(df)
    
    # Concatenate all dataframes in the list
    if dfs:  # Check if there are any dataframes to concatenate
        merged_df = pd.concat(dfs, ignore_index=True)
        
        # Save the merged dataframe to a new CSV file
        merged_csv_path = os.path.join(folder_path, f'{folder}_merged.csv')
        merged_df.to_csv(merged_csv_path, index=False)
        
        print(f'Merged CSV for folder {folder} saved as {merged_csv_path}')
    else:
        print(f'No CSV files found in folder {folder}')
