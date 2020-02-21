from prettyprint import PrettyTable


class Player():

    def __init__(self, name):
        self.name = name
        self.card = {"Ones": None,
                     "Twos": None,
                     "Threes": None,
                     "Fours": None,
                     "Fives": None,
                     "Sixes": None,
                     "Bonus": None,
                     "Three of a kind": None,
                     "Four of a kind": None,
                     "Full house": None,
                     "Small straight": None,
                     "Large straight": None,
                     "Yahtzee": None,
                     "Chance": None,
                     "Yahtzee bonus": None}
        self.round = 0

    # prettytable generated scorecard
    def card_gen(self):
        pretty_card = PrettyTable(["Category", self.name])
        pretty_card.add_row(["Ones", self.card["Ones"]])
        pretty_card.add_row(["Twos", self.card["Twos"]])
        pretty_card.add_row(["Threes", self.card["Threes"]])
        pretty_card.add_row(["Fours", self.card["Fours"]])
        pretty_card.add_row(["Fives", self.card["Fives"]])
        pretty_card.add_row(["Sixes", self.card["Sixes"]])
        pretty_card.add_row(["Bonus", self.card["Bonus"]])
        pretty_card.add_row(["------------", "-"])
        pretty_card.add_row(["3 of a kind", self.card["Three of a kind"]])
        pretty_card.add_row(["4 of a kind", self.card["Four of a kind"]])
        pretty_card.add_row(["Full House", self.card["Full house"]])
        pretty_card.add_row(["Small straight", self.card["Small straight"]])
        pretty_card.add_row(["Large straight", self.card["Large straight"]])
        pretty_card.add_row(["YAHTZEE", self.card["Yahtzee"]])
        pretty_card.add_row(["Chance", self.card["Chance"]])
        pretty_card.add_row(["YAHTZEE BONUS", self.card["Yahtzee bonus"]])
        pretty_card.add_row(["TOTAL SCORE", "--"])
        print(pretty_card)
