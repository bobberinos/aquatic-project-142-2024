import pandas as pd

# Load the filtered data
filtered_kelp_file_path = 'filtered/filtered_kelp_ph_data.csv'  # Replace with your file path
filtered_kelp_data = pd.read_csv(filtered_kelp_file_path)

# Add a new column 'SUM' after 'HOLDFASTS' that is the sum of 'KELP_PLANTS' and 'HOLDFASTS'
filtered_kelp_data.insert(
    filtered_kelp_data.columns.get_loc('HOLDFASTS') + 1, 
    'SUM', 
    filtered_kelp_data['KELP_PLANTS'] + filtered_kelp_data['HOLDFASTS']
)

# Filter out rows where kelp_area_km2 is 0 to avoid division by zero
filtered_kelp_data = filtered_kelp_data[filtered_kelp_data['kelp_area_m2'] != 0]

# Add a new column 'SUM_per_km2' after 'pH' that is the quotient of 'SUM' divided by 'kelp_area_km2'
filtered_kelp_data.insert(
    filtered_kelp_data.columns.get_loc('pH') + 1,
    'count_per_m2',
    filtered_kelp_data['SUM'] / filtered_kelp_data['kelp_area_m2']
)

# Save the final updated data to a new CSV file
filtered_kelp_data.to_csv('filtered/final_filtered_data.csv', index=False)  # Replace with your save path
