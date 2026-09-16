# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "Clean_Dataset.csv"

# Load the latest version
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "shubhambathwal/flight-price-prediction",
  file_path,
  # Provide any additional arguments like
  # sql_query or pandas_kwargs. See the
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

df = df.rename(columns={"Unnamed: 0": "ID"})

print("\n")
print("First 5 records:")
print(df.head())
print("\n")
print("Last 5 records:")
print(df.tail(5))
print("\n")
print("DataFrame:")
print(df.info())
print("\n")
print("Summary statistics:")
print(df.describe())
print("\n")
print("Shape - rows, columns:")
print(df.shape)
print("\n")
print("Column data types:")
print(df.dtypes)
print("\n")
print("Column names:")
print(df.columns)
print("\n")
print("Row index:")
print(df.index)