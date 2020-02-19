"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2 = [], []
        # Put l1 and l2 into list1 and list2 respectively
        while l1 or l2:
            if l1:
                list1.append(l1.val)
                l1 = l1.next
            if l2:
                list2.append(l2.val)
                l2 = l2.next
        flag = 0
        p = ListNode(-1)
        while list1 or list2:
            res = 0
            if list1:
                res += list1.pop()
            if list2:
                res += list2.pop()
            res += flag
            flag = res // 10
            head = ListNode(res % 10)
            head.next = p.next
            p.next = head
        if flag:
            head = ListNode(flag)
            head.next = p.next
            p.next = head
        return p.next