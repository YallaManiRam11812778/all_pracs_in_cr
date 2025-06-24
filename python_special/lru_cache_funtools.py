import time
import random
import math

# Simulated expensive function with complex computation
def expensive_computation(x):
    # Perform a complex mathematical operation
    result = 0
    for i in range(1, 15000):
        result += math.sqrt(x * i)
    return result

def process_data(data):
    results = []
    for item in data:
        result = expensive_computation(item)
        results.append(result)
    return results

# Generating a huge dataset
data = [random.randint(1, 100) for _ in range(15000)]  # Large dataset

# Measure time without lru_cache
start_time = time.time()
results = process_data(data)
end_time = time.time()

print(f"Processing time without lru_cache: {end_time - start_time:.2f} seconds")

import time
import random
import math
from functools import lru_cache

# Using lru_cache to optimize the expensive computation
@lru_cache(maxsize=None)  # Unlimited cache size
def expensive_computations(x):
    # Perform a complex mathematical operation
    result = 0
    for i in range(1, 15000):
        result += math.sqrt(x * i)
    return result

def process_data(data):
    results = []
    for item in data:
        result = expensive_computations(item)
        results.append(result)
    return results

# Generating a huge dataset
data = [random.randint(1, 100) for _ in range(15000)]  # Same dataset size

# Measure time with lru_cache
start_time = time.time()
results = process_data(data)
end_time = time.time()

print(f"Processing time with lru_cache: {end_time - start_time:.2f} seconds")
