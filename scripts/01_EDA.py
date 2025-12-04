import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "data/MachineLearningRating_v3/MachineLearningRating_v3.txt"

# Try reading as CSV
# Correct: data is pipe separated
df = pd.read_csv(file_path, sep="|")

# --- Data Overview
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

# --- Numeric columns
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print("\nNumeric columns:\n", num_cols)

# --- Missing values
print("\nMissing values:\n", df.isna().sum())

# --- Loss Ratio
if "TotalClaims" in df.columns and "TotalPremium" in df.columns:
    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"].replace({0: np.nan})
    print("\nOverall Loss Ratio:", df["LossRatio"].mean())

# --- Loss Ratio by groups
for g in ["Province", "VehicleType", "Gender"]:
    if g in df.columns:
        print(f"\nAverage Loss Ratio by {g}:")
        print(df.groupby(g)["LossRatio"].mean().sort_values(ascending=False))

# --- Histograms
for col in num_cols:
    plt.figure(figsize=(6,4))
    df[col].hist(bins=50)
    plt.title(f"{col} distribution")
    plt.show()
for col in num_cols:

    # Skip columns with all missing or only one unique value
    if df[col].dropna().nunique() <= 1:
        print(f"Skipping {col} (not enough unique values)")
        continue

    plt.figure(figsize=(6,4))
    sns.boxplot(y=df[col].dropna())
    plt.title(f"Boxplot of {col}")
    plt.show()


# --- Correlation matrix
plt.figure(figsize=(10,8))
corr = df[num_cols].corr()
corr = corr.fillna(0)   # remove NaN values

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

plt.title("Correlation Matrix")
plt.show()
