class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        replace_s_t_dict = {}
        replace_t_s_dict = {}
        for pos in range(len(s)):
            if s[pos] in replace_s_t_dict:
                if replace_s_t_dict[s[pos]] != t[pos]:
                    return False
            if t[pos] in replace_t_s_dict:
                if replace_t_s_dict[t[pos]] != s[pos]:
                    return False
            else:
                    replace_s_t_dict[s[pos]] = t[pos]
                    replace_t_s_dict[t[pos]] = s[pos]
        else:
            return True

solution = Solution()
s = "badc"
t = "baba"
print(solution.isIsomorphic(s, t))