'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-02 08:47:24
@LastEditors: chenhao
@LastEditTime: 2020-03-02 14:19:27
'''

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:  
    # Recursion  
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if root.left is None and root.right is None:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
    
    # Iteration
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False