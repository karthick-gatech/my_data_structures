# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node
# to any node in the tree along the parent-child connections. The path must contain at
# least one node and does not need to go through the root.
#
# Input: [-10,9,20,null,null,15,7]
# Output: 42 (20 + 15 + 7)


class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    max_sum = float('-inf')
    def max_gain(node):
        if not node:
            return 0

        # max sum on the left and right sub-trees of node
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        # the price to start a new path where `node` is a highest node
        price_newpath = node.val + left_gain + right_gain

        # update max_sum if it's better to start a new path
        max_sum = max(max_sum, price_newpath)

        # for recursion :
        # return the max gain if continue the same path
        return node.val + max(left_gain, right_gain)


    max_gain(root)
    return max_sum


class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum

    def dfs(self, node):
        if not node:
            return 0

        # only add positive contributions
        leftST_sum = max(0, self.dfs(node.left))
        rightST_sum = max(0, self.dfs(node.right))

        # check if cumulative sum at current node > global max sum so far
        # this evaluates a candidate path
        self.max_sum = max(self.max_sum, leftST_sum + rightST_sum + node.val)

        # add to the current node ONLY one of the children contributions
        # in order to maintain the constraint of considering only paths
        # if not, we would be exploring explore the whole tree - against problem definition
        return max(leftST_sum, rightST_sum) + node.val
