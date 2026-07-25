class Solution:
    def hammingWeight(self, n: int) -> int:
        bin = ''
        while n!=0:
            bin = str(n%2) + bin
            n = n//2
        cnt = 0
        for c in bin:
            if int(c)&1:
                cnt += 1

        return cnt