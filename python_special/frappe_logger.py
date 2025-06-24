# frappe_logger.py
import requests

headers = {'Authorization': "token 7264a1d22d19d4c:55588ffaf6c143d"}
data = {
"image1":"/home/caratred/Downloads/pos_checks_images/pos_checks_images/cropped_image.png",
"prompt" : "Extract Outlet name, Table number, Page number, chk number, date in dd/mm/yyyy format,time in 24h format from this image.provide output without markdown."}
re = requests.post("http://192.168.1.102:8006/api/method/ezylicensing.ezylicensing.doctype.taxpayerdetail.pos_checks_extraction.generate_image_with_prompt",headers=headers,data=data)
print(re.json(),"U"*100)