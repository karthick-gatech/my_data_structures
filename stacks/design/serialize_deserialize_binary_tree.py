class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# The preorder DFS traverse follows recursively the order of
# root -> left subtree -> right subtree.

# 1,2,3,None,None,4,None,None,5,None,None,


class Codec:

    def serialize(self, root):
        if not root:
            return 'x'
        return root.val, self.serialize(root.left), self.serialize(root.right)

    def deserialize(self, data):
        if data[0] == 'x':
            return None
        node = TreeNode(data[0])
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])
        return node
