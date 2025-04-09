#!/usr/bin/env python3

# SwimMixin providing swimming ability
class SwimMixin:
    def __init__(self):
        # You could add initialization logic specific to swimming behavior
        print("SwimMixin initialized.")

    def swim(self):
        print("The creature swims!")

# FlyMixin providing flying ability
class FlyMixin:
    def __init__(self):
        # You could add initialization logic specific to flying behavior
        print("FlyMixin initialized.")

    def fly(self):
        print("The creature flies!")

# Dragon class inheriting from both SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def __init__(self, name, size):
        # Call the __init__ methods of the parent mixins
        super().__init__()  # This will call the __init__ of SwimMixin and FlyMixin

        # Initialize Dragon specific attributes
        self.name = name
        self.size = size
        print(f"{self.name} the dragon is initialized. Size: {self.size}")

    def roar(self):
        print("The dragon roars!")

# Instantiate a Dragon object
draco = Dragon("Draco", "Large")

# Test the abilities of Dragon
draco.swim()  # Inherited from SwimMixin
draco.fly()   # Inherited from FlyMixin
draco.roar()  # Specific to Dragon
