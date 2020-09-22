import collections

class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def vertical_level_order_tree_traversal(root):
    if not root:
        return None
    d = {}
    Q = collections.deque()
    Q.append((root, 0))
    while Q:
        node, hd = Q.popleft()
        if hd in d:
            d[hd].append(node.data)
        else:
            d[hd] = [node.data]
        if node.left:
            Q.append((node.left, hd - 1))
        if node.right:
            Q.append((node.right, hd + 1))
    for hd in sorted(d.keys()):
        for node in d[hd]:
            print(node, end=' ')
        print()
            

def main():
    root = Node(1);
    root.left = Node(2);
    root.right = Node(3);

    root.left.left = Node(4);
    root.left.right = Node(5);

    root.left.left.left = Node(6);

    vertical_level_order_tree_traversal(root)


if __name__ == '__main__':
    main()

# Output
# -----------------
# 1 2 3 4 5 6
