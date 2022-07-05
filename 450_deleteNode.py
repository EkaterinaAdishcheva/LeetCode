# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def minimum(root):
            if root.left == None:
                return root.val
            else:
                return minimum(root.left)
        
        def delete(root, key):
            if root == None:
                return root
            if root.val == key:
                if root.left == None and root.right == None:
                    return None
                if root.left == None:
                    temp = root.right
                    root = None
                    return temp
                if root.right == None:
                    temp = root.left
                    root = None
                    return temp
                
                root.val = minimum(root.right)
                root.right = delete(root.right, root.val)
                return root

            if root.val > key:
                root.left = delete(root.left, key)
            else:
                root.right = delete(root.right, key)
            return root
        return delete(root,key)