import AlgorithmBase

class CocktailSort(AlgorithmBase.AlgorithmBase):
    def Sort(self):
        left = 0
        right = len(self.items)-1

        while (left<right):
            for i in range(left, right, 1):
                if self.items[i] >  self.items[i+1]:
                    AlgorithmBase.AlgorithmBase.ToSwop(self, i, i+1)

            right-=1

            for i in range(right, left, -1):
                if self.items[i] < self.items[i-1] :
                    AlgorithmBase.AlgorithmBase.ToSwop(self, i, i-1)


            left+=1