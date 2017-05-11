from card import Card

class Player:
    """
    Holds the data of each player
    """
    def __init__(self,name,bet,cards):
        """
        Args:
            param name:String 
            param bet:String 
            param cards: String[] 
        """
        self.__name=name
        self.__bet=int(bet)
        self.__winnings=0
        self.__cards=[Card(card) for card in cards]
        self.__handValue=0

    def __str__(self):
        return "{:20}{:20}{:5}{:5}{:20}".format(self.__name,str(self.__bet),self.__cards[0],self.__cards[1],self.__winnings)

    def getBet(self):
        return self.__bet

    def getCards(self):
        return self.__cards

    def setHandValue(self,value):
        self.__handValue=value

    def getHandValue(self):
        return self.__handValue

    def addWinnings(self,winning):
        self.__winnings+=winning

    def getWinnings(self):
        return self.__winnings