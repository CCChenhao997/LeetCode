'''
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

思路：
二分查找的变形，注意到旋转数组的首元素肯定不小于旋转数组的尾元素，设置中间点。
如果中间点大于首元素，说明最小数字在后面一半，如果中间点小于尾元素，说明最小
数字在前一半。依次循环。同时，当一次循环中首元素小于尾元素，说明最小值就是首
元素。但是当首元素等于尾元素等于中间值，只能在这个区域顺序查找。
'''

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        front, rear = 0, len(rotateArray) - 1
        minVal = rotateArray[0]
        # 首元素小于尾元素，返回首元素（最小值）
        if rotateArray[front] < rotateArray[rear]:
            return rotateArray[front]
        else:
            while (rear - front) > 1:
                mid = (rear + front) // 2
                # 中间元素大于尾元素，front指针移到中间
                if rotateArray[mid] > rotateArray[rear]:
                    front = mid
                # rear指针移动
                elif rotateArray[mid] < rotateArray[front]:
                    rear = mid
                # 此时需要顺序遍历
                elif rotateArray[mid] == rotateArray[front] == rotateArray[rear]:
                    for i in range(1, len(rotateArray)):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                            rear = i
            minVal = rotateArray[rear]
            return minVal


