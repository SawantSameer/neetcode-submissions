class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def NumOfBits(k):
            bin = ''
            while k!=0:
                bin = str(k%2) + bin
                k = k//2
            cnt = 0
            for c in bin:
                if int(c)&1:
                    cnt += 1

            return cnt

        for i in range(n+1):
            res.append(NumOfBits(i))

        return res