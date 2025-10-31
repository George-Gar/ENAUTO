

class Filters:

    def __init__(self) -> None:
        return
    
    def int_subtree(self) -> str:
        filter_ = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
</filter>
"""
        return filter_
    
    def int_xpath(self, name:str) -> tuple:
        """
        Method for providing the xpath filter to get the specified interface by name
        PARAMS:
          <name>: name of specified interface
        """
        ns_map = {'if': 'urn:ietf:params:xml:ns:yang:ietf-interfaces'}
        xpath = f"/if:interfaces/if:interface[if:name={name}]"
        filter_ = ("xpath", (ns_map, xpath))

        return filter_

    def ip_int_config(self):
        config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface xmlns:nf="urn:ietf:params:xml:ns:netconf:base:1.0" nf:operation="create">
      <name>GigabitEthernet2</name>
      <enabled>false</enabled>
    </interface>
  </interfaces>
</config>
"""
        return config

if __name__ == "__main__":
  c = Filters()
  print(c.int_subtree())
