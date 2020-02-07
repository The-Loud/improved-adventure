'''
Yahtzee. 2 - 4 players.
2020 Seve Martinez
'''

import random


class Player():

    def __init__(self):
        total_score = 0
        scorecard = {'Ones': 0, 'Twos': 0, 'Threes': 0,
                     'Fours':0, 'Fives': 0, 'Sixes': 0,
                     'Full House': 0, 'Four of a kind': 0, 'Little Straight': 0,
                     'Big Straight': 0, 'Chance': 0, 'Yahtzee': 0}


class Die():

    def __init__(self):
        self.sides = 6

    def roll(self):
        return random.randint(1, self.sides)


def p_scorecard(player):
    pass


def turn(dielist, roller):
    for i in range(roller):
        dielist.pop()
    for i in range(roller):
        die = Die()
        dielist.append(die.roll())
    return dielist



playing = True

while playing:

    turnset = 0
    print("Welcome to Yahtzee!\n")
    pnum = (int(input("How many are playing today? (1-4): ")))
    for _ in range(pnum):
        player_

    while turnset != 3:
        # Turn 1:
        # first roll of 5 dice.
        dielist = []
        counter = 0
        while counter < 5:
            dice = Die()
            dielist.append(dice.roll())
            counter += 1

        print(dielist)

        # ask the user for input. reroll number or keep score
        roller = int(input("Please enter the number of dice to reroll (1-5): "))
        turn(dielist, roller)
        print(dielist)


    # If score isn't selected, Turn 2:
    # turn 3

    # ask the user for input

    # pop that number off the original list
    # append x new random rolls to the list
