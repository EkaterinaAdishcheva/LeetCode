# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> list[int]:
        def recursion(root: Node):
            if root is None:
                return []
            res = []
            res.append(root.val)
            if root.children is None:
                return res
            for child in root.children:
                res_ = recursion(child)
                res.extend(res_)
            return res

        return recursion(root)       


root = Node(1,[Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
solution = Solution()
print(solution.preorder(root))