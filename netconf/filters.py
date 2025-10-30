

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

if __name__ == "__main__":
  c = Filters()
  print(c.int_subtree())
