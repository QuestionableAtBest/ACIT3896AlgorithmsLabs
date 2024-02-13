
class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        self.parent = None
        self.children = []
      
    def __repr__(self):
        # this is a mediocre repr function, it's not very good at all, but it'll do for now
        return f"TreeNode('{self.contents}')"

    def addAsLastChild(self, contents):
        # should create a new node and add it as a child of the current node, AFTER any existing nodes
        new_node = TreeNode(contents)
        new_node.parent = self
        self.children.append(new_node)
        return new_node

    def addAsFirstChild(self, contents):
        # should create a new node and add it as a child of the current node, BEFORE any existing nodes
        new_node = TreeNode(contents)
        new_node.parent = self
        self.children.insert(0,new_node)
        return new_node

    def findRoot(self):
        # returns the root of the tree that the current node is in (note that current node might be root)
        if self.parent == None:
            return self
        else:
            return self.parent.findRoot()

    def findLeftmostDescendant(self):
        # a "descendant" is a child, or a child-of-child, or child-of-child-of-child, etc
        # this one should travel only down the left edge of the tree, as far as it can
        if self.children == []:
            return self
        else:
            return self.children[0].findLeftmostDescendant()


def case1():
    # This is supposed to make this tree:
    #
    #            A
    #         /  |  \
    #        B   C   D
    root = TreeNode("A")
    root.addAsLastChild("B")
    root.addAsLastChild("C")
    root.addAsLastChild("D")


def case2():
    # This is supposed to make the same tree as last time, but differently:
    #
    #            A
    #         /  |  \
    #        B   C   D
    root = TreeNode("A")
    root.addAsLastChild("C")
    root.addAsLastChild("D")
    root.addAsFirstChild("B")

def case3():
    # This is supposed to make this tree:
    #
    #            A
    #         /  |  \
    #        B   C   D
    #        |      / \
    #        E     F   G
    root = TreeNode("A")
    c = root.addAsLastChild("C")
    d = root.addAsLastChild("D")
    b = root.addAsFirstChild("B")
    f = d.addAsLastChild("F")
    g = d.addAsLastChild("G")
    e = b.addAsLastChild("E")
    # and all of the following should print the root node (each one prints itself and then the root):
    for node in [root, b, c, d, e, f, g]:
        print(node, node.findRoot())
    # and the following should be able to find E:
    print("leftDescendant of root:", root.findLeftmostDescendant())
    # and the following should be able to find F:
    print("leftDescendant of D:", d.findLeftmostDescendant())



def main(args):
    case1()
    case2()
    case3()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])