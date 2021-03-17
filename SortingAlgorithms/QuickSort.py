"""
快速排列：
1. 从数列中挑出一个元素，称为 “基准”（pivot）；
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，
所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。
这个称为分区（partition）操作；
3. 递归地（recursive）把小于基准值元素的子数列和
大于基准值元素的子数列排序。
"""

def partition(arr, left, right):
    # 设定基准值
    pivot = left
    while left < right:
        # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
        while left < right and arr[right] >= arr[pivot]:
            right -= 1
        # 如果列表前边的数,比基准数小或相等,则后移一位直到有比基准数大的数出现
        while left < right and arr[left] <= arr[pivot]:
            left += 1
        # 此时已找到一个比基准大的数，和一个比基准小的数，将他们互换位置
        arr[left], arr[right] = arr[right], arr[left]
    # 当从两边分别逼近，直到两个位置相等时结束，将左边小的数字与基准进行交换
    arr[left], arr[pivot] = arr[pivot], arr[left]
    # 返回目前基准所在位置的索引
    return left


def recur(arr, left, right):
    if left >= right: return
    # 从基准开始分区
    mid = partition(arr, left, right)
    # 递归调用
    recur(arr, left, mid-1)
    recur(arr, mid+1, right)


def quickSort(nums):
    n = len(nums)
    if n < 2: return nums
    recur(nums, 0, n-1)


nums = [5,2,6,4,3,1,8,7]
print(f"Original array: {nums}")
quickSort(nums)
print(f"Sorted array: {nums}")
