'''
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。

链接：https://leetcode-cn.com/problems/remove-element
'''
from typing import List

'''
# 自己的解法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            if val in nums:
                nums.remove(val)
            else: break
        return len(nums)
'''


'''
# 解法二: 覆盖
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i为不同元素的数组的长度
        i = 0
        for j in range(0, len(nums)):
            # 如果nums[j]不等于val，则将nums[j]赋值给nums[i]即可，i自增
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
'''


# 解法三: 双指针
'''
用双指针，一个从头向后扫，一个从尾向前扫,头指针把等于 val 和尾指针不等于 val 调换即可。
时间复杂度：O(n)
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0     # 如果 nums 为空列表则返回0
        slow = 0
        n = len(nums)
        fast = n - 1
        while slow < fast:
            while slow < fast and nums[slow] != val:
                slow += 1
            while slow < fast and nums[fast] == val:
                fast -= 1
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast -= 1
        res = 0                   # res 为返回的数组长度
        for i in range(n):
            if nums[i] == val:
                return res
            res += 1



if __name__=='__main__':
    X = Solution()
    nums = [3,2,2,3]
    val = 3
    print(X.removeElement(nums, val))
        

