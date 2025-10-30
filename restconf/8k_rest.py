import requests
import json

base_url = "https://192.168.1.200:443"
api_resource_path = "/restconf"
username = "george"
password = "George1347$"
headers = {
    "Accept":"application/yang-data+json"
}
auth = (username,password)

response = requests.get(url=f"{base_url}{api_resource_path}", headers=headers, auth=auth, verify=False)
print(response.text)

