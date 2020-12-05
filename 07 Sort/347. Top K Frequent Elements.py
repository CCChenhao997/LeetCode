"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List

class Solution:
    # 堆
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict, Counter
        import heapq
        lookup = Counter(nums)
        heap = []
        for key, value in lookup.items():
            heapq.heappush(heap, [-value, key])
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        c = collections.Counter(nums)
        return heapq.nlargest(k, c, key=lambda x: c[x])
        
    
    # 桶排序
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        
        c = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for x, y in c.items():
            buckets[y].append(x)
        res = []
        for i in range(len(nums), -1, -1):
            if len(res) > k:
                break
            res.extend(buckets[i])
        return res[:k]
        
    
    
s = Solution()
print(s.topKFrequent([1, 3, 1, 2, 2], 2))