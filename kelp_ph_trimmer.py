import pandas as pd

# Load the merged dataset
merged_kelp_file_path = 'filtered/kelp_ph_data.csv'  # Replace with your file path
merged_kelp_data = pd.read_csv(merged_kelp_file_path)

# Remove rows without a pH value (NaN in the pH column)
filtered_data = merged_kelp_data.dropna(subset=['pH'])

# Save the filtered data to a new CSV file
filtered_data.to_csv('filtered/filtered_kelp_ph_data.csv', index=False)  # Replace with your save path

