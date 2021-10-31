class Shape:
    def __init__(self):
        pass
        
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

rectangle = Rectangle()
square = Square()
rectangle.what_am_i()
