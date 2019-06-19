class BagOfDice:

    def __init__(self, dice):
        self.dice = list(dice)
        self.total = 0

    def add_die_to_bag(self, die):
        self.dice.append(die)
    
    def roll(self):
        for die in self.dice:
            self.total += die.roll()
            
        return self.total
