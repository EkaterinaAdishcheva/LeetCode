def isBadVersion(version: int) -> bool:
    return (version >= 4)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binary_serach(start, end):
            if end - start < 1:
                return start
            mid = ( start + end ) // 2
            if isBadVersion(mid):
                return binary_serach(start, mid)
            else:
                return binary_serach(mid + 1, end)

        return binary_serach(0 , n)

n = 5
solution = Solution()
print(solution.firstBadVersion(n))