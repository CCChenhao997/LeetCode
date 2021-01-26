'''
Description: 
version: 
Author: chenhao
Date: 2021-01-25 23:44:27
'''

"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 
提示：
输入的字符串长度不会超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        # center expansion
        # n = len(s)
        # ans = 0
        # for center in range(2*n - 1):
        #     left = center // 2
        #     right = left + center % 2
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         ans += 1
        #         left -= 1
        #         right += 1
        # return ans
        
        # dynamic progamming
        if not s: return 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        ans = 0
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]: ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings("abc"))
