'''
Description: 
version: 
Author: chenhao
Date: 2021-01-28 10:22:45
'''

"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp_max = [-float('inf')] * n
        # dp_min = [float('inf')] * n
        # dp_max[0], dp_min[0] = nums[0], nums[0]
        # for i in range(1, n):
        #     dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
        #     dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
        # return max(dp_max)
        
        # * 空间优化 (由于第 i 个状态只和第 i - 1 个状态相关)
        n = len(nums)
        maxF, minF, ans = nums[0], nums[0], nums[0]
        for i in range(1, n):
            tmp_max, tmp_min = maxF, minF
            maxF = max(tmp_max * nums[i], tmp_min * nums[i], nums[i])
            minF = min(tmp_max * nums[i], tmp_min * nums[i], nums[i])
            ans = max(maxF, ans)
        return ans