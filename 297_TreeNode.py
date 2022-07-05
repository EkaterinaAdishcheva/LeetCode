# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        nodes = {}

        def select_nodes(node, num):
            if node is None:
                return
            nodes[num] = node
            if node.left:
                select_nodes(node.left, 2 * num + 1)
            if node.right:
                select_nodes(node.right, 2 * num + 2)

        if root is None:
            return ''

        
        select_nodes(root, 0)
        nodes_list_ind = list(nodes.keys())

        res = []
        for i in range(max(nodes_list_ind) + 1):
            if i in nodes:
                res.append(str(nodes[i].val))
            else:
                res.append('null')
        res = ','.join(res)
        return res

    def deserialize(self, data):
        r_list = data.split(",")
        if len(r_list) == 0:
            return None
        
        nodes = {}

        for i in range(len(r_list)):
            if r_list[i] != 'null':
                new_node = TreeNode(int(r_list[i]))
                nodes[i] = new_node
                if i > 0:
                    if i % 2 == 1:
                        nodes[(i - 1) / 2].left = new_node
                    else:
                        nodes[(i - 2) / 2].right = new_node
        return nodes[0]           


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))