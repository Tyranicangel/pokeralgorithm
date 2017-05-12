from random import randint


class Deck(object):
    """
    Holds the data for the deck
    """

    def __init__(self):
        """
        __cards:List of available cards
        __suits:List of suits
        __cardPrimes:List of prime values for each card
        __cardIntValues:Mapping for primes to each card
        """
        self.__cards = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
        self.__suits = ('C', 'D', 'H', 'S')
        self.__cardPrimes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
        self.__cardIntValues = dict(zip(self.__cards, self.__cardPrimes))
        self.generateDeck()

    def getPrime(self, card):
        """
        To get the prime value of the card
        Args:
            param card:String The face value of the card
        Returns:
            int:The prime value of the card
        """
        return self.__cardIntValues[card[0]]

    def getNumeric(self, card):
        """
        To get the face value of a card
        Args:
            param card:String The face value of the card
        Returns:
            int:The numeric value of the card
        """
        return self.__cards.index(card[0])

    def generateDeck(self):
        """
            Generates a deck of 52 cards
        """
        self.__deck = []
        for card in self.__cards:
            for suit in self.__suits:
                self.__deck.append(card + suit)

    def drawCards(self, number):
        """
            Draws defined number of cards from the deck
        Args:
            param number: int
        Returns:
            list[Strings]: List of cards drawn
        """
        cardList = []
        for i in range(number):
            card = randint(0, len(self.__deck) - 1)
            cardList.append(self.__deck[card])
            self.__deck.pop(card)
        return cardList
