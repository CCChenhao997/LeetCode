'''
Description: 
version: 
Author: chenhao
Date: 2020-11-28 20:43:01
'''

"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return
        
        candidates.sort()
        results = []
        
        def backtrack(i, tmp_sum, tmp_list):
            if tmp_sum == target:
                results.append(tmp_list)
                return 
            for j in range(i, len(candidates)):
                if tmp_sum + candidates[j] > target:
                    return
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])
        
        backtrack(0, 0, [])    
        return results