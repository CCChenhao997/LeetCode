'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5

链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
'''

'''
# 解法一: 自己的想法就是naive，未考虑时间复杂度
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums3 = sorted(nums1 + nums2)
        len_nums3 = len(nums3)
        if len_nums3 % 2 == 1:
            return (float(nums3[len_nums3//2]))
        else:
            return (float(nums3[len_nums3//2] + nums3[len_nums3//2 - 1]) / 2)
'''



# 解法二
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        def getKth(nums1, start1, end1, nums2, start2, end2, k):
            len1 = end1 - start1 + 1
            len2 = end2 - start2 + 1
            # 让len1的长度小于len2，这样就能保证如果有数组空了，一定是len1
            if len1 > len2: return getKth(nums2, start2, end2, nums1, start1, end1, k)
            # nums1数组为空
            if len1 == 0: return nums2[start2 + k -1]

            if k == 1: return float(min(nums1[start1], nums2[start2]))

            # i,j 相当于双指针
            i = start1 + min(len1, k//2) - 1
            j = start2 + min(len2, k//2) - 1

            if nums1[i] > nums2[j]:
                return getKth(nums1, start1, end1, nums2, j+1, end2, k - (j - start2 + 1))
            else:
                return getKth(nums1, i+1, end1, nums2, start2, end2, k - (i - start1 + 1))

        n = len(nums1)
        m = len(nums2)
        left = (n+m+1) // 2
        right = (n+m+2) // 2
        return (getKth(nums1, 0, n-1, nums2, 0, m-1, left) + getKth(nums1, 0, n-1, nums2, 0, m-1, right))*0.5



if __name__=='__main__':
    nums1 = [1, 2]
    nums2 = [3, 4] 
    X = Solution()
    print(X.findMedianSortedArrays(nums1, nums2))