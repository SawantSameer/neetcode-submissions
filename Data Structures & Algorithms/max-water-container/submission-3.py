class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        for i in range(n-1): 
            c_area = 0
            for j in range(i+1, n):
                c_area = min(heights[i], heights[j])*(j-i)
                area = max(area, c_area)

        return area