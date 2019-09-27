# Collin Bauer
# cardObjects.py
#
# This is a series of obejcts made for decks of playing cards.

from random import randint, shuffle


'''
This class creates a standard playing card.
Valid playing cards include cards in the suits Hearts, Spades, Clubs,
  and Diamonds.
Valid card values include all cards from Ace to King, with values accepted
  as integers from 1 to 13.
This class also creates special "Joker" cards if no arguments are given,
  or if the argumentsare invalid.
'''
class Card:

    def __init__(self,suit="",val=0):
        #default values, for error handling
        #if no suit or val is is given, generates a joker card
        self.val = -1
        self.suit = "Joker"
        self.name = "Joker"
        self.color = "N/A"
        self.face = "up"

        #suit handler
        if suit.lower() == "hearts" or suit.lower() == "heart":
            self.suit = "Hearts"
            self.color = "red"
        elif suit.lower() == "spades" or suit.lower() == "spade":
            self.suit = "Spades"
            self.color = "black"
        elif suit.lower() == "diamonds" or suit.lower() == "diamond":
            self.suit = "Diamonds"
            self.color = "red"
        elif suit.lower() == "clubs" or suit.lower() == "club":
            self.suit = "Clubs"
            self.color = "black"
        
        #value handler
        if self.suit != "joker":
            if type(val) == float:
                val = int(val)
            if type(val) == int and val >= 1 and val <= 13:
                self.val = val
        
        #string representation of value
        if self.val >= 2 and self.val <= 10:
            self.name = str(self.val)
        elif self.val == 1:
            self.name = "Ace"
        elif self.val == 11:
            self.name = "Jack"
        elif self.val == 12:
            self.name = "Queen"
        elif self.val == 13:
            self.name = "King"

    def flip(self):
        if self.face == "down":
            self.face = "up"
        else:
            self.face = "down"

    def isFlipped(self):
        return self.face

    def getSuit(self):
        return self.suit

    def getName(self):
        return self.name

    def getFullName(self):
        if self.val != -1:
            return self.name + " of " + self.suit
        else:
            return "Joker"

    def getVal(self):
        return self.val

    # Bear in mind, this code considers an Ace the lowest possible val
    #   (1), while some games may consider it the highest possible val.
    # This issue should be addressed in such a game's code.
    def compareTo(self,anotherCard):
        return self.val - anotherCard.getVal()

    def __str__(self):
        rtnStr = "A playing card\n"
        if self.isFlipped() == "down":
            rtnStr += "Card is currently face down.\n"
        else:
            rtnStr +=("Card is currently face up.\n"
                      + self.getFullName())
        return rtnStr


'''
A deck is a list of cards.
This class creates a blank deck, which may be manually added to or imported
  into a more complex class.
This class considers the first position in the list as the bottom of the deck,
  and the last position as the top. Therefore, drawing a card removes and
  returns the last position of the deck.
'''
class Deck:

    def __init__(self):
        self.deck = []

    def shuffle(self):
        shuffle(self.deck)
        print("Shuffled deck.\n")

    def drawCard(self,pos=-1):
        #by default, draws the top card.
        #change pos value to grab a specific card.
        try:
            return self.deck.pop(pos)
        except:
            print("Error: Deck out of cards.")

    def insertCard(self,card,pos="0"):
        #by default, inserts a card at the botom of the deck.
        #change pos value to insert at a different location.
        if card.isFlipped == "up":
            card.flip()
        self.deck.insert(pos,card)

    def insertOnTop(self,card):
        #This method exists because insertCard cannot place cards on top.
        if card.isFlipped == "up":
            card.flip()
        self.deck.append(card)

    def listDeck(self):
        rtnStr = ""
        for card in self.deck:
            rtnStr += str(card.getFullName()) + "; "
        return rtnStr[:-2]

    def getDeck(self):
        return self.deck

    def getSize(self):
        return len(self.deck)

    def __str__(self):
        rtnStr = ("A deck of cards.\nCurrently contains "
                  + str(len(self.deck)) + " cards.")
        return rtnStr


