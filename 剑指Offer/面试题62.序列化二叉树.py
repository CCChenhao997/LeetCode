"""
题目描述:
请实现两个函数，分别用来序列化和反序列化二叉树。这里没有规定序列化的方式。

思路:
最终要实现的是二叉树的序列化和反序列化。
首先来看二叉树的序列化，二叉树的序列化就是采用前序遍历二叉树输出节点，
再碰到左子节点或者右子节点为None的时候输出一个特殊字符"#"。
对于反序列化，就是针对输入的一个序列构建一棵二叉树，我们可以设置一个
指针先指向序列的最开始，然后把指针指向位置的数字转化为二叉树的结点，
后移一个数字，继续转化为左子树和右子树。当遇到当前指向的字符为特殊字符
"#"或者指针超出了序列的长度，则返回None，指针后移，继续遍历。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        # write code here
        serializeStr = ''
        if root == None:
            return '#'
        stack = []
        while root or stack:
            while root:
                serializeStr += str(root.val) + ','
                stack.append(root)
                root = root.left
            serializeStr += '#,'
            root = stack.pop()
            root = root.right
        serializeStr = serializeStr[:-1]
        return serializeStr
        
    def Deserialize(self, s):
        # write code here
        serialize = s.split(',')
        tree, sp = self.deserialize(serialize, 0)
        return tree
    
    def deserialize(self, s, sp):
        if sp >= len(s) or s[sp] == '#':
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.deserialize(s, sp)
        node.right, sp = self.deserialize(s, sp)
        return node, sp