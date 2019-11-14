"""
题目描述:
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母

思路:
依次取一个元素，然后依次和之前递归形成的所有子串组合，形成新的字符串。
"""

class Solution:
    def Permutation(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        
        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i-1]:
                continue
            temp = self.Permutation(''.join(charList[:i]) + ''.join(charList[i+1:]))
            for j in temp:
                pStr.append(charList[i]+j)
        return pStr
    
if __name__ == "__main__":
    ss = 'abc'
    S = Solution()
    print(S.Permutation(ss)) 