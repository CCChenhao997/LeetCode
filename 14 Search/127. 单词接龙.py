'''
Description: 
version: 
Author: chenhao
Date: 2020-12-07 08:55:23
'''

"""
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。

说明:
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出: 5
解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
     
示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出: 0
解释: endWord "cog" 不在字典中，所以无法进行转换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0         
        if beginWord in word_set:
            word_set.remove(beginWord)
        
        # * BFS 
        # queue = deque()
        # queue.append(beginWord)
        # visited = set()
        # visited.add(beginWord)
        # word_len = len(beginWord)
        # step = 1
        # while queue:
        #     current_size = len(queue)
        #     for i in range(current_size):
        #         word = queue.popleft()  # hit
        #         word_list = list(word)  # ['h', 'i', 't']
        #         for j in range(word_len):
        #             origin_char = word_list[j]
        #             for k in range(26):
        #                 word_list[j] = chr(ord('a') + k)
        #                 next_word = ''.join(word_list)
        #                 if next_word in word_set:
        #                     if next_word == endWord:
        #                         return step + 1
        #                     if next_word  not in visited:
        #                         queue.append(next_word)
        #                         visited.add(next_word)
        #             word_list[j] = origin_char
        #     step += 1
        # return 0
        
        # * 双向BFS
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)
        begin_visited = set()
        begin_visited.add(beginWord)
        end_visited = set()
        end_visited.add(endWord)
        word_len = len(beginWord)
        step = 1
        while begin_visited and end_visited:
            if len(begin_visited) > len(end_visited):
                begin_visited, end_visited = end_visited, begin_visited
            next_level_visited =set()
            for word in begin_visited:
                word_list = list(word)
                for j in range(word_len):
                    origin_char = word_list[j]
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word in end_visited:
                                return step + 1
                            if next_word not in visited:
                                next_level_visited.add(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            begin_visited = next_level_visited
            step += 1
        return 0
        
 
if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    res = solution.ladderLength(beginWord, endWord, wordList)
    print(res)