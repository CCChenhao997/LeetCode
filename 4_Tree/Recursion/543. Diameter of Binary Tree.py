'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-02-28 09:33:20
@LastEditors: chenhao
@LastEditTime: 2020-02-28 10:00:45
'''

"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxDiameter = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxDeep(root)
        return self.maxDiameter
        
    def maxDeep(self, root):
        if not root:
            return 0
        left = self.maxDeep(root.left)
        right = self.maxDeep(root.right)
        if left + right > self.maxDiameter:
            self.maxDiameter = left + right
        return max(left, right) + 1
        