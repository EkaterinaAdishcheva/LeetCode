from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def display(self):
        pointer = self
        res = []
        while pointer:
            res.append(pointer.val)
            pointer = pointer.next
        print(res)

def buildListNode(l):
    res = ListNode()
    pointer = res
    for i in l:
        pointer.next = ListNode(i)
        pointer = pointer.next
    return res.next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_dict = {}
        level = 0
        pointer = head
        while pointer:
            node_dict[level] = pointer
            pointer = pointer.next
            level += 1
        node_keys_list = list(node_dict.keys())
        for i in range(len(node_keys_list)// 2):
            current_node = ListNode(node_dict[len(node_keys_list) - 1 - i].val)
            node_dict[len(node_keys_list) - 2 - i].next = None
            node_dict[len(node_keys_list) - 1 - i] = None
            current_node.next = node_dict[i + 1]
            node_dict[i].next = current_node
        return node_dict[0]

head = buildListNode([1,2,3,4,5])
head.display()
solution = Solution()
res = solution.reorderList(head)
res.display()