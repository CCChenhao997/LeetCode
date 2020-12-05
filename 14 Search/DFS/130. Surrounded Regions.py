'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-20 10:35:30
@LastEditors: chenhao
@LastEditTime: 2020-07-20 11:11:23
'''

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        row = len(board)
        col = len(board[0])
        
        def dfs(i, j):
            board[i][j] = 'B'
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == 'O':
                    dfs(tmp_i,tmp_j)
        
        for j in range(col):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[row-1][j] == 'O':
                dfs(row-1, j)

        for i in range(row):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][col-1] == 'O':
                dfs(i, col-1)
                
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'