# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 
"""
if decreasing array, return 0
else
    return highest sell - lowest buy

[1,2,3,4,5,6] => 5

[7,1,2,3,4,5,6] => 5

Input: prices = [3,10,1,5,3,6,4]
buy low => 3
sell high => 10

[6,5,4,3,2,1] => 0

[2,1,2,1,0,1,2] => 
buy low: 1
sell high: 2
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_low = float('inf')
        sell_high = float('-inf')
        profit = 0

        for price in prices:
            if price < buy_low:
                buy_low = price
            elif price >= sell_high or profit <= price - buy_low:
                sell_high = price
                profit = sell_high - buy_low

        return profit
