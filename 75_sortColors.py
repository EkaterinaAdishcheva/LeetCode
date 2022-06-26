class Solution:
    def sortColors(self, nums: list[int]) -> None:
        MAX = 2
        """
        Do not return anything, modify nums in-place instead.
        """
        color_qnt = [0, 0, 0]
        for elem in nums:
            color_qnt[elem] += 1
            if elem == MAX:
                continue
            shift = 0
            for i in range(MAX + 1):
                if 0 < color_qnt[i]:
                    nums[color_qnt[i] - 1 + shift] = i
                    shift += color_qnt[i]
        
        return nums

solution = Solution()
print(solution.sortColors([1]))

