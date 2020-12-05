'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-04 20:01:49
@LastEditors: chenhao
@LastEditTime: 2020-03-04 20:23:02
'''

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
        
    def helper(self, node1: TreeNode, node2: TreeNode) -> bool:
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)