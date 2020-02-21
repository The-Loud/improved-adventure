'''
Yahtzee. 2 - 4 players.
2020 Seve Martinez
'''

from player import Player
from dice import Die


def p_dice(cup):
    print(cup)


def p_scorecard(player):
    pass


playing = True

while playing:

    die = Die()
    print("Welcome to Yahtzee!\n")
    pnum = (int(input("How many are playing today? (1-4): ")))
    name = (input("Name of player 1: "))
    players = [Player(name) for _ in range(pnum)]
    print(f"Setting up scorecard for {pnum} players.")

    dec = input((f"What would you like to do? (Roll, view scorecard, quit)(1-3): "))

    # ask the user for input

    # pop that number off the original list
    # append x new random rolls to the list
