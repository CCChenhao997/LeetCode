from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans, ma = 0, 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i:
                ans += 1
        return ans