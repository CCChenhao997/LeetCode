'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-26 15:07:51
@LastEditors: chenhao
@LastEditTime: 2020-03-26 15:32:29
'''

"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note:
There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        preNode = None
        minDiff = float('inf')
        
        def inOrder(node):
            if not node:
                return
            nonlocal preNode
            nonlocal minDiff
            inOrder(node.left)
            if preNode:
                minDiff = min(minDiff, node.val - preNode.val)
            preNode = node
            inOrder(node.right)
            
        inOrder(root)
        return minDiff