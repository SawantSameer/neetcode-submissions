class Solution:
    def minSwaps(self, s: str) -> int:
        extraClose = 0
        maxClose = 0

        for char in s:
            if char=='[':
                extraClose-=1
            else:
                extraClose+=1

            maxClose = max(maxClose, extraClose)

        return (maxClose+1)//2