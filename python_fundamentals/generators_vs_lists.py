import time
start_time = time.time()
# squares = [x**2 for x in range(1_000_000)]
squares = (x**2 for x in range(1_000_000))
print(time.time() -start_time)
