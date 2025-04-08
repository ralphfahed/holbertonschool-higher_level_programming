#!/usr/bin/python3
'''
This script defines a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
'''

def inherits_from(obj, a_class):
    '''
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class, otherwise False.
    
    Parameters:
    obj: The object to check.
    a_class: The class to check against.
    
    Returns:
    True if obj is an instance of a subclass of a_class, False otherwise.
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
