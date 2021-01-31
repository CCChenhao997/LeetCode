'''
Description: 
version: 
Author: chenhao
Date: 2021-01-31 15:25:54
'''

"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

提示：
链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # * 递归归并 Time O(nlogn), Space O(logn)
        # def merge(head1, head2):
        #     dummyHead = ListNode(0)
        #     temp, temp1, temp2 = dummyHead, head1, head2
        #     while temp1 and temp2:
        #         if temp1.val <= temp2.val:
        #             temp.next = temp1
        #             temp1 = temp1.next
        #         else:
        #             temp.next = temp2
        #             temp2 = temp2.next
        #         temp = temp.next
        #     temp.next = temp1 if temp1 else temp2
        #     return dummyHead.next
        
        # def get_mid(node):
        #     if not node: return node
        #     slow, fast = node, node
        #     while fast.next and fast.next.next:
        #         slow = slow.next
        #         fast = fast.next.next
        #     return slow
        
        # if not head or not head.next:
        #     return head
        # mid = get_mid(head)
        # left = head
        # right = mid.next
        # mid.next = None
        # return merge(self.sortList(left), self.sortList(right))
        
        # * 迭代递归 Time O(nlogn), Space O(1)
        h, length, intv = head, 0, 1
        while h:
            h = h.next
            length += 1
            
        res = ListNode(0)
        res.next = head
        while intv < length:    # 当单元长度 >= 链表长度时，归并结束
            pre, h = res, res.next
            while h:
                h1, i = h, intv
                while i and h:
                    h = h.next
                    i -= 1
                if i: break     # 说明上个while中 h 已经 None 了 (h2 is None)
                
                h2, i = h, intv
                while i and h:
                    h = h.next
                    i -= 1
                
                c1, c2 = intv, intv - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 = c1 - 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 = c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                
                while c1 > 0 or c2 > 0:
                    pre = pre.next
                    c1 -= 1
                    c2 -= 1
                pre.next = h
                
            intv *= 2
            
        return res.next