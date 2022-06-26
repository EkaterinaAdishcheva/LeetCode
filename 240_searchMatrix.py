class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def searchMatrixStep(matrix, target, m1, m2, n1, n2):
            print(m1, m2, n1, n2)
            if m1 >= ( m2 - 1 ) and n1 >= ( n2 - 1 ):
                return matrix[m1][n1] == target
            if target < matrix[m1][n1] or target > matrix[m2 - 1][n2 - 1]:
                return False
            res = searchMatrixStep(matrix, target, m1, m1 + (m2 - m1) // 2, n1, n1 + (n2 - n1) // 2) or \
                  searchMatrixStep(matrix, target, m1, m1 + (m2 - m1) // 2, n1 + (n2 - n1) // 2, n2) or \
                  searchMatrixStep(matrix, target, m1 + (m2 - m1) // 2, m2, n1, n1 + (n2 - n1) // 2) or \
                  searchMatrixStep(matrix, target, m1 + (m2 - m1) // 2, m2, n1 + (n2 - n1) // 2, n2)
            return res

        return searchMatrixStep(matrix, target, 0, len(matrix), 0, len(matrix[0]))         

solution = Solution()
print(
    solution.searchMatrix(matrix = [[1,4,7,11,20, 30, 40]], target = 20)
)