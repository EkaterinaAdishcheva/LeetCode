class Solution:
    def maxSubArray1(self, nums: list[int]) -> int:
        nums_sum = [[0] * len(nums) for i in range(len(nums))]
        for num, elem in enumerate(nums):
            for i in range(num + 1):
                for j in range(num, len(nums)):
                    nums_sum[i][j] += elem
        nums_sum_flat = [x for n, xs in enumerate(nums_sum) for x in xs[n:]]
        nums_sum_max = max(nums_sum_flat)
        print(nums_sum_flat)
        return nums_sum_max

    def maxSubArray2(self, nums: list[int]) -> int:
        nums_sum = [[0] * len(nums) for i in range(len(nums))]
        for start in range(len(nums)):
            nums_sum[start][start] = nums[start]
            for end in range(start + 1, len(nums)):
                nums_sum[start][end] = nums_sum[start][end - 1] + nums[end]
        nums_sum_flat = [x for n, xs in enumerate(nums_sum) for x in xs[n:]]
        nums_sum_max = max(nums_sum_flat)
        print(nums_sum_flat)
        return nums_sum_max


    def maxSubArray(self, nums: list[int]) -> int:
        nums_sum_max = nums[0]
        nums_sum_current = nums[0]
        end = 0
        for end in range(1, len(nums)):
            if nums_sum_current < 0:
                nums_sum_current = nums[end]
            else:
                nums_sum_current = nums_sum_current + nums[end]
            if nums_sum_current > nums_sum_max:
                nums_sum_max = nums_sum_current            

        return nums_sum_max


solution = Solution()
print(solution.maxSubArray([5,4,-1,7,8]))


