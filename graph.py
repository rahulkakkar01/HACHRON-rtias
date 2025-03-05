import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import json

# Load Blinkit dataset
df = pd.read_csv("blinkit_dataset.csv")

# Data Cleaning
#df = df.dropna(subset=["product", "brand"])  # Remove rows with missing product/brand

# Standardize column names to lowercase and remove spaces
df.columns = df.columns.str.strip().str.lower()  # Convert to lowercase

print(df.columns)

# Ensure correct column name usage
if 'sales volume' in df.columns:
    df["normalized_demand"] = (df["sales volume"] - df["sales volume"].min()) / (df["sales volume"].max() - df["sales volume"].min())
else:
    print("Warning: 'Sales Volume' column not found! Using 'price' as fallback.")
    df["normalized_demand"] = (df["price"] - df["price"].min()) / (df["price"].max() - df["price"].min())

# K-Means Clustering to categorize demand
num_clusters = 3  # High, Medium, Low demand
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
df["demand_category"] = kmeans.fit_predict(df[["normalized_demand"]])

# Assign meaningful labels
demand_labels = {0: "Low Demand", 1: "Medium Demand", 2: "High Demand"}
df["demand_category"] = df["demand_category"].map(demand_labels)

# Optimize inventory placement
inventory_strategy = {
    "High Demand": "Central warehouse, closest to delivery hubs",
    "Medium Demand": "Regional warehouses, moderate priority",
    "Low Demand": "Stored in secondary locations, replenished as needed"
}
df["inventory_strategy"] = df["demand_category"].map(inventory_strategy)

# Visualization
plt.figure(figsize=(8, 5))
plt.hist(df["normalized_demand"], bins=30, color='blue', alpha=0.7)
plt.xlabel("Normalized Demand Score")
plt.ylabel("Number of Products")
plt.title("Demand Distribution")
plt.show()

# Save processed data as CSV
df.to_csv("optimized_inventory_blinkit.csv", index=False)

# Save processed data as JSON
df.to_json("optimized_inventory_blinkit.json", orient="records", lines=True)