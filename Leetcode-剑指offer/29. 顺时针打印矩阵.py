'''
Description: 
version: 
Author: chenhao
Date: 2021-01-17 00:00:30
'''

"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix) == 0:
            return []
        
        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r, c = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[r][c]
            visited[r][c] = True
            nextR, nextC = r + directions[directionIndex][0], c + directions[directionIndex][1]
            if not (0 <= nextR < rows and 0 <= nextC < columns and not visited[nextR][nextC]):
                directionIndex = (directionIndex + 1) % 4
            r += directions[directionIndex][0]
            c += directions[directionIndex][1]
        
        return order
    

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    print(s.spiralOrder(matrix))