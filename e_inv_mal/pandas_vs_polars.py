import pandas as pd
import numpy as np
import time

df = pd.DataFrame({'A': np.random.randint(1, 100000000000000000, 16**7)})

start = time.time()
result = df[df['A'] > 50]
end = time.time()
print(f"Pandas Time: {end - start:.4f} seconds")

import polars as pl
import numpy as np
import time

df = pl.DataFrame({'A': np.random.randint(1, 100000000000000000, 16**7)})

start = time.time()
result = df.filter(pl.col('A') > 50)
end = time.time()
print(f"Polars Time: {end - start:.4f} seconds")
