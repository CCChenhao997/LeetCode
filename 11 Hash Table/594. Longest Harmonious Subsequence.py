'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-05-31 00:26:56
@LastEditors: chenhao
@LastEditTime: 2020-05-31 09:41:56
'''

from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hash_dict = {}
        for value in nums:
            hash_dict[value] = hash_dict.get(value, 0) + 1
        
        longest = 0
        for i, k in enumerate(hash_dict):
            if k + 1 in hash_dict:
                longest = max(longest, hash_dict.get(k) + hash_dict.get(k+1))
            
        return longest
    

s = Solution()
print(s.findLHS([1,1,1,1]))