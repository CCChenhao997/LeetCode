'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-09 10:59:59
@LastEditors: chenhao
@LastEditTime: 2020-03-09 21:31:56
'''

"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \ 
     3   1
Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \ 
 1   3   1
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum1 = root.val
        if root.left:
            sum1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            sum1 += self.rob(root.right.left) + self.rob(root.right.right)
        sum2 = self.rob(root.left) + self.rob(root.right)
        return max(sum1, sum2)
    
    
    def rob2(self, root):
        def robInternal(root):
            if not root:
                return [0] * 2
            left, right = robInternal(root.left), robInternal(root.right)
            # 列表中，list[0]表示当前结点不偷，偷的是两个子结点；list[1]表示当前结点偷，两个子结点不偷
            return [max(left) + max(right), left[0] + right[0] + root.val]

        return max(robInternal(root))

