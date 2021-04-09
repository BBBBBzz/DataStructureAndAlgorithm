# This is a repository containing notes and examples of common data structure and algorithms.

1. **Notes:** 关于不同数据结构的笔记，包括数组，堆栈，队列，堆，链表，树，哈希图等。
2. **Array:** 常见数组算法题中对个人而言比较重要的部分罗列如下:

   * Intersect
* MaxProfit2
   * Rotate
3. **LinkedList**: 常见链表算法题对个人而言比较重要的部分罗列如下：
   - Start of LinkedList Cycle (Medium)
4. **SortingAlgorithm:**

* **SelectionSort:** 选择排序，从头往后依次遍历，每一轮中，首先找到数组中最小的元素，然后将其与当前值做交换。
* **InsertionSort:** 插入排序，像打牌时改变手牌顺序的步骤一样，对于第i张牌而言，我们认为前i-1张牌已经排好序，并    且通过比对大小将第i张牌插入到第j个位置(j<=i)，并且将j+1到第i-1张牌向后移动一格。
* **ShellSort:** 希尔排序（升级版InsertionSort），将一个数组分成多个含有h个元素的数组，在每一个子数组中进行以h为间隔的插入排序，并且逐步减小h的值（比如h = len(nums) // 2, h = h//2），最后对大数组做插入排序。
* **QuickSort:** 快速排序，从数列中挑选一个元素作为基准 (pivot)，重新排序数列，将比基准大的数移动到基准后面，比基准小的数移动到基准前面。完成时这个基准就处于数列中的位置。然后更新基准为其前一个数，递归地完成上述操作直到满足边界条件 (left >= right)。
* **MergeSort:** 归并排序，将数列先利用分的思想对半分解成一个小数组，然后利用治的思想将前面得到的小数组组合起来得到有序数组。

