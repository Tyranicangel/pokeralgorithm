from card import Card

class Table:
    def __init__(self,cards):
        self.__cards=[Card(card) for card in cards]

    def getCards(self):
        return self.__cards