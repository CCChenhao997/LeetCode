"""
题目描述：
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列
都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数
组中是否含有该整数。

思路：
首先选取二维数组中右上角的数字。
如果该数字等于要查找的数字，查找过程结束；
如果该数字大于要查找的数字，剔除这个数字所在的列；
如果该数字小于要查找的数字，剔除这个数字所在的行。

具体做法：
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
"""

# 将(row, col)初始在右上角
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        # 行和列的长度
        rows, cols = len(array), len(array[0])
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if array[row][col] == target:
                return True
            # 删除一列
            elif array[row][col] > target:
                col -= 1
            # 删除一行
            else:
                row += 1
        return False


# 将(row, col)初始在左下角
class Solution1:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        # 行和列的长度
        rows, cols = len(array), len(array[0])
        row, col = rows - 1, 0
        while row >= 0 and col < cols:
            if array[row][col] == target:
                return True
            # 删除一行
            elif array[row][col] > target:
                row -= 1
            # 删除一列
            else:
                col += 1
        return False



if __name__=='__main__':
    X = Solution1()
    target = 7
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(X.Find(target, array))