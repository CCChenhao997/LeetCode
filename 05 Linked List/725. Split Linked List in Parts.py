"""
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".
The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.
The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.
Return a List of ListNode's representing the linked list parts that are formed.
Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].

Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

Note:
The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
"""


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        retList = []
        if not root:
            while k:
                retList.append(None)
                k -= 1
            return retList
        
        length = 0
        head = root
        while head:
            length += 1
            head = head.next
        if length <= k:
            res = k - length
            p1 = root
            p2 = p1.next
            while length:
                p1.next = None
                retList.append(p1)
                p1 = p2
                if p2:
                    p2 = p2.next
                length -= 1
            while res:
                retList.append(None)
                res -= 1
        else:
            res = length // k
            ram = length % k
            numList = []
            for i in range(k):
                if ram > 0:
                    numList.append(res + 1)
                    ram -= 1
                else:
                    numList.append(res)
            p1 = root
            head = p1
            pre = p1
            for num in numList:
                while num - 1:
                    head = head.next
                    num -= 1
                p1 = head.next
                head.next = None
                head = p1
                retList.append(pre)
                pre = p1
        return retList
    
    
    # Approach#1: Create New Lists
    def splitListToParts2(self, root: ListNode, k: int) -> List[ListNode]:
        cur = root
        for N in range(10001):
            if not cur:
                break
            cur = cur.next
        width, remainder = divmod(N, k)
        
        ans = []
        cur = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                # write.next = ListNode(cur.val)
                # write = ListNode(cur.val)
                if cur:
                    cur = cur.next
                ans.append(head.next)
        return ans
    
    
    # Approach#2: Split Input List
    def splitListToParts2(self, root: ListNode, k: int) -> List[ListNode]:
        cur = root
        for N in range(1001):
            if not cur:
                break
            cur = cur.next
        width, remainder = divmod(N, k)
        
        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(width + (i < remainder) - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
        
        

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7

s = Solution()
print(list(s.splitListToParts(l1, 3)))