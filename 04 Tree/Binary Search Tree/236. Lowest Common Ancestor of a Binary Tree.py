'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-20 21:48:35
@LastEditors: chenhao
@LastEditTime: 2020-03-21 00:44:58
'''

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 
Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return root
        elif left:
            return left
        elif right:
            return right
        
    
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = None
        
        def helper(root, p, q):
            if not root or self.result:
                return 0
            count = helper(root.left, p, q) + helper(root.right, p, q)
            if root == p or root == q:
                count += 1
            if count == 2 and self.result is None:
                self.result = root
            return count
        
        helper(root, p ,q)
        return self.result
        
        
if __name__=="__main__":
    # root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    node1 = TreeNode(3)
    node2 = TreeNode(5)        
    node3 = TreeNode(1)
    node4 = TreeNode(6)
    node5 = TreeNode(2)
    node6 = TreeNode(0)
    node7 = TreeNode(8)
    node8 = TreeNode(7)
    node9 = TreeNode(4)
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9
    
    s = Solution()
    print("lca:", s.lowestCommonAncestor1(node1, node2, node9).val)
    