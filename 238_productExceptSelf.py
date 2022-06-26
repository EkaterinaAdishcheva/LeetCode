class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zero_qnt = 0
        zero_pos = None
        prod = 1
        for num in range(len(nums)):
            if 0 == nums[num]:
                zero_qnt += 1
                if 2 == zero_qnt:
                    break
                zero_pos = num
            else:
                prod *= nums[num]
        
        res = []

        if 2 == zero_qnt:
            res = [0 for x in range(len(nums))]
            return res

        if 1 == zero_qnt:
            res = [0 for x in range(zero_pos)]
            res.append(prod)
            res.extend([0 for x in range(len(nums) - zero_pos - 1)])
            return res
        res = [prod // x for x in nums]
        return res

solution = Solution()
nums = [-1,1,0,-3,3]
print(solution.productExceptSelf(nums))