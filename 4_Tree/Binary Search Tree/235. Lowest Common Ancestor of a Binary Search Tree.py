'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-19 23:01:26
@LastEditors: chenhao
@LastEditTime: 2020-03-19 23:27:07
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果 p 和 q 的值满足 p.val > root.val > q.val 或者 p.val < root < q.val，则root即为最近公共祖先
        # 注：自己也可以是自己的祖先
        if p.val > root.val > q.val or p.val < root.val < q.val or root.val == p.val or root.val == q.val:
            return root
        
        # 如果 p 和 q 的值均大于 root 的值，则最近公共祖先在右子树中
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # 如果 p 和 q 的值均小于 root 的值，则最近公共祖先在左子树中
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
    
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val
        node = root
        while node:
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node