class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        pos = 0
        s = 0
        res = ""
        while pos < max(len1, len2):
            if pos < len1:
                a1 = int(num1[len1-1-pos])
            else:
                a1 = 0
            if pos < len2:
                a2 = int(num2[len2-1-pos])
            else:
                a2 = 0
            _ = a1 + a2 + s
            res_c =  _ % 10
            s =  _ // 10
            res = str(res_c) + res
            pos += 1
        if 1 == s:
            res = str(s) + res
        
        return res

solution = Solution()
num1 = "0"
num2 = "0"
print(solution.addStrings(num1, num2))
            