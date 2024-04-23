from txt2tree import txt2tree


def dfs(node1, node2, stack):
    if len(node1.children) != len(node2.children):
        stack.append((node1, node2))

    if node1.node_type != node2.node_type or node1.data != node2.data:
        stack.append((node1.data, node2.data))

    for child1, child2 in zip(node1.children, node2.children):
        if not dfs(child1, child2, stack):
            continue

    return stack


def file_diff(ground_truth, pred):
    tree1, tree2 = txt2tree(ground_truth), txt2tree(pred)
    return dfs(tree1, tree2, [])


if __name__ == '__main__':
    file1, file2 = "result_1.txt", "claude_1_attempt_0.txt"
    print(file_diff(file1, file2))
