'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List

'''
# 自己写的二分查找法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        if nums[0] > target:  # nums是有序数组，所以只需要比较第一个
            return 0
            
        while low <= high:
            mid = (low + high) // 2

            # 未在列表中找到target情况
            if low == high:
                if nums[mid] > target:
                    return mid
                elif nums[mid] < target:
                    return mid + 1
            if low == mid and low != high:
                if nums[mid] > target:
                    return mid
                elif nums[mid] < target and nums[high] > target:
                    return mid + 1  
                elif nums[mid] < target and nums[high] < target:
                    return mid + 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
'''


# 二分查找，精品版
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        # 特判
        if size == 0:
            return 0
        # 特判 2 ：如果比最后一个数字还要大，直接接在它后面就可以了
        if target > nums[-1]:
            return size

        left = 0
        right = size - 1
        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                assert nums[mid] >= target
                right = mid
        return left


'''
# 暴力循环
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            # 找到大于target的元素，则返回当前索引
            if v >= target:
                return i
        # 说明没有任何元素大于target，则插入到数组的末尾
        return len(nums)
'''


if __name__=='__main__':
    X = Solution()
    nums = [1, 3]
    target = 0
    print(X.searchInsert(nums, target))
            