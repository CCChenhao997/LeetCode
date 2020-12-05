'''
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        # 更牛
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
        """
        # 易懂
        new_head = None
        while head:
            tmp = head.next   # 备份原来head结点的next地址
            head.next = new_head
            new_head = head
            head = tmp
        return new_head