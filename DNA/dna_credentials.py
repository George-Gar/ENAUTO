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

print("hello")
c = Credentials()
print(c.authenticate())
