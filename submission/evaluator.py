from __future__ import division
from itertools import combinations
from generator import Generator
from json import load
from functools import reduce


class Evaluator(object):
    """
        Evaluator for strength of each hand
    """

    def __init__(self):
        """
            __strengths:List of poker hands ordered in increasing order of strength
            __hands:List of possible hand values loaded from json file
        """
        g = Generator()
        with open('hands.json') as data:
            self.__hands = load(data)
        self.__strengths = (
            "onepair",
            "twopair",
            "threeofkind",
            "straight",
            "flush",
            "fullhouse",
            "fourofkind",
            "straightflush")

    def evaluate(self, player, table):
        """
        Generates all possible hand combinations for the player
        Runs a evaluation of the hand strengths
        Sets the hand value of the player
        Args:
            param player: Player
            param table:  Table
        """
        allCards = player.getCards() + table.getCards()
        cardCombos = list(combinations(allCards, 5))
        player.setHandValue(self.run(cardCombos))
        # cardproduct=reduce((lambda x,y:x*y.getValue()),self.__allCards,1)

    def run(self, cardCombo):
        """
        Runs the tests against each hand and returns the best hand
        Args:
            param cardCombo: All possible 5 card combinations for the player
        Returns:
            return: The best hand strength
        """
        cardListStr = []
        for cardList in cardCombo:
            cardListStr.append(self.testCases(cardList))
        return max(cardListStr)

    def testCases(self, cardList):
        """
        Checks the cards against the look-up and generates the strength of the hand
        The hand strength is a decimal between 0 and 10
        Args:
            param cardList: List of 5 Cards
        Returns:
            return:float:The strength of the card
        """
        cardproduct = reduce((lambda x, y: x * y.getPrime()), cardList, 1)
        for i in reversed(range(len(self.__strengths))):
            if getattr(
                    self,
                    'eval_' +
                    self.__strengths[i])(
                    cardproduct,
                    cardList):
                if cardproduct == 47355:
                    cardproduct = 2310
                return (i + 1) + (cardproduct / 1000000000)
        return cardproduct / 1000000000

    def eval_straightflush(self, cardproduct, cardList):
        """
        Verifies if the 5 Cards complete a straight flush and returns true if verified else false
        Args:
            param cardproduct:int: The prime product of all 5 cards
            param cardList: Cards list of length 5
        Returns
            return:bool:True/False
        """
        if(self.eval_flush(cardproduct, cardList) and self.eval_straight(cardproduct, cardList)):
            return True
        return False

    def eval_fourofkind(self, cardproduct, cardList):
        """
        Verifies if the 5 Cards complete a four of a kind and returns true if verified else false
        Args:
            param cardproduct:int: The prime product of all 5 cards
            param cardList: Cards list of length 5
        Returns
            return:bool:True/False
        """
        if cardproduct in self.__hands['fourofkind']:
            return True
        return False

    def eval_fullhouse(self, cardproduct, cardList):
        """
        Verifies if the 5 Cards complete a full house and returns true if verified else false
        Args:
            param cardproduct:int: The prime product of all 5 cards
            param cardList: Cards list of length 5
        Returns
            return:bool:True/False
        """
        if cardproduct in self.__hands['fullhouse']:
            return True
        return False

    def eval_flush(self, cardproduct, cardList):
        """
        Verifies if the 5 Cards complete a flush and returns true if verified else false
        Args:
            param cardproduct:int: The prime product of all 5 cards
            param cardList: Cards list of length 5
        Returns
            return:bool:True/False
        """
        if cardList[0].getSuit() == cardList[1].getSuit() == cardList[2].getSuit(
        ) == cardList[3].getSuit() == cardList[4].getSuit():
            return True
        return False

    def eval_straight(self, cardproduct, cardList):
        """
        Verifies if the 5 Cards complete a straight and returns true if verified else false
        Args:
            param cardproduct:int: The prime product of all 5 cards
            param cardList: Cards list of length 5
        Returns
            return:bool:True/False
        """
        if cardproduct in self.__hands['straight']:
            return True
        return False

    def eval_threeofkind(self, cardproduct, cardList):
        """
        Verifies if the 5 Cards complete a three of a kind and returns true if verified else false
        Args:
            param cardproduct:int: The prime product of all 5 cards
            param cardList: Cards list of length 5
        Returns
            return:bool:True/False
        """
        if cardproduct in self.__hands['threeofkind']:
            return True
        return False

    def eval_twopair(self, cardproduct, cardList):
        """
        Verifies if the 5 Cards complete a two pair and returns true if verified else false
        Args:
            param cardproduct:int: The prime product of all 5 cards
            param cardList: Cards list of length 5
        Returns
            return:bool:True/False
        """
        if cardproduct in self.__hands['twopair']:
            return True
        return False

    def eval_onepair(self, cardproduct, cardList):
        """
        Verifies if the 5 Cards complete a single pair and returns true if verified else false
        Args:
            param cardproduct:int: The prime product of all 5 cards
            param cardList: Cards list of length 5
        Returns
            return:bool:True/False
        """
        if cardproduct in self.__hands['onepair']:
            return True
        return False
