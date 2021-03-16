"""
问题：
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false

示例：
输入: [1,2,3,1]
输出: true
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        n = len(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
