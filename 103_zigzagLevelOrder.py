from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        root_levels = {}
        def saveNode(root, level):
            if root is None:
                return
            if level not in root_levels:
                root_levels[level] = []
            root_levels[level].append(root.val)
            saveNode(root.left, level + 1)
            saveNode(root.right, level + 1)

        saveNode(root, 0)
        res = []
        print(root_levels)
        for i in range(len(list(root_levels.keys()))):
            if i % 2 == 0:
                res.append(root_levels[i])
            else:
                res.append(list(reversed(root_levels[i])))
        
        return res

solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root = TreeNode(0, TreeNode(2, TreeNode(1, TreeNode(5), TreeNode(1)), None), TreeNode(4, TreeNode(3, None, TreeNode(6)),
TreeNode(-1, None, TreeNode(8))))

print(solution.zigzagLevelOrder(root))
