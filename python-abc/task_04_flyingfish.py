#!/usr/bin/env python3

# Parent Class 1: Fish
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

# Parent Class 2: Bird
class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

# FlyingFish class inherits from both Fish and Bird
class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")  # Overridden swim method

    def fly(self):
        print("The flying fish is soaring!")  # Overridden fly method

    def habitat(self):
        print("The flying fish lives both in water and the sky!")  # Overridden habitat method

# Test the FlyingFish class
flying_fish = FlyingFish()
flying_fish.swim()  # Call the overridden swim method
flying_fish.fly()   # Call the overridden fly method
flying_fish.habitat()  # Call the overridden habitat method

# Check the Method Resolution Order (MRO)
print(FlyingFish.mro())  # Print the MRO
