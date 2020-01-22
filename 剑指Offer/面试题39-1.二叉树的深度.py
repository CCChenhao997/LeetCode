"""
题目描述：
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

思路：
1. 递归
2. 非递归
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    # 递归
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        else:
            return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
    
    # 非递归(广度优先遍历)  
    def TreeDepth2(self, pRoot):
        if not pRoot:
            return 0
        a = [pRoot]
        depth = 0
        while a:
            b = []
            for node in a:
                if node.left:
                    b.append(node.left)
                if node.right:
                    b.append(node.right)
            a = b
            depth += 1
        return depth
    
    # 使用队列
    def TreeDepth3(self, pRoot):
        if not pRoot:
            return 0
        from collections import deque   # 双端队列
        dq = deque()
        layer = 1
        dq.append((pRoot, 1))
        while dq:
            node, layer = dq.popleft()
            depth = layer
            if node.left:
                dq.append((node.left, layer+1))
            if node.right:
                dq.append((node.right, layer+1))
        return depth