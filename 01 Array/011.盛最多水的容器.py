'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 即是找两条线与x轴围起来的面积最大，既要考虑x轴的长度，也要考虑两条线的最小高度
from typing import List

'''
# 思路: 把任意两条线的围起来的面积全部算出来(暴力循环，没有通过)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        store_list = []
        for i in range(n-1):
            S = 0
            for j, value in enumerate(height[i+1:]):
                # j = j + i + 1               # 这里j = j + i + 1是为了保证两条线的距离正确
                # w = j - i                   # 宽度
                w = j + 1                   # 可以把上面两步省略掉，直接写成一步
                h = min(value, height[i])   # 高度
                s = w * h
                if S < s:
                    S = s
            store_list.append(S)
        return max(store_list)
'''


# 双指针法
# 木桶原理，把短板增高。
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height)-1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res




if __name__=='__main__':
    height = [1,8,6,2,5,4,8,3,7]
    X = Solution()
    print(X.maxArea(height))