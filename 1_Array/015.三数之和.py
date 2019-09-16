'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List

# 排序+双指针，时间复杂度O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums_len = len(nums)
        if nums_len < 3: return ans   # 长度小于3，返回空列表
        nums.sort()    # 排序
        for i in range(nums_len - 2):
            if nums[i] > 0: break   # 如果当前最小的数字大于0，三数之和必大于0，所以结束
            if i > 0 and nums[i] == nums[i-1]: continue    # 去重
            L, R = i + 1, nums_len - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R]
                if sum == 0:
                    ans.append([nums[i], nums[L], nums[R]])
                    while L<R and nums[L] == nums[L+1]: L += 1  # 去重
                    while L<R and nums[R] == nums[R-1]: R -= 1  # 去重
                    L += 1
                    R -= 1
                elif sum < 0: L += 1
                else: R -= 1
        return ans



if __name__=='__main__':
    X = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(X.threeSum(nums))