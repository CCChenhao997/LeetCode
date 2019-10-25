"""
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路:
利用二叉搜索树的性质
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False

        root = sequence[-1]
        length = len(sequence)
        temp = 0
        for i in range(length - 1):
            # * 如果sequence=[1,2,3,4,5]
            # * 这里 if 进不来，temp也就没有值，所以把temp放到if外面来
            temp = i
            if sequence[i] > root:
                # temp = i
                print("temp:", temp)
                break

        # * 因为第temp个在上一步就已经判断了是大于root的
        # * 所以这里从 temp + 1 开始，否则出错，如例[4, 6, 7, 5]
        for j in range(temp + 1, length - 1):
            if sequence[j] < root:
                # print("zheli")
                return False

        left = True
        if temp > 0:
            left = self.VerifySquenceOfBST(sequence[:temp])

        right = True
        if temp < length - 1:
            right = self.VerifySquenceOfBST(sequence[temp : length - 1])
        # print("left", left)
        # print("right", right)
        return left and right


test = Solution()
# print(test.VerifySquenceOfBST([4, 6, 7, 5]))
print(test.VerifySquenceOfBST([1, 2, 3, 4, 5]))
