class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

def lca_bst(root, n1, n2):
    if root is None:
        return None
    if root.key > n1 and root.key > n2:
        return lca_bst(root.left, n1, n2)
    if root.key < n1 and root.key < n2:
        return lca_bst(root.right, n1, n2)
    return root

def main():
  root = Node(10)
  root.left = Node(5)
  root.right = Node(20)

  root.left.left = Node(3)
  root.left.right = Node(7)

  lca = lca_bst(root, 3, 70)
  if lca:
    print('Found, key: %d, id: %d' % (lca.key, id(lca)))
  else:
    print('One of the 2 nodes not found in tree')

main()
