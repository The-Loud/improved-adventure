import player
import dice


def score(player, die):
    sc = input("Where would you like to put your score? ")
    player.card[sc] = sum(die.dice)
    player.card_gen()
