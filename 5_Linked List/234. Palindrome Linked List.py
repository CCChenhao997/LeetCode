"""
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # 双指针法: 时间复杂度O(n)，空间复杂度O(n)
    def isPalindrome(self, head: ListNode) -> bool:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        return list1 == list1[::-1]
        # p1, p2 = 0, len(list1) - 1
        # while p1 <= p2:
        #     if list1[p1] != list1[p2]:
        #         return False
        #     p1 -= 1
        #     p2 -= 1
        # return True
        
    
    # 切成两半，把后半段反转，然后比较两半是否相等。
    # 时间复杂度: O(n)，空间复杂度: O(1)
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        # Find the end of first half and reverse second half
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        
        # Check whether or not there's a palindrome
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
            
        # Restore the list and return the result
        first_half_end.next = self.reverse_list(second_half_start)
        return result
    
    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous