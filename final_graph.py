import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

# Load the final filtered data
final_filtered_kelp_file_path = 'filtered/final_filtered_data.csv'  # Replace with your file path
data = pd.read_csv(final_filtered_kelp_file_path)

# Filter out data points with SUM_per_km2 > 0.25E7 or SUM_per_m2 == 0
sum_cutoff = 0.5 # 0.25e7
ph_lower_cutoff = 6
ph_upper_cutoff = 9
filtered_data = data[(data['count_per_m2'] <= sum_cutoff) & (data['count_per_m2'] != 0) & (data['pH'] >= ph_lower_cutoff) & (data['pH'] <= ph_upper_cutoff)] 

# Extract relevant columns
pH_values = filtered_data['pH']
SUM_per_m2_values = filtered_data['count_per_m2']

# Pearson correlation
pearson_corr, pearson_p = pearsonr(pH_values, SUM_per_m2_values)

# Spearman correlation
spearman_corr, spearman_p = spearmanr(pH_values, SUM_per_m2_values)

# Print correlation results
print(f"Pearson Correlation: {pearson_corr:.4f}, p-value: {pearson_p:.4e}")
print(f"Spearman Correlation: {spearman_corr:.4f}, p-value: {spearman_p:.4e}")

# Scatter plot of pH vs SUM_per_km2
plt.figure(figsize=(10, 6))
plt.scatter(pH_values, SUM_per_m2_values, alpha=0.7)
plt.title('Wrack Count per m2 vs. pH', fontsize=16)
plt.xlabel('pH', fontsize=14)
plt.ylabel('Wrack Count per m2', fontsize=14)
plt.grid(True)
plt.show()


