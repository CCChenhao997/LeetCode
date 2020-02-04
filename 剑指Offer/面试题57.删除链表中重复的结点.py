"""
题目描述:
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。

思路:
我们需要设置一个指针preNode，preNode最开始为None，然后设置两个指针，
pNode指向当前节点，pNext指向pNode下一个结点，
⓵如果pNext不为空而且pNext的值等于pNode的值，那么就说明出现了重复数字的结点，
就需要删除，然后从pNode开始遍历，如果结点值等于前面那个重复值，继续遍历。
当遍历到None或者不同值结点的时候，这时候需要判断preNode结点，
如果preNode结点为None，就说明我们刚才的重复结点是从整个链表的头结点开始重复的，
就直接把pHead设置为当前结点，pNode也设置为当前结点。
反之，如果preNode不为None，直接把preNode的下一个指针指向当前节点，pNode指向preNode即可；
⓶如果pNext为空或者pNext的值不等于pNode的值，说明当前的这个pNode和后面的值不重复，
直接令preNode = pNode，pNode指向下一个结点即可。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution:
    def deleteDuplication(self, pHead):
        if pHead == None:
            return
        preHead = None
        pNode = pHead
        while pNode != None:
            needDelete = False
            nextNode = pNode.next
            if nextNode != None and nextNode.val == pNode.val:
                needDelete = True
            if needDelete == False:
                preHead = pNode
                pNode = pNode.next
            else:
                nodeVal = pNode.val
                pToBeDel = pNode
                while pToBeDel != None and pToBeDel.val == nodeVal:
                    pToBeDel = pToBeDel.next
                if preHead == None:
                    pHead = pToBeDel
                    pNode = pToBeDel
                    continue
                else:
                    preHead.next = pToBeDel
                pNode = preHead
        return pHead
                    

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(s.deleteDuplication(node1).val)