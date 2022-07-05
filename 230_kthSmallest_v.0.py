from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self):
        node_list = []
        level = 0
        def collect_node(pointer, level):
            if len(node_list) < level + 1:
                node_list.append([])
            node_list[level].append(pointer.val)
            if pointer.left:     
                collect_node(pointer.left, level + 1)
            if pointer.right:     
                collect_node(pointer.right, level + 1)
        collect_node(self, 0)
        print(node_list)

def buildTreeNode(l):
    nodes_dict = {}
    for n in range(len(l)):
        print(l[20], l[41])
        if l[n] is not None:
            new_node = TreeNode(l[n])
            nodes_dict[n] = new_node
            if n == 0:
                continue
            if n % 2 == 1:
                print(n)
                nodes_dict[(n - 1) // 2].left = nodes_dict[n]
            if n % 2 == 0:
                print(n)
                nodes_dict[(n - 2) // 2].right = nodes_dict[n]
    return nodes_dict[0]


class Solution:
    def findSmallestNode(root: Optional[TreeNode],  parent_node = {}) -> TreeNode:
        pointer = root
        while pointer and pointer.val:
            current = pointer
            if pointer.left and pointer.left.val:
                parent_node[pointer.left] = pointer
            pointer = pointer.left
        return current

    def findNextNode(node, parent_node):
        if node.right:
            parent_node[node.right] = node
            res = Solution.findSmallestNode(node.right, parent_node)
            return res
        if parent_node[node].left == node:
            return parent_node[node]
        else:
            pointer = node
            while pointer in parent_node:
                if parent_node[pointer].right == pointer:
                    pointer = parent_node[pointer]
                else:
                    return parent_node[pointer]
            else:
                return None


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        parent_node = {}
        nextNode = Solution.findSmallestNode(root, parent_node)
        nextNode.display()
        if k == 1:
            return nextNode.val 
        for i in range(k - 1):
            nextNode = Solution.findNextNode(nextNode, parent_node)
            nextNode.display()
        return nextNode.val

solution = Solution()
root_list = [
41,
37, 44,
24, 39, 42, 48,
1,  35, 38, 40, None,   43,     46,     49,
0,  2,  30,     36,     None,   None,   None,   None,   None,   None,   45,     47,     None,None,  None,   None,
None,   4,      29,     32,     None,   None,   None,   None,   None,   None,   3,      9,  26,     None,   31,  34,     None,   None,   7,  11,     25,     27,     None,   None,   33,     None,   6,  8,  10,     16,
None,None,None,28,None,None,5,None,None,None,None,None,15,19,None,None,None,None,12,None,18,20,None,13,17,None,None,22,None,14,None,None,21,23]
k = 25
root = buildTreeNode(root_list)
root.display()

print(solution.kthSmallest(root, k))
