'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-21 21:43:29
@LastEditors: chenhao
@LastEditTime: 2020-03-21 22:19:33
'''

"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def toBST(nums, sIdx, eIdx):
            if sIdx > eIdx:
                return
            mIdx = (sIdx + eIdx) // 2
            root = TreeNode(nums[mIdx])
            root.left = toBST(nums, sIdx, mIdx - 1)
            root.right = toBST(nums, mIdx + 1, eIdx)
            return root
        
        return toBST(nums, 0, len(nums) - 1)