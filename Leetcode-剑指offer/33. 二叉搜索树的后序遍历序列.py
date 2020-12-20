'''
Description: 
version: 
Author: chenhao
Date: 2020-12-20 23:05:02
'''

"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
 
示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder or len(postorder) == 0:
            return True
        
        inorder = sorted(postorder)
        root = postorder[-1]
        idx = inorder.index(root)
        left = self.verifyPostorder(postorder[: idx])
        right = self.verifyPostorder(postorder[idx: -1])
        
        for val in postorder[: idx]:
            if val > root:
                return False
        
        for val in postorder[idx: -1]:
            if val < root:
                return False
         
        return left and right