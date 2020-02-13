'''
Yahtzee. 2 - 4 players.
2020 Seve Martinez
'''

import random


class Player():
    '''
    Players have a scorecard, basically. The scorecard method will handle the details.
    '''

    def __init__(self):
        total_score = 0
        scorecard = {'Ones': 0, 'Twos': 0, 'Threes': 0,
                     'Fours':0, 'Fives': 0, 'Sixes': 0,
                     'Full House': 0, 'Four of a kind': 0, 'Little Straight': 0,
                     'Big Straight': 0, 'Chance': 0, 'Yahtzee': 0}

    def scorecard(self, score, spot):
        pass

    def p_card(self, card):
        
        print(



class Die():

    def __init__(self):
        self.sides = 6

    def roll(self):
        return random.randint(1, self.sides)


def p_dice(cup):
    print(cup)


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
    players = [Player() for _ in range(pnum)]
    print(f"Setting up scorecard for {pnum} players.")

    while turnset != 2:
        # Turn 1:
        # first roll of 5 dice.
        dielist = []
        for _ in range(0, 5):
            dice = Die()
            dielist.append(dice.roll())
        p_dice(dielist)

        # ask the user for input. reroll number or keep score
        roller = int(input("Please enter the number of dice to reroll (1-5): "))
        turn(dielist, roller)
        turnset += 1

    p_dice(dielist)

    # ask if the user wants to reroll the dice or use their score

    # ask the user for input

    # pop that number off the original list
    # append x new random rolls to the list
