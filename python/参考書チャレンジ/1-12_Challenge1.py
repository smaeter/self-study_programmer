class Apple:
    def __init__(self,w,c,p,q):
        self.weight = w
        self.color = c
        self.price = p
        self.quantity= q
        print("Created!")

    def sum_price(self):
        return self.price * self.quantity

apple = Apple(10,"red",100,10)
print(apple.sum_price())


