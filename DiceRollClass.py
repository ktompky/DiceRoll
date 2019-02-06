import random


class Dice:

    def __init__(self, die_sides):
        self.die_sides = die_sides
        self.roll()

    def roll(self):
        value = random.randint(1, self.die_sides)
        return value


player_choice = input("Would you like to roll the dice? 'y' for yes or 'n' for no.  ")

while player_choice == 'y':

    attack_dice = Dice(6)
    attack_roll = attack_dice.roll()
    print(attack_roll)
    player_choice = input("Would you like to roll again? 'y' for yes or 'n' for no. ")
if player_choice == 'n':
    print("Have a good day then! ")
