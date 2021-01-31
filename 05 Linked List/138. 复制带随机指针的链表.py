'''
Description: 
version: 
Author: chenhao
Date: 2021-01-31 14:44:11
'''

"""
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
要求返回这个链表的深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
 
示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

示例 4：
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 
提示：
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 复制: 指的是深拷贝，也就是创建新的对象，内存地址不同
        # 解题思路：遍历链表，对每个节点创建一个新的节点，然后用 next 或者 random 指针连接起来
        # hashmap: key 用来存放原链表中的每个节点, value 存放对应创建的新节点
        # * Time O(n), Space O(n)
        # if not head: return None
        # hashmap = {}
        # cur_head = head
        # while cur_head:
        #     hashmap[cur_head] = Node(cur_head.val)
        #     cur_head = cur_head.next
        # # 把 next 和 random 指针连接起来
        # cur_head = head
        # while cur_head:
        #     hashmap[cur_head].next = hashmap[cur_head.next] if cur_head.next else None
        #     hashmap[cur_head].random = hashmap[cur_head.random] if cur_head.random else None
        #     cur_head = cur_head.next
        # return hashmap[head]
        
        # * Time O(n), Space O(1)
        if not head: return None
        
        # 把新节点放到原节点的next
        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        
        # 构建新节点的random
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        
        # A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head         # A->B->C
        ptr_new_list = head.next    # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new