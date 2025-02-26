import pandas as pd

# Load the dataset
file_path = "/mnt/data/samsung_sales_data.csv"
df = pd.read_csv(file_path)

# Group sales data by Year, Month, and Model
df_grouped = df.groupby(['Year', 'Month', 'Model'])['Units Sold'].sum().reset_index()

# Save the processed monthly sales data
processed_file_path = '/mnt/data/processed_samsung_sales.csv'
df_grouped.to_csv(processed_file_path, index=False)

processed_file_path  # Return file path for download