import json
from ncclient import manager
import xml.dom.minidom

m = manager.connect(host="10.0.15.118",port="830",username="admin",password="cisco",hostkey_verify=False)

netconf_reply = m.get_config(source="running")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

