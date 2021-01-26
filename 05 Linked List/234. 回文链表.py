'''
Description: 
version: 
Author: chenhao
Date: 2021-01-26 20:00:04
'''

"""
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        pre = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow
            slow = slow.next
            tmp.next = pre
            pre = tmp
            
        if fast: slow = slow.next   # 如果链表长度为奇数
        while pre and slow:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next
        return True
