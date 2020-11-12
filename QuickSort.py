import AlgorithmBase

class QuickSort(AlgorithmBase.AlgorithmBase):
    def Sort(self):
        self.QSort(0, len(self.items)-1)

    def QSort(self, left, right):
        if left >= right:
            return
        pivot = self.Sorting(left, right)
        self.QSort(left, pivot-1)
        self.QSort(pivot+1, right)

    def Sorting(self, left : int, right : int) -> int:
        pointer = left
        for i in range(left, right, 1):
            if self.items[i] < self.items[right]:
                AlgorithmBase.AlgorithmBase.ToSwop(self, pointer, i)
                pointer += 1
        AlgorithmBase.AlgorithmBase.ToSwop(self, pointer, right)
        return pointer




