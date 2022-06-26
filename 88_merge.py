class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        if 0 == n:
            print(nums1)
            return
        if 0 == m:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        i, j = 0, 0
        while i < m or j < n:
            print(i, j, m, n, nums1, nums2)
            if m == i:
                print(list(range(j, n)))
                for k in (range(j, n)):
                    print(k, i + k - j)
                    nums1[i + k - j] = nums2[k]
                break
            if n == j:
                break
            if nums2[j] < nums1[i]:
                for k in reversed(range(i + 1, m + 1)):
                    nums1[k] = nums1[k - 1]
                nums1[i] = nums2[j]
                j += 1
                i += 1
                m += 1
                continue
            i += 1    
        return


solution = Solution()
print(solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))