# Question: Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

from math import pi

# class Circle takes input "radius"
class Circle:
    # Initialise the class 
    def __init__(self, radius: float):
        # Assign the input "radius" to the self internal variable called "radius"
        self.radius = radius

    def area(self):
        radius = self.radius
        return round(radius * radius * pi, 2)
    
    def perimeter(self):
        radius = self.radius
        return round(2 * radius * pi, 2)

circle = Circle(5)
print(circle.area())
        

