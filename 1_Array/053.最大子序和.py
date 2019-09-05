'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

链接：https://leetcode-cn.com/problems/maximum-subarray
'''

from typing import List

'''
题目中的关键字是“连续”，首先我们尝试就将状态定义成题目要求的结果，即：dp[i] 表示 nums 在区间 [0, i] 中连续子数组的最大和。
在思考“状态转移方程”的时候，dp[i] 之前的，例如 dp[i - 1] 就有可能是是更前面的连续子数组的最大和，不利于我们分类讨论。

但是我们有相关的经验，例如「力扣」第 300 题：“最长上升子序列”，既然一个连续子数组一定要以一个数作为结尾，那么我们就将状态定义成：
dp[i]：表示以 nums[i] 结尾的连续子数组的最大和。

这里要注意一件事情：
如果状态的定义不是题目中的问题的定义，一定思考一下输出是什么，不能直接将最后一个状态返回回去。
输出应该是把所有的 dp[0]、dp[1]、……、dp[n - 1] 都看一遍，取最大值。 同样的情况也适用于「力扣」第 300 题：“最长上升子序列”。我经常在这一步“摔跟头”，请各位也留意。

2、状态转移方程
接下来分类讨论就变得容易多了，dp[i] 的值要看 dp[i - 1]，因为 nums[i] 一定被选取，那么 dp[i - 1] 的正负就作为分类的标准。
如果 dp[i - 1] >= 0，那么可以把 nums[i] 直接接在 dp[i - 1] 表示的那个数组的后面。
如果 dp[i - 1] < 0，那么加上前面的数反而我越来越小了，干脆“另起炉灶”吧，单独的一个 nums[i]，就是 dp[i]。
'''
'''
# 状态转移方程1 时间复杂度O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]
        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
'''

'''
# 状态转移方程2 时间复杂度O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]
        dp[0]=nums[0]
        for i in range(1, size):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)
'''

'''
# 分治法 时间复杂度:O(NlogN) 还没看懂
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        return self.__max_sub_array(nums, 0, size-1)

    def __max_sub_array(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) >> 1
        return max(self.__max_sub_array(nums, left, mid),
                   self.__max_sub_array(nums, mid+1, right),
                   self.__max_cross_array(nums, left, mid, right))

    def __max_cross_array(self, nums, left, mid, right):
        # 一定包含 num[mid] 元素的最大连续子数组的和，
        # 思路是看看左边“扩散到底”，得到一个最大数，右边“扩散到底”得到一个最大数
        # 然后再加上中间数
        left_sum_max = 0
        start_left = mid - 1
        s1 = 0
        while start_left >= left:
            s1 += nums[start_left]
            left_sum_max = max(left_sum_max, s1)
            start_left -= 1
        
        right_sum_max = 0
        start_right = mid + 1
        s2 = 0
        while start_right <= right:
            s2 += nums[start_right]
            right_sum_max = max(right_sum_max, s2)
            start_right += 1
        return left_sum_max + nums[mid] + right_sum_max
'''

# python 特色解法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            # 当前索引 i 永远存储 0～i 的最大和
            nums[i] = max(nums[i], nums[i]+nums[i-1])
        # 返回每个索引最大和的最大值
        return max(nums)



if __name__=='__main__':
    X = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(X.maxSubArray(nums))