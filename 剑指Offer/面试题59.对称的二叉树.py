"""
题目描述:
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

思路:
分为递归和非递归的两种方式，思想是一样的。
主要就是把叶子节点的None节点也加入到遍历当中。按照前序遍历二叉树，存入一个序列中。
然后按照和前序遍历对应的先父节点，然后右子节点，最后左子节点遍历二叉树，存入一个序列。
如果前后两个序列相等，那么说明二叉树是对称的。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def isSymmetrical(self, pRoot):
        return self.selfIsSymmetrical(pRoot, pRoot)
    
    def selfIsSymmetrical(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.selfIsSymmetrical(pRoot1.left, pRoot2.right) and self.selfIsSymmetrical(pRoot1.right, pRoot2.left)
   

# 非递归
class Solution2:
    def isSymmetrical(self, pRoot):
        preList = self.preOrder(pRoot)
        mirrorList = self.mirrorPreOrder(pRoot)
        if preList == mirrorList:
            return True
        return False
    
    def preOrder(self, pRoot):
        if pRoot == None:
            return [None]
        treeStack = []  # 存储结点
        output = []     # 存储结点的值
        pNode = pRoot
        while pNode or len(treeStack) > 0:
            while pNode:
                treeStack.append(pNode)
                output.append(pNode.val)
                pNode = pNode.left
                if not pNode:
                    output.append(None)
            if len(treeStack):
                pNode = treeStack.pop()
                pNode = pNode.right
                if not pNode:
                    output.append(None)
        return output
    
    def mirrorPreOrder(self, pRoot):
        if pRoot == None:
            return [None]
        treeStack = []
        output = []
        pNode = pRoot
        while pNode or len(treeStack) > 0:
            while pNode:
                treeStack.append(pNode)
                output.append(pNode.val)
                pNode = pNode.right
                if not pNode:
                    output.append(None)
            if len(treeStack):
                pNode = treeStack.pop()
                pNode = pNode.left
                if not pNode:
                    output.append(None)
        return output
        
 

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(6)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(7)
pNode7 = TreeNode(5)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution2()
result = S.isSymmetrical(pNode1)
print(result)