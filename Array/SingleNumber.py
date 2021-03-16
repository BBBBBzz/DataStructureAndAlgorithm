"""
题目:
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素

示例：
输入: [2,2,1]
输出: 1
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 使用异或运算，相同的数字异或会得到0
        # 非零数字与零进行疑惑运算会得到本身
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]

        return res
