import random
from card import Card

class Deck(object):
    def __init__(self):
        self.cards = []
        def createDeck():
            numbers = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace',]
            suits = ['Hearts','Diamonds','Spades','Clubs',]
            for x in range(0, len(numbers)):
                for y in range(0,len(suits)):
                    card = Card(str(numbers[x]), str(suits[y]))
                    self.cards.append(card)
        createDeck()              

    def shuffle(self):
        for i in range(0,52):
            index = random.randint(0,51)
            temp = self.cards[index]
            self.cards[index]=self.cards[i]
            self.cards[i]=temp
        return self
    
    def deal(self):
        card = self.cards.pop()
        return card


