import requests, uuid, json
import pandas as pd
from ast import literal_eval
# Add your key and endpoint
key = "c955a0f41d2948f6b23fb8b5232f1e42"        #"<your-translator-key>"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "southeastasia"        #"<YOUR-RESOURCE-LOCATION>"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'ko',
    'to': ['en']
}

uio = pd.read_excel("Combination of google tranlator and Azure Translated_korean_sheet.xlsx")
# print(uio.columns)
supplier_name = uio["Supplier name"].tolist()
product_name = uio["Product name"].tolist()
supplier_name_aws = []
product_name_aws = []


headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}
for i in supplier_name:
    body = [{
            'text': i
        }]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    translations_response = json.dumps(response)
    if isinstance(translations_response,str):
        translations_response = literal_eval(translations_response)
    supplier_name_aws.append(translations_response[0]["translations"][0]["text"])

for j in product_name:
    body = [{
            'text': j
        }]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    translations_response = json.dumps(response)
    if isinstance(translations_response,str):
        translations_response = literal_eval(translations_response)
    product_name_aws.append(translations_response[0]["translations"][0]["text"])

print(supplier_name_aws,"\n\n",product_name_aws,"\n\n")
uio["Product name AWS"] = product_name_aws
uio["Supplier name AWS"] = supplier_name_aws
uio.to_excel("Combination of google tranlator and Azure Translated_korean_sheet.xlsx",index=False)
print("#"*100)