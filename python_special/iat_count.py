# iat_count.py
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
print(df_list)
df_list = [np.array(d) for d in df_list]

all_dfs = []
for i in df_list:
    df_is = pd.DataFrame(i, columns= ['guest_name', 'trx_no', 'room'])
    df_is.set_index("trx_no",inplace=True)
    
    arr = df_is.index.values.tolist()
    separated_df_is = np.split(df_is, (np.flatnonzero(np.diff(arr)!=1)+1))

    for separated_df in separated_df_is:
        all_dfs.append(separated_df)

for i in all_dfs:
    print("#"*100,i,"\n","----",len(i),"\n\n")