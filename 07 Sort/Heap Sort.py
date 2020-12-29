'''
Description: 
version: 
Author: chenhao
Date: 2020-12-25 20:12:44
'''

class Solution(object):
    
    def heapSort(self, array):
        i, l = 0, len(array)
        self.array = array
        # 构造大顶堆，从非叶子节点开始倒序遍历，因此是l//2 -1 就是最后一个非叶子节点
        for i in range(l//2-1, -1, -1):
            self.buildHeap(i, l-1)
        # 上面的循环完成了大顶堆的构造，那么就开始把根节点跟末尾节点交换，然后重新调整大顶堆  
        for j in range(l-1, -1, -1):
            array[0], array[j] = array[j], array[0]
            self.buildHeap(0, j-1)
        return array

    def buildHeap(self, i, l): 
        """构建大顶堆"""
        left, right = 2*i+1, 2*i+2 ## 左右子节点的下标
        large_index = i
        if left <= l and self.array[i] < self.array[left]:
            large_index = left

        if right <= l and self.array[large_index] < self.array[right]:
            large_index = right
 
        # 通过上面跟左右节点比较后，得出三个元素之间较大的下标，如果较大下标不是父节点的下标，说明交换后需要重新调整大顶堆
        if large_index != i:
            self.array[i], self.array[large_index] = self.array[large_index], self.array[i]
            self.buildHeap(large_index, l)
 

if __name__ == "__main__":
    s = Solution()
    array = [10, 7, 8, 9, 1, 5]
    print(s.heapSort(array))