"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy, dummy.next = ListNode(0), head
        p1 = dummy
        p2, p3 = p1.next, p1.next.next
        
        while p2 and p3:
            p1.next = p3
            p2.next = p3.next
            p3.next = p2

            p1 = p2
            p2 = p1.next
            if p2:
                p3 = p2.next
            
        return dummy.next
    
        
        # Recursion
        def swapPairs2(self, head: ListNode) -> ListNode:
            # If the list has no node or has only node left.
            if not head or not head.next:
                return head
            
            # Nodes to be swapped
            first_node = head
            second_node = head.next
            
            # Swapping
            first_node.next = self.swapPairs(second_node.next)
            second_node.next = first_node
            
            return second_node
        
        
        # Iteration
        def swapPairs3(self, head: ListNode) -> ListNode:
            # Dummy node acts as the prevNode for the head node of the list
            # and hence stores pointer to the head node.
            dummy = ListNode(-1)
            dummy.next = head
            
            prev_node = dummy
            
            while head and head.next:
                
                # Nodes to be swapped
                first_node = head
                second_node = head.next
                
                # Swapping
                prev_node.next = second_node
                first_node.next = second_node.next
                second_node.next = first_node
                
                # Reinitializing the head and prev_node for next swap
                prev_node = first_node
                head = first_node.next
                
            # Return the new head node.
            return dummy.next