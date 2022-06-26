class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []
        intervals.sort()
        i_0 = intervals[0]
        for i_1 in intervals[1:]:
            if i_0[1] >= i_1[0]:
                i_0[1] = i_1[1] if i_1[1] >= i_0[1] else i_0[1]
            else:
                res.append(i_0)
                i_0 = i_1
        res.append(i_0)

        return res


solution = Solution()
solution.merge([[1,4],[4,5]])