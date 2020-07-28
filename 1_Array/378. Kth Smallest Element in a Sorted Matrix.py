'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-28 00:37:28
@LastEditors: chenhao
@LastEditTime: 2020-07-28 21:26:33
'''

"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""

from typing import List
import heapq

class Solution:
    
    # 归并排序
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)
        
        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
            
        return heapq.heappop(pq)[0]
    
    
    # 二分查找
    def kthSmallest_binary_search(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num > k
        
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        
        