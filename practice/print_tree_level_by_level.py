import collections

class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

def insert(root, k):
    if not root:
        return Node(k)
    elif root.k > k:
        root.left = insert(root.left, k)
    elif root.k < k:
        root.right = insert(root.right, k)
    else:
        print('Duplicate node: %d' % k)
        return root
    return root

def print_tree_level_by_level(root):
    if root is None:
        return None
    Q = collections.deque([root])
    while Q:
        size = len(Q)
        while size:
            size -= 1
            node = Q.popleft()
            print(node.k, end=' ')
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        print()


def main():
  bst = BST()

  # Level 1
  bst.root = insert(bst.root, 5)

  # Level 2
  bst.root = insert(bst.root, 3)
  bst.root = insert(bst.root, 8)

  # Level 3
  bst.root = insert(bst.root, 4)
  bst.root = insert(bst.root, 6)
  bst.root = insert(bst.root, 10)
  bst.root = insert(bst.root, 1)

  print('\n\nNodes level by level: ')
  print_tree_level_by_level(bst.root)

if __name__ == '__main__':
  main()

# Output:
# ------------------------
# Inorder traversal:
# 1 3 4 5 6 8 10
#
# Nodes level by level:
# 5
# 3 8
# 1 4 6
