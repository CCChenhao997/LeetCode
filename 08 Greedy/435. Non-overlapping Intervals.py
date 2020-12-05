'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-03-30 12:55:10
@LastEditors: chenhao
@LastEditTime: 2020-04-01 18:30:15
'''

"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 
Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key=lambda x:x[1])
        intervals.sort(key=self.takeSecond)
        pre = float('-inf')
        maxNum = 0
        for term in intervals:
            if term[0] >= pre:
                maxNum += 1
                pre = term[1]
        return len(intervals) - maxNum
    
    @staticmethod
    def takeSecond(elem):
        return elem[1]