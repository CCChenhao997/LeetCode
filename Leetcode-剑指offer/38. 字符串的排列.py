'''
Description: 
version: 
Author: chenhao
Date: 2021-01-17 13:03:53
'''

"""
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

限制：
1 <= s 的长度 <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        result = []
        n = len(s)
        visited = [False] * n
        # * 一定要排序!
        slist = list(s)
        slist.sort()

        def backtracking(path):
            if len(path) == n:
                result.append(path)
                return
            for i in range(n):
                if visited[i] or (i > 0 and slist[i] == slist[i - 1] and not visited[i - 1]): 
                    continue
                visited[i] = True
                backtracking(path + slist[i])
                visited[i] = False
            
        backtracking('')
        return result
    

if __name__ == "__main__":
    test = 'aba'
    s = Solution()
    print(s.permutation(test))