

class Filters:

    def __init__(self) -> None:
        return
    
    def int_subtree(self) -> str:
        filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
</filter>
"""
        return filter
    
    def ip_int_config(self):
        config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
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
