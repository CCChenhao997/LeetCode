'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

链接：https://leetcode-cn.com/problems/palindrome-number
'''

'''
# 我的菜🐔解法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        is_pn = True
        s1 = str(x)
        s2 = s1[:: -1]          # 将字符串反转 
        s1_len = len(s1)
        for i in range(s1_len):
            if s1[i] != s2[i]:
                is_pn = False
                break
        return is_pn
if __name__=='__main__':
    x = int(input("请输入一个整数:"))
    S = Solution()
    if S.isPalindrome(x):
        print("true")
    else:
        print("false")
'''

'''
# 大佬的一行代码解决
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
'''

# 不使用字符串的解法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or not x % 10 and x: return False  # 1. x<0  2. x>0且x%10=0
        r = 0
        while x > r:
            x, rem = x // 10, x % 10
            r = r * 10 + rem
            print(x, r)
        return x == r or x == r // 10