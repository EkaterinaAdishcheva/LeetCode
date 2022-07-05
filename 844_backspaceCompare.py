class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_final = ""
        for s_l in s:
            if s_l != "#":
                s_final += s_l
            else:
                s_final = s_final[:-1]

        t_final = ""
        for t_l in t:
            if t_l != "#":
                t_final += t_l
            else:
                t_final = t_final[:-1]

        return t_final == s_final