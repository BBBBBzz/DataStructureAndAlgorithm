"""
题目：
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例：
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        cash = 0            # 持有现金
        hold = -prices[0]   # 持有股票
        precash = cash      # 前次持有现金
        prehold = hold      # 前次持有股票
        for i in range(1, n):
            # 当天不持有股票的情况下
            # 状态可以是来自前次不持有股票，或者在前次持有股票的情况下在当天卖出股票
            cash = max(precash, hold + prices[i])
            # 当天持有股票的情况下
            # 状态可以是来自前次就持有股票，或者前次没有股票的情况下当天买入股票
            hold = max(prehold, cash - prices[i])
            precash = cash
            prehold = hold
        # 最后买入股票无意义，所以只关注持有的现金状态（不持有股票）
        return cash

solution = Solution()
res = solution.maxProfit([1,2,3,4,5])
print("The correst result: 4.")
print(f"Your result: {res}.")
