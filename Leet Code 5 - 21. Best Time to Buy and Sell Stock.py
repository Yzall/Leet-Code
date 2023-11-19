# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        # Variables to keep track of minimum price and maximum profit
        min_price = prices[0]
        max_profit = 0

        # Iterate through the prices
        for price in prices:
            # Update the minimum price if the current price is lower
            min_price = min(min_price, price)

            # Update the maximum profit if selling at the current price yields a higher profit
            max_profit = max(max_profit, price - min_price)

        return max_profit
