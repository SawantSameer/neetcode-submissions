class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,1
        profit = 0
        while j<len(prices):
            if prices[i:j+1]==sorted(prices[i:j+1]):
                j+=1
            else:
                profit += prices[j-1]-prices[i]
                i=j
                j+=1
        profit += prices[j-1]-prices[i]
        return profit
                
                