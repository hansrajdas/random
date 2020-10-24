class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None

def lca_utils(root, n1, n2, found):
    if root is None:
        return None
    if root.k == n1:
        found[n1] = True
        return root
    if root.k == n2:
        found[n2] = True
        return root
    lca_left = lca_utils(root.left, n1, n2, found)
    lca_right = lca_utils(root.right, n1, n2, found)

    if lca_left and lca_right:
        return root
    if lca_left is None:
        return lca_right
    return lca_left

def find(root, n):
    if root is None:
        return False
    if root.k == n or find(root.left, n) or find(root.right, n):
        return True
    return False

def get_lca(root, n1, n2):
    found = {n1: False, n2: False}
    lca = lca_utils(root, n1, n2, found)

    if (found[n1] and found[n2]) or (found[n1] and find(lca, n2)) or (found[n2] and find(root, n1)):
        return lca
    return None

def main():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)

  root.left.left = Node(4)
  root.left.right = Node(5)

  root.right.left = Node(6)
  root.right.right = Node(7)

  lca = get_lca(root, 4, 7)
  if lca:
    print(lca.k)
  else:
    print('na')

  # Round-2
  lca = get_lca_2(root, 4, 7)
  if lca:
    print(lca.k)
  else:
    print('na')


# Round-2
def get_lca_2(root, n1, n2):
    found = {n1: False, n2: False}
    lca = get_lca_utils(root, n1, n2, found)

    if (found[n1] and found[n2]) or (found[n1] and find(lca, n2)) or (found[n2] and find(lca, n1)):
        return lca
    return None

def get_lca_utils(root, n1, n2, found):
    if root is None:
        return None
    if root.k == n1 or root.k == n2:
        found[root.k] = True
        return root

    lca_left = get_lca_utils(root.left, n1, n2, found)
    lca_right = get_lca_utils(root.right, n1, n2, found)

    if lca_left and lca_right:
        return root
    return lca_left if lca_left else lca_right

def find(root, n):
    if root is None:
        return False
    if root.k == n:
        return True
    return find(root.left, n) or find(root.right, n)

main()
