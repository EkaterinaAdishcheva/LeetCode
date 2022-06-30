# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check_root(root, p, q):
            if root.val >= p.val and root.val <= q.val:
                return root
            if root.val < p.val:
                return check_root(root.right, p, q)
            return check_root(root.left, p, q)
        [p, q] = [p, q] if p.val < q.val else [q, p]
        
        return check_root(root, p, q)