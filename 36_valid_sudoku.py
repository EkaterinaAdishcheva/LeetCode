class Solution:
    def __init__(self) -> None:
        pass

    def test_digital_line(self, digital_line):
        stat = set()
        for d in digital_line:
            if d in stat or d > 9 or d < 1:
                return False
            stat.add(d)
        return True

    def test_column(self, column, board):
        digital_line = [int(x) for x in [board[i][column] for i in range(9)] if x != '.']
        return self.test_digital_line(digital_line)

    def test_row(self, row, board):
        digital_line = [int(x) for x in [board[row][i] for i in range(9)] if x != '.']
        return self.test_digital_line(digital_line)

    def test_square(self, r, c, board):
        digital_line = [int(x) for x in [board[3 * r + i][3 * c + j] for i in range(3) for j in range(3)] if x != '.']
        return self.test_digital_line(digital_line)

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            if False == self.test_column(i, board):
                return False
            if False == self.test_row(i, board):
                return False
        for i in range(3):
            for j in range(3):
                if False == self.test_square(i, j, board):
                    return False
        return True
                

solution = Solution()
print(solution.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))