import xarray as xr
import pandas as pd

# Create sample Xarray dataset
data = {
    'temperature': (('time', 'location'), [[25, 30], [28, 32], [26, 31]]),
    'humidity': (('time', 'location'), [[60, 65], [55, 58], [62, 67]]),
}
coords = {'time': pd.date_range('2022-01-01', periods=3),
          'location': ['New York', 'London']}
xarray_ds = xr.Dataset(data, coords=coords)

# Convert Xarray dataset to Pandas DataFrame
pandas_df = xarray_ds.to_dataframe()

print("Xarray Dataset:")
print(xarray_ds)
print("\nPandas DataFrame:")
print(pandas_df)