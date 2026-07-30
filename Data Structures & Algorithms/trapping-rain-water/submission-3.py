class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix, suffix = [height[0]]*n, [height[-1]]*n

        for i in range(1,n):
            prefix[i] = max(prefix[i-1], height[i])

        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        #return prefix
        res = 0
        for i, h in enumerate(height):
            bar = min(prefix[i], suffix[i])
            if h<bar:
                res += bar - h

        return res