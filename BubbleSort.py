import AlgorithmBase

class BubbleSort(AlgorithmBase.AlgorithmBase):
    def Sort(self):
        count = len(self.items)
        for j in range (0, count-1, 1):

            for i in range(0, count-2, 1):
                a = self.items[i]
                b = self.items[i+1]
                if (a>b):
                    AlgorithmBase.AlgorithmBase.ToSwop(self, i, (i+1))
            count-=1


