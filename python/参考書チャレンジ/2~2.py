list = []

class Square:
    def __ini__(self,w,l):
        self.width = w
        self.len = l

    def square_list(self):
        s_list = [self.width,self.len]
        list.append(s_list)

new_list = Square(10,5)
print(list)
