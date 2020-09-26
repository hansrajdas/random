class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def height(root, d):
    """Returns height of tree and updates diameter variable."""
    if root is None:
        return 0
    h_left = height(root.left, d)
    h_right = height(root.right, d)
    d[0] = max(d[0], h_left + h_right)
    return 1 + max(h_left, h_right)

def main():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)

  root.left.left = Node(7)
  root.left.right = Node(6)

  root.right.left = Node(5)
  root.right.right = Node(4)
  diameter = [0]  # To make diameter mutable
  # Above tree is
  #       1
  #   2       3
  # 7    6 5      4
  h = height(root, diameter)
  print('Diameter: %d' % diameter[0])  # Diameter: 5


if __name__ == '__main__':
  main()

