"""
插入排序:
将数组的第一个数认为是有序数组，从后往前（从前往后）扫描该有序数组，
把数组中其余n-1个数，根据数值的大小，插入到有序数组中，直至数组中的所有数有序排列为止。

复杂度：
1. 时间复杂度：最坏情况下需要N^2/2，即O(N^2)
2. 空间复杂度：最坏的情况下需要N^2/2，即O(N^2)
"""

def insertionSort(nums):
    n = len(nums)
    if n < 2: return nums
    for i in range(1, n):
        # 在当前位置从后往前遍历
        j = i
        # 假设当前值
        min = nums[i]
        while j > 0 and nums[j-1] > min:
            # 如果当前位置之前的值大于当前值(min)
            # 将前面比较大的值向后推一格，模拟人打牌时将牌插入到一个位置
            # 这张牌后面的牌都相当于往后退了一格
            nums[j] = nums[j-1]
            j -= 1
        # 找到合适的位置，将数字插入
        nums[j] = min

nums = [5,2,6,4,3,1,8,7]
print(f"Original array: {nums}")
insertionSort(nums)
print(f"Sorted array: {nums}")
