from card import Card

class Table:
    def __init__(self,cards):
        self.__cards=[Card(card) for card in cards]

    def __str__(self):
        return "{:10}{:5}{:5}{:5}{:5}{:5}".format("Table:",self.__cards[0],self.__cards[1],self.__cards[2],self.__cards[3],self.__cards[4])

    def getCards(self):
        return self.__cards