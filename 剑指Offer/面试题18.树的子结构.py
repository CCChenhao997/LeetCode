'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

注意需要判断指针是不是None，避免访问空指针而造成程序崩溃。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1haveTree2(pRoot1, pRoot2)
            # 判断A的左子树中是否包含B树的结构
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            # 判断A的右子树中是否包含B树的结构
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result


    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        # 如果B树为空（首结点之后的为空），那么算B是A的子结构
        if pRoot2 == None:
            return True
        # 到这一步时，说明B的子树不为空，如果A子树为空，当然B不属于A
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        # 根节点值相同，再判断左右子树是否都相同
        return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)


# A树
pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

# B树
pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

test = Solution()
print(test.HasSubtree(pRoot1, pRoot8))