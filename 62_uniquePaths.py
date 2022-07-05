from math import factorial
RIGHT = "0"
DOWN = "1"

class Solution:
    def uniquePathsAnalitics(self, m: int, n: int) -> int:
        return factorial(n + m - 2)/factorial(m -1)/factorial(n- 1)

    def uniquePathsList(self, m: int, n: int) -> int:
        def findPath(m, n):
            paths = []
            if 0 == m:
                path = [RIGHT for j in range(n)]
                paths.append(path)
                return paths
            if 0 == n:
                path = [RIGHT for j in range(m)]
                paths.append(path)
                return paths
            for i in range(m + 1):
                path = [RIGHT for j in range(i)]
                path.append(DOWN)
                rest = findPath(m - i, n - 1)
                for r in rest:
                    path.extend(r)
                    paths.append(path)
            return paths

    def calculatePathsCount(self, m: int, n: int) -> int:
        def findPath(m, n):
            if 0 == m:
                return 1
            if 0 == n:
                return 1
            res = 0
            for i in range(m + 1):
                rest = findPath(m - i, n - 1)
                res += rest
            return res

        res = findPath(m - 1, n - 1)
        return res

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]    

solution = Solution()
print(solution.calculatePaths(7, 3))