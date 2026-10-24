import pandas as pd

file_name = "/Users/xiang/Documents/PROJECT/Marketing/Customer Segmentation/Mall_Customers_Enhanced.csv"

try:
    df = pd.read_csv(file_name)
    print("--- Data Preview ---")
    print(df.head())

except Exception as e:
    print(
        "error!!",
        e,
    )

print("\n--- 1. Data Size (row, column) ---")
print(df.shape)

print("\n--- 2. Column's Title ---")
print(df.columns)

print("\n--- 3. Statistical Summary Metrics (mean, minimum, and maximum values) ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Customer Segmentation by Income and Spending ---")

income_median = df["Annual Income (k$)"].median()
spending_median = df["Spending Score (1-100)"].median()

def segment_customer(row):
  if (
      row["Annual Income (k$)"] >= income_median
      and row["Spending Score (1-100)"] >= spending_median
  ):
    return "1. VIP / high income & high spend (main target)"
  elif (
      row["Annual Income (k$)"] >= income_median
      and row["Spending Score (1-100)"] < spending_median
  ):
    return "2. high income & low spend (high potential)"
  elif (
      row["Annual Income (k$)"] < income_median
      and row["Spending Score (1-100)"] >= spending_median
  ):
    return "3. low income & high spend (regular customer/shopper)"
  else:
    return "4. low income & low spend (economy class)"

df["Customer_Segment"] = df.apply(segment_customer, axis=1)

segment_counts = df["Customer_Segment"].value_counts()
print(segment_counts)

desktop_path = "/Users/xiang/Desktop/Mall_Customers_Segmented.csv"
df.to_csv(desktop_path, index=False)

print("File Saved to Desktop!")







