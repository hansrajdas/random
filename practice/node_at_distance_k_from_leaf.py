class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def k_distance_from_leaf_utils(root, k, path, visited, path_len):
    if root is None:
        return None
    path[path_len] = root.data
    path_len += 1
    
    if (root.left is None and root.right is None and path_len - k - 1 >= 0 and not visited[path_len - k - 1]):
        print(path[path_len - k - 1])
        visited[path_len - k - 1] = True
    k_distance_from_leaf_utils(root.left, k, path, visited, path_len)
    k_distance_from_leaf_utils(root.right, k, path, visited, path_len)


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def k_distance_from_leaf(root, k):
    h = height(root)
    path = {i: None for i in range(h)}
    visited = {i: False for i in range(h)}
    k_distance_from_leaf_utils(root, k, path, visited, 0)


def main():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)

  root.left.left = Node(4)
  root.left.right = Node(5)

  root.right.left = Node(6)
  root.right.right = Node(7)

  root.right.left.right = Node(8)

  k_distance_from_leaf(root, 2)  # 1 3


if __name__ == '__main__':
  main()
