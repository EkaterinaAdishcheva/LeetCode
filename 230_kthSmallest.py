from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraverse(root, nodes, steps):
            if len(nodes) == steps:
                return
            if root.left:
                if len(nodes) < steps:
                    inorderTraverse(root.left, nodes, steps)
                else:
                    return
            nodes.append(root.val)
            if root.right:
                if len(nodes) < steps:
                    inorderTraverse(root.right, nodes, steps)
                else:
                    return
        nodes = []
        steps = k
        inorderTraverse(root, nodes, steps)

        return nodes[k-1]
        

