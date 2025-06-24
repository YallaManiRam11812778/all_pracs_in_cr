import pandas as pd
import polars as pl
import numpy as np
import time
# Define the size of the dataset
N = 100_000_000

# Generate a large dataset
data = {
    "category": np.random.choice(['A', 'B', 'C', 'D'], N),
    "value": np.random.rand(N),
    "timestamp": pd.date_range(start='2020-01-01', periods=N, freq='T')
}
df_pandas = pd.DataFrame(data)
df_polars = pl.DataFrame(data)

# Pandas operations
# Filter
start_time = time.time()
filtered_pandas = df_pandas[df_pandas['value'] > 0.5]
pandas_filter_time = time.time() - start_time
print(f"Pandas filter took {pandas_filter_time:.4f} seconds")

# Sort
start_time = time.time()
sorted_pandas = filtered_pandas.sort_values(by='timestamp')
pandas_sort_time = time.time() - start_time
print(f"Pandas sort took {pandas_sort_time:.4f} seconds")

# Aggregate
start_time = time.time()
aggregated_pandas = sorted_pandas.groupby('category').agg({'value': 'mean'})
pandas_aggregate_time = time.time() - start_time
print(f"Pandas aggregate took {pandas_aggregate_time:.4f} seconds")

# Polars operations
# Filter
start_time = time.time()
filtered_polars = df_polars.filter(pl.col('value') > 0.5)
polars_filter_time = time.time() - start_time
print(f"Polars filter took {polars_filter_time:.4f} seconds")

# Sort
start_time = time.time()
sorted_polars = filtered_polars.sort(by='timestamp')
polars_sort_time = time.time() - start_time
print(f"Polars sort took {polars_sort_time:.4f} seconds")

# Aggregate
start_time = time.time()
aggregated_polars = sorted_polars.group_by('category').agg(pl.col('value').mean())
polars_aggregate_time = time.time() - start_time
print(f"Polars aggregate took {polars_aggregate_time:.4f} seconds")
