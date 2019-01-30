import random


class Dice:

    def __init__(self, die_sides):
        self.die_sides = die_sides
        self.roll()
        self.value = value

    def roll(self):
        self.value = random.randrange(self.die_sides) + 1
        return self.value




