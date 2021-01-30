'''
Description: 
version: 
Author: chenhao
Date: 2021-01-29 21:44:33
'''

"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
 
提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # * 小根堆
        # nums = []
        # for row in matrix:
        #     nums += row

        # def buildMinHeap(i, max_len):
        #     largest_id = i
        #     left, right = 2 * i + 1, 2 * i + 2
        #     if left < max_len and nums[left] < nums[largest_id]:
        #         largest_id = left
        #     if right < max_len and nums[right] < nums[largest_id]:
        #         largest_id = right
        #     if i != largest_id:
        #         nums[i], nums[largest_id] = nums[largest_id], nums[i]
        #         buildMinHeap(largest_id, max_len)
        
        # max_len = len(nums)
        # for i in range(max_len // 2 - 1, -1, -1):
        #     buildMinHeap(i, max_len)
        # for j in range(max_len - 1, -1, -1):
        #     k -= 1
        #     if k == 0:
        #         return nums[0]
        #     nums[0], nums[j] = nums[j], nums[0]
        #     buildMinHeap(0, j)
        
        # * 二分法
        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
            

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,5,9], [10,11,13], [12,13,15]]
    k = 8
    print(s.kthSmallest(matrix, k))