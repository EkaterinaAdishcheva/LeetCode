class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        
        match_pattern_s = {}
        match_s_pattern = {}
        
        for pos in range(len(pattern)):
            if pattern[pos] in match_pattern_s:
                if s_list[pos] != match_pattern_s[pattern[pos]]:
                    return False
            else:
                match_pattern_s[pattern[pos]] = s_list[pos]
            if s_list[pos] in match_s_pattern:
                if pattern[pos] != match_s_pattern[s_list[pos]]:
                    return False
            else:
                match_s_pattern[s_list[pos]] = pattern[pos]
        else:
            return True

solution = Solution()
pattern = "aaaa"
s = "dog cat cat dog"

print(solution.wordPattern(pattern, s))