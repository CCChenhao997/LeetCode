'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-23 09:33:19
@LastEditors: chenhao
@LastEditTime: 2020-03-23 18:09:39
'''

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # Time Complexity O(N), Space Complexity O(N)
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        
        def toBST(nums, sIdx, eIdx):
            if sIdx > eIdx:
                return
            mIdx = (sIdx + eIdx) // 2
            root = TreeNode(nums[mIdx])
            root.left = toBST(nums, sIdx, mIdx - 1)
            root.right = toBST(nums, mIdx + 1, eIdx)
            return root
        
        return toBST(nums, 0, len(nums) - 1)
    
    
    # Time Complexity O(N), Space Complexity O(logN)
    def sortedListToBST1(self, head: ListNode) -> TreeNode:
        size = 0
        p = head
        while p:
            size += 1
            p = p.next
            
        def rebuildTree(l, r):
            nonlocal head
            if l >= r:
                return None
            
            mid = (l + r) // 2
            
            left = rebuildTree(l, mid)
            root = TreeNode(head.val)
            root.left = left
            
            head = head.next
            
            root.right = rebuildTree(mid + 1, r)
            
            return root
        
        return rebuildTree(0, size)