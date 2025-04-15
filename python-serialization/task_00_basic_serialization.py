import json
"""Importing the built-in json module to handle serialization and deserialization."""


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.
    
    Args:
        data (dict): The data to serialize.
        filename (str): The name of the file where the data will be saved.
    """
    with open(filename, "w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load data from a JSON file and deserialize it into a Python dictionary.
    
    Args:
        filename (str): The name of the JSON file to load.
    
    Returns:
        dict: The deserialized data as a Python dictionary.
    """
    with open(filename, "r") as file:
        return json.load(file)
