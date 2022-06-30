# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkNode(root, max_val, min_val):
            print(root.val, max_val, min_val)
            if root.left is None and root.right is None:
                return True
            if root.left is None:
                if root.right.val <= root.val:
                    return False
                if max_val is not None and root.right.val >= max_val:
                    return False
                else:
                    if min_val is None:
                        min_val = root.val
                    else:
                        min_val = max(min_val, root.val)
                    return checkNode(root.right, max_val, min_val)
            if root.right is None:
                if root.left.val >= root.val:
                    return False
                if min_val is not None and root.left.val <= min_val:
                    return False
                else:
                    if max_val is None:
                        max_val = root.val
                    else:
                        max_val = min(max_val, root.val)
                    return checkNode(root.left, max_val, min_val)
            if root.right.val <= root.val:
                return False
            if max_val is not None and root.right.val >= max_val:
                return False
            if root.left.val >= root.val:
                return False
            if min_val is not None and root.left.val <= min_val:
                return False
            if max_val is None:
                max_val_n = root.val
            else:
                max_val_n = min(max_val, root.val)
            if min_val is None:
                min_val_n = root.val
            else:
                min_val_n = max(min_val, root.val)
            return checkNode(root.right, max_val, min_val_n) and checkNode(root.left, max_val_n, min_val)
                                                 
        
        def checkNode_fast(root, left, right):
            if root is None:
                return True
            if root.val >= right or root.val <= left:
                return False
            return checkNode_fast(root.left, left, root.val) and checkNode_fast(root.right, root.val, right)

        return checkNode(root, None, None)