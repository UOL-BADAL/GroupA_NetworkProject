import base64
import pickle
import json
import xml.etree.ElementTree as ET

def dictionary_to_binary(data: dict):
    """
    Params:
        - data: dict -> the dictionary to convert to binary
    Returns: 
        - serialised_dict: bytes -> binary representation of the dictionary
    """
    serialised_dict = base64.b64encode(pickle.dumps(data))
    return serialised_dict

def dictionary_to_json(data: dict):
    """
    Params:
        - data: dict -> the dictionary to convert to JSON
    Returns: 
        - serialised_dict: str -> the JSON representation of the dictionary
    """
    serialised_dict = json.dumps(data)
    return serialised_dict

def dictionary_to_xml(data: dict):
    """
    Params:
        - data: dict -> the dictionary to convert to XML
    Returns: 
        - serialised_dict: bytes -> the XML representation of the dictionary
    """
    root = ET.Element('dict')
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    serialised_dict = ET.tostring(root)
    return serialised_dict



def binary_to_dictionary(data: bytes):
    """
    Params:
        - data: bytes -> the bynary data to convert
    Returns: 
        - my_dict: dict -> the dictionary extracted from the binary data
    """
    my_dict = pickle.loads(base64.b64decode(data))
    return my_dict

def json_to_dictionary(data: str):
    """
    Params:
        - data: str -> the JSON string to convert
    Returns: 
        - my_dict: dict -> the dictionary extracted from the JSON string
    """
    my_dict = json.loads(data)
    return my_dict

def xml_to_dictionary(data: bytes):
    """
    Params:
        - data: bytes -> the XML bytes to convert
    Returns: 
        - my_dict: dict -> the dictionary extracted from the XML bytes
    """
    root = ET.fromstring(data)
    my_dict = {}
    for child in root:
        my_dict[child.tag] = child.text
    return my_dict
