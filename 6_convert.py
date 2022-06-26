class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if 1 == numRows:
            return s
        pattern = [
            [None for i in range((len(s) // ( 2 * numRows - 2 ) + 1) * (numRows - 1))]\
                for j in range(numRows)
            ]
        col = -1
        pos = -1
        while True:
            col += 1
            for line in range(numRows):
                pos += 1
                if pos == len(s):
                    break
                pattern[line][col] = s[pos]
            else:
                for line in reversed(range(1, numRows - 1)):
                    col += 1
                    pos += 1
                    if pos == len(s):
                        break
                    pattern[line][col] = s[pos]
            if pos == len(s):
                break

        for line in range(numRows):
            pattern[line] = "".join([x for x in pattern[line] if x])
        res_str = "".join(pattern)
        return res_str                


solution = Solution()
print(solution.convert(s = "A", numRows = 1))
