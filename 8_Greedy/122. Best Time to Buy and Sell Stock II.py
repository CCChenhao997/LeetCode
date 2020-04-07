'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-04-07 09:45:42
@LastEditors: chenhao
@LastEditTime: 2020-04-07 10:12:16
'''

"""
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            else:
                profit += (prices[i] - buy)
                buy = prices[i]
        return profit
    
    
    def maxProfit1(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit