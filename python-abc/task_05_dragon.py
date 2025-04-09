#!/usr/bin/env python3

# SwimMixin providing swimming ability
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# FlyMixin providing flying ability
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Dragon class inheriting from both SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Instantiate a Dragon object
draco = Dragon()

# Test the abilities of Dragon
draco.swim()  # Inherited from SwimMixin
draco.fly()   # Inherited from FlyMixin
draco.roar()  # Specific to Dragon
