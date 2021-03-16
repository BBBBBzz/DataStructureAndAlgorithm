# This is a repository containing notes and examples of common data structure and algorithms.

1. **Notes:** notes of different data structure including array, stack, queue, heap, linked list, tree, hash map, etc.

2. **Array:** exercises related to array, important ones are listed here:

   * Intersect

   * MaxProfit2

   * Rotate

3. **SortingAlgorithm:**
   * SelectionSort: 选择排序，从头往后依次遍历，每一轮中，首先找到数组中最小的元素，然后将其与当前值做交换。
   * InsertionSort: 插入排序，像打牌时改变手牌顺序的步骤一样，对于第i张牌而言，我们认为前i-1张牌已经排好序，并    且通过比对大小将第i张牌插入到第j个位置(j<=i)，并且将j+1到第i-1张牌向后移动一格。
   * ShellSort: 希尔排序（升级版InsertionSort），将一个数组分成多个含有h个元素的数组，在每一个子数组中进行以h为间隔的插入排序，并且逐步减小h的值（比如h = len(nums) // 2, h = h//2），最后对大数组做插入排序。