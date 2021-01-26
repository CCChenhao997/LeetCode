'''
Description: 
version: 
Author: chenhao
Date: 2021-01-26 11:53:31
'''

"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # * 记忆化回溯
        # @lru_cache()
        memo = [True] * (len(s) + 1)
        wordSet = set(wordDict)
        def dfs(start_index):
            if start_index == len(s):
                return True
            elif start_index > len(s):
                return False
            for i in range(start_index, len(s)):
                if memo[i + 1] and s[start_index: i + 1] in wordSet:
                    if dfs(i + 1):
                        return True
                    else:
                        memo[start_index] = False
            return False
        return dfs(0)
        
        # * 动态规划
        # n = len(s)
        # dp = [False] * (n + 1)
        # dp[0] = True
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         if dp[i] and s[i: j] in wordSet:
        #             dp[j] = True
        # return dp[-1]


if __name__ == '__main__':
    string = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]
    s = Solution()
    print(s.wordBreak(string, wordDict))