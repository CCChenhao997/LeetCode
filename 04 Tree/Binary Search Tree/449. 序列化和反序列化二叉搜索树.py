'''
Description: 
version: 
Author: chenhao
Date: 2020-12-01 16:05:07
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def preorder(root):
            pre_list = []
            if root:
                pre_list += [str(root.val)]
                pre_list += preorder(root.left)
                pre_list += preorder(root.right)
            return pre_list
        
        return ' '.join(preorder(root))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None

        # 根据前序序列和中序序列构建二叉搜索树
        def helper(preorder, inorder):
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[0])
            idx = inorder.index(root.val)
            root.left = helper(preorder[1: idx + 1], inorder[: idx])
            root.right = helper(preorder[idx + 1: ], inorder[idx + 1: ])
            return root
        
        preorder = [int(s) for s in data.split()]
        inorder = sorted(preorder)
        return helper(preorder, inorder)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans