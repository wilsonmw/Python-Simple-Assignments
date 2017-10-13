from player import Player
from deck import Deck
from card import Card


deck1 = Deck()
deck1.shuffle()


print "\n******************************"
print "**           POKER          **"
print "******************************\n"

playerName = raw_input ("What is your name? ")

raw_input ("\n Press enter to deal your hand.")


p1 = Player(playerName, deck1)
p2 = Player("Poker Robot", deck1)

p1.draw().draw().draw().draw().draw()
p2.draw().draw().draw().draw().draw()


print "\n" + playerName + "'s Hand"
print "-------------------------------------"
for i in range(0,len(p1.hand)):
    print str(i+1) + ") " + str(p1.hand[i].number), str(p1.hand[i].suit)
print "------------------------------------- \n"

p1.tradeCard()

print "------------------------------------- \n"
print playerName + "'s New Hand"
print "-------------------------------------"
for i in range(0,len(p1.hand)):
    print str(i+1) + ") " + str(p1.hand[i].number), str(p1.hand[i].suit)
print "------------------------------------- \n\n"
raw_input ("Press enter to see Poker Robot's hand.")

print "\n" + p2.name + "'s Hand"
print "-------------------------------------"
for i in range(0,len(p2.hand)):    
    print p2.hand[i].number, p2.hand[i].suit
print "-------------------------------------\n"


