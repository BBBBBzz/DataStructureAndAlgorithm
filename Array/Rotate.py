"""
题目：
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例：
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        start = 0
        count = 0
        while count < n:
            cur = start       # 当前坐标，从0开始交换位置
            pre = nums[cur]   # 前一个数字
            while True:       # 循环暂停，回到起始位置，角落无人
                nxt = (cur+k) % n   # 下一个坐标
                tmp = nums[nxt]       # 保存下一个坐标里的数字避免被覆盖
                nums[nxt] = pre       # 交换
                pre = tmp
                cur = nxt
                count += 1
                if start == cur:
                    break
            start += 1

    def rotate(self, nums: List[int], k: int) -> None:
        # 先整体翻转一遍，然后翻转前k个，再翻转剩余部分
        n = len(nums)
        k %= n
        if k == 0:
            return
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)


    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start+=1
            end -= 1

solution = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
solution.rotate(nums, k)
print("The correst result: [5, 6, 7, 1, 2, 3, 4].")
print(f"Your result: {nums}.")
