# Create a correlation heatmap from the dataset

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = r"C:\Users\ASUS\Desktop\DS project\dataset\Master\sri_lanka_master_monthly_dataset_not_cleaned.csv"
df = pd.read_csv(file_path)

# Select numeric columns only
numeric_df = df.select_dtypes(include=['number'])

# Compute correlation
corr = numeric_df.corr()

# Plot heatmap
plt.figure()
plt.imshow(corr, aspect='auto')
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")

plt.tight_layout()

# Save figure
output_path = r"C:\Users\ASUS\Desktop\DS project\dataset\Master\correlation_heatmap.png"
plt.savefig(output_path)

output_path