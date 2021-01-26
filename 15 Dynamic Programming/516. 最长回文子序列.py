'''
Description: 
version: 
Author: chenhao
Date: 2021-01-25 17:21:04
'''

"""
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

示例 1:
输入:
"bbbab"
输出:
4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:
"cbbd"
输出:
2
一个可能的最长回文子序列为 "bb"。

提示：
1 <= s.length <= 1000
s 只包含小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]
    

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindromeSubseq("cbbd"))
    