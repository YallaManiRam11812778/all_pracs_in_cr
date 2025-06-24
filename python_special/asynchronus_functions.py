# asynchronus_functions.py
# import requests
# from requests import Response

# response : Response = requests.get("http://192.168.1.102:8003/api/resource/WF%20Workflow%20Requests")

# print(response.json(),"................")


fibonacci_memo = {}

import functools
# import time
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(99919)
@functools.cache
def fibonacci(k):
    if k < 2:
        return k
    # if k not in fibonacci_memo:

    fibonacci_memo[k] = fibonacci(k-2) + fibonacci(k-1)
    # print(fibonacci_memo[k],"-"*100,k)
    # time.sleep(1)
    return fibonacci_memo[k]
a =fibonacci(9990)
print(a,"^"*100)