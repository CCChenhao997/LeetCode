'''
Description: 
version: 
Author: chenhao
Date: 2020-12-18 14:47:13
'''

def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[high], array[i + 1] = array[i + 1], array[high]
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
    return array


if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print(quickSort(array, 0, len(array) - 1))