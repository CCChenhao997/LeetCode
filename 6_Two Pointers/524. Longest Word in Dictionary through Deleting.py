"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output: 
"apple"

Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]
Output: 
"a"

Note:
1. All the strings in the input will only contain lower-case letters.
2. The size of the dictionary won't exceed 1,000.
3. The length of all the strings in the input won't exceed 1,000.
"""

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        if not s or not d:
            return ""
        d = sorted(d, key = lambda i:(-len(i), i))
        sList = list(s)
        for i, string in enumerate(d):
            p1, p2 = 0, 0
            dList = list(string)
            while p1 < len(sList):
                if sList[p1] == dList[p2]:
                    p1 += 1
                    p2 += 1
                    if p2 >= len(dList):
                        return string
                else:
                    p1 += 1
        return ""
            
        
        

# myList = ["ba","ab","a","b"]
# #myList.sort(reverse=True)
# myList = sorted(myList, key = lambda i:(-len(i), i))
# print(myList) 