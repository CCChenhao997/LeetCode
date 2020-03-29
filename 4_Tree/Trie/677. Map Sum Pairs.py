'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-29 09:54:04
@LastEditors: chenhao
@LastEditTime: 2020-03-29 10:38:16
'''

"""
Implement a MapSum class with insert, and sum methods.
For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}
        

    def insert(self, key: str, val: int) -> None:
        tree = self.lookup
        for a in key:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = val
        

    def sum(self, prefix: str) -> int:
        tree = self.lookup
        self.prefixSum = 0
        for a in prefix:
            if a not in tree:
                return self.prefixSum
            tree = tree[a]
        self.recursion(tree)
        return self.prefixSum
        
        
    def recursion(self, tree):
        if not tree:
            return
        for a in tree:
            if a == "#":
                self.prefixSum += tree["#"]
            else:
                self.recursion(tree[a])
        
        


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3),
obj.insert("app", 2)
param_2 = obj.sum("ap")
print(param_2)


