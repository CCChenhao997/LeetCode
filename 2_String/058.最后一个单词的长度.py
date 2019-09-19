'''
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:
输入: "Hello World"
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
# 解法一: 自己写的
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        len_s = len(s)
        j = 0
        if len_s == 0:
            return j
        for i in range(len_s - 1, -1, -1):
            if s[i] != ' ': 
                j += 1
            elif s[i] == ' ': 
                return j
        return j               # 若字符串中就一个单词，且单词前/后无空格
"""

# 解法二: 一行解决
'''
思路:
    先去掉字符串的最后空格
    将字符串按照空格分组
    取分组后的最后一项
    计算它的长度
    完事儿
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])




if __name__ == "__main__":
    X = Solution()
    s = "World"
    print(X.lengthOfLastWord(s))