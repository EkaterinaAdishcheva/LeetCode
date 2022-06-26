class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        DNA_seqences = set()
        res = set()
        for i in range(len(s) - 10 + 1):
            if s[i:i + 10] in DNA_seqences:
                res.add( s[i:i + 10] )
            else:
                DNA_seqences.add( s[i:i + 10] )
        
        return list(res)

solution = Solution()
s = 'AAAAAAAAAAAAAA'
print(solution.findRepeatedDnaSequences(s))