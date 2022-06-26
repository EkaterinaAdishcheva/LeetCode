class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit_fix, buy_min = 0, prices[0]
        for sell in range(1, len(prices)):
            profit_fix = max(prices[sell] - buy_min, profit_fix)
            buy_min = min(buy_min, prices[sell])
        print(profit_fix)
        return profit_fix

solution = Solution()
solution.maxProfit([7,6,4,3,1])
