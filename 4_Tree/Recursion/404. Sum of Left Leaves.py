'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-06 10:14:22
@LastEditors: chenhao
@LastEditTime: 2020-03-06 11:06:00
'''

"""
Find the sum of all left leaves in a given binary tree.

Example:
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    
    
    def sumOfLeftLeaves2(self, root: TreeNode) -> int:
        sum_ = 0
        if not root:
            return 0
        ans = [root]
        while ans:
            r = ans.pop()
            if r.left and not r.left.left and not r.left.right:
                sum_ += r.left.val
            if r.left:
                ans.append(r.left)
            if r.right:
                ans.append(r.right)
        return sum_