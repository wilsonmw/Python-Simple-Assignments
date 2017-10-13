from random import randint

class Deck(object):
    def __init__(self):
        self.cards = []
        def createcards():
            numbers = [2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"]
            suits = ["hearts", "diamond","clubs", "spades"]
            for x in range(0, len(suits)):
                for y in range(0, len(numbers)):
                    card ={}
                    card["name"] = str(numbers[y]) + " of " + str(suits[x])
                    self.cards.append(card)
        createcards()
        print self.cards
    def deckdraw(self):
        return self.cards.pop()
    def shuffle(self):
        for x in range(0,len(self.cards)):
            tempindex = randint(0,len(self.cards)-1)
            temp = self.cards[tempindex]
            self.cards[tempindex] = self.cards[x]
            self.cards[x] = temp
        #print len(self.cards)
        return self.cards

mydeck = Deck()
print mydeck.deckdraw()
#print mydeck.shuffle()





class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
    def playerdraw(self,card):
        return self.hand.append(card)
    def showHand(self):
        for card in range(0, len(self.hand)):
            print self.hand[card]
    def discard(self):
        return self.hand.pop()



player1= Player("aaa")
player1.playerdraw(mydeck.deckdraw())
print "_____"
print player1.hand
player1.playerdraw(mydeck.deckdraw())
print "_____"
player1.showHand()
print "_____"
player1.discard()
print player1.hand
