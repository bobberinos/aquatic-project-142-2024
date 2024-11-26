import pandas as pd

# Load the data files
kelp_file_path = 'filtered/merged_kelp_wrack_area.csv'  # Replace with your file path
ph_filtered_file_path = 'filtered/ph_filtered.csv'    # Replace with your file path

kelp_data = pd.read_csv(kelp_file_path)
ph_filtered_data = pd.read_csv(ph_filtered_file_path)

# Rename columns in pH_filtered for consistency with merged_kelp_coverage
ph_filtered_data.rename(columns={"Year": "YEAR", "Month": "MONTH", "site": "pH_SITE"}, inplace=True)

# Define site mapping
site_mapping = {
    "ARQ": "AQB",
    "NPR": "IVWB",
    "MKO": "ABB",
    "CPR": ["SCLB", "CSB-CCB"]
}

# Create a mapping of pH_SITE to kelp SITE, duplicating rows for CPR to handle multiple mappings
ph_filtered_data_expanded = ph_filtered_data.copy()
for cpr_site in site_mapping["CPR"]:
    temp_data = ph_filtered_data[ph_filtered_data["pH_SITE"] == "CPR"].copy()
    temp_data["SITE"] = cpr_site
    ph_filtered_data_expanded = pd.concat([ph_filtered_data_expanded, temp_data], ignore_index=True)
ph_filtered_data_expanded = ph_filtered_data_expanded[ph_filtered_data_expanded["pH_SITE"] != "CPR"]

# Map the remaining sites (excluding CPR)
ph_filtered_data_expanded["SITE"] = ph_filtered_data_expanded["pH_SITE"].map(site_mapping)

# Merge pH data into kelp data based on YEAR, MONTH, and SITE
kelp_data_with_ph = kelp_data.merge(ph_filtered_data_expanded, on=["YEAR", "MONTH", "SITE"], how="left")

# Drop unnecessary columns and keep relevant ones
kelp_data_with_ph = kelp_data_with_ph.drop(columns=["pH_SITE"])

# Save the merged dataset if needed
kelp_data_with_ph.to_csv('filtered/kelp_ph_data.csv', index=False)  # Replace with your save path

