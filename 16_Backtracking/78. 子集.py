'''
Description: 
version: 
Author: chenhao
Date: 2020-11-28 20:43:42
'''

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return
        
        results = []
        n = len(nums)
        
        def backtrack(i, path, nums):
            results.append(path)
            for j in range(i, n):
                backtrack(j + 1, path + [nums[j]], nums)
        
        backtrack(0, [], nums)
        return results  