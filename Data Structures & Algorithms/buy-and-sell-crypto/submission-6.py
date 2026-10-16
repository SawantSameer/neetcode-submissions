class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        curProfit = maxProfit = 0
        while r<len(prices):
            if prices[r]<prices[l]:
                l = r
                r = r+1
                curProfit = 0
            else:
                curProfit = prices[r]-prices[l]
                maxProfit = max(maxProfit, curProfit)
                r+=1
            
        return maxProfit