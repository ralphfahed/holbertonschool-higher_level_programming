from abc import ABC, abstractmethod
import math

# Step 1: Define the abstract base class 'Shape'
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Step 2: Define the concrete class 'Circle' that inherits from 'Shape'
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Step 3: Define the concrete class 'Rectangle' that inherits from 'Shape'
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Step 4: Define the function 'shape_info' that accepts a Shape object and prints its area and perimeter
def shape_info(shape):
    # Duck typing: We don't care about the object's exact class, we just use its methods
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Step 5: Test the shape_info function with instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Print shape info for circle and rectangle
print("Circle Info:")
shape_info(circle)

print("\nRectangle Info:")
shape_info(rectangle)

