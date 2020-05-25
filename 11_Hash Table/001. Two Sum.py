'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-05-25 20:16:51
@LastEditors: chenhao
@LastEditTime: 2020-05-25 20:45:52
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for i, value in enumerate(nums):
            hash_dict[value] = i
        for i, value in enumerate(nums):
            j = hash_dict.get(target - value)
            if j is not None and j != i:
                return [i, j]
            
            
    def twoSum1(self, nums: List[int], target: int) -> List[int]:        
        hash_dict={}
        for i,num in enumerate(nums):
            if hash_dict.get(target - num) is not None:
                return [i,hash_dict.get(target - num)]
            hash_dict[num] = i