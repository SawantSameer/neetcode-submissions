class Solution:
    def climbStairs(self, n: int) -> int:
        res = 1 
        for i in range(1, n//2 + 1):
            res += math.comb(n-i, i)
        return res
