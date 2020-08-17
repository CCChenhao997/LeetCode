"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(nlogn) time complexity?
"""

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # * O(n2)
        # if not nums:
        #     return 0
        
        # dp = [1] * len(nums)
        # for j in range(len(nums)):
        #     for i in range(j):
        #         if nums[j] > nums[i] and dp[j] < dp[i] + 1:
        #             dp[j] = dp[i] + 1
        
        # return max(dp)
    
        # * O(nlogn)
        dp = []
        for n in nums:
            if not dp or n > dp[-1]:
                dp.append(n)
            else:
                l, r = 0, len(dp) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if dp[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                dp[loc] = n
        return len(dp)