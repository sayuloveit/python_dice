from random import randrange

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return randrange(1, self.sides + 1)
