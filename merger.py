import pandas as pd

# Load the datasets
kelp_area_data_path = "filtered/combined_kelp_area.csv"  # Replace with actual path
sorted_kelp_wrack_path = "filtered/filtered_kelp_wrack.csv"  # Replace with actual path

kelp_area_data = pd.read_csv(kelp_area_data_path)
sorted_kelp_wrack_data = pd.read_csv(sorted_kelp_wrack_path)

# Filter kelp area data for quarter 4
kelp_area_q4 = kelp_area_data[kelp_area_data['quarter'] == 4]

# Merge kelp area data (quarter 4) into the sorted kelp wrack dataset by matching year and site
merged_data = sorted_kelp_wrack_data.merge(
    kelp_area_q4[['year', 'region', 'kelp_area_m2']],
    left_on=['YEAR', 'SITE'],
    right_on=['year', 'region'],
    how='left'
)

# Drop redundant columns
merged_data = merged_data.drop(columns=['year', 'region'])

# Save the merged dataset to a new CSV file
output_merged_file_path = "filtered/merged_kelp_wrack_area.csv"  # Replace with desired output path
merged_data.to_csv(output_merged_file_path, index=False)
