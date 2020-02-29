'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-02-29 22:49:31
@LastEditors: chenhao
@LastEditTime: 2020-02-29 23:29:59
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Recursion
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        
        if t1 is None and t2:
            return t2
        elif t1 and t2 is None:
            return t1
        
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1
    
    
    # Iterative Method
    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not (t1 and t2):
            return t2 if not t1 else t1
        
        queue = [(t1, t2)]
        while queue:
            r1, r2 = queue.pop(0)
            r1.val += r2.val
            if r1.left and r2.left:
                queue.append((r1.left, r2.left))
            elif not r1.left:
                r1.left = r2.left
            if r1.right and r2.right:
                queue.append((r1.right, r2.right))
            elif not r1.right:
                r1.right = r2.right
        return t1