"""
题目描述：
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。

思路：
归并排序，时间复杂度O(nlogn)
"""


class Solution:
    def InversePairs(self, data):
        length = len(data)
        if data == None or length <= 0:
            return 0
        copy = [0]*length
        for i in range(length):
            copy[i] = data[i]
        count = self.InversePairsCore(data, copy, 0, length-1)
        return count

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start)//2
        left = self.InversePairsCore(copy, data, start, start+length)
        right = self.InversePairsCore(copy, data, start+length+1, end)
        
        # i初始化为前半段最后一个数字的下标
        i = start + length
        # j初始化为后半段最后一个数字的下标
        j = end
        
        indexCopy = end     # 辅助数组的索引
        count = 0
        while i >= start and j >= start+length+1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start -length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1
        
        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start+length+1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return (left + right + count)%1000000007
    
    
    def InversePairs2(self, data):
        import copy
        if len(data) <= 0:
            return 0
        count = 0
        Copy = copy.deepcopy(data)
        Copy.sort()
        i = 0
        while len(Copy) > i:
            count += data.index(Copy[i])
            data.remove(Copy[i])
            i += 1
        return count            
   
    
s = Solution()
print(s.InversePairs2([7, 5, 6, 4]))
