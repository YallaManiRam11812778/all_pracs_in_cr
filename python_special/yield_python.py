

# # Reading huge file by comparing for loop and yield
# import time

# start_time = time.time()
# def fetching_lines(filename):
#     with open(filename,"r") as file:
#         lines = []
#         for line in file:
#             lines.append(line)
#         # print(lines)
#         return lines
    

# def fetching_lines_through_yield(filename):
#     with open(filename,"r") as file:
#         yield from file

# file_path = fetching_lines_through_yield("output-3407.txt")
# print(len(list(file_path)))
# # print(list(file_path))
# # print("--- %s seconds ---" % (time.time() - start_time))



# # yield_python.py
# def yielding(listy):
#     for i in listy:
#         yield i
# a = [1,2,3]
# # for i in a
# b = yielding(a)
# print(next(b))
# print(next(b))
# print(list(b))
# def randd():
#     yield from yielding(a)

# yield_python.py
import pandas as pd
import numpy as np
d110 = [{"trx_no":101,"guest_name":"Ram","room":"01"},{"trx_no":105,"guest_name":"Veeru","room":"04"}]
d140 = [{"trx_no":102,"guest_name":"Ram","room":"01"},{"trx_no":102,"guest_name":"Ram","room":"01"},{"trx_no":104,"guest_name":"Ram","room":"01"},{"trx_no":106,"guest_name":"Veeru","room":"04"},{"trx_no":107,"guest_name":"veeru","room":"04"},{"trx_no":108,"guest_name":"Veeru","room":"04"},{"trx_no":109,"guest_name":"Veeru","room":"05"}]

df_right = pd.DataFrame.from_dict(d110)
df_left = pd.DataFrame.from_dict(d140)

df_all = pd.concat([df_right,df_left], ignore_index=True)
df_all = df_all.sort_values(by=['trx_no',"guest_name","room"], ascending=True)

df_all = df_all.groupby(['guest_name','trx_no', "room"],as_index=True).sum().reset_index()


df_list = [d for _, d in df_all.groupby(['room',"guest_name"])]

df_list = [np.array(d) for d in df_list]



def creating_dataframe_through_yield(df_list):
    all_dfs = []
    for i in df_list:
        all_dfs.append(creating_df(i))
    return all_dfs
    # yield creating_df(df_list)

def creating_df(list_is):
    df = pd.DataFrame(list_is, columns=["guest_name", "trx_no","room"])
    df.set_index("trx_no",inplace=True)
    yield df


trx_data_to_dfs = creating_dataframe_through_yield(df_list)
# for i in trx_numbers:
#     print(list(i))
trx_num_to_list = np.concatenate(df_list,axis=0).T[1]


# combining_for_getting_trx_numbers = np.concatenate(trx_numbers,axis=0)
# print(combining_for_getting_trx_numbers,">"*100)
# combined_and_got_trx_numbers = combining_for_getting_trx_numbers.T[1]
# combined_and_got_trx_numbers = list(combined_and_got_trx_numbers)

print(np.flatnonzero(np.diff(trx_num_to_list)!=1)+1,">"*1000)
separated_df_is = np.split(trx_data_to_dfs, (np.flatnonzero(np.diff(trx_num_to_list)!=1)+1))
# for i in separated_df_is:    
#     print(list(i))
for i in separated_df_is:
    # print(i)
    for j in i:
        print(list(j))

# # for i in (0,len(trx_numbers)):
# #     print(trx_numbers[0].T[1])

# # all_dfs = []
# # for i in df_list:
# #     df_is = pd.DataFrame(i, columns= ['guest_name', 'trx_no', 'room'])
# #     df_is.set_index("trx_no",inplace=True)
    
# #     arr = df_is.index.values.tolist()
# #     separated_df_is = np.split(df_is, (np.flatnonzero(np.diff(arr)!=1)+1))

# #     for separated_df in separated_df_is:
# #         all_dfs.append(separated_df)

# # for i in all_dfs:
# #     print("#"*100,i,"\n","----",len(i),"\n\n")