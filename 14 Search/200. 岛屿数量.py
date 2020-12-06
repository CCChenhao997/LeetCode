'''
Description: 
version: 
Author: chenhao
Date: 2020-12-06 20:45:25
'''

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 
提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Collection, List

class Solution:
    # * 深搜 
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     nr = len(grid)      # 行
    #     if nr == 0:
    #         return 0
    #     nc = len(grid[0])   # 列

    #     num_islands = 0
    #     for r in range(nr):
    #         for c in range(nc):
    #             if grid[r][c] == '1':
    #                 num_islands += 1
    #                 self.dfs(grid, r, c)
        
    #     return num_islands
    
    # def dfs(self, grid, r, c):
    #     grid[r][c] = '0'
    #     nr, nc = len(grid), len(grid[0])
    #     for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
    #         if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
    #             self.dfs(grid, x, y)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)      # 行
        if nr == 0:
            return 0
        nc = len(grid[0])   # 列
        
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    grid[r][c] = '0'
                    neighbors = [(r, c)]
                    while neighbors:
                        r, c = neighbors.pop(0)
                        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                                neighbors.append((x, y))
                                grid[x][y] = '0'
        return num_islands