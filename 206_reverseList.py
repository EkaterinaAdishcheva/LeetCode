from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def display(head: Optional[ListNode]):
    head_list = []
    while head:
        head_list.append(head.val)
        head = head.next
    print(head_list)        

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode

        return prev


solution = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

print(solution.reverseList(list1))