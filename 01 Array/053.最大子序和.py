'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

链接：https://leetcode-cn.com/problems/maximum-subarray
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [-float('inf')] * n
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])
        # return max(dp)
        
        # * 空间优化
        n = len(nums)
        maxF, ans = nums[0], nums[0]
        for i in range(1, n):
            maxF = max(maxF + nums[i], nums[i])
            ans = max(ans, maxF)
        return ans


if __name__=='__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))