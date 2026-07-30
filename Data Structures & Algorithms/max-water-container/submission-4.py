class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        area = 0
        while l<=r:
            area =max(area, min(heights[l],heights[r])*(r-l))
            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                l, r = l+1, r-1

        return area