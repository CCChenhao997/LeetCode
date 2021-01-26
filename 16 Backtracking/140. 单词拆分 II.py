'''
Description: 
version: 
Author: chenhao
Date: 2021-01-26 16:10:47
'''

"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]

示例 2：
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。

示例 3：
输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from functools import lru_cache

class Solution:
    # 带备忘录的记忆化搜索
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res, temp = [], []
        memo = [True] * (len(s) + 1)
        wordDict = set(wordDict)
        
        def dfs(start_index):
            num = len(res)                  # 回溯前先记下答案中有多少个元素
            if start_index == len(s):
                res.append(" ".join(temp))
                return
            for i in range(start_index, len(s)):
                if memo[i + 1] and s[start_index: i + 1] in wordDict: # 添加备忘录的判断条件
                    temp.append(s[start_index: i + 1])
                    dfs(i + 1)
                    temp.pop()
            # 答案中的元素没有增加，说明s[pos:]不能分割，修改备忘录        
            memo[start_index] = True if len(res) > num else False
            
        dfs(0)
        return res


if __name__ == '__main__':
    string = "aaaaaaa"
    wordDict = ["aaaa","aaa"]
    s = Solution()
    print(s.wordBreak(string, wordDict))