from tkinter import N


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        elem_stat = {}
        max_qnt, max_elem = None, None
        for n in nums:
            if n in elem_stat:
                elem_stat[n] += 1
            else:
                elem_stat[n] = 1
            if max_qnt is None or max_qnt < elem_stat[n]:
                max_qnt, max_elem = elem_stat[n], n
        return max_elem