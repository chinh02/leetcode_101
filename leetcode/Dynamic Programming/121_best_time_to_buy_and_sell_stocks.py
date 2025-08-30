# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
prices = [7,1,5,3,6,4]


import sys
from typing import List


def maxProfit(prices: List[int]) -> int:
        result = 0
        min_price = sys.maxsize
        for price in prices:
            if min_price > price:
                min_price = price
            elif price - min_price > result:
                result = price - min_price
        return result

print(maxProfit(prices))