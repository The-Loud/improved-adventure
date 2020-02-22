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
        input("Press ENTER to roll the dice")
        self.dice = self.roll(5)
        print(self.dice)
        return self.dice

    def s_roll(self, dice):
        print(self.dice)
        keep = input(f"Which dice would you like to keep? {dice}: ")
        keep = [int(i) for i in keep.split()]
        tmp = self.roll(5 - len(keep))
        self.dice = keep + tmp
        return self.dice

    def t_roll(self, dice):
        print(self.dice)
        keep = input(f"Which dice would you like to keep? {dice}: ")
        keep = [int(i) for i in keep.split()]
        tmp = self.roll(5 - len(keep))
        self.dice = keep + tmp
        return self.dice
