'''
Description: 
version: 
Author: chenhao
Date: 2021-01-28 23:33:26
'''

"""
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意

示例 2：
输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组

示例 3：
输入：nums = [2,1,5,0,4,6]
输出：true
解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6

提示：
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-triplet-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # * 动态规划 Time O(n^2), Space O(n)
        # n = len(nums)
        # dp = [1] * n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #            # dp[i] = max(dp[i], dp[j] + 1)
        #            dp[i] = dp[j] + 1
        #         if dp[i] >= 3:
        #             return True
        # return False
        
        # * 双指针 Time O(n), Space O(1)
        # minValue_1, minValue_2 = float('inf'), float('inf')
        # for num in nums:
        #     if num <= minValue_1:
        #         minValue_1 = num
        #     elif num <= minValue_2:
        #         minValue_2 = num
        #     else:
        #         return True
        # return False
        
        # * 前后遍历 Time O(n), Space O(n)
        n = len(nums)
        forward, backward = nums[:], nums[:]
        backward[n - 1] = nums[n - 1]
        for i in range(1, n):
            forward[i] = min(forward[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            backward[i] = max(backward[i + 1], nums[i])
        for i in range(n):
            if forward[i] < nums[i] < backward[i]:
                return True
        return False
    

if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    s = Solution()
    print(s.increasingTriplet(nums))