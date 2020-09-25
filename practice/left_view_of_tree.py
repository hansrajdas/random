class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def left_view(root, level, max_level):
    if root is None:
        return None
    if level == max_level[0]:
        max_level[0] += 1
        print(root.data, end=' ')
    left_view(root.left, level + 1, max_level)
    left_view(root.right, level + 1, max_level)

def print_left_view(root):
    max_level = [0]
    left_view(root, 0, max_level)
    print()

def right_view(root, level, max_level):
    if root is None:
        return None
    if level == max_level[0]:
        max_level[0] += 1
        print(root.data, end=' ')
    right_view(root.right, level + 1, max_level)
    right_view(root.left, level + 1, max_level)

def print_right_view(root):
    max_level = [0]
    right_view(root, 0, max_level)
    print()

def main():
  # TC - 1
  root = Node(12)
  root.left = Node(10)
  root.right = Node(20)
  root.right.left = Node(25)
  root.right.right = Node(40)

  print_left_view(root)  # 12 10 25
  print_right_view(root)  # 12 20 40

  # TC - 2
  root = Node(12)
  root.left = Node(10)
  root.right = Node(20)
  root.right.right = Node(30)
  root.right.right.right = Node(40)

  print_left_view(root)  # 12 10 30 40
  print_right_view(root)  # 12 20 30 40


if __name__ == '__main__':
  main()
