class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l
        print("Created!")

    def area(self):
        return self.width * self.len

    def change_size(self,w,l):
        self.width = w
        self.len = l
        print("Re Created!")

rectangle = Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())
