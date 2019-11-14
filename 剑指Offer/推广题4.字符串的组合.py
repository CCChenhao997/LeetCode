"""
比如输入abc, 则他们的组合有['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'], 
ab和ba属于不同的排列, 但属于同一个组合。
"""

class Solution:
    def group(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        
        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            pStr.append(charList[i])
            if i > 0 and charList[i] == charList[i-1]:
                continue
            temp = self.group(''.join(charList[i+1:]))
            for j in temp:
                pStr.append(charList[i] + j)
            pStr = list(set(pStr))
            pStr.sort()
        return pStr
    
if __name__=="__main__":
    ss = 'acb'
    S = Solution()
    print(S.group(ss))