'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-19 00:37:53
@LastEditors: chenhao
@LastEditTime: 2020-03-19 10:19:39
'''

"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
          
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def traver(root: TreeNode):
            if not root:
                return 
            traver(root.right)
            self.total += root.val
            root.val = self.total
            traver(root.left)
        traver(root)
        return root
    
    
    def convertBST1(self, root: TreeNode) -> TreeNode:
        total = 0
        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximun on the stack
            while node is not None:
                stack.append(node)  
                node = node.right
            
            node = stack.pop()
            total += node.val
            node.val = total
            
            # all nodes with value between the current and its parent
            # lie in the left subtree
            node = node.left
        
        return root
            