'''
Description: 
version: 
Author: chenhao
Date: 2020-12-20 23:30:29
'''

"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:
[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, tmp = [], []
        def DFS(root, sum):
            if not root: return
            tmp.append(root.val)
            sum -= root.val
            if sum == 0 and not root.left and not root.right:
                res.append(list(tmp))
            DFS(root.left, sum)
            DFS(root.right, sum)
            tmp.pop()
        
        DFS(root, sum)
        return res