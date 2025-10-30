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
        self.username = os.getenv("username")
        self.password = os.getenv("password")
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
        """
        Method for discovering device capabilities
        PARAMS:
            <host>: ip or domain of device to run operation on
        """
        with manager.connect(**self.device(host=host)) as m:
            capabilities = m.server_capabilities
            [print(capability) for capability in capabilities if "yang" in capability.lower() and "cisco" in capability.lower() and "interface" in capability.lower()]

    def subtree_get(self, host:str, filter:str) -> json:
        """
        Method for executing an RPC <get> operarion
        PARAMS:
            <host>: ip or domain of device to run operation on
            <filter>: xml filter and body
        """
        with manager.connect(**self.device(host=host)) as m:
            response = m.get(filter=filter)
            json_resp = json.dumps(xmltodict.parse(response.xml))
        return json_resp
    
    def xpath_get(self, host:str, filter:str) -> json:
        """
        Method for executing an RPC <get> operarion
        PARAMS:
            <host>: ip or domain of device to run operation on
            <filter>: xml filter and body
        """
        with manager.connect(**self.device(host=host)) as m:
            response = m.get(filter=filter)
            json_resp = json.dumps(xmltodict.parse(response.xml))
        return json_resp
    
    def edit_config(self, host:str, config:str, target:str) -> json:
        """
        Method for pushing configuration to a target datastore
        PARAMS:
            <host>: ip or domain of device to run operation on
            <filter>: xml configuration body
            <targer>: target datastore
        """
        with manager.connect(**self.device(host=host)) as m:
            response = m.edit_config(target=target, config=config)
            json_resp = json.dumps(xmltodict.parse(response.xml))
            return json_resp


if __name__ == "__main__":
    host = "192.168.1.200"
    client = Client_Class()
    #print(client.edit_config(host=host, target="running", config=client.ip_int_config()))

    print(client.xpath_get(host=host, filter=client.int_xpath()))
    # print(client.subtree_get(host="192.168.1.200", filter=client.int_subtree()))


