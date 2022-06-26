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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        prev = None
        cur = head
        k = 0
        while cur is not None:
            nextnode = cur.next
            cur = nextnode
            k += 1
        cur = head
        for i in range(k // 2):
            nextnode = cur.next
            cur = nextnode
        return cur

solution = Solution()
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

print(solution.middleNode(list1))