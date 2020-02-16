'''
Yahtzee. 2 - 4 players.
2020 Seve Martinez
'''

import random


class Die():

    def __init__(self):
        self.dice = []

    def roll(self, num):
        self.dice = [random.randint(1, 6) for i in range(0, num)]
        return self.dice

    def f_roll(self):
        input(f"Press ENTER to roll the dice")
        self.dice = self.roll(5)
        return self.dice

    def s_roll(self, dice):
        keep = input(f"Which dice would you like to keep? {dice}: ")
        keep = [int(i) for i in keep.split()]
        tmp = self.roll(5 - len(keep))
        print(tmp)

    def t_roll(self, roll):
        pass


die = Die()
print(die.dice)
print(die.f_roll())
print(die.s_roll(die.dice))
