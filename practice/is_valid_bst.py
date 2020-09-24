class Node:
  """Initialises a new tree node."""
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BST:
  """Manages BST."""
  def __init__(self):
    """Initialises a new BST."""
    self.root = None

  def insert(self, root, data):
    if not root:
      return Node(data)
    elif data < root.data:
      root.left = self.insert(root.left, data)
    elif data > root.data:
      root.right = self.insert(root.right, data)
    else:
      print('Duplicate node - %d' % data)
    return root

def is_valid_bst_utils(root, _min, _max):
    if root is None:
        return True
    if root.data < _min or root.data > _max:
        return False
    return is_valid_bst_utils(root.left, _min, root.data) and is_valid_bst_utils(root.right, root.data, _max)

def is_valid_bst(root):
    return is_valid_bst_utils(root, float('-Inf'), float('Inf'))

def main():
  # Valid BST
  valid = BST()
  valid.root = valid.insert(valid.root, 10)
  valid.root = valid.insert(valid.root, 5)
  valid.root = valid.insert(valid.root, 20)
  valid.root = valid.insert(valid.root, 4)
  valid.root = valid.insert(valid.root, 7)
  valid.root = valid.insert(valid.root, 15)
  valid.root = valid.insert(valid.root, 25)
  valid.root = valid.insert(valid.root, 30)

  print(is_valid_bst(valid.root))  # True

  # Invalid BST
  invalid = BST()
  invalid.root = Node(10)
  invalid.root.left = Node(5)
  invalid.root.right = Node(20)
  invalid.root.left.left = Node(3)
  # This value is not correct, all nodes in left sub tree should be less than
  # root - 10
  invalid.root.left.right = Node(12)

  print(is_valid_bst(invalid.root))  # False


if __name__ == '__main__':
  main()
