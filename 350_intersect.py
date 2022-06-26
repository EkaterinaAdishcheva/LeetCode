class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_s = {}
        for i in range(len(nums1)):
            if nums1[i] in nums1_s:
                nums1_s[nums1[i]] += 1
            else:
                nums1_s[nums1[i]] = 1


        res = []
        for i in range(len(nums2)):
            if nums2[i] in nums1_s and nums1_s[nums2[i]] > 0:
                nums1_s[nums2[i]] -= 1
                res.append(nums2[i])     
        print(res)
        return res
    
solution = Solution()
solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
