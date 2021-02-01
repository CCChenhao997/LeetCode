'''
Description: 
version: 
Author: chenhao
Date: 2021-01-31 23:19:25
'''

"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    
示例 1:
输入: "A"
输出: 1

示例 2:
输入: "AB"
输出: 28

示例 3:
输入: "ZY"
输出: 701

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        # ord() 字符转ASCII   'a': 97, 'A': 65
        # chr() ASCII转字符
        # 本题就是10进制转26进制

        # dic = {}
        # for i in range(65, 65 + 26):
        #     dic[chr(i)] = i - 64
        
        res = 0
        for ch in s:
            # res = 26 * res + dic[ch]
            res = 26 * res + (ord(ch) % 64)
        return res
    

if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('AB'))