class Node(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def insert(self, d):
        if self.data == d:
            return False
        elif d < self.data:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True

    def find(self, d):
        if self.data == d:
            return True
        elif d < self.data and self.left:
            return self.left.find(d)
        elif d > self.data and self.right:
            return self.right.find(d)
        return False

    def preorder(self, l):
        l.append(self.data)
        if self.left:
            self.left.preorder(l)
        if self.right:
            self.right.preorder(l)
        return l

    def postorder(self, l):
        if self.left:
            self.left.postorder(l)
        if self.right:
            self.right.postorder(l)
        l.append(self.data)
        return l

    def inorder(self, l):
        if self.left:
            self.left.inorder(l)
        l.append(self.data)
        if self.right:
            self.right.inorder(l)
        return l

# class Node:
#
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
#         self.ans = 0
#
#     def insert(self, data):
#         if data < self.data:
#             if self.left is None:
#                 self.left = Node(data)
#             else:
#                 self.left.insert(data)
#         elif data > self.data:
#             if self.right is None:
#                 self.right = Node(data)
#             else:
#                 self.right.insert(data)
#         else:
#             print "Data already in tree"
#
#     def search(self, value):
#         if value < self.data:
#             if self.left is None:
#                 return False
#             return self.left.search(value)
#         elif value > self.data:
#             if self.right is None:
#                 return False
#             return self.right.search(value)
#         else:
#             return True
#
#     def printTree(self):
#         if self.left:
#             self.left.printTree()
#         print self.data
#         if self.right:
#             self.right.printTree()
#
#     def sizeTree(self):
#         if self is None:
#             return 0
#         size_of_tree = 1
#         if self.left:
#             size_of_tree = size_of_tree + self.left.sizeTree()
#         if self.right:
#             size_of_tree = size_of_tree + self.right.sizeTree()
#         return size_of_tree
#
#     def minValue(self):
#         if self.left is None:
#             return self.data
#         return self.left.minValue()

def rangeSum(root, L, R):
    def dfs(node):
        if node:
            if L <= node.data <= R:
                root.ans += node.data
            if L < node.data:
                dfs(node.left)
            if node.data < R:
                dfs(node.right)
    dfs(root)
    return root.ans
        


def sameTree(Tree, anotherTree):
    if Tree is None and anotherTree is None:
        return True
    elif Tree and anotherTree:
        return Tree.data == anotherTree.data and sameTree(Tree.left, anotherTree.left) and sameTree(Tree.right, anotherTree.right)
    else:
        return False


def main():
    root = Node(10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)
    root.insert(0)
    root.insert(18)
    root.printTree()
    #print root.minValue()
    print rangeSum(root, 7, 15)

    
#    print 'Size of tree - {}'.format(root.sizeTree())
#    root1 = Node(12)
#    print 'Size of tree - {}'.format(root1.sizeTree())

#    if sameTree(root, root1):
#        print 'Two trees are same'
#    else:
#        print 'Not same'


main()
