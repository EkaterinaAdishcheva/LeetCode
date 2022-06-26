class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        def getPascal(index: int):
            if 0 == index:
                return [1]        
            previous_line = self.getRow(index - 1)
            result_line = [previous_line[0]]
            for k in range(1, index):
                result_line.append(previous_line[k] + previous_line[k-1])
            result_line.append(previous_line[-1])
            return result_line
        
        return getPascal(rowIndex)

solution = Solution()
print(solution.getRow(rowIndex = 3))