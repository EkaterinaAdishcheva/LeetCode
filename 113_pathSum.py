from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        res = []
        def checkSum(root, path, target):
            path_c = path.copy()
            path_c.append(root.val)
            if root.left is not None:
                checkSum(root.left, path_c, target)
            if root.right is not None:
                checkSum(root.right, path_c, target)
            if root.left is None and root.right is None:
                if sum(path_c) == target:
                    res.append(path_c)
                return

        path = []
        checkSum(root, path, targetSum)
        return(res)  
   

solution = Solution()

def buildTreeNodeFromList(l):
    nodes = {}
    tree = TreeNode(l[0])
    nodes[0] = tree
    for i in range(1, len(l)):
        nodes[i] = TreeNode(l[i])
        if i % 2 == 1:
            nodes[(i - 1) / 2].left = nodes[i]
        else:
            nodes[(i - 2) / 2].right = nodes[i]
        
    return nodes[0]


targetSum = 22
root_list = [5,4,8,11,None,13,4,7,2,None,None,5,1]
root = buildTreeNodeFromList(root_list)
print(solution.pathSum(root, targetSum))