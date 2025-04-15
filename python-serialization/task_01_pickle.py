import pickle
"""Importing pickle module to handle serialization and deserialization of custom Python objects."""


class CustomObject:
    """Custom class with attributes for name, age, and is_student, and methods to serialize and deserialize."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance with name, age, and is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the CustomObject in a formatted manner."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle.
        
        Args:
            filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle.
        
        Args:
            filename (str): The name of the file to load the object from.
        
        Returns:
            CustomObject or None: The deserialized object or None if error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
