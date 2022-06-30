from typing import List

LAND = "1"
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        checked_grid = [[False for x in range(len(grid[0]))] for x in range(len(grid))]
        res = 0

        def checkCell(sr, sc, land):
            if checked_grid[sr][sc]:
                return
            checked_grid[sr][sc] = True
            if grid[sr][sc] != land:
                return
            for dir_r, dir_c in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                if sr + dir_r < len(grid) and  sr + dir_r >= 0 and sc + dir_c < len(grid[0]) and sc + dir_c >=0:
                    checkCell(sr + dir_r, sc + dir_c, land)

        for i, j in [[x, y] for x in range(len(grid)) for y in range(len(grid[0]))]:
            if not checked_grid[i][j]:
                if grid[i][j] == LAND:
                    res += 1
                    checkCell(i, j, LAND)     

        return res

solution =  Solution()
grid = [
    ["1","0","1","1","0","1","1"]
    ]
print(solution.numIslands(grid))