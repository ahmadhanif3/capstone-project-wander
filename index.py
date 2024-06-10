import pandas as pd
import os

base_path = r'C:\Users\ACER\Documents\Capstone\Hotel_DS'
clean_path = r'C:\Users\ACER\Documents\Capstone\Hotel_DS_clean'

# Ensure the clean directory exists
os.makedirs(clean_path, exist_ok=True)

# Function to extract latitude and longitude from 'geometry' column
def extract_lat_lng(geometry):
    return (geometry['location']['lat'], geometry['location']['lng'])

# Loop through the directory containing the CSV files
for file_name in os.listdir(base_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(base_path, file_name)
        # Read the CSV file
        df = pd.read_csv(file_path)
        # Check if 'geometry' column exists
        if 'geometry' in df.columns:
            # Extract latitude and longitude
            df[['lat', 'lng']] = df['geometry'].apply(eval).apply(extract_lat_lng).apply(pd.Series)
            # Drop the 'geometry' column
            df.drop(columns=['geometry'], inplace=True)
            # Save the modified DataFrame back to CSV
            clean_file_path = os.path.join(clean_path, file_name)
            df.to_csv(clean_file_path, index=False)
            print(f"Processed: {file_name}")
        else:
            print(f"No 'geometry' column found in {file_name}, skipping.")

print("All files processed.")