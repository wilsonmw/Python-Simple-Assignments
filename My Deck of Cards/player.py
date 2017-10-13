from deck import Deck

class Player(object):
    def __init__(self, name, deck):
        self.name = name
        self.hand = []
        self.deck = deck
        
    #function to draw a card
    def draw(self):
        self.hand.append(self.deck.deal())
        return self

    #function to remove a card from the player's hand *** must be used with 'draw' function to actually trade cards
    def trade(self, card):  
        self.card = card
        self.hand.pop(card)
        return self

    #function to allow the player to choose which card(s) to trade in
    def tradeCard(self):    
        trader = int(raw_input ("Enter the number of the card you'd like to trade in (Enter 0 if you're done trading in cards): "))
        if trader == 0:
            count = 5-len(self.hand)
            for x in range(0,count):
                self.draw()
            return trader
        for x in range (1,len(self.hand)+1):
            if trader == x:
                self.trade(trader-1)
                print "\n Cards remaining in hand"
                print "------------------------------------- \n"
                for i in range(0,len(self.hand)):
                    print str(i+1) + ") " + str(self.hand[i].number), str(self.hand[i].suit)
                print "\n"
                self.tradeCard()
                break
        else:           
            print "That is not a valid choice."
            self.tradeCard()
