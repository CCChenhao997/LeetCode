'''
Description: 
version: 
Author: chenhao
Date: 2020-12-29 10:37:39
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
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        n = len(self.nums)
        for i in range(n // 2 - 1, -1, -1):
            self.buildHeap(i, n)

        for j in range(n - 1, -1, -1):
            k -= 1
            if k == 0:
                return self.nums[0]
            self.nums[0], self.nums[j] = self.nums[j], self.nums[0]
            self.buildHeap(0, j - 1)

    def buildHeap(self, i, n):
        left, right = 2*i+1, 2*i+2
        largest_idx = i
        if left < n and self.nums[left] > self.nums[i]:
            largest_idx = left
        if right < n and self.nums[largest_idx] < self.nums[right]:
            largest_idx = right
        if largest_idx != i:
            self.nums[largest_idx], self.nums[i] = self.nums[i], self.nums[largest_idx]
            self.buildHeap(largest_idx, n)