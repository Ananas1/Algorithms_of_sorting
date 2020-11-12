import random


class AlgorithmBase:
    def __init__(self):
        self.items = []
    def ToSwop(self, positionA, positionB):
        if (positionA < len(self.items) and positionB < len(self.items)):
            #temp = self.items[positionA]
            self.items[positionA], self.items[positionB] = self.items[positionB], self.items[positionA]
            #self.items[positionB] = self.items[positionA]
    def FullRandom(self, count):
        rnd = random

        for i in range(0, count, 1):
            #print(rnd.randint(1,100))
            self.items.append(rnd.randint(1,100))
            print(self.items[i])
        print()
    def Sort(self):
        self.items.Sort();
