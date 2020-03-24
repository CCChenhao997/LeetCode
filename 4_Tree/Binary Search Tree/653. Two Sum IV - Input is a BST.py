'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-24 09:06:38
@LastEditors: chenhao
@LastEditTime: 2020-03-24 09:36:12
'''

"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
Output: True

Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 28
Output: False
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        valList = []
        
        def inOrder(root):
            if not root:
                return
            nonlocal valList
            inOrder(root.left)
            valList.append(root.val)
            inOrder(root.right)
        
        inOrder(root)
        
        left, right = 0, len(valList) - 1
        while left < right:
            value = valList[left] + valList[right]
            if value > k:
                right -= 1
            elif value < k:
                left += 1
            else:
                return True
        return False
        
    

if __name__=="__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    node3 = TreeNode(3)
    
    node1.left = node2
    node1.right = node3
    
    s = Solution()
    print(s.findTarget(node1, 4))