class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1],]
        for i in range(1, numRows):
            line = [triangle[-1][0]]
            for k in range(1, len(triangle[-1])):
                line.append(triangle[-1][k] + triangle[-1][k-1])
            line.append(triangle[-1][-1])
            triangle.append(line)
        return triangle

solution = Solution()
solution.generate(numRows = 1)