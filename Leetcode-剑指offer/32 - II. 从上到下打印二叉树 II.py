'''
Description: 
version: 
Author: chenhao
Date: 2020-12-20 21:43:30
'''

"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
   
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        treelevellist = [root]
        while treelevellist:
            vallevellist = []
            tmp = []
            while treelevellist:
                node = treelevellist.pop(0)
                vallevellist.append(node.val)
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            treelevellist = tmp
            res.append(vallevellist)
        return res