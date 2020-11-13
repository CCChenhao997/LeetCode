# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        newhead = head
        prehead = ListNode(None)
        for i in range(m - 1):
            prehead = head
            head = head.next
        modify_list_tail = head

        tmp = None
        for i in range(n - m + 1):
            backup = head.next
            head.next = tmp
            tmp = head
            head = backup
        
        modify_list_tail.next = head
        prehead.next = tmp
        
        if prehead.val == None:
            return tmp
        return newhead
    

if __name__ == "__main__":
    a = ListNode(3)
    b = ListNode(5)
    c = ListNode(2)
    a.next = b
    b.next = c

    s = Solution()
    head = s.reverseBetween(a, 2, 3)
    while head:
        print(head.val)
        head = head.next