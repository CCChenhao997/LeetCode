'''
题目描述：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

思路：
前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边。
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # 排除一些情况
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None

        # 得到根结点
        root = TreeNode(pre[0])
        # 获取根结点在中序遍历中的索引值
        i = tin.index(pre[0])
        # 递归
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[0:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root


# 按层序遍历输出树中某一层的值
def PrintNodeAtLevel(treeNode, level):
    if not treeNode or level < 0:
        return 0
    if level == 0:
        print(treeNode.val)
        return 1
    PrintNodeAtLevel(treeNode.left, level-1)
    PrintNodeAtLevel(treeNode.right, level-1)


# 已知树的深度按层遍历输出树的值
def PrintNodeByLevel(treeNode, depth):
    for level in range(depth):
        PrintNodeAtLevel(treeNode, level)