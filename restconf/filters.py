

class XML_FILTERS:

    def __init__(self) -> None:
        self.root_endpoint = "/restconf"
        self.schema_endpoint = "/ietf-yang-library:modules-state"
        self.datastore_endpoint = "/data"
        self.operations_endpoint = "/operations"
        return
    
    def capability_schema(self) -> str:
        filter_ = f"{self.root_endpoint}{self.datastore_endpoint}{self.schema_endpoint}" 
        return filter_
    
    def config_filter(self) -> str:
        query = "?content=config"
        filter_ = f"{self.root_endpoint}{self.datastore_endpoint}{query}"
        return filter_
    
    def interfaces_filter(self, name:str|None=None, leaf:str|None=None) -> str:
        if name and not leaf:
            endpoint = f"/ietf-interfaces:interfaces-state/interface={name}"
            filter_ = f"{self.root_endpoint}{self.datastore_endpoint}{endpoint}" 
        elif name and leaf:
            endpoint = f"/ietf-interfaces:interfaces-state/interface={name}/{leaf}"
            filter_ = f"{self.root_endpoint}{self.datastore_endpoint}{endpoint}" 
        else:
            endpoint = "/ietf-interfaces:interfaces-state"
            filter_ = f"{self.root_endpoint}{self.datastore_endpoint}{endpoint}" 

        return filter_
    
    def operations(self) -> str:
        filter_ = f"{self.root_endpoint}{self.operations_endpoint}" 
        return filter_

if __name__ == "__main__":
    filters = XML_FILTERS()
    print(filters.operations())