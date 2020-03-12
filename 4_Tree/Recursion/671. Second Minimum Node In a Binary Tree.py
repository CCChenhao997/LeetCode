'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-12 16:07:32
@LastEditors: chenhao
@LastEditTime: 2020-03-12 16:50:00
'''

"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.
Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
 

Example 2:
Input: 
    2
   / \
  2   2
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root or not root.left:
            return -1
        
        leftVal, rightVal = root.left.val, root.right.val
        if leftVal != root.val and rightVal != root.val:
            return min(leftVal, rightVal)
        if leftVal == root.val:
            leftVal = self.findSecondMinimumValue(root.left)
        if rightVal == root.val:
            rightVal = self.findSecondMinimumValue(root.right)
        if leftVal != -1 and rightVal != -1:
            return min(leftVal, rightVal)
        return leftVal if leftVal != -1 else rightVal
