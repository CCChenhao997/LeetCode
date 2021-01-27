'''
Description: 
version: 
Author: chenhao
Date: 2021-01-27 00:20:54
'''

"""
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例 1：
输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
输出：["eat","oath"]

示例 2：
输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]

提示：
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] 是一个小写英文字母
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] 由小写英文字母组成
words 中的所有字符串互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # * 构建Trie树
        trie = {}
        for word in words:
            tree = trie
            for w in word:
                if w not in tree:
                    tree[w] = {}
                tree = tree[w]
            tree['end'] = 1
            
        def backtracking(i, j, trie, s):
            c = board[i][j]
            if c not in trie: return    # 回溯终止条件
            trie = trie[c]              # 进入trie树下一层
            if 'end' in trie and trie['end'] == 1:
                res.append(s + c)
                trie['end'] = 0         # 防止重复数组加入
            board[i][j] = '#'           # 已访问过标志
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i, tmp_j = i + x, j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] != '#':
                    backtracking(tmp_i, tmp_j, trie, s + c)
            board[i][j] = c             # 恢复（回溯）
        
        res = []
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                backtracking(i, j, trie, '')
        return res
    

if __name__ == '__main__':
    board = [["o","a","a","n"], ["e","t","a","e"], ["i","h","k","r"], ["i","f","l","v"]]
    words = ["oath", "pea", "eat", "rain"]
    s = Solution()
    print(s.findWords(board, words))