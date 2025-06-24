d = dict(apple=4, orange=5, pear=6, pineapple=7)
a = {1:1,2:2}
b={"apple":33,44:4}
x= {**d,**b,**a}
print(x)

# first error in code
# second error in code
# partial functions
# lambda with dataframe
# lambda normal
# list comprehension
# dict comprehension
from functools import lru_cache
@lru_cache
def a():
    try:
        while True:
            import time
            time.sleep(2)
    except KeyboardInterrupt:
        print('\n Control "C" clicked or Interrupted')
a()