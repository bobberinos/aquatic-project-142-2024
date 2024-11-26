import pandas as pd

# Load the CSV file
file_path = 'raw/ph_temp.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Parsing datetime and extracting Year and Month
data['datetime_UTC'] = pd.to_datetime(data['datetime_UTC'])
data['Year'] = data['datetime_UTC'].dt.year
data['Month'] = data['datetime_UTC'].dt.month

# Filter based on conditions
filtered_data = data[
    (data['site'].isin(['ARQ', 'NPR', 'MKO', 'CPR'])) &  # Include specific sites
    (data['Year'].between(2011, 2022)) &                 # Include years 2011-2022
    (data['Month'].isin([9, 10, 11, 12]))                # Include months Sep-Dec
]

# Group by Year, Month, and Site to calculate the average pH
averaged_data = filtered_data.groupby(['Year', 'Month', 'site'])['pH'].mean().reset_index()

# Sort by Year, Month, and Site
averaged_data = averaged_data.sort_values(by=['Year', 'Month', 'site'])

# Save to a new CSV if needed
averaged_data.to_csv('filtered/ph_filtered.csv', index=False)  # Replace with your save path

