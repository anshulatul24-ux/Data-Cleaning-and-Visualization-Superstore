# ============================================================
# Data Cleaning and Visualization of Superstore Sales Dataset
# Internship Project - Thiranex
#
# Submitted by: Anshul Patil
# Domain: Data Science
# ============================================================

# ==========================
# Import Libraries
# ==========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Plot Style
plt.style.use("ggplot")

# ==========================
# Load Dataset
# ==========================

print("Loading dataset...")

df = pd.read_csv("../dataset/Superstore.csv", encoding="latin1")

print("Dataset loaded successfully!\n")

# ==========================
# Basic Information
# ==========================

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# ==========================
# Missing Values
# ==========================

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================
# Duplicate Records
# ==========================

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Shape After Removing Duplicates:", df.shape)

# ==========================
# Save Cleaned Dataset
# ==========================

df.to_csv("../dataset/Cleaned_Superstore.csv", index=False)

print("\nCleaned dataset saved successfully!")

# ============================================================
# DATA VISUALIZATION
# ============================================================

# --------------------------
# Sales by Category
# --------------------------

plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x="Category",
    y="Sales",
    estimator=sum,
    errorbar=None
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("../images/sales_by_category.png")

plt.show()

# --------------------------
# Sales by Region
# --------------------------

plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x="Region",
    y="Sales",
    estimator=sum,
    errorbar=None
)

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("../images/sales_by_region.png")

plt.show()

# --------------------------
# Profit Distribution
# --------------------------

plt.figure(figsize=(8,5))

sns.histplot(df["Profit"], bins=30, kde=True)

plt.title("Profit Distribution")
plt.xlabel("Profit")

plt.tight_layout()

plt.savefig("../images/profit_distribution.png")

plt.show()

# --------------------------
# Sales vs Profit
# --------------------------

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category"
)

plt.title("Sales vs Profit")

plt.tight_layout()

plt.savefig("../images/sales_vs_profit.png")

plt.show()

# --------------------------
# Top 10 States by Sales
# --------------------------

top_states = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,5))

sns.barplot(
    x=top_states.values,
    y=top_states.index
)

plt.title("Top 10 States by Sales")
plt.xlabel("Sales")
plt.ylabel("State")

plt.tight_layout()

plt.savefig("../images/top_states_sales.png")

plt.show()

# --------------------------
# Correlation Heatmap
# --------------------------

numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("../images/correlation_heatmap.png")

plt.show()

# --------------------------
# Monthly Sales Trend
# --------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
      .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12,5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

plt.savefig("../images/monthly_sales_trend.png")

plt.show()

# ============================================================
# Business Insights
# ============================================================

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

print("""
• Technology category generated the highest sales.

• Regional sales varied significantly.

• Some products generated high sales but low profit.

• Monthly sales showed seasonal trends.

• Correlation analysis revealed relationships
  among numerical variables.
""")

# ============================================================
# Conclusion
# ============================================================

print("=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)

print("""
Project Summary

✔ Dataset Loaded
✔ Data Cleaned
✔ Missing Values Checked
✔ Duplicate Records Removed
✔ Cleaned Dataset Saved
✔ 7 Visualizations Generated
✔ Business Insights Extracted

Thank you!
""")
