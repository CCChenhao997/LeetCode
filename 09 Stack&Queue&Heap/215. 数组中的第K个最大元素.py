'''
Description: 
version: 
Author: chenhao
Date: 2021-01-29 15:11:20
'''

"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-nums
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # * 快排思想
        # def partition(nums, low, high):
        #     i = low - 1
        #     pivot = nums[high]
        #     for j in range(low, high):
        #         if nums[j] <= pivot:
        #             i += 1
        #             nums[i], nums[j] = nums[j], nums[i]
        #     nums[high], nums[i + 1] = nums[i + 1], nums[high]
        #     return i + 1
        
        # def quickSort(nums, low, high):
        #     pi = partition(nums, low, high)
        #     if pi < target:
        #         return quickSort(nums, pi + 1, high)
        #     elif pi > target:
        #         return quickSort(nums, low, pi - 1)
        #     return nums[pi]

        # target = len(nums) - k
        # return quickSort(nums, 0, len(nums) - 1)
        
        # * 堆排思想
        def buildHeap(i, max_len):
            largest_id = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < max_len and nums[left] > nums[largest_id]:
                largest_id = left
            if right < max_len and nums[right] > nums[largest_id]:
                largest_id = right
            if i != largest_id:
                nums[i], nums[largest_id] = nums[largest_id], nums[i]
                buildHeap(largest_id, max_len)
        
        max_len = len(nums)
        for i in range(max_len // 2 - 1, -1, -1):
            buildHeap(i, max_len)
        for j in range(max_len - 1, -1, -1):
            k -= 1
            if k == 0:
                return nums[0]
            nums[0], nums[j] = nums[j], nums[0]
            buildHeap(0, j)
    

if __name__ == '__main__':
    # nums = [3,2,1,5,6,4]
    # k = 2
    # nums = [3,2,3,1,2,4,5,5,6]
    # k = 4
    nums = [2, 1]
    k = 1
    s = Solution()
    print(s.findKthLargest(nums, k))