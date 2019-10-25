"""
题目描述:
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

思路:
使用队列
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        store = []
        if root is None:
            return []
        Deque = []
        Deque.append(root)
        while Deque:
            temp = Deque.pop(0)
            store.append(temp.val)
            if temp.left != None:
                Deque.append(temp.left)
            if temp.right != None:
                Deque.append(temp.right)
        return store


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

test = Solution()
print(test.PrintFromTopToBottom(pNode1))
