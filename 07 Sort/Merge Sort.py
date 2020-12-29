'''
Description: 
version: 
Author: chenhao
Date: 2020-12-25 20:24:51
'''

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def mergeSort(array):
    if len(array) <= 1:
        return array
    mid_index = len(array) // 2  #直接取整，不然会报错(python3）
    left = mergeSort(array[:mid_index])
    right = mergeSort(array[mid_index:])
    return merge(left, right)

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print(mergeSort(array))