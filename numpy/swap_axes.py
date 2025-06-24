# enni list of lists unte anni axes untai
import numpy as np
list1 = [[  [["a"]],[["b"]],[["c"]],[["d"]],[["e"]]],
            
         [  
            [["p"]],[["q"]],[["r"]],[["s"]],[["t"]],
            ]]
nump_array = np.array(list1)
# print(nump_array,"\n&&&&&&&&&&&&&&&&&&&&&&&&&&\n",nump_array.swapaxes(3,0),"\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4\n",nump_array.swapaxes(2,0))
print(nump_array.swapaxes(0,3),"\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
inside_second_element = np.array([[["a", "1"], ["c", "d"], ["e", "f"]],
                                  [["g", "h"], ["i", "3"], ["k", "l"]]])