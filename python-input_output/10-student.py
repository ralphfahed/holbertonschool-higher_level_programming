#!/usr/bin/python3
"""
This module defines a Student class with methods to retrieve
a dictionary representation of the Student instance.
"""


class Student:
    """
    This class defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include
                                     in the returned dictionary. If None,
                                     all attributes are included.

        Returns:
            dict: A dictionary representing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
