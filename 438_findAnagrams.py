from typing import List, Optional

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = {}
        for l in p:
            if l in p_dict:
                p_dict[l] += 1
            else:
                p_dict[l] = 1
        
        s_dict = {}
        for l in s[:len(p)]:
            if l in p_dict:
                if l in s_dict:
                    s_dict[l] += 1
                else:
                    s_dict[l] = 1

        res = []
        for n in range(len(s) - len(p) +1):
            if s_dict == p_dict:
                res.append(n)
            if s[n] in s_dict:  
                s_dict[s[n]] -= 1
            if n + len(p) < len(s):
                if s[n + len(p)] in p_dict:
                    if s[n + len(p)] in s_dict:
                        s_dict[s[n + len(p)]] += 1
                    else:
                        s_dict[s[n + len(p)]] = 1
        
        return res

solution = Solution()
s = "abab"
p = "ab"
print(solution.findAnagrams(s, p))