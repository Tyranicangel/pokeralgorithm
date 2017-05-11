from deck import Deck
from player import Player
from table import Table
from evaluator import Evaluator
import sys
import csv
from collections import defaultdict

def groupByPot(playerList):
    """
    Groups the players by their bet amount
    Args:
        param playerList: List of players
    Returns:
        return:list:grouped list of players
    """
    output={}
    for player in playerList:
        key=player.getBet()
        if key in output:
            pass
        else:
            output[key]=[]
    for player in playerList:
        for key in output:
            if key <= player.getBet():
                output[key]+=[player]
    return output

def sort(playerList,attr,order):
    """
    Sorts the players based on the hand strength
    Args:
        param playerList: List of players
    """
    i=1
    while i<len(playerList):
        key=playerList[i]
        j=i-1
        while j>=0 and ((getattr(playerList[j][0],attr)()<getattr(key[0],attr)() and order=="DESC") or (getattr(playerList[j][0],attr)()>getattr(key[0],attr)() and order=="ASC")):
            playerList[j+1]=playerList[j]
            j-=1
        if getattr(playerList[j][0],attr)()==getattr(key[0],attr)():
            playerList[j]+=key
            playerList.pop(j+1)
        else:
            playerList[j+1]=key
            i+=1

if __name__=='__main__':
    d=Deck()
    e=Evaluator()
    playerList=[]
    ##Read player input
    fName=sys.argv[1]+".csv"
    with open(fName,"rb") as file:
        reader=csv.reader(file,delimiter=",",quotechar="'")
        for row in reader:
            if row[0]=="Table":
                table = Table(row[1:])
            else:
                playerList.append(Player(row[0],row[1],row[2:]))
    ##Evaluate each player's hand
    for player in playerList:
        e.evaluate(player,table)
    tplayerList=groupByPot(playerList)
    pot=0
    ##Sort and group players
    for key in sorted(tplayerList):
        tplayerList[key]=list([x] for x in tplayerList[key])
        sort(tplayerList[key],"getHandValue","DESC")
        playersInPot=reduce((lambda x,y:x+len(y)),tplayerList[key],0)
        winnings=playersInPot*(key-pot)/float(len(tplayerList[key][0]))
        ##Add winnings to the player
        for player in tplayerList[key][0]:
            player.addWinnings(winnings)
        pot=key
    ##Output
    print "{:20}{:20}{:^10}{:^20}".format("Player","Bet","Cards","Winnings")
    for player in playerList:
        print player