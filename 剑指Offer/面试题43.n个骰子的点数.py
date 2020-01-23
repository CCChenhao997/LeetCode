"""
题目描述:
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的概率。
"""


# 基于递归求骰子点数，时间效率不够高
class Solution:
    def numberCount(self, n, s):
        if n < 1 or s < n or s > 6 * n:
            return 0
        if n == 1:
            return 1
        count = 0
        count = self.numberCount(n-1, s-1) + self.numberCount(n-1, s-2) + \
                self.numberCount(n-1, s-3) + self.numberCount(n-1, s-4) + \
                self.numberCount(n-1, s-5) + self.numberCount(n-1, s-6)
        return count
    
    def numberOfDice(self, n):
        if n < 1:
            return
        res = []
        for i in range(n, 6 * n + 1):
            res.append(self.numberCount(n, i))
        return ["%.2f%%" % (x/sum(res) * 100) for x in res]
 

# 动态规划
class Solution2:
    #coding=utf8
    def get_ans(self, n):
        dp = [[0 for i in range(6*n)] for i in range(n)]
        for i in range(6):
            dp[0][i] = 1
        # print dp
        for i in range(1, n):  #1，相当于2个骰子。
            for j in range(i, 6*(i+1)):   #[0,i-1]的时候，频数为0（例如2个骰子不可能投出点数和为1）
                dp[i][j] = dp[i-1][j-6] + dp[i-1][j-5] + dp[i-1][j-4] + \
                           dp[i-1][j-3] + dp[i-1][j-2] + dp[i-1][j-1]
    
        count = dp[n-1]
        return count  #算得骰子投出每一个点数的频数。再除以总的排列数即可得到频率
        

s =Solution2()
print(s.get_ans(3))