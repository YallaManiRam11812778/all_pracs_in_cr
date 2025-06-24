# numpy_example_prac.py
import numpy as np
inside_second_element = np.array([[["a", "1"], ["c", "d"], ["e", "f"]],
                                  [["g", "h"], ["i", "3"], ["k", "l"]]])

print("shape\t------------------------",inside_second_element.shape)
print("size\t++++++++++++++++++++++++++",inside_second_element.size)
print("dtype\t___________________",inside_second_element.dtype)
# inside_second_element[1,1,1] =  inside_second_element[1,1,1].astype(int)
# inside_second_element[1,1,1].dtype = inside_second_element[1,1,1].astype(int)
# print(inside_second_element[1,1,1].dtype)
print("ndim\t***********************",inside_second_element.ndim,"//////////")
print(np.full((2,3,4,5),4).flatten(),">>>>>>>>>>>>>>>>")
import sys
a = np.unique([100,88,87,87,88,99,100])
print(a)
import pandas as pd

print(pd.DataFrame(a))
sys.exit()
print(np.ones((2,2,2)))
# print(np.empty((2.2)))
print(np.arange(2,200,2))

list1 = [1,2,4,5]
list2 = [[7],[5]]

num_arr_l1 = np.array(list1)
num_arr_l2 = np.array(list2)

print(list1*2,num_arr_l1*2)
print("\n*********",list2*2,"\n--------------",num_arr_l2*list1,"\n++++++++++++++",list1*num_arr_l2)

list1.append("o")
print(list1)

print(np.append(num_arr_l1, "john"),"???????????????????")
print(num_arr_l1,"/////////////////////")
print(np.insert(num_arr_l1, 2 , 3))



# index = 0  means row wies horizontal x axis
a = list2
print(np.delete(a, 1, 0),"22222222222222")  # a = list , 1 = element , 0 = row wies horizontal x axis
