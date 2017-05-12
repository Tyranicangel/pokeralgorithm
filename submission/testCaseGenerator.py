from deck import Deck
import sys
import csv
from random import randint
"""
    This file generates a random test case. It takes the filename to be generated as params.
    It always generates a .csv file to be used in the algorithm.
    A Table with 5 random cards and 9 players with 2 random cards each and random bet between 1000 and 9000
    are generated and written to the file
    Usage testCaseGenerator.py <filename>
"""
if __name__=="__main__":
    d=Deck()
    fName=sys.argv[1]
    with open(fName+'.csv','wb') as csvfile:
        writer=csv.writer(csvfile,delimiter=",",quotechar="'",quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Table"]+d.drawCards(5))
        writer.writerow(["Player1", randint(1,9)*1000]+d.drawCards(2))
        writer.writerow(['Player2', randint(1,9)*1000] + d.drawCards(2))
        writer.writerow(['Player3', randint(1,9)*1000] + d.drawCards(2))
        writer.writerow(['Player4', randint(1,9)*1000] + d.drawCards(2))
        writer.writerow(['Player5', randint(1,9)*1000] + d.drawCards(2))
        writer.writerow(['Player6', randint(1,9)*1000] + d.drawCards(2))
        writer.writerow(['Player7', randint(1,9)*1000] + d.drawCards(2))
        writer.writerow(['Player8', randint(1,9)*1000] + d.drawCards(2))
        writer.writerow(['Player9', randint(1,9)*1000] + d.drawCards(2))