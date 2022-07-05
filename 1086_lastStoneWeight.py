from typing import List
def insert_binary_ordered(list_elem, elem):
    if len(list_elem) == 0:
        list_elem = [elem]
        return list_elem
    step = len(list_elem)
    l, r = 0, step
    if list_elem[r - 1] < elem:
        list_elem.append(elem)
        return list_elem
    if list_elem[l] >= elem:
        list_elem.insert(0, elem)
        return list_elem
    while step > 1:
        step = (r - l + 1) // 2
        if list_elem[l + step - 1] < elem:
            l += step
        else:
            r = l + step
    list_elem.insert(l, elem)
    return list_elem

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        print(stones)
        while len(stones) > 1:
            smash = stones[-1] - stones[-2]
            stones.pop()
            stones.pop()
            stones = insert_binary_ordered(stones, smash)
        return stones[0]



