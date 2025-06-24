import sys
import time

# Sample data: a list of dictionaries
data = [{'a': i, 'b': i + 2, 'c': i * 2} for i in range(10000000)]  # Data with 1 million items

# Helper Function 1: Increases a number by 3 if even, else squares it
def transform_a(a):
    if a % 2 == 0:
        return a + 3
    else:
        return a ** 2

# Helper Function 2: Decreases a number by 1 if greater than 10, else doubles it
def transform_b(b):
    if b > 10:
        return b - 1
    else:
        return b * 2

# Helper Function 3: Multiplies a number by 5 if divisible by 3, else adds 7
def transform_c(c):
    if c % 3 == 0:
        return c * 5
    else:
        return c + 7

# Helper Function 4: Combines values of a and b, multiplies them if sum is greater than 20
def combine_a_b(a, b):
    if a + b > 20:
        return a * b
    else:
        return a + b

# Regular loop-based approach (storing results)
def process_data_with_list(data):
    processed_items = []  # List to store processed items
    for item in data:
        a, b, c = item['a'], item['b'], item['c']
        a = transform_a(a)
        b = transform_b(b)
        c = transform_c(c)
        combined = combine_a_b(a, b)

        if combined > 100:
            a = a // 2
        elif c < 50:
            b = b + 5
        else:
            c = c - 3

        processed_items.append({'a': a, 'b': b, 'c': c, 'combined': combined})
    
    return processed_items  # Return the full list of processed items

# Generator-based approach (lazy processing, no storage)
def process_data_with_generator(data):
    for item in data:
        a, b, c = item['a'], item['b'], item['c']
        a = transform_a(a)
        b = transform_b(b)
        c = transform_c(c)
        combined = combine_a_b(a, b)

        if combined > 100:
            a = a // 2
        elif c < 50:
            b = b + 5
        else:
            c = c - 3

        yield {'a': a, 'b': b, 'c': c, 'combined': combined}

# Return-based approach (accumulates results in a list and returns)
def process_data_with_return(data):
    processed_items = []  # List to store processed items
    for item in data:
        a, b, c = item['a'], item['b'], item['c']
        a = transform_a(a)
        b = transform_b(b)
        c = transform_c(c)
        combined = combine_a_b(a, b)

        if combined > 100:
            a = a // 2
        elif c < 50:
            b = b + 5
        else:
            c = c - 3

        processed_items.append({'a': a, 'b': b, 'c': c, 'combined': combined})
    
    return processed_items  # Return the full list of processed items

# Time and memory comparison for list-based approach (storing results)
start_time = time.time()
processed_with_list = process_data_with_list(data)
end_time = time.time()
list_time = end_time - start_time
list_memory = sys.getsizeof(processed_with_list)

# Time and memory comparison for generator-based approach (lazy processing)
start_time = time.time()
processed_with_generator = process_data_with_generator(data)
for _ in processed_with_generator:  # Consume the generator
    pass
end_time = time.time()
generator_time = end_time - start_time
generator_memory = sys.getsizeof(processed_with_generator)

# Time and memory comparison for return-based approach (storing results)
start_time = time.time()
processed_with_return = process_data_with_return(data)
end_time = time.time()
return_time = end_time - start_time
return_memory = sys.getsizeof(processed_with_return)

# Output results
print(f"Time taken with list (storing results in a list): {list_time:.5f} seconds")
print(f"Memory used with list (storing results): {list_memory} bytes")

print(f"Time taken with generator (lazy processing): {generator_time:.5f} seconds")
print(f"Memory used with generator (lazy processing): {generator_memory} bytes")

print(f"Time taken with return (storing results in a list): {return_time:.5f} seconds")
print(f"Memory used with return (storing results): {return_memory} bytes")
