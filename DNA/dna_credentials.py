import requests
import json

class Credentials:

    def __init__(self) -> None:
        self.base_url = "https://sandboxdnac.cisco.com"
        self.auth_endpoint = "/dna/system/api/v1/auth/token"
        self.username = "devnetuser"
        self.password = "Cisco123!"
        self.auth = (self.username, self.password)
        self.headers = {
            "Accept":"application/json",
            "Content-Type":"application/json",
            "x-auth-token": self.authenticate()
        }

    def authenticate(self) -> str:
        response = requests.get(url=f"{self.base_url}{self.auth_endpoint}", auth=self.auth, verify=False).json()
        return response.get("x-token-auth", None)
    
    def get_cli_creds(self) -> None:
        endpoint = "/dna/intent/api/v1/global-credential"
        params = {
            "credentialSubType":"CLI"
        }
        response = requests.get(url=f"{self.base_url}{endpoint}", headers=self.headers, params=params).json()
        return response.get("response", None).get("id", None)


import requests
from dotenv import load_dotenv
import json
import xmltodict
import os

load_dotenv()

class REST:

    def __init__(self) -> None:
        self.username = os.getenv("username")
        self.password = os.getenv("password")
        self.base_url = "https://192.168.1.200:443"
        self.root_finder_endpoint = "/.well-known/host-meta"
        self.root_endpoint = "/restconf"
        self.auth = (self.username, self.password)
        self. headers={
            "Accept":"application/yang-data+json"
            }

    def request_method(self, method:str, data:dict|None) -> dict:
        session = requests.session()
        match method:
                case "get":
                    resp = session.get(url=f"{self.base_url}{self.root_finder_endpoint}", headers=session.headers, verify=False).json()
                    return resp
                case "post":
                    if data:
                        resp = 

    def request(self, auth:bool=False, method:str="get", data:dict|None=None) -> dict|str:
        if auth:
            resp = requests.get(url=f"{self.base_url}{self.root_finder_endpoint}", auth=self.auth, headers=self.headers, verify=False)
            return resp
        else:

if __name__ == "__main__":
    print("hello")
    c = Credentials()
    print(c.authenticate())
