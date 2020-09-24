class Node:
  """Initialises a new tree node."""
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def inorder(self, root):
    if root:
      self.inorder(root.left)
      print(root.data, end=' ')
      self.inorder(root.right)

def find_mirror_image(root):
    if not root:
        return None
    find_mirror_image(root.left)
    find_mirror_image(root.right)
    root.left, root.right = root.right, root.left

def main():
  t = Tree()
  t.root = Node(1)
  t.root.left = Node(2)
  t.root.right = Node(3)
  t.root.left.left = Node(4)
  t.root.right.right = Node(5)
  t.root.left.right = Node(6)
  t.root.right.left = Node(7)

  print('Inorder traversal of tree: ')
  t.inorder(t.root)  # 4 2 6 1 7 3 5

  find_mirror_image(t.root)
  
  print ('\nMirror image of above tree: ')
  t.inorder(t.root)  # 5 3 7 1 6 2 4


if __name__ == '__main__':
  main()
