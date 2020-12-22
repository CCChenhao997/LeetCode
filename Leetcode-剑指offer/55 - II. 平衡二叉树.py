'''
Description: 
version: 
Author: chenhao
Date: 2020-12-22 22:13:28
'''

"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def recur(root):
            if not root:
                return 0

            leftDepth = recur(root.left)
            if leftDepth == -1: return -1

            rightDepth = recur(root.right)
            if rightDepth == -1: return -1

            if abs(leftDepth - rightDepth) > 1:
                return -1
            return max(leftDepth, rightDepth) + 1
        
        return recur(root) != -1