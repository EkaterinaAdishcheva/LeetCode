class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sum_position = {}
        for i, n in enumerate(nums):
            if (target - n) in sum_position:
                return [sum_position[target - n], i]
            sum_position[n] = i
        return None

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
