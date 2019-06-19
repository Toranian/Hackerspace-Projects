import random
class Die:

    def __init__(self, sides):
        self.sides = sides
        self.last_role = 0
    
    def roll(self):
        self.last_role = random.randint(1, self.sides)
        return self.last_role