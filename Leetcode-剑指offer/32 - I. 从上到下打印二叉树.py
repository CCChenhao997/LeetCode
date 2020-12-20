'''
Description: 
version: 
Author: chenhao
Date: 2020-12-20 21:42:08
'''

"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
   
返回：
[3,9,20,15,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
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
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        levelList = [root]
        while levelList:
            node = levelList.pop(0)
            res.append(node.val)
            if node.left: levelList.append(node.left)
            if node.right: levelList.append(node.right)
        return res