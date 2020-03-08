'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-08 09:50:28
@LastEditors: chenhao
@LastEditTime: 2020-03-08 10:44:39
'''

"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:
              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

Example 2:
Input:
              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            leftLength = dfs(node.left)
            rightLength = dfs(node.right)
            leftPath = rightPath = 0
            if node.left and node.left.val == node.val:
                leftPath = 1 + leftLength
            if node.right and node.right.val == node.val:
                rightPath = 1 + rightLength
            self.ans = max(self.ans, leftPath + rightPath)  # update the longest path
            return max(leftPath, rightPath)
        dfs(root)
        return self.ans