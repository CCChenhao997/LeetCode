"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input:
"tree"
Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"
Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"
Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""


class Solution:
    # Buckets sort
    def frequencySort(self, s: str) -> str:
        sList = list(s)
        buckets = [[] for _ in range(len(sList) + 1)]
        
        from collections import Counter
        c = Counter(sList)
        
        for x, y in c.items():
            buckets[y].append(x*y)
        res = []
        for i in range(len(sList), -1, -1):
            res.extend(buckets[i])
        return ''.join(res)
    
    
    # Heap sort
    def frequencySort2(self, s: str) -> str:
        from collections import defaultdict
        import heapq
        
        countFrequency = defaultdict(int)
        for i in s:
            countFrequency[i] += 1
        lst = []
        heapq.heapify(lst)      # transform list into heap
        for i in countFrequency:
            for j in range(countFrequency[i]):
                heapq.heappush(lst, (-countFrequency[i], i))
        
        return ''.join([heapq.heappop(lst)[1] for _ in range(len(s))])
        
        
    
    
s =Solution()
print(s.frequencySort2('sttrrr'))