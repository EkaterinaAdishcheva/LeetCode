class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_qnt = {}
        for element in magazine:
            if element in magazine_qnt:
                magazine_qnt[element] += 1
            else:
                magazine_qnt[element] = 1

        ransomNote_qnt = {}
        for element in ransomNote:
            if element not in magazine_qnt:
                return False
            if element in ransomNote_qnt:
                ransomNote_qnt[element] += 1
            else:
                ransomNote_qnt[element] = 1
            if magazine_qnt[element] < ransomNote_qnt[element]:
                return False
        
        return True

solution = Solution()
print(solution.canConstruct("aa", "ab"))