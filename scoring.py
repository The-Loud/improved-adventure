import player
import dice

ref = {"Ones": 1,
        "Twos": 2,
        "Threes": 3,
        "Fours": 4,
        "Fives": 5,
        "Sixes": 6}


def nums(player, die):
    sc = input("Where would you like to put your score? ")
    score = [i for i in die.dice if i == ref[sc]]
    player.card[sc] = sum(score)
    player.card_gen()
