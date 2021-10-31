class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width * 2) + (self.len * 2)

    def change_size(self,w,l):
        self.width = self.width - (w)
        self.len = l - (l)

class Square:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width * 2) + (self.len * 2)

rectangle = Rectangle(10,10)
print(rectangle.calculate_perimeter())
square = Square(10,10)
print(square.calculate_perimeter())
