"""
中心思想：
1. 首先，找到数组中最小的元素，将其与数组中第一个元素进行交换（如果第一个元素就是最小的元素那么它就自己和自己换）
2. 其次，在剩下的元素中找到最小的元素，将其与数组中第二个元素进行交换，以此类推

复杂度：
1. 时间复杂度：最多需要进行(N^2)/2 比较, 即O(N^2)
2. 空间复杂度：最多需要进行N次交换， 即O(N)
"""


def insertionSort(nums):
    n = len(nums)
    if n <= 1: return nums
    for i in range(0, n):
        # 初始化当前最小值的索引
        min = i
        for j in range(i+1, n):
            # 从前往后开始遍历，如果遇到比当前值更小的值
            # 更新索引
            if nums[j] < nums[min]: min = j
        # 把找到的最小值与当前值做交换
        nums[i], nums[min] = nums[min], nums[i]

nums = [5,2,6,4,3,1,8,7]
print(f"Original array: {nums}")
insertionSort(nums)
print(f"Sorted array: {nums}")
