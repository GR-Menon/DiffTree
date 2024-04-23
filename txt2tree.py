from tree import TreeNode


def txt2tree(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    lines = text.strip().split("\n")
    root = TreeNode("start")
    stack = [(0, root)]

    for line in lines:
        tokens = line.split(' - ')

        depth = len(tokens[0].split('.'))
        node_type = tokens[1]
        data = tokens[2]

        node = TreeNode(data, node_type)
        while stack[-1][0] >= depth:
            stack.pop()

        stack[-1][1].add_child(node)
        stack.append((depth, node))
    return root


if __name__ == "__main__":
    file_path = "result_1.txt"
    root = txt2tree(file_path)
    root.print_tree()
