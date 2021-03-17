"""
冒泡排序:
1. 无序序列头部开始，进行两两比较，根据大小交换位置，
直到最后将最大（小）的数据元素交换到了无序队列的队尾，从而成为有序序列的一部分。
2. 从头开始遍历数组直到结束为止。

算法复杂度：
1. 时间复杂度：O(n^2)
2. 空间复杂度：O(1)
"""

def bubbleSort(nums):
    n = len(nums)
    if n < 2: return
    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                # 如果当前值比后面一个邻近值大，交换他们
                nums[j], nums[j+1] = nums[j+1], nums[j]
                already_sorted = False
        if already_sorted:
            break

nums = [5,2,6,4,3,1,8,7]
print(f"Original array: {nums}")
bubbleSort(nums)
print(f"Sorted array: {nums}")
