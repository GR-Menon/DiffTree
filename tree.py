class TreeNode(object):
    def __init__(self, data=None, node_type=None):
        self.node_type = node_type
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_depth(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_depth()
        prefix = spaces + f"{self.get_depth()}- " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
