'''
Description: 
version: 
Author: chenhao
Date: 2020-11-30 21:53:21
'''

"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

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
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
from typing import List

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        stack = []
        path = []

        def dfs(node, value):
            if not node:
                return
            value -= node.val
            stack.append(node.val)
            if not node.left and not node.right and value == 0:    # 叶子结点
                path.append(stack[:])
            dfs(node.left, value)
            dfs(node.right, value)
            stack.pop()
        
        dfs(root, sum)
        return path
            