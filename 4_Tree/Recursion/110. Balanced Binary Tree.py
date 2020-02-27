'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-02-26 09:18:30
@LastEditors: chenhao
@LastEditTime: 2020-02-27 10:13:54
'''

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
 

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 自顶向下递归，时间复杂度:O(nlogn)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return abs(left - right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
       
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    

# 自底向上递归，时间复杂度:O(n)
class Solution:  
    def __init__(self):
        self.flag = True

    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            if abs(left - right) > 1:
                self.flag = False
            return max(left, right)
        helper(root)
        return self.flag