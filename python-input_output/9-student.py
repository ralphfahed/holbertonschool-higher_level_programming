#!/usr/bin/python3
"""
This module defines a class Student with attributes and a method 
to return the dictionary description of an instance for JSON serialization.
"""


class Student:
    """
    A class representing a student.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.

    Methods:
        to_json(): Returns the dictionary representation of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the student instance with first name, last name, and age.

        Parameters:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary representation of a Student instance.

        Returns:
            dict: Dictionary of the student's attributes.
        """
        return self.__dict__

