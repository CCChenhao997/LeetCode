'''
Description: 
version: 
Author: chenhao
Date: 2020-12-01 14:58:54
'''

"""
给你一个整数数组 nums ，和一个整数 target 。

该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。

请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
 
示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1
 

提示：
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
nums 肯定会在某个点上旋转
-10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 当目标值 target == nums[mid]，直接返回mid

        # 当目标值 target < nums[mid]
        # Case 1: 如果nums[begin] < nums[mid]
        # if target >= nums[begin]: 在递增区间[begin, mid - 1]中查找
        # 否则，在旋转区间[mid + 1, end]中查找
        # Case 2: 如果nums[begin] > nums[mid]
        # 直接在递增区间[begin, mid - 1]中查找
        # Case 3: 如果nums[begin] == nums[mid]
        # 目标只可能在[mid + 1, end]间

        # 当目标值 target > nums[mid]
        # Case 1: 如果nums[begin] < nums[mid]，去旋转区间查找
        # 递增区间为 [begin, mid - 1]，旋转区间为 [mid + 1, end]
        # Case 2: 如果nums[begin] > nums[mid]
        # if target >= nums[begin]: 在旋转区间[begin, mid - 1]查找
        # 否则，在递增区间[mid + 1, end]中查找
        # Case 3: 如果nums[begin] == nums[mid]，说明目标只可能在[mid + 1, end]间，该情况下nums就两个元素 

        if not nums or len(nums) == 0:
            return -1
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target: return mid
            elif target < nums[mid]:
                if nums[left] < nums[mid]:   # 递增区间
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[left] > nums[mid]: # 旋转区间
                    right = mid - 1
                else:
                    left = mid + 1
            elif target > nums[mid]:
                if nums[left] < nums[mid]:
                    left = mid + 1
                elif nums[left] > nums[mid]:
                    if target >= nums[left]:   
                        right = mid - 1         # 旋转区间
                    else:
                        left = mid + 1          # 递增区间
                else:
                    left = mid + 1
        return -1
