"""
题目描述:
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。

思路:
中序遍历
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.treeNode = []
    
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k <= 0 or not pRoot:
            return None
        self.inOrder(pRoot)
        if len(self.treeNode) < k:
            return None
        return self.treeNode[k-1]   
    
    def inOrder(self, pRoot):
        if not pRoot:
            return None
        if pRoot.left:
            self.inOrder(pRoot.left)
        self.treeNode.append(pRoot)
        if pRoot.right:
            self.inOrder(pRoot.right)
        