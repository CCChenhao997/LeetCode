'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List

"""
# 解法一: 纯数学方法，求出总和减去列表数字之和。（最好使用等差数列求和公式）
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        list_len = len(nums)
        sum1, sum2 = 0, 0
        for i in range(list_len + 1):
            sum1 += i
        for j in nums:
            sum2 += j
        return (sum1 - sum2)
"""

"""
# 解法二: 排序
'''
首先我们对数组进行排序，随后我们可以在常数时间内判断两种特殊情况：
0 没有出现在数组的首位，以及 nn 没有出现在数组的末位。
如果这两种特殊情况都不满足，那么缺失的数字一定在 0 和 nn 之间（不包括两者）。
此时我们可以在线性时间内扫描这个数组，如果某一个数比它前面的那个数大了超过 1，
那么这两个数之间的那个数即为缺失的数字。
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing is on the range (0, n)
        if i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num
"""


"""
# 解法三: 哈希表
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
"""


"""
# 解法四: 二分法
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1
        return left
"""

# 解法五: 位运算，^ 是按位异或
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for idx, num in enumerate(nums):
            res = res ^ idx ^ num   
        return res ^ len(nums)



if __name__=='__main__':
    X = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print(X.missingNumber(nums))