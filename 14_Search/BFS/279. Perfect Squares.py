'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-04 21:26:30
@LastEditors: chenhao
@LastEditTime: 2020-07-04 22:08:41
'''

"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class node:
    def __init__(self, value, step=0):
        self.value = value
        self.step = step
    
    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value,self.step)
        

class Solution:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])
        
        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - n*n for n in range(1, int(vertex.value**.5) + 1)]
            for i in residuals:
                new_vertex = node(i, vertex.step+1)
                if i == 0:
                    return new_vertex.step
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
        return -1