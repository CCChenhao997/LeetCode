'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-27 09:19:47
@LastEditors: chenhao
@LastEditTime: 2020-03-27 09:58:01
'''

"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 
For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        bstDict = {}
        
        def inOrder(node):
            if not node:
                return
            nonlocal bstDict
            inOrder(node.left)
            bstDict[node.val] = bstDict.get(node.val, 0) + 1
            inOrder(node.right)
            
        inOrder(root)
        res = []
        for key, value in bstDict.items():
            if value == max(bstDict.values()):
                max_key = key
                res.append(key)
        return res
    
    
    def findMode1(self, root: TreeNode) -> List[int]:
        
        self.curCnt, self.maxCnt = 1, 1
        self.preNode = None
        self.nums = []
        
        def inOrder(node, nums):
            if not node:
                return
            inOrder(node.left, nums)
            if self.preNode:
                if self.preNode.val == node.val:
                    self.curCnt += 1
                else: self.curCnt = 1
            if self.curCnt > self.maxCnt:
                self.maxCnt = self.curCnt
                nums.clear()
                nums.append(node.val)
            elif self.curCnt == self.maxCnt:
                nums.append(node.val)
            
            self.preNode = node
            inOrder(node.right, nums)   
        
        inOrder(root, self.nums)
        return self.nums