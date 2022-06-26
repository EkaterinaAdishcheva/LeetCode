class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print(f"s: {s}, p:{p}")
        if 0 == len(s) and 0 == len(p):
            return True
        if 0 == len(p):
            return False
        if 1 == len(p):
            if ('.' == p and 1 == len(s)) or s == p:
                return True
            return False
        if '*' == p[1]:
            if '.' ==  p[0]:
                for l in range(len(s) + 1):
                    if self.isMatch(s[l:], p[2:]):
                        return True
                else:
                    return False
            if self.isMatch(s, p[2:]):
                return True
            for l in range(len(s)):
                if s[l] == p[0]:
                    if self.isMatch(s[l+1:], p[2:]):
                        return True
                else:
                    return False
            else:
                return self.isMatch("", p[2:])

        if '.' == p[0]:
            if 0 == len(s):
                return False
            return self.isMatch(s[1:], p[1:])
        else:
            if 0 == len(s):
                return False
            if p[0] == s[0]:
                return self.isMatch(s[1:], p[1:])
            return False

solution = Solution()
res = solution.isMatch("bb", ".bab")
print(res)