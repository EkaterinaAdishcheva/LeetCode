from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def recursion(pos: int, root: Optional[TreeNode]):
            print(root.val, pos, res)
            if root is None:
                return
            if len(res) < pos + 1:
                res.append([])
            res[pos].append(root.val)
            if root.left is not None:
                recursion(pos + 1, root.left)
            if root.right is not None:
                recursion(pos + 1, root.right)
        
        if root is None:
            return []
        
        res = []
        recursion(0, root)
        return res


root = TreeNode(3,TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
print(solution.levelOrder(root))
