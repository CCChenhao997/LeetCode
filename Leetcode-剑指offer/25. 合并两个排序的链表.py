'''
Description: 
version: 
Author: chenhao
Date: 2020-12-20 20:19:48
'''

"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        newlist = ListNode(-1)
        backup = newlist
        while l1 and l2:
            if l1.val < l2.val:
                newlist.next = l1
                l1 = l1.next
            else:
                newlist.next = l2
                l2 = l2.next
            
            newlist = newlist.next
        
        newlist.next = l1 if l1 else l2
        return backup.next