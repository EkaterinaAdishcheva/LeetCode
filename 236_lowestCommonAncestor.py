# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x, nl=None, nr=None):
        self.val = x
        self.left = nl
        self.right = nr

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root_edges = {}
        if root is None:
            return None 
        nodes = [root]
        root_edges[root] = None
        start = 0
        specific_nodes = []
        if root in [p, q]:
            specific_nodes.append(root)

        while len(specific_nodes) < 2:
            new_start = len(nodes)
            for node in nodes[start:]:
                if node.left:
                    root_edges[node.left] = node
                    nodes.append(node.left)
                    if node.left.val in [p, q]:
                        specific_nodes.append(node.left)
                        if len(specific_nodes) == 2:
                            break
                if node.right:
                    root_edges[node.right] = node
                    nodes.append(node.right)
                    if node.right.val in [p, q]:
                        specific_nodes.append(node.right)
                        if len(specific_nodes) == 2:
                            break
            start = new_start

        print(specific_nodes, ancestor, pointer)
        print(root_edges)
        ancestor = [[specific_nodes[0]],[specific_nodes[1]]]
        pointer = specific_nodes
        add_new_node_ind = True
        while add_new_node_ind:
            add_new_node_ind = False
            if pointer[1] in ancestor[0]:
                return  pointer[1]
            if pointer[0] in ancestor[1]:
                return  pointer[0]
            if root_edges[pointer[1]] is not None:    
                pointer[1] = root_edges[pointer[1]]
                if pointer[1] in ancestor[0]:
                    return  pointer[1]
                ancestor[1].append(pointer[1])
                add_new_node_ind = True
            if root_edges[pointer[0]] is not None:    
                pointer[0] = root_edges[pointer[0]]
                if pointer[0] in ancestor[1]:
                    return  pointer[0]
                ancestor[0].append(pointer[0])
                add_new_node_ind = True
            if not add_new_node_ind:
                return None

solution = Solution()
root = TreeNode(1, None, TreeNode(2))
print(solution.lowestCommonAncestor(root, 1, 2))