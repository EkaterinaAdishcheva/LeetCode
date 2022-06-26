class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum_nums = nums[:1]
        for m in range(1, len(nums)):
            sum_nums.append(sum_nums[-1] + nums[m])
        return sum_nums