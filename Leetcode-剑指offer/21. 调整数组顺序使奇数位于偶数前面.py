'''
Description: 
version: 
Author: chenhao
Date: 2020-12-22 21:16:44
'''

"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 
提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            while nums[p1] % 2 == 1 and p1 < p2:   # 如果是奇数
                p1 += 1
            while nums[p2] % 2 == 0 and p1 < p2:   # 如果是偶数
                p2 -= 1
            nums[p1], nums[p2] = nums[p2], nums[p1]
        return nums 