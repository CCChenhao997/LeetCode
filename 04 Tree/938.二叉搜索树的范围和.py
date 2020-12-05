'''
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
二叉搜索树保证具有唯一的值。

示例 1：
输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32

示例 2：
输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
输出：23

提示：
    1.树中的结点数量最多为 10000 个。
    2.最终的答案保证小于 2^31。

链接：https://leetcode-cn.com/problems/range-sum-of-bst
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
方法一：深度优先搜索
我们对树进行深度优先搜索，对于当前节点 node，如果 node.val 小于等于 L，那么只需要继续搜索它的右子树；
如果 node.val 大于等于 R，那么只需要继续搜索它的左子树；如果 node.val 在区间 (L, R) 中，则需要搜索它的所有子树。

我们在代码中用递归和迭代的方法分别实现了深度优先搜索。
'''

# 递归实现深度优先搜索
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def dfs(node):
            if node:
                if L <= node.val <=R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.left)
        
        self.ans = 0
        dfs(root)
        return self.ans

'''
# 迭代实现深度优先搜索
class Solution(object):
    def rangeSumBST(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans
'''