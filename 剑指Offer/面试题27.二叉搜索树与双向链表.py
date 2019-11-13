"""
题目描述：
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

思路：
按照左右子树分治，递归实现。根的左边连接左子树的最右边结点，右边连接右子树的最左边结点。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        
        # * 处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        
        # * 连接根结点与左子树最大结点
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree
            
        # * 处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        
        # * 连接根与右子树最小结点
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree
            
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
            
        return pRootOfTree
    
if __name__=='__main__':
    
    pNode1 = TreeNode(10)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(4)
    pNode4 = TreeNode(8)
    pNode5 = TreeNode(14)
    pNode6 = TreeNode(12)
    pNode7 = TreeNode(16)

    pNode1.left = pNode2
    pNode1.right = pNode5
    pNode2.left = pNode3
    pNode2.right = pNode4
    pNode5.left = pNode6
    pNode5.right = pNode7

    S = Solution()
    newList = S.Convert(pNode1)
    while newList:
        print(newList.val)
        newList = newList.right