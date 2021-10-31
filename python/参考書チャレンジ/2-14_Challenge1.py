list = []

class Square:
    def __init__(self,l):
        self.len = l
        print("ok")

    def square_list(self):
        list.append(self.len)
        print("{} by {} by {} by {}".format(self.len,self.len,self.len,self.len))

a_square = Square(29).square_list()
a_square = Square(27).square_list()
print(list)
