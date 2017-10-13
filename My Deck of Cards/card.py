
class Card(object):
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number
        self.value = self.number
        if self.value == "Jack":
            self.value = 11
        if self.value == "Queen":
            self.value = 12
        if self.value == "King":
            self.value = 13
        if self.value == "Ace":
            self.value = 14
