
class Node:
  """Initialises a new tree node."""
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

def check_symmetric(left, right):
    if left is None and right is None:
        return True
    if (left is None and right is not None) or (left is not None and right is None):
        return False
    if left.data != right.data:
        return False
    return check_symmetric(left.left, right.right) and check_symmetric(left.right, right.left)

def is_tree_symmetric(root):
    if not root:
        return True
    return check_symmetric(root.left, root.right)

def main():
  ## Case 1
  t = Tree()
  t.root = Node(10)
  t.root.left = Node(5)
  t.root.right = Node(5)
  t.root.left.left = Node(1)
  t.root.right.right = Node(1)
  t.root.left.right = Node(2)
  t.root.right.left = Node(2)

  print(is_tree_symmetric(t.root))  # True

  ## Case 2
  t = Tree()
  t.root = Node(10)
  t.root.left = Node(5)
  t.root.right = Node(5)
  t.root.left.left = Node(1)
  t.root.right.right = Node(1)
  t.root.left.right = Node(2)

  print(is_tree_symmetric(t.root))  # False

if __name__ == '__main__':
  main()
