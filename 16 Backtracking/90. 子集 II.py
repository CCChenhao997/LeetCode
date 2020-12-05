'''
Description: 
version: 
Author: chenhao
Date: 2020-11-28 20:54:53
'''

"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return
        
        results = []
        n = len(nums)
        nums.sort()
        
        def backtrack(i, path, nums):
            results.append(path)
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                backtrack(j + 1, path + [nums[j]], nums)
        
        backtrack(0, [], nums)
        return results  