# sliding window. time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = float("inf"), 0
        for price in prices:
            # slightly faster than min_price = min(price, min_price)
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit