class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    node = root
    stack = []
    while True:
        while node:
            stack.append(node)
            node = node.left

        if not stack:
            break
        node = stack.pop()
        print(node.data, end=' ')

        node = node.right
    print()

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    inorder(root)

    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(8)

    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)

    inorder(root)  # 3 5 8 10 12 15 18

    inorder(None)
main()
