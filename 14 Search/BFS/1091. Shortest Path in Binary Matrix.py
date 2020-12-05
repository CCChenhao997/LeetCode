'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-06-24 10:28:20
@LastEditors: chenhao
@LastEditTime: 2020-06-24 11:19:50
'''

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 1
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        res = 1
        path = deque()
        path.append([0, 0])  # 先压入起点
        grid[0][0] = -1
        while path: # BFS模板
            for _ in range(len(path)):  # 对BFS的某一层中的所有点向8个方向进行扩展
                x, y = path.popleft()
                for new_x, new_y in [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1],
                                     [x, y + 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]:
                    if new_x == n - 1 and new_y == n - 1:  # 如果扩展的点到达了终点
                        return res + 1
                    if not 0 <= new_x < n or not 0 <= new_y < n: # 扩展的点超出边界，则跳过
                        continue
                    if grid[new_x][new_y] == 1:  # 若扩展的点为阻塞，则跳过
                        continue
                    if grid[new_x][new_y] == -1: # 若扩展的点已经访问过，则跳过
                        continue
                    if grid[new_x][new_y] == 0:  # 若为通畅点
                        grid[new_x][new_y] = -1 # 当前层已经访问过该点
                        path.append([new_x, new_y])
            res += 1
        return -1