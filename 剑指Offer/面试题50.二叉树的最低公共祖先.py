
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 二叉排序树中求解两个结点的最低公共祖先
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root:
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left, p, q)
            elif root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else: 
                return root
        return None
    

# 普通二叉树中求解两个结点的最低公共祖先
class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or p is None or q is None:
            return None
        path1 = []
        self.getPath(root, p, path1)
        path2= []
        self.getPath(root, q, path2)
        result = None
        for i in range(min(len(path1), len(path2))):
            if path1[i] == path2[i]:
                result = path1[i]
            else:
                break
        return result
    
    def getPath(self, root, targetNode, path):
        if len(path) > 0 and path[-1] == targetNode:
            return
        if root:
            path.append(root)
            self.getPath(root.left, targetNode, path)
            self.getPath(root.right, targetNode, path)
            if len(path) > 0 and path[-1] != targetNode:
                path.pop()