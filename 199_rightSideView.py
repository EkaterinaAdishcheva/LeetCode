# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        tree_level = []
        def levelTreeNode(root, level):
            if root is None:
                return
            if len(tree_level) < level + 1:
                tree_level.append([])
            tree_level[level].append(root.val)
            if root.left:
                levelTreeNode(root.left, level + 1)
            if root.right:
                levelTreeNode(root.right, level + 1)
            
        levelTreeNode(root, 0)
        res = []
        for nodes in tree_level:
            res.append(nodes[-1])
        
        return res        