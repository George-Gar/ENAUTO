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

response = requests.get(url=f"{base_url}{api_resource_path}/data/ietf-interfaces:interface", headers=headers, auth=auth, verify=False)
print(response.text)

# import requests
# import urllib3

# # Disable SSL warnings (sandbox uses self-signed cert)
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# base_url = "https://devnetsandboxiosxec8k.cisco.com/restconf"
# username = "garciag1646"
# password = "EM5v-66-yb0ciIs"

# headers = {
#     "Accept": "application/yang-data+json",
#     "Content-Type": "application/yang-data+json"
# }

# response = requests.get(
#     f"{base_url}/data/ietf-interfaces:interfaces",
#     headers=headers,
#     auth=(username, password),
#     verify=False
# )

# print("Status Code:", response.status_code)
# print("Response Text:", response.text)
