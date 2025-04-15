import xml.etree.ElementTree as ET

"""Module for serializing and deserializing Python dictionaries using XML format."""


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML data.

    Returns:
        None
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The XML filename to read.

    Returns:
        dict: The deserialized dictionary, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except Exception:
        return None
