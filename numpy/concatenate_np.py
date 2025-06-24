import numpy as np
import pandas as pd
one_dim_array_1 = ["a","b","c"]
one_dim_array_2 = ["d","e","f"]

one_d_arrays_conc = np.concatenate([one_dim_array_1, one_dim_array_2])
# print(one_d_arrays_conc)
# print(pd.DataFrame(one_d_arrays_conc))
two_dimension_array_1 = [["p","q","r"],["s","t","u"]]
two_dimension_array_2 = [["v","w","x"],["y","z","a"]]

two_dimen_arr_conc = np.vstack([two_dimension_array_1,two_dimension_array_2])
print(two_dimen_arr_conc,"\n")

two_dimen_arr_conc = np.hstack([two_dimension_array_1,two_dimension_array_2])
print(two_dimen_arr_conc,"\n")
print(pd.DataFrame(two_dimen_arr_conc))
two_dimen_arr_conc = np.dstack([two_dimension_array_1,two_dimension_array_2])
print(two_dimen_arr_conc,"\n")



# Splitting array
splitting_2d = np.array_split(two_dimen_arr_conc[0],4)
for i in splitting_2d:
    print(i,">"*100)