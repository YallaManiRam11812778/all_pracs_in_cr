import xml.etree.ElementTree as ET
def minify_xml(xml_string):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        print(f"Error in Parsing XML... {str(e)}")
    return ET.tostring(root, encoding="unicode", method="xml")

file = "/home/caratred/Downloads/output_27942.xml"
file_new = "/home/caratred/Downloads/output_27942_new.xml"
with open(file, 'rb') as f:
    xml_data = f.read()
    data_str = minify_xml(xml_data)
    with open(file_new, "w") as file:
        file.write(data_str)