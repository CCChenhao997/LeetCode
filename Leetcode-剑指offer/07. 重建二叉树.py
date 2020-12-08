'''
Description: 
version: 
Author: chenhao
Date: 2020-12-08 10:49:04
'''

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：
0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        # 前序遍历的第一个节点一定是根节点
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        # 递归构造左子树和右子树
        root.left = self.buildTree(preorder[1 : 1 + idx], inorder[: idx])
        root.right = self.buildTree(preorder[1 + idx: ], inorder[idx + 1: ])
        return root