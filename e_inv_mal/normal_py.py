pdfs = [
    # "/home/caratred/Downloads/Inv223682_Wedd-Tam Wei Ping & Kevin Low.pdf",
    # "/home/caratred/Downloads/Inv220201_Fraser & Neave Malaya Sdn Bhd.pdf",
    # "/home/caratred/Downloads/Inv220165_ECP Global Events Sdn Bhd.pdf",
    # "/home/caratred/Downloads/Inv220163_UMW Corporation Sdn Bhd.pdf",
    # "/home/caratred/Downloads/Inv219570_Rafaz Rich Resource.pdf",
    # "/home/caratred/Downloads/Inv219518_Celcom_Rental April 2024_.pdf",
    # "/home/caratred/Downloads/Inv218582 - PETRONAS Technical Training Sdn Bhd.pdf",
    # "/home/caratred/Downloads/Inv214961_Tenaga Nasional Berhad.pdf",
    "/home/caratred/Downloads/Inv181500_Affin Bank Berhad.pdf",
]

def file_parsing(pdf:str):
    import tabula
    import pandas as pd
    import numpy as np
    file_naming = pdf.split("/")[-1].split(".pdf")[0]
    """ Take Units if in pixels (px/96 dpi) * 72 """
    Top = A = 96.75
    Left = B = 400.75
    Areas_Width = C = 150
    Areas_Length = D = 120
    invoice_details = tabula.read_pdf(pdf, area=[[A,B,A+D,B+C]], pandas_options={'header':None},pages='1')[0]
    invoice_details[1] = invoice_details[1].str.replace(":","").str.strip()
    invoice_details = dict(zip(invoice_details[0],invoice_details[1]))


    """ Take Units if in pixels (px/96 dpi) * 72 """
    Top = A = 115
    Left = B = 15
    Areas_Width = C = 226
    Areas_Length = D = 80
    guest_address = tabula.read_pdf(pdf, area=[[A,B,A+D,B+C]], pandas_options={'header':None},pages='1')[0][0].tolist()
    guest_address = " ".join(guest_address)

    """ Take Units if in pixels (px/96 dpi) * 72 """
    Top = A = 218.25
    Left = B = 11.25
    Areas_Width = C = 570
    Areas_Length = D = 542

    entire_data_extraction = tabula.read_pdf(pdf, pages='all', area=[[A,B,A+D,B+C]],guess=True,columns=[55,400,450,520])
    listing_all_individual_dfs_to_one_list = []

    for i in entire_data_extraction:
        i = i.drop(i[(i['Charges'] == "MYR") & (i['Pmts/Credits'] == "MYR") & (i["Amount Due"] == "MYR")].index)
        i.dropna(axis = 0, how = 'all', inplace = True)
        i["T_F"] = i["Date"].str.contains(r'(?![\d_])\w')
        mask = i.index[i['T_F'] == True].tolist()
        
        if len(mask)>0:
            i.drop(i.loc[mask[0]:].index, inplace=True)
        i.drop("T_F",axis=1,inplace=True)
        listing_all_individual_dfs_to_one_list.append(i)
    listing_all_individual_dfs_to_one_list = pd.concat(listing_all_individual_dfs_to_one_list, ignore_index=True)

    fetching_indexes_based_on_string = listing_all_individual_dfs_to_one_list["Reference/Description"].str.contains("Guest Total")

    index_numbers_by_fetching_from_ref_des_col = listing_all_individual_dfs_to_one_list[fetching_indexes_based_on_string].index
    index_numbers_by_fetching_from_ref_des_col = list(index_numbers_by_fetching_from_ref_des_col)

    index_numbers_by_fetching_from_ref_des_col.append(listing_all_individual_dfs_to_one_list.index[-1]+1)

    list_of_indexes_based_on_col = []
    first_index = 0
    for i in index_numbers_by_fetching_from_ref_des_col:
        list_of_indexes_based_on_col.append((first_index,i))
        first_index=i+1

    mapping_index_numbers_where_guest_total_occured = [listing_all_individual_dfs_to_one_list.iloc[range(*i),:] for i in list_of_indexes_based_on_col]

    for i in range(0,len(mapping_index_numbers_where_guest_total_occured)):
        if len(mapping_index_numbers_where_guest_total_occured[i])>0:
            
            date_or_nan = mapping_index_numbers_where_guest_total_occured[i]["Date"].tolist()
            date_or_nan = date_or_nan[0]
            if np.nan_to_num(date_or_nan, 0)==0:
                guest_ref = mapping_index_numbers_where_guest_total_occured[i]["Reference/Description"].tolist()[0]
                # removing first row because it is reference name which should be tagged for every record
                mapping_index_numbers_where_guest_total_occured[i] = mapping_index_numbers_where_guest_total_occured[i].iloc[1:]
                mapping_index_numbers_where_guest_total_occured[i]["tagging_member_with_room"] = guest_ref
            else:
                mapping_index_numbers_where_guest_total_occured[i]["tagging_member_with_room"] = ""
            mapping_index_numbers_where_guest_total_occured[i] = mapping_index_numbers_where_guest_total_occured[i].where(pd.notnull(mapping_index_numbers_where_guest_total_occured[i]), None)
            mapping_index_numbers_where_guest_total_occured[i]["hash_tag"] = mapping_index_numbers_where_guest_total_occured[i].apply(lambda x: None if x['Date'] == None  else "", axis = 1)
            mapping_index_numbers_where_guest_total_occured[i] = mapping_index_numbers_where_guest_total_occured[i][["Date","Reference/Description","hash_tag",
                                                                                                                    "Charges","Pmts/Credits","Amount Due","tagging_member_with_room"]]
            
            mapping_index_numbers_where_guest_total_occured[i].loc[:,["Reference/Description","hash_tag"]] = mapping_index_numbers_where_guest_total_occured[i][["Reference/Description","hash_tag"]].fillna(method="ffill", axis=1, limit=1)
            
            hash_tag_cutting_first_row = mapping_index_numbers_where_guest_total_occured[i]["hash_tag"].to_list()
            hash_tag_cutting_first_row = ["!@#$%^&*()$%^&*()" if x == '' else x for x in hash_tag_cutting_first_row]
            hash_tag_cutting_first_row = " ".join(hash_tag_cutting_first_row)
            hash_tag_cutting_first_row = hash_tag_cutting_first_row.split("!@#$%^&*()$%^&*()")
            hash_tag_cutting_first_row.pop(0)
            
            mapping_index_numbers_where_guest_total_occured[i].dropna(subset=['Date'], inplace=True)
            mapping_index_numbers_where_guest_total_occured[i]["hash_tag"] = hash_tag_cutting_first_row
        
        
    mapping_index_numbers_where_guest_total_occured = pd.concat(mapping_index_numbers_where_guest_total_occured, ignore_index=True)
    mapping_index_numbers_where_guest_total_occured["T_F"] = mapping_index_numbers_where_guest_total_occured["Reference/Description"].str.contains('%', regex= True, na=False)
    mapping_index_numbers_where_guest_total_occured["service_tax"] = mapping_index_numbers_where_guest_total_occured.apply(lambda col : col["Reference/Description"] if col["T_F"]==True else False, axis = 1)

    service_tax_values = mapping_index_numbers_where_guest_total_occured.index[mapping_index_numbers_where_guest_total_occured['service_tax'] != False].tolist()
    # service_charges_values = mapping_index_numbers_where_guest_total_occured["Charges"].tolist()

    indexes_fetching_from_service_tax_col_and_should_be_removed = list(service_tax_values)

    values_from_service_tax_col = mapping_index_numbers_where_guest_total_occured["service_tax"].tolist()
    values_from_service_tax_col.pop(0)
    values_from_service_tax_col.append(False)
    values_from_service_tax_col = ["True" if i==True else None if i==False else i for i in values_from_service_tax_col]

    # service_charges_values.pop(0)
    # service_charges_values.append(np.nan)

    mapping_index_numbers_where_guest_total_occured = mapping_index_numbers_where_guest_total_occured.drop("T_F",axis=1)
    mapping_index_numbers_where_guest_total_occured["service_tax"] = values_from_service_tax_col
    mapping_index_numbers_where_guest_total_occured["service_tax"].fillna("",inplace=True)
    mapping_index_numbers_where_guest_total_occured = mapping_index_numbers_where_guest_total_occured[~mapping_index_numbers_where_guest_total_occured.index.isin(indexes_fetching_from_service_tax_col_and_should_be_removed)]
    mapping_index_numbers_where_guest_total_occured.reset_index(inplace=True,drop=True)
    mapping_index_numbers_where_guest_total_occured["service_tax_rate"] = mapping_index_numbers_where_guest_total_occured.apply(lambda x : str(x["service_tax"]).split("%")[0].split()[-1] if len(str(x["service_tax"]))>0 else "",axis=1)
    charges_for_multiplication = mapping_index_numbers_where_guest_total_occured["Charges"].tolist()

    service_tax_rate_for_multiplication = mapping_index_numbers_where_guest_total_occured["service_tax_rate"].tolist()
    service_tax_rate_for_multiplication = [float(x.strip().replace(",","") or 0) for x in service_tax_rate_for_multiplication]
    charges_for_multiplication = ["" if i is None else i.replace(",","") for i in charges_for_multiplication]
    charges_for_multiplication = [float(x.strip() or 0) for x in charges_for_multiplication]
    charges_for_multiplication = np.asarray(charges_for_multiplication)
    service_tax_rate_for_multiplication = np.asarray(service_tax_rate_for_multiplication)
    
    multi = np.multiply(charges_for_multiplication,service_tax_rate_for_multiplication)
    multi = np.round(np.divide(multi,100), decimals=2)
    mapping_index_numbers_where_guest_total_occured["Service_Charges"] = multi
    return {"invoice_details":invoice_details,"guest_address":guest_address,"entire":mapping_index_numbers_where_guest_total_occured.to_dict("records")}

parsed_file = file_parsing(pdfs[0])