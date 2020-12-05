'''
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false

示例 3:
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 解法一: 递归
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p and q are both None
        if not p and not q:
            return True
        
        # one of p and q is None
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        # return True if left and right are both True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


"""
# 解法二: 迭代
'''
从根开始，每次迭代将当前结点从双向队列中弹出。然后，进行方法一中的判断：
- p 和 q 不是 None,
- p.val 等于 q.val,
若以上均满足，则压入子结点。
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        from collections import deque
        
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):  # check(p, q) 返回 False
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        
        return True
"""        
            
