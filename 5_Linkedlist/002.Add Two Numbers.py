"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return None
        maxList, minList, maxLen, minLen = self.judgeLength(l1, l2)
        MaxList = maxList
        a = 0   # a表示进位
        for i in range(minLen):
            sumVal = maxList.val + minList.val + a
            a = 0
            maxList.val = sumVal % 10
            if minList.next:
                maxList = maxList.next
                minList = minList.next
            if sumVal >= 10:
                a = 1
        while a == 1:
            if not maxList.next:
                maxList.next = ListNode(0)
            maxList = maxList.next
            sumVal = maxList.val + a
            a = 0
            maxList.val = sumVal % 10
            if sumVal >= 10:
                a = 1
        return MaxList
            
    
    def judgeLength(self, l1, l2):
        ml1, ml2 = l1, l2
        length1, length2 = 0, 0
        while l1:
            length1 += 1
            l1 = l1.next
        while l2:
            length2 += 1
            l2 = l2.next
        return (ml1, ml2, length1, length2) if length1 >= length2 else (ml2, ml1, length2, length1)
    
    
    def addTwoNumbers2(self, l1, l2):
        re = ListNode(0)
        r = re
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s%10)
            r = r.next
            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
        if carry>0:
            r.next=ListNode(1)
        return re.next

    
    
# node_a = ListNode(2)
# node_b = ListNode(4)
# node_c = ListNode(3)
# node_A = ListNode(5)
# node_B = ListNode(6)
# node_C = ListNode(4)

# node_a.next = node_b
# node_b.next = node_c
# node_A.next = node_B
# node_B.next = node_C

node_a = ListNode(5)
node_A = ListNode(5)

s = Solution()
node = s.addTwoNumbers(node_a, node_A)
while node:
    # print("循环")
    print(node.val)
    node = node.next