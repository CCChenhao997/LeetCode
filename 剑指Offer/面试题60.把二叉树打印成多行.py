"""
题目描述：
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

思路:
引入两个队列。首先把当前层的节点存入到一个队列queue1中，然后遍历当前队列queue1，
在遍历的过程中，如果节点有左子树或右子树，依次存入另一个队列queue2。
然后遍历队列queue2，如此往复。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if pRoot == None:
            return []
        nodes, res = [pRoot], []
        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            res.append(curStack)
            nodes = nextStack
        return res