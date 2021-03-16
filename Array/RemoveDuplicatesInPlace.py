"""
题目：
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例1：
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针 slow, fast
        # 当slow指向的元素与fast指向的元素相同时，fast后移一位
        # 当slow指向的元素与fast指向的元素不等时，
        # 更新slow+1的内容使它等于fast指向的内容，slow后移一位
        length = len(nums)
        if length < 2:
            return length
        slow, fast = 0, 1
        while fast < length:
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

solution = Solution()
nums = [1,1,2,2,3]
res = solution.removeDuplicates(nums)
print("The correst result: 3.")
print(f"Your result: {res}.")
