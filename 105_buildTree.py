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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTreeRecursion(head, preorder, inorder):
            if preorder == []:
                return
            print(preorder, inorder)
            head = TreeNode(preorder[0])
            num = inorder.index(preorder[0])
            head.left = buildTreeRecursion(head.left, preorder[1: num+1], inorder[:num])
            head.right = buildTreeRecursion(head.right, preorder[num+1:], inorder[num+1:])
            return head

        head = None
        head = buildTreeRecursion(head, preorder, inorder)
        return head
    
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

solution = Solution()
tree = solution.buildTree(preorder, inorder)
tree.display()