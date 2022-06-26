class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        dim = len(matrix)
        for i in range( (dim + 1) // 2):
            for j in range( dim // 2):
                save_element = matrix[i][j]
                matrix[i][j] = matrix[dim - 1 - j][i]
                matrix[dim - 1 - j][i] = matrix[dim - 1 - i][dim - 1 - j]
                matrix[dim - 1 - i][dim - 1 - j] = matrix[j][dim - 1 - i]
                matrix[j][dim - 1 - i] = save_element
        print(matrix)

solution = Solution()
solution.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])