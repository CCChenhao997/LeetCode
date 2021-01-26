'''
Description: 
version: 
Author: chenhao
Date: 2021-01-25 18:16:06
'''

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。

示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import copy

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
        def dfs(start_index, s, path, res):
            if start_index == len(s):
                res.append(copy.deepcopy(path))
                # res.append(path)    # path 还会继续变化
                return
            for i in range(start_index, len(s)):
                if dp[start_index][i]:
                    path.append(s[start_index: i+1])
                    dfs(i + 1, s, path, res)
                    path.pop()
        
        path, res = [], []
        dfs(0, s, path, res)
        return res
    

if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))