'''
A deck is a list of cards.
This class creates a deck of cards following the standard 52-card format,
  or 54 if you count jokers. To add jokers, simply set the jokers value to
  True when creating the deck.
By default, all cards in a deck should be face down, but cards built with
  the Card class are face up by default. The init flips over the cards
  to compensate.
This deck class does not support adding cards from outside the original deck.
'''
class StdDeck(Deck):

    def __init__(self,jokers=False):
        self.deck = []
        self.jokers = jokers
        for suit in ["hearts","diamonds","clubs","spades"]:
            for i in range(1,14):
                self.deck.append(Card(suit,i))
        if jokers:
            self.deck.append(Card())
            self.deck.append(Card())
        for card in self.deck:
            card.flip()
        self.initLength = len(self.deck)

    def __str__(self):
        rtnStr = ("Standard deck of " + str(self.initLength)
                  + " playing cards.")
        if self.jokers:
            rtnStr +="\nDeck contains jokers."
        diff = self.initLength - len(self.deck)
        if diff == 1:
            rtnStr += "\n1 card is missing from the deck."
        elif diff > 1:
            rtnStr += ("\n" + str(diff)
                       + " cards are missing from the deck.")
        return rtnStr


'''
A discard pile.
This acts similarly to the Deck class, but is empty by default, and forces
  all cards inside to be face up.
'''
class Discard:

    def __init__(self):
        self.deck = []

    def discard(self,card):
        if card.isFlipped() == "down":
            card.flip()
        self.deck.append(card)

    def __str__(self):
        rtnStr = ("A discard pile." + "\nCurrently contains: "
                  + str(len(self.deck)) + " cards.")


'''
Acts as a hand of playing cards.
This class isn't exactly necessary, to be honest, and it mostly serves as a
  formality, but it helps keep the code in main() cleaner by keeping related
  variables grouped together.
'''
class Player:

    def __init__(self,deck,playerName="Player 1",initDraw=0):
        self.name = playerName
        self.hand = []
        for i in range(initDraw):
            self.hand.append(deck.drawCard())

    def drawCards(self,deck,count=1):
        for i in range(count):
            card = deck.drawCard()
            #print(newCard)
            if card != None:
                self.hand.append(card)

    def showHand(self):
        rtnStr = ""
        for card in self.hand:
            rtnStr += card.getFullName()+ "; "
        return rtnStr[:-2]

    def dropCard(self,pos=-1):
        return self.hand.pop(-1)

    def setName(self,playerName):
        self.name = playerName

    def getHandLength(self):
        return len(self.hand)

    def getCard(self,pos=-1):
        return self.hand[pos]

    def getName(self):
        return self.name

    def __str__(self):
        rtnStr = (self.name + "'s hand."
                  + "\nCurrently contains: "
                  + str(len(self.hand)) + " cards.")
        return rtnStr


'''
(not to be confused with the Player class)
A list of, players.
This class contains methods for handling players, including adding and
  removing them. This simplifies game turns and the anomalies of players
  joining and leaving mid-game.
For now, this class adds new players via console input from the user.
'''
class Players:
    
    def __init__(self,deck,initPlayerCount=2,initDraw=0):
        self.players = []
        for i in range(initPlayerCount):
            playerName = input("Player {0}'s name: ".format(i+1))
            self.players.append(Player(deck,playerName,initDraw))
        self.playerCount = initPlayerCount
        self.currentTurn = 1

    def nextTurn(self):
        if self.currentTurn < self.playerCount:
            self.currentTurn += 1
        else:
            self.currentTurn = 1
        print(self.currentTurn)

    def getPlayers(self):
        return self.players

    def getPlayerCount(self):
        return len(self.players)

    def getCurrentTurn(self):
        return self.currentTurn

    def get(self,index):
        return self.players[index]

    def __str__(self):
        rtnStr = "A list of players."
        for i in range(len(self.players)):
            rtnStr += "\nPlayer {0}: {1}".format(
                i+1,self.players[i].getName())
        return rtnStr
