class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def postorder(root):
    # left > right > node
    import collections
    stack = []
    node = root
    while True:
        while node:
            stack.append(node)
            stack.append(node)
            node = node.left

        if not stack:
            break
        node = stack.pop()
        if stack and stack[-1].data == node.data:
            node = node.right
        else:
            print(node.data, end=' ')
            node = None
    print()


def main():
  root = Node(10)
  root.left = Node(5)
  root.left.left = Node(3)
  root.left.right = Node(8)

  root.right = Node(15)
  root.right.left = Node(12)
  root.right.right = Node(18)

  postorder(root)

if __name__ == '__main__':
  main()
