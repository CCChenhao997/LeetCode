'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-26 10:56:38
@LastEditors: chenhao
@LastEditTime: 2020-07-26 11:24:12
'''

from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums:
            return None
        raw_r = len(nums)
        raw_c = len(nums[0])
        if r * c != raw_r * raw_c or (r == raw_r and c == raw_c):
            return nums
        
        res = []
        for i in nums:
            res += i
        return [res[i*c: i*c+c] for i in range(r)]
    

s = Solution()
print(s.matrixReshape([[1,2,3,4]], 2, 2))