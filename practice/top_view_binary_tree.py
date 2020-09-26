import collections


class Node:
  def __init__(self, k):
    self.k = k
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def insert(self, root, k):
    if root is None:
      return Node(k)

    if root.k > k:
      root.left = self.insert(root.left, k)
    elif root.k < k:
      root.right = self.insert(root.right, k)
    else:
      print('Duplicates not allowed in BST')
      return root

    return root

  def inorder(self, root):
    if root:
      self.inorder(root.left)
      print(root.k)
      self.inorder(root.right)

def top_view(root):
    if not root:
        return None
    Q = collections.deque([(root, 0)])
    d = {}
    while Q:
        node, offset = Q.popleft()
        if offset not in d:
            d[offset] = node.k
        if node.left:
            Q.append((node.left, offset - 1))
        if node.right:
            Q.append((node.right, offset + 1))

    for level in sorted(d.keys()):
        print(d[level], end=' ')


def main():
  bst = BST()
  items = [5, 10, 2, 3, 8, 12, 16]
  for i in items:
    bst.root = bst.insert(bst.root, i)

  print('Inorder traversal...')
  bst.inorder(bst.root)

  print('\nTop view of binary tree...')
  top_view(bst.root)


if __name__ == '__main__':
  main()


# Output:
# -----------
# Inorder traversal...
# 2
# 3
# 5
# 8
# 10
# 12
# 16
#
# Top view of binary tree...
# 2
# 5
# 10
# 12
# 16
