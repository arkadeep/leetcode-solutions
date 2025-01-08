class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        p1 = 0
        p2 = 1

        max_profit = 0

        while p2 < len(prices):
            
            # print(f"Current pointers: {p1}, {p2}")
            profit = prices[p2] - prices[p1]
            # print(f"Current profit: {profit}")

            if profit < 0:
                p1 = p2
            else:
                p2 += 1
                max_profit = max(profit, max_profit)

        return max_profit