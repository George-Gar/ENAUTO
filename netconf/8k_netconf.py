from ncclient import manager
from dotenv import load_dotenv
from filters import Filters
import os
import json
import xmltodict

#Load creds
load_dotenv()

class Client_Class(Filters):

    def __init__(self) -> None:
        super().__init__()
        self.username = os.getenv("ios_user")
        self.password = os.getenv("ios_password")
        self.port = 830

    def device(self, host:str) -> dict:
        return {
            "host":host,
            "username":self.username,
            "password":self.password,
            "port":self.port,
            "hostkey_verify": False
        }
    
    def capabilities(self, host:str) -> None:
        with manager.connect(**self.device(host=host)) as m:
            capabilities = m.server_capabilities
            [print(capability) for capability in capabilities if "yang" in capability.lower() and "cisco" in capability.lower() and "interface" in capability.lower()]

    def subtree_get(self, host:str, filter:str) -> None:
        with manager.connect(**self.device(host=host)) as m:
            response = m.get(filter=filter)
            json_resp = xmltodict.parse(response.xml)
        return json_resp


if __name__ == "__main__":
    host = "devnetsandboxiosxec8k.cisco.com"
    client = Client_Class()
    print(client.subtree_get(host=host, filter=client.int_subtree()))

    # print(client.subtree_get(host="192.168.1.200", filter=client.int_subtree()))


