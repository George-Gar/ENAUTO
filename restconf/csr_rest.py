import requests
from dotenv import load_dotenv
from filters import XML_FILTERS
import json
import xmltodict
import os

load_dotenv()

class REST(XML_FILTERS):

    def __init__(self) -> None:
        super().__init__()
        self.username = os.getenv("username")
        self.password = os.getenv("password")
        self.base_url = "https://192.168.1.200:443"
        self.root_finder_endpoint = "/.well-known/host-meta"
        self.root_endpoint = "/restconf"
        self.session = requests.session()
        self.session.auth = (self.username, self.password)
        self.session.headers.update({
            "Accept":"application/yang-data+json",
            "Content-Type":"application/yang-data+json"
            })
        
    def request(self, endpoint:str, method:str='get', data:dict|None=None) -> json:
        match method:
            case "get":
                resp = self.session.get(url=f"{self.base_url}{endpoint}", verify=False).json()
                return resp
            case "post":
                if data:
                    resp = self.session.post(url=f"{self.base_url}{endpoint}", data=data, verify=False).json()
                    return resp
            case "put":
                if data:
                    resp = self.session.put(url=f"{self.base_url}{endpoint}", data=data, verify=False).json()
                    return resp
            case "patch":
                if data:
                    resp = self.session.patch(url=f"{self.base_url}{endpoint}", data=data, verify=False).json()
                    return resp

            
                    
if __name__ == "__main__":
    rest = REST()
    print(rest.request(endpoint=rest.operations()))