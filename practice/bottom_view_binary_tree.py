import collections

class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None

def bottom_view(root):
    if not root:
        return None
    q = collections.deque([(root, 0)])
    d = {}
    while q:
        node, vd = q.popleft()
        d[vd] = node.k
        if node.left:
            q.append((node.left, vd - 1))
        if node.right:
            q.append((node.right, vd + 1))
    for vd in sorted(d.keys()):
        print(d[vd], end=' ')

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.right.right = Node(5)

    root.left.right = Node(6)
    root.right.left = Node(7)

    bottom_view(root)

if __name__ == '__main__':
    main()
