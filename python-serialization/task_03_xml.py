import xml.etree.ElementTree as ET
"""Module for XML serialization and deserialization"""


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)
