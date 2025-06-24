# D140_reverse_revenue_tax_reconcilation.py
import pandas as pd
import numpy as np
file="/home/caratred/Downloads/D140_Reverse.xlsx"
df=pd.read_excel(file,header=0)
print(df.columns)

df=(df.set_index('trx_no')
   .reindex(range(df.trx_no.iat[0],df.trx_no.iat[-1]+1), fill_value='kali')
   .reset_index())
print(df.head(30))
split_string = 'kali'

split_indices = df[df['reversal_calculation'] == split_string].index

df.to_excel("/home/caratred/Downloads/fillnans.xlsx",index=False)
sum_not_zero=[]
print(split_indices)
lists = []
start = 0
for end in split_indices:
    lists.append(df.iloc[start:end])
    locking=df.iloc[start:end]
    locking["reversal_calculation"]=locking["reversal_calculation"].astype(float).round()
    if locking["reversal_calculation"].sum()!=0:
        sum_not_zero.append(locking)
    start = end + 1

lists.append(df.iloc[start:])
locking=df.iloc[start:]
if locking["reversal_calculation"].sum()!=0:
        sum_not_zero.append(locking)


not_zero_rows=pd.concat(sum_not_zero, axis=0, ignore_index=False)
not_zero_rows.to_excel("/home/caratred/Downloads/trashcan/sum_not_zero.xlsx", index=False)