import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# 1. LOAD CLEANED DATASET
# ==========================================
df = pd.read_excel("cleaned_dataset.xlsx")

# ==========================================
# 2. CREATE FOLDER TO SAVE CHARTS
# ==========================================
output_folder = "EDA_Charts"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ==========================================
# 3. DISPLAY BASIC INFORMATION
# ==========================================
print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

# ==========================================
# 4. HISTOGRAMS
# ==========================================
df.hist(figsize=(14, 10))

plt.suptitle("Histograms of Numerical Columns")

plt.tight_layout()

# Save Histogram
plt.savefig(f"{output_folder}/histograms.png")

plt.show()

# ==========================================
# 5. BOXPLOT FOR OUTLIER DETECTION
# ==========================================
plt.figure(figsize=(12, 6))

sns.boxplot(data=df.select_dtypes(include=np.number))

plt.xticks(rotation=45)

plt.title("Boxplot for Outlier Detection")

# Save Boxplot
plt.savefig(f"{output_folder}/boxplot_outliers.png")

plt.show()

# ==========================================
# 6. CORRELATION HEATMAP
# ==========================================
plt.figure(figsize=(10, 6))

correlation = df.corr(numeric_only=True)

sns.heatmap(correlation,
            annot=True,
            cmap='coolwarm',
            linewidths=0.5)

plt.title("Correlation Heatmap")

# Save Heatmap
plt.savefig(f"{output_folder}/correlation_heatmap.png")

plt.show()

# ==========================================
# 7. COUNTPLOT - PAYMENT METHOD
# ==========================================
plt.figure(figsize=(8, 5))

sns.countplot(x='paymentmethod', data=df)

plt.title("Payment Method Distribution")

plt.xticks(rotation=45)

# Save Countplot
plt.savefig(f"{output_folder}/payment_method_countplot.png")

plt.show()

# ==========================================
# 8. COUNTPLOT - ORDER STATUS
# ==========================================
plt.figure(figsize=(8, 5))

sns.countplot(x='orderstatus', data=df)

plt.title("Order Status Distribution")

plt.xticks(rotation=45)

# Save Countplot
plt.savefig(f"{output_folder}/order_status_countplot.png")

plt.show()

# ==========================================
# 9. LINE CHART - SALES TREND OVER TIME
# ==========================================
sales_trend = df.groupby('date')['totalprice'].sum()

plt.figure(figsize=(12, 6))

sales_trend.plot()

plt.title("Sales Trend Over Time")

plt.xlabel("Date")

plt.ylabel("Total Sales")

# Save Line Chart
plt.savefig(f"{output_folder}/sales_trend.png")

plt.show()

# ==========================================
# 10. TOP PRODUCTS ANALYSIS
# ==========================================
top_products = df['product'].value_counts().head(10)

plt.figure(figsize=(10, 6))

top_products.plot(kind='bar')

plt.title("Top 10 Products")

plt.xlabel("Product")

plt.ylabel("Count")

plt.xticks(rotation=45)

# Save Bar Chart
plt.savefig(f"{output_folder}/top_products.png")

plt.show()

# ==========================================
# 11. SUMMARY MESSAGE
# ==========================================
print(f"\nAll charts have been saved inside the '{output_folder}' folder.")