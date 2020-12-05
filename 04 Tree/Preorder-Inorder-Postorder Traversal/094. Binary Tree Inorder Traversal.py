'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-16 14:55:47
@LastEditors: chenhao
@LastEditTime: 2020-03-16 16:51:03
'''

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]

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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodeStack = []
        valList = []
        cur = root
        while nodeStack or cur:
            while cur:
                nodeStack.append(cur)
                cur = cur.left
            cur = nodeStack.pop()
            valList.append(cur.val)
            cur = cur.right
        return valList 
    
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        valList = []
        nodeStack = []
        nodeStack = [(WHITE, root)]
        while nodeStack:
            color, node = nodeStack.pop()
            if not node: continue
            if color == WHITE:
                nodeStack.append((WHITE, node.right))
                nodeStack.append((GRAY, node))
                nodeStack.append((WHITE, node.left))
            else:
                valList.append(node.val)
        return valList
        


if __name__=="__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(1)
    
    node1.left = node2
    node2.left = node3
    
    s = Solution()
    print(s.inorderTraversal(node1))