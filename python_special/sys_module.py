# sys_module.py
# import sys
# import time
# sys.stdout.write("[")
# for i in range(0,10):
#     time.sleep(.1)
#     sys.stdout.write("#")
#     sys.stdout.flush()
# sys.stdout.write("]")


from itertools import permutations
paths = permutations([1, 2, 3,4,5,2])  # Generate all permutations of the list [1, 2, 3]
po = []
paths = [po.append(i) for i in paths]
o = 0
for path in paths:
    o+=1
    print(path,o)
print(len(paths))