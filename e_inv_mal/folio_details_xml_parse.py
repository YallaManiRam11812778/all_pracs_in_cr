import pandas as pd
import xmltodict
import sys
file = "/home/caratred/Downloads/KULDMFOL241218 .xml"
fileptr = open(file,"r")

index_count = 0

def group_header_child_field_values(x):
    x = pd.DataFrame.from_records(x)
    x = x[["@Name","FormattedValue"]]
    invoice_details = {key : value for (key,value) in zip(x["@Name"].tolist(), x["FormattedValue"].tolist())}
    return invoice_details

def group_header_pick_field_from_df(x):
    x = group_header_child_field_values(x["Field"])
    return x

def child_of_details_level_3(x):
    x = pd.DataFrame.from_records(x)
    x['Section']=x['Section'].map(group_header_pick_field_from_df)
    x = x["Section"].tolist()
    return x

def group_pick_details_from_df(x):
    if isinstance(x,dict):
        if isinstance(x["Details"],list):
            x = child_of_details_level_3(x["Details"])
    return x

xml_content= fileptr.read()
my_ordered_dict=xmltodict.parse(xml_content)
data = my_ordered_dict["CrystalReport"]["Group"]
df = pd.DataFrame(data=data)
# print(df)
# df.to_excel("/home/caratred/Downloads/xml_daframe.xlsx",index=False)
group_header = df["GroupHeader"].tolist()
group_header_df = pd.DataFrame.from_records(group_header)
group_header_df["Section"] = group_header_df["Section"].map(group_header_pick_field_from_df)
group_header_df = group_header_df["Section"].tolist()
group_header_df = pd.DataFrame.from_records(group_header_df)

every_counted_level_3_list = []

def count_needed_group_header_child_field_values(x):
    x = pd.DataFrame.from_records(x)
    x = x[["@Name","FormattedValue"]]
    invoice_details = {key : value for (key,value) in zip(x["@Name"].tolist(), x["FormattedValue"].tolist())}
    return invoice_details

def count_needed_group_header_pick_field_from_df(x,count):
    x = count_needed_group_header_child_field_values(x["Field"])
    x= x | {"index_count":count}
    every_counted_level_3_list.append(x)
    return x

def count_needed_child_of_details_level_3(x,count):
    x = pd.DataFrame.from_records(x)
    x['Section']=x['Section'].apply(lambda x : count_needed_group_header_pick_field_from_df(x,count))
    x = x["Section"].tolist()
    return x

def count_needed_group_pick_details_from_df(x):
    global index_count
    if isinstance(x,dict):
        if isinstance(x["Details"],list):
            x = count_needed_child_of_details_level_3(x["Details"],index_count)
    index_count+=1
    return x

group = df["Group"].to_list()
group_df = pd.DataFrame.from_records(group)
group_df = group_df.map(count_needed_group_pick_details_from_df)
new_df = pd.DataFrame.from_records(every_counted_level_3_list)
# print(new_df,">"*100)
# merged_df = pd.merge(group_header_df, new_df, left_on='county_ID', right_on='countyid')
# print(merged_df)