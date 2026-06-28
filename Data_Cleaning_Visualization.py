# # Data Cleaning and Visualization of Superstore Sales Dataset
# 
# ## Internship Project - Thiranex
# 
# ### Submitted by:
# **Anshul Patil**
# 
# ### Internship Domain:
# **Data Science**
# 
# ### Tools Used
# - Python
# - Pandas
# - NumPy
# - Matplotlib
# - Seaborn
# - Jupyter Notebook
# 
# ---
# 
# ## Objective
# 
# The objective of this project is to clean the Superstore Sales dataset, perform exploratory data analysis, and create meaningful visualizations to derive business insights.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style

# Plot style
plt.style.use("ggplot")

print("Libraries imported successfully!")

# %%
df = pd.read_csv("../dataset/Superstore.csv")

df.head()

# %%
df = pd.read_csv("../dataset/Superstore.csv")

# %%
file_path = "../dataset/Superstore.csv"

with open(file_path, "rb") as f:
    print(f.read(100))

# %%
import pandas as pd

df = pd.read_csv("../dataset/Superstore.csv", encoding="latin1")

df.head()

# %%
print("Number of Rows and Columns:")
print(df.shape)

# %%
print("Column Names:")
print(df.columns)

# %%
df.info()

# %%
df.describe()

# %%
print(df.isnull().sum())

# %%
print("Duplicate Rows:", df.duplicated().sum())

# %%
df = df.drop_duplicates()

print("Dataset Shape After Removing Duplicates:")
print(df.shape)

# %%
df.to_csv("../dataset/Cleaned_Superstore.csv", index=False)

print("Cleaned dataset saved successfully!")

# %%
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
plt.ylabel("Total Sales")

plt.show()

# %%
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
plt.ylabel("Total Sales")

plt.show()

# %%
plt.figure(figsize=(8,5))

sns.histplot(df["Profit"], bins=30, kde=True)

plt.title("Profit Distribution")
plt.xlabel("Profit")

plt.show()

# %%
plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category"
)

plt.title("Sales vs Profit")

plt.show()

# %%
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

plt.show()

# %%
numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()

# %%
df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
      .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12,5))

monthly_sales.plot(marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.grid(True)

plt.show()

# %% [markdown]
# # Conclusion
# 
# ## Key Findings
# 
# - The dataset was successfully loaded and cleaned.
# - Duplicate records were identified and removed.
# - Missing values were checked.
# - Sales and profit trends were analyzed using different visualizations.
# - Correlation between numerical variables was examined.
# - Business insights were generated from regional and category-wise sales.
# 
# ## Future Scope
# 
# - Build a machine learning model using this dataset.
# - Develop an interactive dashboard using Power BI or Tableau.
# - Perform sales forecasting using time series analysis.
# 
# ## Technologies Used
# 
# - Python
# - Pandas
# - NumPy
# - Matplotlib
# - Seaborn
# - Jupyter Notebook

# %% [markdown]
# 