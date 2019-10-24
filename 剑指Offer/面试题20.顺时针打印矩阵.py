'''
题目描述:
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

思路:
首先需要判断每一步开始坐标点是否满足小于行数的一半且小于列数的一半，
在最后一圈中，可能出现仅能向右走一行，仅能向右走一行向下走一列，向右走
一行向下走一列向左走一行，能走完整一圈，一共四种情况。其中只有能向左走
一行必然发生，不必判断，剩余的都需要判断发生条件。
'''


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix == None:
            return
        rows = len(matrix)        # 行数
        columns = len(matrix[0])  # 列数
        start = 0
        # 循环继续的条件是 rows > start * 2 并且 columns > start * 2
        while rows > start * 2 and columns > start * 2:
            self.printMatrixInCircle(matrix, columns, rows, start)
            start += 1
        print('')

    def printMatrixInCircle(self, matrix, columns, rows, start):
        endX = columns - 1 - start
        endY = rows - 1 - start

        # 从左到右打印一行
        for i in range(start, endX+1):
            number = matrix[start][i]
            print(number, ' ', end='')
        
        # 从上到下打印一列
        if start < endY:
            for i in range(start+1, endY+1):
                number = matrix[i][endX]
                print(number, ' ', end='')
        
        # 从右到左打印一行
        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                number = matrix[endY][i]
                print(number, ' ', end='')
        
        # 从下到上打印一列
        if start < endX and start < endY - 1:
            for i in range(endY-1, start, -1):
                number = matrix[i][start]
                print(number, ' ', end='')


class Solution1:
    # 逆时针翻转矩阵
    def traverse(self, matrix):
        row_num = len(matrix)
        col_num = len(matrix[0])
        traversed = []
        # 添加顺序是倒的
        for c in range(col_num):
            row = []
            for r in range(row_num):
                row.append(matrix[r][c])
            traversed.append(row)
        traversed.reverse()
        print(traversed)
        return traversed
    
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        array = []
        while matrix:
            for item in matrix[0]:
                array.append(item)
            del matrix[0]
            if len(matrix) == 0:
                break
            matrix = self.traverse(matrix)
        return array



matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

S = Solution1()
S.traverse(matrix)
