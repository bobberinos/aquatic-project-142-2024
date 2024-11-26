import pandas as pd

# Define file paths and region mappings
file_paths = {
    "arroyo_burro.csv": "ABB",
    "arroyo_quemado.csv": "AQB",
    "carpinteria.csv": "CSB-CCB",
    "east_santa_barbara_city.csv": "ESBB",
    "east_ucsb.csv": "EUCB",
    "isla_vista.csv": "IVWB",
    "santa_claus.csv": "SCLB"
}

# Initialize an empty list to store processed dataframes
processed_dfs = []

# Process each file
for file_name, region_code in file_paths.items():
    file_path = f"raw/{file_name}"  # Replace '/path/to/' with your actual file path
    df = pd.read_csv(file_path)
    
    # Select only the required columns
    df = df[['year', 'quarter', 'kelp_area_m2']]
    
    # Filter for the years 2011 to 2020
    df = df[(df['year'] >= 2011) & (df['year'] <= 2022)]

    # Add the 'region' column
    df['region'] = region_code

    # Reorder columns
    df = df[['year', 'region', 'quarter', 'kelp_area_m2']]

    # Append to list
    processed_dfs.append(df)

# Concatenate all dataframes
combined_df = pd.concat(processed_dfs, ignore_index=True)

# Sort by year
combined_df = combined_df.sort_values(by='year')

# Save the combined dataframe to a CSV file
output_file_path = "filtered/combined_kelp_area.csv"  # Replace '/path/to/' with your desired output directory
combined_df.to_csv(output_file_path, index=False)
