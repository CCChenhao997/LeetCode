'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-16 10:36:04
@LastEditors: chenhao
@LastEditTime: 2020-03-16 11:56:53
'''

"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        nodeStack = []
        valList = []
        if root:
            nodeStack.append(root)
        while nodeStack:
            node = nodeStack.pop()
            valList.append(node.val)
            if node.right: nodeStack.append(node.right)
            if node.left: nodeStack.append(node.left)
        return valList