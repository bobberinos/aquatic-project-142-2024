import pandas as pd

# Load the dataset
input_file_path = "raw/kelp_cover.csv"  # Replace with the actual file path
kelp_data = pd.read_csv(input_file_path)

# Remove invalid values
kelp_data.replace(-99999, 0, inplace=True)

# Filter the data based on the specified conditions
filtered_kelp_data = kelp_data[(kelp_data['YEAR'] >= 2011) & 
                               (kelp_data['YEAR'] <= 2022) & 
                               (kelp_data['MONTH'] >= 9) & 
                               (kelp_data['MONTH'] <= 12)]

# Select only the specified columns
filtered_kelp_data_selected = filtered_kelp_data[['YEAR', 'MONTH', 'SITE', 'KELP_PLANTS', 'HOLDFASTS']]

# Sort the data by YEAR and within each YEAR by MONTH
filtered_kelp_data_sorted = filtered_kelp_data_selected.sort_values(by=['YEAR', 'MONTH'])

# Save the sorted data to a CSV file
output_sorted_file_path = "filtered/filtered_kelp_wrack.csv"  # Replace with your desired output path
filtered_kelp_data_sorted.to_csv(output_sorted_file_path, index=False)
