# # e_inv_malay.py
# import pandas
# pd = pandas.read_excel("/home/caratred/Downloads/Malaysia Sandbox details/Malaysia Metadata.xlsx",sheet_name="Excel & JSON Input mapping")
# fields = pd["Excel Input Mapping"].tolist()

# count = 1
# new = []
# for i in pd["Fields"].tolist():
#     new.append({
#             "label": i,
#             "fieldname": str(i).lower().replace(" ","_").replace("-","_"),
#             "fieldtype": "Data",
#             "idx": count
#         })
#     count += 1
# print(new)

import pandas as pd
file = "/home/caratred/Downloads/mrp_stay_activity16420379.txt"
df = pd.read_csv(file, delimiter = "\t")
print(df)