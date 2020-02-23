# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return '-'
        return ' '.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())
        
        def dsrl():
            val = next(vals)
            if val == '-': return None
            root = TreeNode(val)
            root.left = dsrl()
            root.right = dsrl()
            return root
        
        return dsrl()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
