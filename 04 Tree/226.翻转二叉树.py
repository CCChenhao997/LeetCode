'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 解法一: DFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


"""
# 解法二: BFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        from collections import deque
        if not root:
            return
        queue = deque()  # 双端队列
        queue.appendleft(root)
        while queue:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        return root
"""