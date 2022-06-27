from typing import List, Optional

from pkg_resources import resource_listdir    
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res_dict = {}
        while head:
            if head.val not in res_dict:
                res_dict[head.val] = 0
            res_dict[head.val] += 1
            head = head.next
        
        res_list = []
        for r in res_dict:
            if res_dict[r] == 1:
                res_list.append(r)
        
        res = []
        for r in reversed(res_list):
            res = ListNode(r, res)

        return res
                
