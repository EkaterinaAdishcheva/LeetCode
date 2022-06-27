from typing import List, Optional

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums: List[int], target: int, start: int, end: int):
            if end - start < 1:
                return -1
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < target:
                return binary_search(nums, target, mid + 1, end)
            else:
                return binary_search(nums, target, start, mid)
            return start

        res = binary_search(nums, target, 0, len(nums))
        return res
        
nums = [-1,0,3,5,9,12]
target = 2

solution = Solution()
print(solution.search(nums, target))