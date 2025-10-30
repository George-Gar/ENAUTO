import requests
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")
base_url = "https://192.168.1.200:443"
root_finder_endpoint = "/.well-known/host-meta"
root_endpoint = "/restconf"
auth = (username, password)
headers={
    "Accept":"application/yang-data+json"
}

r = requests.get(url=f"{base_url}{root_endpoint}", auth=auth, headers=headers, verify=False)
print(username)
print(r.text)
