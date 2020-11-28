'''
Description: 
version: 
Author: chenhao
Date: 2020-11-28 22:34:22
'''

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return

        results = []
        n = len(nums)
        visited = [0] * n

        def backtrack(path, nums):
            if len(path) == len(nums):
                results.append(path)
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = 1
                backtrack(path + [nums[i]], nums)
                visited[i] = 0
        
        backtrack([], nums)
        return results