"""
题目：
给定两个数组，编写一个函数来计算它们的交集。

示例：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
"""
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 将两个数组进行排序，随后用双指针顺序查找相同的元素
        # 时间复杂度：O(max(nlogn, mlogm, n+m))
        # 空间复杂度: O(1)
        nums1.sort()
        nums2.sort()
        res = []
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] == nums2[right]:
                res.append(nums1[left])
                left += 1
                right += 1
            else:
                right += 1
        return res
