'''
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"

示例 2:
输入: 4
输出: "1211"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
# 解法一
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        if n == 2: return '11' 
        pre = '11'          # pre为前一项字符串
        for i in range(3, n+1):
            res = ''        # 初始化
            cnt = 1         # 计数
            string_len = len(pre)
            for j in range(1, string_len):
                if pre[j-1] == pre[j]:
                    cnt += 1
                else:
                    res += str(cnt) + pre[j-1]
                    cnt = 1     # 计数置0
            # 字符串中最后一个字符若与倒数第二个字符相等时，则不进入else就会退出循环，所以要另外计算
            # 字符串中最后一个字符若与倒数第二个字符不相等时，它也不会被计算，所以要另外计算
            res += str(cnt) + pre[j]
            pre = res           # 保存前一项结果
        return res
'''


# 解法二: 用Python的groupby方法来完成
'''
看见1就说1个1，看见n个1就说n个1，看见其他数字也一样，例如：1121 -> 2个1, 1个2, 1个1 -> 211211。
这道题目用groupby方法做就很容易实现，因为这个方法已经帮我们把数的步骤给解决了。使用了groupby方法后，
效果为：1121 -> [['1', '1'], ['2'], ['1']] -> 我们只需要把groupby后的每个子数组长度放在前，
元素放在后，拼接起来即可。
'''
from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for i in range(1, n):
            result = ''.join([str(len(list(g))) + k for k, g in groupby(result)])
        return result



if __name__=='__main__':
    X = Solution()
    n = 5
    print(X.countAndSay(n))
            
        


        
