# text_extraction_wash.py
import pandas as pd
file="/home/caratred/Downloads//D110.csv"
data = pd.read_csv(file)
# print(data,"$"*100)
import numpy as np
pp = np.array_split(data, 3)
oo = 1
for i in pp:
    print(i,">"*100,"\n\n")
    i.to_csv(f"/home/caratred/Downloads/{oo}.csv")
    oo+=1
# data.to_excel("/home/caratred/Downloads/J104-APRIL-2023.xlsx")

