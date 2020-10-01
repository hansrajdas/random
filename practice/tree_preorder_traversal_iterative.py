class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preorder(root):
    # node > left > right
    stack = []
    node = root
    while True:
        while node:
            stack.append(node)
            print(node.data, end=' ')
            node = node.left

        if not stack:
            break
        node = stack.pop()
        node = node.right
    print()

def main():
  root = Node(10)
  root.left = Node(5)
  root.left.left = Node(3)
  root.left.right = Node(8)

  root.right = Node(15)
  root.right.left = Node(12)
  root.right.right = Node(18)

  preorder(root)  # 10 5 3 8 15 12 18

if __name__ == '__main__':
  main()
