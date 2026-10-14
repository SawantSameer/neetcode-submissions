class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        area = 0
        while l<r:
            mHeight = min(heights[l],heights[r])
            area = max(area, mHeight*(r-l))

            if mHeight==heights[l]:
                l+=1
            elif mHeight==heights[r]:
                r-=1
            else:
                l+=1
                r-=1

        return area