"""
归并排序：
1. 利用归并的思想实现的排序方法，该算法采用经典的分治（divide-and-conquer）策略
（分治法将问题分成一些小的问题然后递归求解，而治的阶段则将分的阶段得到的各答案"修补"在一起，
即分而治之)。

复杂度：
1. 时间复杂度：O(nlogn) 以2为底
2. 空间复杂度：O(n),需要一个大小为n的临时数组
"""

def merge(left, right):
    # 如果左子数组为空，直接返回右子数组，反之亦然
    if len(left) == 0: return right
    if len(right) == 0: return left

    res = []
    index_left = index_right = 0

    # 遍历两个数组直到两个数组的元素都被遍历完毕并被放入到结果列表中
    while len(res) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            res.append(left[index_left])
            index_left += 1
        else:
            res.append(right[index_right])
            index_right += 1
        # 如果此时有一个数组已经被遍历完毕，
        # 就把另一个数组的剩余部分直接加到结果列表中
        if index_left == len(left):
            res += right[index_right:]
            break
        if index_right == len(right):
            res += left[index_left:]
            break
    return res

def mergeSort(nums):
    # 递归停止条件
    if len(nums) < 2: return nums
    mid_point = len(nums) // 2
    return merge(left=mergeSort(nums[:mid_point]),
                 right=mergeSort(nums[mid_point:]))

nums = [5,2,6,4,3,1,8,7]
print(f"Original array: {nums}")
nums = mergeSort(nums)
print(f"Sorted array: {nums}")
