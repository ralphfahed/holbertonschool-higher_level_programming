#!/usr/bin/python3
"""
This module defines a class `Student` with public attributes
and methods to convert to/from JSON-style dictionaries.
"""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        Filters attributes if `attrs` list is provided.
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values
        from the given json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
