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
        """
        Method that returns a reusable device object to avoid repeating code
        """
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

    def manager_connect(self, host:str, filter:str, operation:str='get', target:str='candidate') -> str | json:
        """
        Method for handling the manager.connect context manager to avoid code repetition
        PARAMS:
            <host>: ip or domain of device to run operation on
            <filter>: xml filter or configuration
            <operation>: type of rpc operation
            <target>: the datastore we are targeting
                *default target is "candidate" options include ["running", "startup"]*
        """
        match operation:
            case "get":
                with manager.connect(**self.device(host=host)) as m:
                    response = m.get(filter=filter)
                    json_resp = json.dumps(xmltodict.parse(response.xml), indent=2)
                    return json_resp
            case "get_config":
                with manager.connect(**self.device(host=host)) as m:
                    response = m.get_config(source=target, filter=filter)
                    json_resp = json.dumps(xmltodict.parse(response.xml), indent=2)
                    return json_resp
            case "edit_config":
                with manager.connect(**self.device(host=host)) as m:
                    response = m.edit_config(target=target, config=filter)
                    json_resp = json.dumps(xmltodict.parse(response.xml), indent=2)
                    return json_resp
            case _:
                return "Enter Valid RPC operation"


    def subtree_get(self, host:str, filter:str) -> json:
        """
        Method for executing an RPC <get> operarion
        PARAMS:
            <host>: ip or domain of device to run operation on
            <filter>: xml filter and body
        """
        with manager.connect(**self.device(host=host)) as m:
            response = m.get(filter=filter)
            json_resp = json.dumps(xmltodict.parse(response.xml), indent=2)
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
            json_resp = json.dumps(xmltodict.parse(response.xml), indent=2)
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
            json_resp = json.dumps(xmltodict.parse(response.xml), indent=2)
            return json_resp


if __name__ == "__main__":
    host = "192.168.1.200"
    client = Client_Class()
    #print(client.edit_config(host=host, target="running", config=client.ip_int_config()))

    print(client.xpath_get(host=host, filter=client.int_xpath()))
    # print(client.subtree_get(host="192.168.1.200", filter=client.int_subtree()))


