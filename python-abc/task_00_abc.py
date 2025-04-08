from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Subclass 1: Dog
class Dog(Animal):

    def sound(self):
        return "Bark"

# Subclass 2: Cat
class Cat(Animal):

    def sound(self):
        return "Meow"
