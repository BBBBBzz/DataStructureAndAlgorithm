"""
希尔排序：
1. 可以看作是插入排序的简单改进，通过交换不相邻的元素对数组局部进行排序，
并最终使用插入排序将局部有序的数组进行排序。
2. 具体操作是使任意间隔为h的数组的元素都是有序的，这样的数组被称为h有序数组，
一个h有序数组就是h个互相独立的有序数组编织在一起组成一个数组。

复杂度：
1. 时间复杂度：与增量h的大小选择有关
2. 空间复杂度：O(1)
"""

def ShellInsert(arr, d):
    n = len(arr)
    for i in range(d, n):
        # 希尔排序中每组成员是从原来数组中以间隔d提取出来的
        j = i-d
        min = arr[i]
        while j >= 0 and arr[j] > min:
            arr[j+d], arr[j] = arr[j], arr[j+d]
            j -= d

def ShellSort(nums):
    n = len(nums)
    if n < 2: return
    d = n // 2
    while d >= 1:
        ShellInsert(nums, d)
        d //= 2

nums = [5,2,6,4,3,1,8,7]
print(f"Original array: {nums}")
ShellSort(nums)
print(f"Sorted array: {nums}")
