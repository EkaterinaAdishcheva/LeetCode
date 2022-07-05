class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        l = 0
        frequency = {}
        longestLength  = 0
        maxFrequency = 0
        for r in range(length):
            frequency[s[r]] = 1 + frequency.get(s[r], 0)
            maxFrequency = max(maxFrequency, frequency[s[r]])
            while (r - l + 1) - maxFrequency > k:
                frequency[s[l]] -= 1
                l += 1
            print(l, r)
            print(frequency)
            print(maxFrequency)
            longestLength = max(longestLength, r - l + 1)
            print(longestLength)
        return longestLength

                


 

solution = Solution()
s = "AADBACBGGGGGGGGGGBA"
k = 2
print(solution.characterReplacement(s, k))