# a = []    
# with open("/home/caratred/frappe-bench/sites/site.local/logs/ezylicensing_spacy_text_HYT-01.log", 'r') as f:
#     for line in f:
#             a.append(line.lstrip("ezylicensing_spacy_text_HYT-01"))

# with open('/home/caratred/frappe-bench/sites/site.local/logs/ezylicensing_spacy_text_HYT-01.txt', 'w') as f:
#     for line in a:
#         f.write(f"{line}")
filters = """{"business":"opopo","cm":["like","%carat op%"],"name":["in",["43","46","65"]],"number":["!=","3"]}"""
from ast import literal_eval
filters = literal_eval(filters)
a = " and ".join((((f"{key} {str(value[0]) + ' '  + f'{tuple(value[1])}'}") if type(value[1])==list or type(value[1])==tuple else f"""{key} {value[0]} '{value[1]}'""" if isinstance(value[1],str) else f"""{key} {value[0]} {value[1]}""") if type(value)==list else f"{key} = '{value}'" for key, value in filters.items()))
print(a)
