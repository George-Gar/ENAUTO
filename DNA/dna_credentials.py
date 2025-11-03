import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

class Credentials:

    def __init__(self) -> None:
        self.base_url = "https://sandboxdnac2.cisco.com"
        self.auth_endpoint = "/dna/system/api/v1/auth/token"
        self.username = os.getenv("devnetuser")
        self.password = os.getenv("devnetpassword")
        self.auth = (self.username, self.password)
        self.headers = {
            "Accept":"application/json",
            "Content-Type":"application/json",
            "x-auth-token": self.authenticate()
        }

    def authenticate(self) -> str:
        response = requests.post(url=f"{self.base_url}{self.auth_endpoint}", auth=self.auth, verify=False).json()
        return response.get("Token", None)
    
    def get_cli_creds(self) -> None:
        endpoint = "/dna/intent/api/v1/global-credential"
        params = {
            "credentialSubType":"CLI"
        }
        response = requests.get(url=f"{self.base_url}{endpoint}", headers=self.headers, params=params, verify=False).json()
        return response
    
    def get_devices(self) -> json:
        endpoint = "/dna/intent/api/v1/network-device"
        response = requests.get(url=f"{self.base_url}{endpoint}", headers=self.headers, verify=False).json()
        return response
    
    def get_sites(self) -> json:
        endpoint = "/dna/intent/api/v1/site"
        response = requests.get(url=f"{self.base_url}{endpoint}", headers=self.headers, verify=False).json()
        return response.get("response", None)
    
    def get_site_by_id(self) -> list:
        sites = self.get_sites()
        site_ids = []
        [site_ids.append(site['id']) for site in sites] 
        
        #get site by id for each id in site_ids list
        sites = []
        for id in site_ids:
            endpoint = "/dna/intent/api/v1/site" #repeating this for memorization
            response = requests.get(url=f"{self.base_url}{endpoint}?siteId={id}", headers=self.headers, verify=False).json()
            sites.append(response)
        
        return sites


if __name__ == "__main__":
    c = Credentials()
    print(c.get_devices())
