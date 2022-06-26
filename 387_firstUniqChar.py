class Solution:
    def firstUniqChar(self, s: str) -> int:
        element_qnt = {}
        element_pos = {}
        for n, element in enumerate(s):
            if element in element_qnt:
                element_qnt[element] += 1
            else:
                element_qnt[element] = 1
                element_pos[element] = n
        for item in element_qnt:
            if element_qnt[item] == 1:
                return element_pos[item]
        
        return -1


