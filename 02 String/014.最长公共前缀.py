'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。

链接：https://leetcode-cn.com/problems/longest-common-prefix
'''

'''
# 我的菜🐔解法
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        pre_str = ""
        strs_Slen = len(strs)                       # 字符串列表的长度
        if strs_Slen == 0:
            return pre_str
        min_strs_len = min([len(i) for i in strs])  # 找出最小字符串的长度
        flag = True
        for i in range(min_strs_len):
            ch = strs[0][i]
            for j in range(1, strs_Slen):
                if ch != strs[j][i]:
                    flag = False
                    break
            if flag:
                pre_str += ch
            else:
                break
        return pre_str
'''


'''
利用好 zip 和 set
【第一行】每次都取各个字符串的同一列字符，放进 set，set 中不会储存重复元素，
        所以长度为1代表各个字符都是相同的，此时 == 会让它变成 True
【第二行】index 搜索第一个 0 的位置，0 与 False 在值上是等价的，相当于搜索
        第一个 False 的位置也就是公共前缀的长度
'''
'''
# 别人的解法
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
        return strs[0][:r.index(0)] if strs else ''
'''

'''
nums = ['flower','flow','flight']
for i in zip(*nums):
    print(i)
# 输出结果
('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
('w', 'w', 'g')
'''


# 可读性加强版
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        L = zip(*strs)
        # list(zip(*["abc","efg","jk"])) --例子输出-→ [('a', 'e', 'j'), ('b', 'f', 'k')] 
        r = [len(set(c)) == 1 for c in L] + [False]
        if strs != []:
            s = r.index(False)   # 查找第一个False的下标
            return strs[0][0:s]  # 列表查找+切片
        else:
            return ""


if __name__=='__main__':
    X = Solution()
    strs = ["flower","flow","flight"]
    # strs = ["dog","racecar","car"]
    # strs = []
    print(X.longestCommonPrefix(strs))
