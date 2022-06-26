class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                res += self.matrix_obj[i][j]
        return res    

my_matrix = NumMatrix([
    [3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]],
 [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4])

for t in my_matrix.tasks:
    print(my_matrix.sumRegion(t[0], t[1], t[2], t[3]))


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)