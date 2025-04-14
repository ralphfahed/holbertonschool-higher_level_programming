#!/usr/bin/python3
"""
This module defines a class `Student` that represents a student with 
attributes first_name, last_name, and age. It also includes a method 
to retrieve a dictionary representation of the student instance, 
with an optional filtering of attributes.
"""

class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the provided first_name, 
        last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        Optionally filters the attributes to include only those specified 
        in the `attrs` list.

        Args:
            attrs (list, optional): A list of attribute names to include. 
                                     If None, all attributes are returned.

        Returns:
            dict: A dictionary representing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        
        # Only include attributes from the list 'attrs'
        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result
