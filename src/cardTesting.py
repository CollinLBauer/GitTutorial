# Collin Bauer
# cardTesting.py
#
# Code for testing elements of cardObjects.py

from cardObjects import *


def war(deck,playerCount=2):
    print("Let's play war!\n")
    deck.shuffle()

    players = Players(deck,playerCount)
    scores = [0]*playerCount
    roundCards = []
    cardPile = []

    while deck.getSize() > 1:
        for i in range(players.getPlayerCount()):
            roundCards.append(deck.drawCard())
            print("{}:\t{}".format(players.get(i).getName(),roundCards[i].getName())) #debug
        topCard = 0
        for i in range(len(roundCards) - 1):
            #print("Difference: "
            #      + str(roundCards[i].compareTo(roundCards[i+1]))) #debug
            if roundCards[i].compareTo(roundCards[i+1]) == 0:
                topCard = -1
            if roundCards[i].compareTo(roundCards[i+1]) < 0:
                topCard = i + 1
        
        
        if topCard == -1:
            print("No winner for round.",end="")
            cardPile.extend(roundCards)
        else:
            print("Player {} wins round.".format(topCard+1),end="")
        roundCards = []
        input("")
            
            

def goFish(deck,playerCount=2):
    print("Let's play: Go Fish!\n")

    #Initial game properties
    discard = Discard()
    players = []
    if playerCount < 1:
        print("Error: playerCount value too low. Defaulting to 2 players.")
        playerCount = 2
    for i in range(playerCount):
        players.append(Player("Player {0}".format(i+1),deck,5))

    #Game in while loop:
    gameOver = False
    #while not gameOver:
    for player in players:
        print(player.getName() + "'s hand")
        print(player.showHand())
        print()
        


def main():
    #code for testing card objects:
    myDeck = StdDeck()
    war(myDeck)
    
main()
