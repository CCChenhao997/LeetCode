'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-27 20:41:35
@LastEditors: chenhao
@LastEditTime: 2020-07-27 20:58:33
'''

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        row, col = len(matrix), len(matrix[0])
        r, c = 0, col - 1
        cur_value = matrix[r][c]
        
        while cur_value != target:
            if cur_value > target:
                if c - 1 < 0:
                    return False
                cur_value = matrix[r][c-1]
                c -= 1
            elif cur_value < target:
                if r + 1 >= row:
                    return False
                cur_value = matrix[r+1][c]
                r += 1
        
        return True
    
    
s = Solution()
print(s.searchMatrix([[]], 5))