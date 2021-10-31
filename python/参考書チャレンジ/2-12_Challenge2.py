class Circle:
    def __init__(self,r,p):
        self.radius = r
        self.pi = p
        print("Created!")

    def area(self):
        return math.pi * self.radius * self.radius

import math
circle = Circle(10,3.14)
print(circle.area())

