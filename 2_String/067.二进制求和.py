'''
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
# 解法一: 自己写的
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        str_len = max(len(a), len(b))
        a = '0'*(str_len - len(a)) + a
        b = '0'*(str_len - len(b)) + b
        c = ''
        r = 0
        for i in range(str_len -1 , -1, -1):
            sum_ab = int(a[i]) + int(b[i]) + r
            r = sum_ab // 2
            c = str(sum_ab % 2) + c
        if r:
            c = str(r) + c
        return c
"""


# 解法二: Python 内置函数
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # int(a, 2) 将二进制数转成10进制数
        # bin() 再将10进制数转成2进制数
        return bin(int(a, 2) + int(b, 2))[2:]



if __name__=='__main__':
    X = Solution()
    a = '1010'
    b = '1011'
    print(X.addBinary(a, b))