'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-16 10:05:44
@LastEditors: chenhao
@LastEditTime: 2020-03-16 10:15:40
'''

"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:
    2
   / \
  1   3
Output:
1

Example 2:
Input:
        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7
Output:
7

Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        nodeList = []
        nodeList.append(root)
        while nodeList:
            lenOfNodeList = len(nodeList)
            for i in range(lenOfNodeList):
                node = nodeList.pop(0)
                if i == 0:
                    leftVal = node.val
                if node.left: nodeList.append(node.left)
                if node.right: nodeList.append(node.right)
        return leftVal