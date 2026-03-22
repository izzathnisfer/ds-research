# Create a correlation heatmap from the dataset

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
base_dir = Path(__file__).resolve().parent
file_path = base_dir / "V_2_sri_lanka_master_monthly_dataset_not_cleaned.xlsx"
df = pd.read_excel(file_path)

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
output_path = base_dir / "correlation_heatmap.png"
plt.savefig(output_path)

output_path