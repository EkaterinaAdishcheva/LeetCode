class Solution:
    # def __init__(self):
    #     pass

    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0
        str_len = len(s)
        for i in range(str_len):
            middle_start = i
            middle_end = middle_start + 1
            while middle_end < str_len and s[middle_start] ==  s[middle_end]:
                middle_end += 1
            k = 1
            while middle_start - k > -1 and middle_end + k - 1 < str_len and s[middle_start - k] == s[middle_end + k -1]:
                k += 1
            
            if middle_end - middle_start + 2 * k - 2 > max_len:
                max_len = middle_end - middle_start + 2 * k - 2
                res = s[middle_start - k + 1: middle_end + k -1]

        return res
            

s = "cbbd"
solution = Solution()
print(solution.longestPalindrome(s))