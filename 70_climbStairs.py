from math import factorial


class Solution:
    def climbStairsCombinations(self, n: int) -> int:
        res = 0
        for k in range( (n+1) // 2, n):
            res += factorial(n)/factorial(k)/factorial(n-k)
        return res

    def climbStairs(self, n: int) -> int:
        res = 0
        for k in range( (n+1) // 2, n):
            res += factorial(n)/factorial(k)/factorial(n-k)
        return res