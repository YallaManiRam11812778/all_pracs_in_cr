import threading
import time
# def worker(i):
#     print(f"Entered worker {i}")
#     time.sleep(1)
#     print(f"Ended up {i}")

# def on_done():
#     print(">>>>>>>>>>>>>>")
# threads = []
# for i in range(1,3):
#     thread = threading.Thread(target=worker, args=[i],daemon='')
#     thread.start()
#     threads.append(thread)
# # time.sleep(5)
# print(threads)
# threadSet = set(threads)
# # while len(threadSet) > 0:
#     # time.sleep(1)
# for thread_bro in threadSet:
#     # while thread_bro.is_alive():
#     #     print("thread now terminated ================ ")
#     if not thread_bro.is_alive():
#         print ("Thread "+" terminated")
#         threadSet.remove(thread_bro)
# while not thread.is_alive():
    # print("%"*100)
# Loop until both threads have finished
# while thread.is_alive()
#     # Check for new results in the queue every 0.1 seconds
#     try:
#         result = q.get(timeout=0.1)
#         print(result)
#     except queue.Empty:
#         pass
list1 = [4, 4, 1, 1, 0]
# ---
from collections import Counter

counts = Counter(list1)  # > Counter({4: 3, 1: 1, 5: 1})
print(counts.values())
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)
checking_all_same_or_not = all_equal(counts.values())
print(checking_all_same_or_not)
# total = sum(count>1 for count in counts.values())

# print(total)