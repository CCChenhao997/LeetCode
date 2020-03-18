'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-18 09:35:24
@LastEditors: chenhao
@LastEditTime: 2020-03-18 10:07:48
'''

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        # self.valList = []
        self.k = k
        def DFS(root):
            if not root:
                return
            DFS(root.left)
            self.k -= 1
            if not self.k:
                self.value = root.val
                return
            # self.valList.append(root.val)
            DFS(root.right)
        DFS(root)
        # return self.valList[k-1]
        return self.value
        
        
    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right