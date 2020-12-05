'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-05-10 21:25:10
@LastEditors: chenhao
@LastEditTime: 2020-05-10 21:41:49
'''

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if not letters or not target:
            return None
        left, right = 0, len(letters) - 1
        res = ''
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] > target:
                right = mid - 1
                res = letters[mid]
            else:
                left = mid + 1
        return res if res else letters[0]
    