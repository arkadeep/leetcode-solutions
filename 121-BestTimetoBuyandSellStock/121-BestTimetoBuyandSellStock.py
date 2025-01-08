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
                p1 += 1
            else:
                p2 += 1
                max_profit = max(profit, max_profit)

        return max_profit



    # More efficient solution:


    # class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     l, r = 0, 1
    #     maxP = 0

    #     while r < len(prices):
    #         if prices[l] < prices[r]:
    #             profit = prices[r] - prices[l]
    #             maxP = max(maxP, profit)
    #         else:
    #             l = r
    #         r += 1
    #     return maxP