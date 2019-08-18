'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 
27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，
而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:
输入: "III"
输出: 3

示例 2:
输入: "IV"
输出: 4

示例 3:
输入: "IX"
输出: 9

示例 4:
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

链接：https://leetcode-cn.com/problems/roman-to-integer
'''


'''
# 自己的菜🐔解法
class Solution:
    def romanToInt(self, s: str) -> int:
        Rome_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        s_len = len(s)
        sum = 0
        i = 0
        if s_len >= 2:
            while i < s_len:
                if  i <= (s_len - 2) and Rome_dict[s[i]] < Rome_dict[s[i+1]]:
                    sum = sum + Rome_dict[s[i+1]] - Rome_dict[s[i]]
                    i += 2
                else:
                    sum += Rome_dict[s[i]]
                    i += 1
        else: sum += Rome_dict[s[i]]
        return sum
'''


'''
1.构建一个字典记录所有罗马数字子串，注意长度为2的子串记录的值是（实际值 - 子串内左边罗马数字代表的数值）
2.这样一来，遍历整个 s 的时候判断当前位置和前一个位置的两个字符组成的字符串是否在字典内，如果在就记录值，不在就说明当前位置不存在小数字在前面的情况，直接记录当前位置字符对应值
举个例子，遍历经过 IV 的时候先记录 I 的对应值 1 再往前移动一步记录 IV 的值 3，加起来正好是 IV 的真实值 4。max 函数在这里是为了防止遍历第一个字符的时候出现 [-1:0] 的情况
'''
# 别人的高端解法
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))    # 字典get(key, default=None)方法: 返回指定键的值，如果指定键的值不在字典中返回指定值，默认为 None。



if __name__=='__main__':
    s = input("请输入一个罗马数字:")
    X = Solution()
    print(X.romanToInt(s))