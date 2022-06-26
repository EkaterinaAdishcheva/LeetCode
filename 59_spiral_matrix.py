class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[None for j in range(n)] for i in range(n)]
        start = 1
        for k in range(n  // 2):
            for i in range(n - 2 * k - 1):
                matrix[k][k + i] =start + i
                matrix[k + i][n - k - 1] = start +  (n - 2 * k - 1 )+ i
                matrix[n - k - 1][n - k - 1 - i] = start + 2 * (n - 2 * k - 1 ) + i
                matrix[n - k - 1 - i][k] = start + 3 * (n - 2 * k - 1 ) + i
            start += 4 * (n - 2 * k - 1)
        if 1 == ( n % 2 ):
            matrix[n // 2][n // 2] = n**2 
        return matrix
       
        
solution = Solution()
solution.generateMatrix(n = 3)