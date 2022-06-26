class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sum_stat = {}
        current_sum = nums[0]
        sum_stat[current_sum] = 1
        
        for el in nums[1:]:
            current_sum += el
            if current_sum in sum_stat:
                sum_stat[current_sum] += 1
            else:
                sum_stat[current_sum] = 1

        part_sum = 0
        res = 0
        for el in nums:
            if k + part_sum in sum_stat: 
                res += sum_stat[k + part_sum]
            part_sum += el
            sum_stat[part_sum] -= 1

        return res

solution = Solution()
nums = [1, 2, 3]
k = 3
print(solution.subarraySum(nums, k))
