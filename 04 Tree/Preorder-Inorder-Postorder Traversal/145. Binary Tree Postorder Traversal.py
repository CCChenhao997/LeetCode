'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-16 14:27:36
@LastEditors: chenhao
@LastEditTime: 2020-03-16 14:49:24
'''

"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        nodeStack = []
        valList = []
        if root:
            nodeStack.append(root)
        while nodeStack:
            node = nodeStack.pop()
            valList.append(node.val)
            if node.left: nodeStack.append(node.left)
            if node.right: nodeStack.append(node.right)
        valList.reverse()
        return valList
            

# valList = [1, 2, 3]
# valList.reverse()
# print(valList)