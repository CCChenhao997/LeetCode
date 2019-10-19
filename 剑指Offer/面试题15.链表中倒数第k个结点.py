'''
题目描述:
输入一个链表，输出该链表中倒数第k个结点。

解题思路:
这道题的思路很好
如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
然后两个指针一起遍历
当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间


代码的鲁棒性。
需要注意：如果输入的链表为空；k大于链表的长度；k为0的情况。
对于正常情况，设置两个指针分别指向头结点，第一个指针向前走k-1步，
走到正数第k个结点，同时保持第二个指针不动，然后第一个指针和第二个
指针每次同时前移一步，这样第一个指针指向尾结点的时候，第二个指针
指向倒数第k个结点。判断尾结点的条件是 pNode.next == None。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k <= 0:
            return None
        
        pAhead = head
        pBehind = None

        # pAhead先走 k-1 步
        for i in range(k-1):
            if pAhead.next != None:
                pAhead = pAhead.next
            else:
                return None
        
        pBehind = head
        while pAhead.next != None:
            pAhead = pAhead.next
            pBehind = pBehind.next
        
        return pBehind


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
print(S.FindKthToTail(node1, 1).val)
    
        