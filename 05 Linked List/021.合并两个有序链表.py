'''
将两个有序链表合并为一个新的有序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 方法1:递归
'''
想法：
我们可以如下递归地定义在两个链表里的 merge 操作（忽略边界情况，比如空链表等）：
    list1[0]+merge(list1[1:], list2)    list1[0]<list2[0]
    list2[0]+merge(list1, list2[1:])    otherwise
也就是说，两个链表头部较小的一个与剩下元素的 merge 操作结果合并。
算法：
我们直接将以上递归过程建模，首先考虑边界情况。
特殊的，如果 l1 或者 l2 一开始就是 null ，那么没有任何操作需要合并，所以我们只需要返回非空链表。
否则，我们要判断 l1 和 l2 哪一个的头元素更小，然后递归地决定下一个添加到结果里的值。
如果两个链表都是空的，那么过程终止，所以递归过程最终一定会终止。
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# 简化版
'''
备注： 在 Python 中，and 和 or 都有提前截至运算的功能。
    and：如果 and 前面的表达式已经为 False，那么 and 之后的表达式将被 跳过，返回左表达式结果
    or：如果 or 前面的表达式已经为 True，那么 or 之后的表达式将被跳过，直接返回左表达式的结果
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
        

# 方法二：迭代
'''
想法:
我们可以用迭代的方法来实现上述算法。我们假设 l1 元素严格比 l2元素少，
我们可以将 l2 中的元素逐一插入 l1 中正确的位置。
算法:
首先，我们设定一个哨兵节点 "prehead" ，这可以在最后让我们比较容易地返回合并后的链表。
我们维护一个 prev 指针，我们需要做的是调整它的 next 指针。然后，我们重复以下过程，
直到 l1 或者 l2 指向了 null ：如果 l1 当前位置的值小于等于 l2 ，我们就把 l1 的
值接在 prev 节点的后面同时将 l1 指针往后移一个。否则，我们对 l2 做同样的操作。
不管我们将哪一个元素接在了后面，我们都把 prev 向后移一个元素。
在循环终止的时候， l1 和 l2 至多有一个是非空的。由于输入的两个链表都是有序的，
所以不管哪个链表是非空的，它包含的所有元素都比前面已经合并链表中的所有元素都要大。
这意味着我们只需要简单地将非空链表接在合并链表的后面，并返回合并链表。
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next
