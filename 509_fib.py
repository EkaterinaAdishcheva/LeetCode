class Solution:
    def fib(self, n: int) -> int:
        def fibRecursion(n):
            if n < 2:
                return n
            return fibRecursion(n - 1) + fibRecursion(n - 2)

        res = fibRecursion(n)
        return res

        