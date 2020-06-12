class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            print "Data already in tree"

    def search(self, value):
        if value < self.data:
            if self.left is None:
                return False
            return self.left.search(value)
        elif value > self.data:
            if self.right is None:
                return False
            return self.right.search(value)
        else:
            return True

    def printTree(self):
        if self.left:
            self.left.printTree()
        print self.data
        if self.right:
            self.right.printTree()

    def sizeTree(self):
        if self is None:
            return 0
        size_of_tree = 1
        if self.left:
            size_of_tree = size_of_tree + self.left.sizeTree()
        if self.right:
            size_of_tree = size_of_tree + self.right.sizeTree()
        return size_of_tree

    def minValue(self):
        if self.left is None:
            return self.data
        return self.left.minValue()


def sameTree(Tree, anotherTree):
    if Tree is None and anotherTree is None:
        return True
    elif Tree and anotherTree:
        return Tree.data == anotherTree.data and sameTree(Tree.left, anotherTree.left) and sameTree(Tree.right, anotherTree.right)
    else:
        return False


def main():
    root = Node(12)
    root.insert(6)
    root.insert(80)
    root.insert(180)
    root.insert(360)
    root.insert(120)
    #root.printTree()
    print root.minValue()

    print 'Size of tree - {}'.format(root.sizeTree())
    root1 = Node(12)
    print 'Size of tree - {}'.format(root1.sizeTree())

    if sameTree(root, root1):
        print 'Two trees are same'
    else:
        print 'Not same'


main()
