from random import randint


class Deck(object):
    def __init__(self):
        self.cards = []
        def create():
            numbers = [2,3,4,5,6,7,8,9,10, 'jack', 'queen', 'king', 'ace',]
            suits = ['hearts', 'diamonds', 'clubs', 'spades',]
            for i in range(0, len(suits)):
                for k in range(0,len(numbers)):
                    card = {}
                    card["name"]=str(numbers[k]) + " of " + str(suits[i])
                    self.cards.append(card)             
        create()
        
    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        for i in range(0,len(self.cards)):
            tempindex = randint(0,len(self.cards)-1)
            temp = self.cards[tempindex]
            self.cards[tempindex]=self.cards[i]
            self.cards[i]=temp
        return self.cards


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self,card):
        self.hand.append(card)
        print self.hand
        
    def discard(self,card,deck):
        deck.cards.append(self.hand.pop())
        print self.hand
        print deck.cards





myDeck = Deck()
myDeck.shuffle()

player1 = Player("Matt")
player1.draw(myDeck.draw())

player1.discard(player1.hand[0],myDeck)

