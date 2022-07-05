from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self):
        if self is not None:
            right, left = None, None
            if self.right:
                self.right.display()
                right = self.right.val
            if self.left:
                left = self.left.val
                self.left.display()
            print(self.val, left, right)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(head, nums):
            if len(nums) == 0:
                return
            if head is None:
                head = TreeNode(nums[len(nums) // 2])
            head.left = buildBST(head.left, nums[:len(nums) // 2])
            head.right = buildBST(head.right, nums[len(nums) // 2 + 1:])
            return head

        head = None
        head = buildBST(head, nums)
        return head

solution = Solution()
nums = [-10,-3,0,5,9]
head = solution.sortedArrayToBST(nums)
head.display()
