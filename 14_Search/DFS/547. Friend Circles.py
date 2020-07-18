'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-19 00:47:34
@LastEditors: chenhao
@LastEditTime: 2020-07-19 01:02:55
'''

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        count = 0
        visited = set()
        
        def dfs(i):
            for j in range(N):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        for i in range(N):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
                
        return count