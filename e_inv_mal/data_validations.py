import pandas as pd
import json
validations = pd.read_excel("/home/caratred/Downloads/Malaysia Sandbox details/Malaysia Metadata.xlsx",sheet_name="Field Level Validation").fillna("").drop(["S.no","Error/Warning"],axis=1).to_dict("records")
# final = json.dumps(validations, indent=1)
with open('validation_error_messages.json', 'w') as fout:
    json.dump(validations, fout,indent=1)
print(validations)
