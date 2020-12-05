'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：
给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。

示例 1:
输入: n = 3, k = 3
输出: "213"

示例 2:
输入: n = 4, k = 9
输出: "2314"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


"""
import itertools

# 解法一: 使用permutations方法
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num_list = []
        for i in range(1, n+1):
            num_list.append(str(i))

        out_list = list(itertools.permutations(num_list))[k-1]

        out_str = ""
        for i in out_list:
            out_str += i

        return out_str
"""


# 解法二: 回溯+剪枝  没看懂好难呀，
# https://leetcode-cn.com/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/
# https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/
# 阶乘值通过计算得到
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0:
            return []
        nums = [i for i in range(1, n+1)]    # 列表 [1, 2, 3]
        used = [False for _ in range(n)]     # [False, False, False]
        return self.__dfs(nums, used, n, k, 0, [])

    def __factorial(self, n):   # 计算阶乘
        # 这种编码方式包括了 0 的阶乘是 1 这种情况
        res = 1
        while n:
            res *= n
            n -= 1
        return res

    def __dfs(self, nums, used, n, k, depth, pre):
        if depth == n:
            # 在叶子结点处结算
            return ''.join(pre)
        # 后面的数的全排列的个数
        ps = self.__factorial(n - 1 - depth)
        print(ps)
        for i in range(n):
            # 如果这个数用过，就不再考虑
            if used[i]:
                continue
            # 后面的数的全排列的个数小于 k 的时候，执行剪枝操作
            if ps < k:
                k -= ps
                continue
            pre.append(str(nums[i]))
            # 因为直接走到叶子结点，因此状态不用恢复
            used[i] = True
            return self.__dfs(nums, used, n, k, depth + 1, pre)






if __name__=='__main__':
    X = Solution()
    n = 3
    k = 3
    print(X.getPermutation(n, k))