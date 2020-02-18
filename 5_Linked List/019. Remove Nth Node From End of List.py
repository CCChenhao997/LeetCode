"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # if not head:
        #     return None
        p1 = head
        lengthOfList = 0
        while p1:
            lengthOfList += 1
            p1 = p1.next
        
        # Remove the n-th node from the end of list means removing the (len - n + 1)-th node from the beginning of list
        p2 = head
        Nth = 0
        while p2:
            Nth += 1
            if n == lengthOfList:
                return head.next
            if Nth == (lengthOfList - n):
                p2.next = p2.next.next
                return head
            p2 = p2.next
    
    # Approach 1: Two pass algorithm
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        """
        The "dummy" node is used to simplify some corner cases such as a list with only one node, or removing the head of the list. 
        """
        dummy, dummy.next = ListNode(0), head
        length = 0
        first = head
        while first:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

    # Approach 2: One pass algorithm
    # Two pointers
    def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:
        dummy, dummy.next = ListNode(0), head
        first, second = dummy, dummy
        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(n+1):
            first = first.next
        # Move first to the end, maintaining the gap
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next