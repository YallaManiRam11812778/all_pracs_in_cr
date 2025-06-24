import dask.dataframe as dd
import pandas as pd

# Create a sample pandas DataFrame
df = pd.DataFrame({'A': range(1, 10001), 'B': range(10001, 20001)})
print(df)

# Convert pandas DataFrame to Dask DataFrame
ddf = dd.from_pandas(df, npartitions=4)  # 4 partitions

# Define a function to apply
def process_row(row):
    return row ** 2

# Apply the function using Dask's parallelism
ddf = ddf.map_partitions(lambda df: df.apply(process_row, axis=1))
print(ddf)
# # Compute the result
# df_result = ddf.compute()

# # Show the first few rows
# print(df_result)

import dask.dataframe as dd
ddf = dd.from_pandas(df, npartitions=4)
ddf = ddf.map_partitions(lambda df: df.apply(process_row, axis=1))
df_result = ddf.compute()