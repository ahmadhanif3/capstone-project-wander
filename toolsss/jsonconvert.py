import pandas as pd

# Load the CSV file
csv_file_path = 'cleaned_output.csv'
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to a JSON format
json_data = df.to_json(orient='records', lines=True)

# Save the JSON data to a file
json_file_path = 'output.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"CSV data has been converted to JSON and saved to {json_file_path}")
