import os
import pandas as pd
import json

# Path to the folder containing CSV files
csv_folder = r'C:\Users\ACER\Documents\Capstone\TA_DS_clean'

# Path to the folder where you want to save JSON files
json_folder = r'C:\Users\ACER\Documents\Capstone\TA_DS_JSON'

# Iterate through each CSV file in the folder
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith('.csv'):
        # Read CSV file into pandas DataFrame
        df = pd.read_csv(os.path.join(csv_folder, csv_file))
        
        # Convert DataFrame to JSON
        json_data = df.to_json(orient='records')
        
        # Create filename for JSON file (same name as CSV with .json extension)
        json_filename = os.path.splitext(csv_file)[0] + '.json'
        
        # Write JSON data to file in the JSON folder
        with open(os.path.join(json_folder, json_filename), 'w') as json_file:
            json_file.write(json_data)
