'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-04-09 14:16:37
@LastEditors: chenhao
@LastEditTime: 2020-04-09 14:49:03
'''

"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False
        
        i = 0
        while i < len(flowerbed):
            if n == 0:
                return True
            if i == 0 and flowerbed[i] == flowerbed[i+1] == 0:
                n -= 1
                i += 2
            elif i == len(flowerbed) - 1 and flowerbed[i-1] == flowerbed[i] == 0:
                n -= 1
                i += 2
            elif i > 0 and flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                n -= 1
                i += 2
            else:
                i += 1
            print(i)
            
        return True if n == 0 else False
    
    
    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:
        nums = [0] + flowerbed + [0]
        i = 1
        count = 0
        while i < len(flowerbed)+1:
            if nums[i-1] == 0 and nums[i] == 0 and nums[i+1] == 0:
                count += 1
                i += 2
            else:
                i += 1
        return count >= n
        

if __name__=="__main__":
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1], 1))