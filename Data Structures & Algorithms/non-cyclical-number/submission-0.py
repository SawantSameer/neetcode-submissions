class Solution:
    def isHappy(self, n: int) -> bool:
        isSeen = set()

        def sumOfSq(k):
            res = 0
            while k!=0:
                res += (k%10)**2
                k = k//10
            return res
        while n!=1:
            isSeen.add(n)
            n = sumOfSq(n)
            if n in isSeen:
                return False

        return True