class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        old_c = len(mat[0])
        if ( len(mat) * old_c ) != ( r * c ):
            return mat
        res = [[None for i in range(c)] for j in range(r)]
        for i in range(r * c):
            res[i // c][i % c] = mat[i // old_c][i % old_c]
        return res

solution = Solution()
solution.matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4)