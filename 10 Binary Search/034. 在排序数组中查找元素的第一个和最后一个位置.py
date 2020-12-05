'''
Description: 
version: 
Author: chenhao
Date: 2020-12-01 14:54:38
'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        if not nums:
            return [start, end]

        def startBound(left, right):
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] < target:
                        return mid
                    else:
                        right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return -1

        def endBound(left, right):
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] > target:
                        return mid
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return -1

        left, right = 0, len(nums) - 1
        start = startBound(left, right)
        end = endBound(left, right)
        return [start, end]
    

s = Solution()
print(s.searchRange([1], 1))