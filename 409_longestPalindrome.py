class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        
        lenth = 0
        for letter in s_dict:
            lenth += 2 * ( s_dict[letter] // 2 )
        
        if lenth < len(s):
            lenth += 1

        return lenth
             
solution = Solution()
s = "abccccdd"
print(solution.longestPalindrome(s))