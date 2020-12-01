'''
Description: 
version: 
Author: chenhao
Date: 2020-12-01 16:53:21
'''

"""
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例：
输入：nums = [5,2,6,1]
输出：[2,1,1,0] 
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素
 
提示：
0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.count = 0
        self.left = None
        self.right = None

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
    
        def createNode(root, node, i):
            if not root:
                root = node
                return root
            if root.val >= node.val:
                root.count += 1
                root.left = createNode(root.left, node, i)
            else:
                res[i] += 1 + root.count
                root.right = createNode(root.right, node, i)
            return root
        
        res = [0] * len(nums)
        root = None
        for i in range(len(nums) - 1, -1, -1):
            root = createNode(root, TreeNode(nums[i]), i)
        return res