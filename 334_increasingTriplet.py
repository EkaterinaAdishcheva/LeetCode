class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        j, k = None, len(nums) - 1
        k_new = None
        for p in range(k - 1, -1, -1):
            if j is None and nums[p] < nums[k]:
                j = p
                continue
            if j is None and nums[p] >= nums[k]:
                k = p
                continue
            if nums[p] < nums[j]:
                i = p
                return True
            if nums[p] > nums[j] and nums[p] < nums[k]:
                j = p
                continue
            if k_new is None and nums[p] > nums[k]:
                k_new = p
            if k_new is not None and nums[p] > nums[j] and nums[p] < nums[k_new]:
                k = k_new
                j = p
                continue
            if k_new is not None and nums[p] > nums[k_new]:
                k_new = p
                continue
        return False
        
solution = Solution()

nums = [4,5,2147483647,1,2]
print(solution.increasingTriplet(nums))

print(2147483647 > 2)