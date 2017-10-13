from random import randint

class Card(object):
    def __init__(self, cardid, suit, num):
        self.cardid = cardid
        self.suit = suit
        self.num = num

class Deck(object):
    def __init__(self):
        self.cards = []
        self.createcards()
        self.shuffle()
        #print self.cards
    def createcards(self):
        numbers = [2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"]
        suits = ["hearts", "diamond","clubs", "spades"]
        index = 1
        for x in suits:
            for y in range(0, len(numbers)):
                card = Card(index, x, y)
                index += 1
                self.cards.append(card)
        return self.cards

    def shuffle(self):
        for x in range(0,len(self.cards)):
            tempindex = randint(0,len(self.cards)-1)
            temp = self.cards[tempindex]
            self.cards[tempindex] = self.cards[x]
            self.cards[x] = temp
        return self.cards

    def deal(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
    def draw(self,card):
        return self.hand.append(card)
    def discard(self, index):
        return self.hand.pop(index)
    def showHand(self):
        for card in range(0, len(self.hand)):
            print self.hand[card].cardid


class Play(object):
    def __init__(self, arg):
        super(Play, self).__init__()
        self.arg = arg









deck1 = Deck()
print "___test for deckdraw___"
print len(deck1.cards)
print deck1.deal().cardid
print deck1.deal().cardid
print deck1.cards
print len(deck1.cards)
print "___test for shuffle___"
deck1.shuffle()
print deck1.deal().cardid
print deck1.deal().suit
print deck1.deal().cardid
print len(deck1.cards)
print "_____"
print deck1.cards[0].num
print deck1.cards[0].suit
print "___test player__"
player1= Player("aaa")
player1.draw(deck1.deal())
player1.draw(deck1.deal())
print len(deck1.cards)
player1.showHand()
player1.discard(1)
player1.showHand()
