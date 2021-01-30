'''
Description: 
version: 
Author: chenhao
Date: 2021-01-29 23:43:32
'''

"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]

示例 3：
输入：nums = [1,-1], k = 1
输出：[1,-1]

示例 4：
输入：nums = [9,11], k = 2
输出：[11]

示例 5：
输入：nums = [4,-2], k = 2
输出：[4]
 
提示：
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import heapq
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # * 堆 Time: O(nlogn), Space: O(n)
        # res, heap = [], []
        # for i in range(len(nums)):
        #     heapq.heappush(heap, (-nums[i], i))
        #     if i + 1 >= k:
        #         while heap[0][1] <  i - k + 1:
        #             heapq.heappop(heap)
        #         res.append(-heap[0][0])
        # return res
        
        # * 双端队列 Time: O(n), Space: O(k)
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            if deque and deque[0] < i - k + 1:
                deque.popleft()
            while deque and nums[deque[-1]] < num:
                deque.pop()
            deque.append(i)
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res