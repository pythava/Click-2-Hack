import xml.etree.ElementTree as ET

def load_port_info(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    port_info = {}

    for port in root.findall("port"):
        number = int(port.get("number"))

        service = port.findtext("service", default="")
        version = port.findtext("version", default="")
        state = port.findtext("state", default="unknown")

        port_info[number] = {
            "service": service,
            "version": version,
            "state": state,
        }

    return port_info