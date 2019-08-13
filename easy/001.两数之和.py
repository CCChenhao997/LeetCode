'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9  所以返回 [0, 1]


链接：https://leetcode-cn.com/problems/two-sum
'''
'''
# 解法一: 暴力循环 (通过不了)
class Solution(object):
    def twoSum(self, nums, target):
        nums_length = len(nums)
        for i in range(nums_length-1):
            for j in range(i+1, nums_length):
                if nums[i] + nums[j] == target:
                        return [i, j]
'''

# 解法二: 字典模拟哈希  用时：76ms  (推荐，而且容易理解)
class Solution(object):
    def twoSum(self, nums, target):
        _dict = {}
        for i, m in enumerate(nums):
            _dict[m] = i
        for i, m in enumerate(nums):
            j = _dict.get(target - m)  # dict.get()返回指定键的值
            if j is not None and i != j:
                return [i, j]

'''
# 解法三: 一遍字典模拟Hash  用时：120ms
class Solution(object):
    def twoSum(self, nums, target):
        _dict = {}
        for i, m in enumerate(nums):
            if _dict.get(target - m) is not None:
                return [_dict.get(target - m), i]
            _dict[m] = i
'''

X = Solution()
nums = [2, 7 ,11, 15]
target = 9
print(X.twoSum(nums, target))

