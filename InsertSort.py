import AlgorithmBase

class InsertSort(AlgorithmBase.AlgorithmBase):
    def Sort(self):
        for i in range(1, len(self.items)):
            temp = self.items[i]
            j = i
            while (j > 0) and (temp < self.items[j-1]):
                a=self.items[j-1]
                self.items[j]=self.items[j-1]
                j-=1
            self.items[j] = temp