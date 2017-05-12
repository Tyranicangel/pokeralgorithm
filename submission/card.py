from deck import Deck


class Card(object):
    """
    Card object which holds the suit and value of the card
    """

    def __init__(self, card):
        """
        Args:
            card:String
        """
        self.__card = card
        d = Deck()
        self.__value = d.getNumeric(self.__card)
        self.__primeValue = d.getPrime(self.__card)

    def __str__(self):
        return self.__card

    def getPrime(self):
        """
        To get the prime value attached to the card
        Returns:
            int: the prime value attached to the card
        """
        return self.__primeValue

    def getValue(self):
        """
        To get the numeric value of the card
        Returns:
            int: the numeric value of the card
        """
        return self.__value

    def getSuit(self):
        """
        To get the suit of the card
        C-Clubs
        D-Diamonds
        H-Hearts
        S-Spades
        Returns:
            string: the suit of card 
        """
        return self.__card[1]
