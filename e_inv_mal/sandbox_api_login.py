import requests

auth_url = "https://preprod-api.myinvois.hasil.gov.my/connect/token"
client_id = "7da73f71-e5af-439b-bfd3-78f5587a505b"
client_secret = "9f51a310-0be3-42e4-adfd-4b3bf740a6a0"

payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
}

response = requests.post(auth_url, data=payload)

if response.status_code == 200:
    access_token = response.json().get("access_token")
    print("Access Token:", access_token)
else:
    print("Failed to retrieve access token")
    print("Status Code:", response.status_code)
    print("Response:", response.json())
