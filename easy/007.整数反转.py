'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31, 2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

链接：https://leetcode-cn.com/problems/reverse-integer
'''

class Solution:
    def reverse(self, x: int) -> int:
        x_list = list(str(x))
        res_stack = []      # 用于存放反转的元素
        is_minus = False    # 用于处理负数

        while x_list:
            v = x_list.pop()  # 弹出列表最后一个元素
            if v == '-':
                is_minus = True
                continue
            res_stack.append(v)
        res = int(''.join(res_stack))

        if is_minus:
            res *= -1
        
        # 边界条件: res > 2^31 -1 或 res < (-2^31)
        v_max = 0xffffffff / 2
        if res > (v_max-1) or res < (v_max*(-1)):
            res = 0
        
        return res

if __name__=="__main__":
    x = int(input("请输入数值:"))
    test = Solution()
    print(test.reverse(x))
    