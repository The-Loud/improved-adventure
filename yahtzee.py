'''
Yahtzee. 2 - 4 players.
2020 Seve Martinez
'''

from player import Player
from dice import Die
import scoring

def decision():
    while 1:
        try:
            dec = int(input(f"What would you like to do? (Roll, view scorecard, quit)(1-3): "))
            break
        except ValueError:
            print("Please choose only 1, 2, or 3: ")
            continue
    return dec


playing = True

while playing:

    die = Die()
    print("Welcome to Yahtzee!\n")
    name = (input("Enter your name: "))
    # pnum = (int(input("How many are playing today? (1-4): ")))
    # players = [Player(name) for _ in range(pnum)]
    print(f"Setting up scorecard for {name}.")
    player = Player(name)

    if decision() == 1:
        die.f_roll()
        score(player, die)
