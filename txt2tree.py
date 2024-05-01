def txt2tree(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    lines = text.strip().split("\n")
    tree = {}

    for line in lines:
        tokens = line.split(" - ")
        tree[tokens[0]] = (tokens[1], tokens[2])

    return tree


if __name__ == "__main__":
    file_path = "gtm_test.txt"
    tree_dict = txt2tree(file_path)
    print(tree_dict)
