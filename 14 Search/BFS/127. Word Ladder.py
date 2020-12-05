'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-05 14:31:53
@LastEditors: chenhao
@LastEditTime: 2020-07-05 15:22:21
'''


from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        
        if beginWord in word_set:
            word_set.remove(beginWord)
        
        queue = deque()
        queue.append(beginWord)
        
        visited = set()
        visited.add(beginWord)
        
        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()
                
                word_list = list(word)
                for j in range(word_len):
                    origin_char = word_list[j]
                    
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0
    
    
    def ladderLength_bi(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        
        if beginWord in word_set:
            word_set.remove(beginWord)
            
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
            # 打开帮助调试
            # print(begin_visited)
            # print(end_visited)
            
            if len(begin_visited) > len(end_visited):
                begin_visited, end_visited = end_visited, begin_visited
            
            next_level_visited = set()
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
    res = solution.ladderLength_bi(beginWord, endWord, wordList)
    print(res)