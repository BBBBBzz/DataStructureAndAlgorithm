"""
问题：
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

说明：不允许修改给定的链表。

示例：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
"""


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        用快慢指针检测链表是否有环
        链表无环，快慢指针不会相遇，返回Null
        链表有环，快慢指针会在某一时刻在环内相遇
        假设共有a + b个节点
        其中a为链表头到循环起点的路长，b为循环链表的节点数
        快指针的速度是慢指针的两倍，即 f = 2s
        快指针走过的路程可以表达为 f = s + nb, 其中nb代表快指针在循环中比慢指针已经多走过了n个循环的长度才相遇
        所以可以解得s = nb
        如果让其中一个指针回到原点，那么只要走a+nb步，即可再次到达循环入口处，因为从头走a步即到达循环入口，走nb个循环以后
        还是停在循环入口
        现在的问题是不知道a的大小
        于是考虑让s停留在原地，让f到链头处，两个指针同时往前走，此时s正好走了nb步，当f走a步的时候，s走了a+nb步，正好停在
        入口处
        """

    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return self.findStart(head, slow)
        return

    def findStart(self, head, slow):
        cur = head
        while cur != slow:
            cur = cur.next
            slow = slow.next
        return cur
