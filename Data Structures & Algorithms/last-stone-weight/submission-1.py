class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.weight = stones
        if len(self.weight)==1:
            return self.weight[0]

        while len(self.weight)!=1:
            M = max(self.weight)
            S = self.secMax(self.weight)

            self.weight.remove(M)
            self.weight.remove(S)
            self.weight.append(M-S)

        return self.weight[0]

    def secMax(self,l):
        lar = l[0]
        slar = None
        for x in l[1:]:
            if x>lar:
                slar = lar
                lar = x
            elif x!=lar:
                if slar==None or slar<x:
                    slar = x
            else: slar = x
        return slar