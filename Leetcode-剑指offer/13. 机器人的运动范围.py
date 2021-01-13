'''
Description: 
version: 
Author: chenhao
Date: 2021-01-12 21:51:15
'''

"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# * 1. DFS 递归 剪枝
# * 2. BFS 迭代 队列

def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # * DFS
        # def dfs(i, j):
        #     if i >= m or j >= n or k < digitsum(i) + digitsum(j) or (i, j) in visited:
        #         return 0
        #     visited.add((i, j))
        #     return 1 + dfs(i+1, j) + dfs(i, j+1)

        # visited = set()
        # return dfs(0, 0) 
    
        # * BFS
        queue, visited = [(0, 0)], set()
        while queue:
            i, j = queue.pop(0)
            if i >= m or j >= n or k < digitsum(i) + digitsum(j) or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i + 1, j))
            queue.append((i, j + 1))
        return len(visited)