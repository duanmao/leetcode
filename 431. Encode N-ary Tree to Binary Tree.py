"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
# Time: O(n), space: O(H), H is the height of the n-ary tree
class Codec:

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root: return None
        bNode = TreeNode(root.val)
        first = None
        for c in root.children:
            node = self.encode(c)
            if c == root.children[0]:
                first = pre = node
            else:
                pre.right = node
                pre = node
        bNode.left = first
        return bNode
        
    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data: return None
        nNode = Node(data.val, [])
        bNode = data.left
        while bNode:
            nNode.children.append(self.decode(bNode))
            bNode = bNode.right
        return nNode

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
