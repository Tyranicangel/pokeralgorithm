from itertools import permutations
from json import dump

class Generator(object):
    """
    Generates unique 5 card products for each hand type and writes to hands.json file
    """
    def __init__(self):
        self.__cardPrimes= (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
        self.__hands={
            "fourofkind":[],
            "straight":[],
            "fullhouse":[],
            "threeofkind":[],
            "twopair":[],
            "onepair":[]
        }
        for hand in self.__hands:
            getattr(self,"generate_"+hand)()
        self.writeToFile()
    
    def writeToFile(self):
        with open("hands.json","w") as output:
            dump(self.__hands,output)

    def generate_fourofkind(self):
        cList=list(permutations(self.__cardPrimes,2))
        for item in cList:
            self.__hands["fourofkind"].append(item[0]*item[0]*item[0]*item[0]*item[1])

    def generate_straight(self):
        for i in range(0,len(self.__cardPrimes)-4):
            self.__hands["straight"].append(self.__cardPrimes[i]*self.__cardPrimes[i+1]*self.__cardPrimes[i+2]*self.__cardPrimes[i+3]*self.__cardPrimes[i+4])
        self.__hands["straight"].append(47355)

    def generate_fullhouse(self):
        cList=list(permutations(self.__cardPrimes,2))
        for item in cList:
            self.__hands["fullhouse"].append(item[0]*item[0]*item[0]*item[1]*item[1])

    def generate_threeofkind(self):
        cList=list(permutations(self.__cardPrimes,3))
        for item in cList:
            self.__hands["threeofkind"].append(item[0]*item[0]*item[0]*item[1]*item[2])

    def generate_twopair(self):
        cList=list(permutations(self.__cardPrimes,3))
        for item in cList:
            self.__hands["twopair"].append(item[0]*item[0]*item[1]*item[1]*item[2])

    def generate_onepair(self):
        cList=list(permutations(self.__cardPrimes,4))
        for item in cList:
            self.__hands["onepair"].append(item[0]*item[0]*item[1]*item[2]*item[3])