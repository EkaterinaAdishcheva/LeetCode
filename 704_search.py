from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]:
            return -1

        step = len(nums)
        start = 0

        if step == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while True:
            step = (step + 1) // 2
            if step >= 2:
                if nums[start + step] < target:
                    start = start + step
                elif nums[start + step] == target:
                    return start + step
            else:
                if nums[start] == target:
                    return start
                if nums[start + 1] == target:
                    return start + 1
                else:
                    return -1
        
        return start
                    

nums = [-1, 0, 5]
target = 5

solution = Solution()
print(solution.search(nums, target))