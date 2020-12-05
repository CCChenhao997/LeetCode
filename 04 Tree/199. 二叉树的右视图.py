'''
Description: 
version: 
Author: chenhao
Date: 2020-12-01 09:49:00
'''

"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:
输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]

解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def bfs(root):
            if not root:
                return
            queue = []
            queue.append(root)
            path.append([root.val])
            while queue:
                valueList = []
                nextQueue = []
                for node in queue:
                    if node.right:
                        nextQueue.append(node.right)
                        valueList.append(node.right.val)
                    if node.left:
                        nextQueue.append(node.left)
                        valueList.append(node.left.val)
                queue = nextQueue
                if len(valueList) > 0:
                    path.append(valueList[:])
        
        path = []   
        bfs(root)
        res = []
        for vallist in path:
            res.append(vallist[0])
        return res
