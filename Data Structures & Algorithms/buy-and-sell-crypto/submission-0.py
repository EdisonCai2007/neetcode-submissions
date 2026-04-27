class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1
        max_profit = 0

        while rp < len(prices):
            max_profit = max(max_profit, prices[rp] - prices[lp])

            if prices[rp] < prices[lp]:
                lp, rp = rp, rp + 1
            else:
                rp += 1
        
        return max_profit

# [10,1,5,6,7,1]
# max_profit = 6

# [10,8,7,5,2]
# max_profit = 0