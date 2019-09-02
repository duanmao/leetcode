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
        vals = []
        
        def postorder(node):
            if (not node): return
            postorder(node.left)
            postorder(node.right)
            vals.append(str(node.val))
        
        postorder(root)
        return " ".join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = [int(x) for x in data.split()]
        
        def build(low, high):
            if (vals and low < vals[-1] < high):
                val = vals.pop()
                print(val)
                root = TreeNode(val)
                root.right = build(val, high)
                root.left = build(low, val)
                return root
            else:
                return None
        
        return build(float('-inf'), float('inf'))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
