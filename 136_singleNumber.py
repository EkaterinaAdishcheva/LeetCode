class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums_stat = set()
        for n in nums:
            if n in nums_stat:
                nums_stat.remove(n)
            else:
                nums_stat.add(n)
        return list(nums_stat)[0]

