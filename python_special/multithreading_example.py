# multithreading_example.py
import time

# Function to calculate sum of squares
def sum_of_squares(numbers):
    return sum([x * x for x in numbers])

# Example without multithreading
def no_multithreading():
    numbers = range(1, 10000000)
    start_time = time.time()
    
    result = sum_of_squares(numbers)  # Single-threaded execution
    
    end_time = time.time()
    print(f"Result: {result}")
    print(f"Time taken without multithreading: {end_time - start_time:.2f} seconds")

no_multithreading()

import time
from multiprocessing import Pool

# Function to calculate sum of squares
def sum_of_squares(numbers):
    return sum([x * x for x in numbers])

# Example with multiprocessing
def with_multiprocessing():
    numbers = range(1, 10000000)
    start_time = time.time()
    
    # Split the numbers into two halves
    part1 = list(numbers[:len(numbers)//2])
    part2 = list(numbers[len(numbers)//2:])
    
    with Pool(processes=2) as pool:
        # Map the function to the pool of processes
        results = pool.map(sum_of_squares, [part1, part2])
    
    total_result = sum(results)
    
    end_time = time.time()
    print(f"Result: {total_result}")
    print(f"Time taken with multiprocessing: {end_time - start_time:.2f} seconds")

with_multiprocessing()
