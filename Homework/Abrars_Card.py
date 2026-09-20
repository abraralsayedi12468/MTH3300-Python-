import random


class Card:
    _rank_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                   "Jack", "Queen", "King", "Ace"]

    def __init__(self, r="None", s="None"):
        self._rank = r
        self._suit = s

    def display(self):
        print(self._rank, "of", self._suit)

    def beats(self, other):
        order = Card._rank_order
        try:
            pos_self = order.index(self._rank)
            pos_other = order.index(other._rank)
            return pos_self > pos_other
        except:
            raise BreakAbrarsCode("WHY MUST YOU BREAK MY CODE")


class Deck:
    _ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    _suits = ["Hearts", "Clubs", "Diamonds", "Spades"]

    def __init__(self):
        self._cards_left = 52
        self._drawn = []  # 4x13 2D list, with values initialized to False

        for s in range(4):
            self._drawn.append([False] * 13)

    def draw(self):
        if self._cards_left > 0:
            self._cards_left -= 1

            s = random.randrange(4)
            r = random.randrange(13)

            while self._drawn[s][r]:
                s = random.randrange(4)
                r = random.randrange(13)

            self._drawn[s][r] = True

            return Card(Deck._ranks[r], Deck._suits[s])

        else:
            raise BreakAbrarsCode(
                "WANTED TO SEE WHAT WOULD HAPPEN, DID YOU?"
            )


class BreakAbrarsCode(Exception):
    pass