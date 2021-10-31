class Horse:
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self,name):
        self.name = name

rider = Rider("YUUKI")
horse = Horse("Noah",rider)
print(horse.owner.name)
