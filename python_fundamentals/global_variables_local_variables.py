import time
import numpy as np
start_time = time.time()
counter = 0
def count_items(items):
    global counter
    for item in items:
        counter += 1
print(time.time() -start_time)

count_items(np.arange(10000))

start_time = time.time()
def count_items1(items):
    counter = 0
    for item in items:
        counter += 1
print(time.time() -start_time)
count_items1(np.arange(10000))