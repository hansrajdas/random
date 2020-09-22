class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def main():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)

  root.left.left = Node(7)
  root.left.right = Node(6)

  root.right.left = Node(5)
  root.right.right = Node(4)
  # Above tree is
  #       1
  #   2       3
  # 7    6 5      4
  print_spiral_order(root)  # 1 2 3 4 5 6 7


def print_spiral_order(root):
    if not root:
        return None
    s1 = [root]
    s2 = []
    while s1 or s2:
        while s1:
            node = s1.pop()
            print(node.data, end=' ')
            if node.right:
                s2.append(node.right)
            if node.left:
                s2.append(node.left)
        print()
        while s2:
            node = s2.pop()
            print(node.data, end=' ')
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        print()


if __name__ == '__main__':
  main()
