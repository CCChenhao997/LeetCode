'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-04-10 10:29:35
@LastEditors: chenhao
@LastEditTime: 2020-04-10 11:01:17
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p, q = 0, 0
        cnt = len(s)
        while p < len(s) and q < len(t):
            if s[p] == t[q]:
                p += 1
            q += 1
        return cnt == p
    

    # Follow up
    def isSubsequence1(self, s: str, t: str) -> bool:
        # built a hash set of t
        hash_set = {}
        for i, word in enumerate(t):
            if word not in hash_set:
                hash_set[word] = [i]
            else:
                hash_set[word].append(i)
        
        # match
        index = -1
        for word in s:
            if word not in hash_set:
                return False
            # binary search
            indexes = hash_set[word]
            left = 0
            right = len(indexes)
            while left < right:
                mid = left + (right - left) // 2
                if indexes[mid] > index:
                    right = mid
                else:
                    left = mid + 1
            if left == len(indexes):
                return False
            index = indexes[left]
            
        return True