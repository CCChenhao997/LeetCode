"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import heapq

class Solution:
    # 冒泡排序，时间复杂度过高，没通过
    def findKthLargest(self, nums: List[int], k: int) -> int:
        length = len(nums)
        for i in range(length):
            for j in range(length-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            if i + 1 == k:
                return nums[-k]
            
    
    # 堆排序
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
    
    
    # 快速选择
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            
            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            
            return store_index
            
    
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left...right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between
            pivot_index = random.randint(left, right)
            
            # find the pivot position in a sorted position
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)
            
        # kth largest is (n-k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)
            
        