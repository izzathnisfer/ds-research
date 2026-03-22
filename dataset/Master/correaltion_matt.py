import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Load file
base_dir = Path(__file__).resolve().parent
file_path = base_dir / "V_2_sri_lanka_master_monthly_dataset_not_cleaned.xlsx"
df = pd.read_excel(file_path)

# Keep only numeric columns
numeric_df = df.select_dtypes(include=["number"])

# Calculate correlation matrix
corr_matrix = numeric_df.corr()

# Print correlation matrix
print(corr_matrix)

# Save to CSV
corr_matrix.to_csv("correlation_matrix.csv")

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()