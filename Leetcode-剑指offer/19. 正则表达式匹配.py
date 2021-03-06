'''
Description: 
version: 
Author: chenhao
Date: 2021-01-14 22:34:20
'''

"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

'''
1. 递归回溯
https://www.bilibili.com/video/BV13441117i4?from=search&seid=11492999226096514689
2. 动态规划
https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-dong-tai-gui-hua-by-jy/
'''

from functools import lru_cache

class Solution:
    # * 递归
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        """
        递归
        """
        # s和p都为空则为True
        if len(p) == 0:
            return True if len(s) == 0 else False
        
        # 查看首元素是否一致
        first_match = len(s) != 0 and (s[0] == p[0] or p[0] == '.')
        # 如果下一个字符是`*`
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2: ]) or (first_match and self.isMatch(s[1: ], p))
        # 一般情况
        return first_match and self.isMatch(s[1: ], p[1: ])
    
    
    def isMathcDP(self, s: str, p: str):
        """
        动态规划
        """
        ls, lp = len(s), len(p)
        dp = [[False for _ in range(lp + 1)] for _ in range(ls + 1)]
        dp[0][0] = True
        
        # 初始状态: p的第j个字符记为`*` 且 dp[0][j-2]为True
        for j in range(2, lp + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        
        # 转移方程
        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                m, n = i - 1, j - 1
                if p[n] == '*':
                    if s[m] == p[n - 1] or p[n - 1] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]     # `*`匹配或不匹配
                    else: dp[i][j] = dp[i][j - 2]                   # `*`不匹配
                elif s[m] == p[n] or p[n] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]