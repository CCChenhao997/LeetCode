'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 回溯法 backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:    # 只有在当前序列中的左括号数大于右括号数的时候加上右括号才能形成有效序列
                backtrack(S+')', left, right+1)
        
        backtrack()
        return ans


"""
# 动态规划（没看懂）
'''
简单来说，在求N个括号的排列组合时，把第N种情况（也就是N个括号排列组合）视为单独拿一个括号E出来，
剩下的N-1个括号分为两部分，P个括号和Q个括号，P+Q=N-1，然后这两部分分别处于括号E内和括号E的右边，
各自进行括号的排列组合。由于我们是一步步计算得到N个括号的情况的，所以小于等于N-1个括号的排列组合
方式我们是已知的（用合适的数据结构存储，方便后续调用，且在存储时可利用特定数据结构实现题目某些要求，
如排序，去重等），且P+Q=N-1，P和Q是小于等于N-1的，所以我们能直接得到P个和Q个括号的情况，进而得到
N个括号的结果！
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        total_1 = []
        total_1.append([None])      # 0组括号时记为None
        total_1.append(["()"])      # 1组括号只有一种情况
        for i in range(2, n+1):     # 开始计算i组括号时的括号组合
            l = []
            for j in range(i):      # 开始遍历 p q, 其中p+q=i-1, j作为索引
                now_list1 = total_1[j]      # p = j 时的括号组合情况
                now_list2 = total_1[i-1-j]  # q = [i-1] - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)        # 把所有可能的情况添加到 l 中
            total_1.append(l)   # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_1[n]
"""




if __name__=='__main__':
    X = Solution()
    n = 3
    print(X.generateParenthesis(n))