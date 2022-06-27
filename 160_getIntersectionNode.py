import importlib
from typing import List, Optional
# Definition for singly-linked list.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        headA_copy = headA
        while headA_copy:
            lenA += 1
            headA_copy = headA_copy.next

        lenB = 0
        headB_copy = headB
        while headB_copy:
            lenB += 1
            headB_copy = headB_copy.next
        headA_copy = headA
        headB_copy = headB
        if lenA < lenB:
            while lenB > lenA:
                lenB -= 1
                headB_copy = headB_copy.next
        else:
            while lenA > lenB:
                lenA -= 1
                headA_copy = headA_copy.next
        res = None
        while headA_copy != headB_copy:
            headA_copy = headA_copy.next
            headB_copy = headB_copy.next
        res = headB_copy
        return res