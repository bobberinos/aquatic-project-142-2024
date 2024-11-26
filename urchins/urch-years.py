import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'urchins.csv'
data = pd.read_csv(file_path)

# Ensure `DATE_DEPLOYED` is a datetime type
data['DATE_DEPLOYED'] = pd.to_datetime(data['DATE_DEPLOYED'], errors='coerce')

# Filter out negative values and drop rows with NaN dates
data_filtered = data[data['TOTAL_URCHINS'] >= 0].dropna(subset=['DATE_DEPLOYED'])

# Extract the month and compute the average count per month
data_filtered['Month'] = data_filtered['DATE_DEPLOYED'].dt.month
monthly_avg = data_filtered.groupby('Month')['TOTAL_URCHINS'].mean()

# Plot the results
plt.figure(figsize=(10, 6))
monthly_avg.plot(kind='bar')
plt.title('Average Urchin Count Per Month')
plt.xlabel('Month')
plt.ylabel('Average Urchin Count')
plt.xticks(ticks=range(12), labels=[
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
