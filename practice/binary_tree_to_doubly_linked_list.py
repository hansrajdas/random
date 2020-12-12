def print_dll(head):
  print('\nDLL traversal, forward:', end=' ')
  p = head
  while p:
    print(p.data, end=' ')
    p = p.right

  print('\nDLL traversal, backward:', end=' ')
  # Move pointer to end
  p = head
  while p and p.right:
    p = p.right

  # Traverse from back
  while p:
    print(p.data, end=' ')
    p = p.left

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

class Wrapper:
    def BTtoDLL(self, root):
        self.head = None

        def _solve(root):
            if root is None:
                return None
            _solve(root.right)
            root.right = self.head
            if self.head:
                self.head.left = root
            self.head = root
            _solve(root.left)
        _solve(root)
        return self.head

## TC - 2
root = Node(1)

print('\n\nInorder traversal:', end=' ')
inorder(root)  # 1
head = Wrapper().BTtoDLL(root)
print_dll(head)  # forward: 1, backward: 1

## TC - 3
#   1
#  /
# 2
root = Node(1)
root.left = Node(2)

print('\n\nInorder traversal:', end=' ')
inorder(root)  # 2 1
head = Wrapper().BTtoDLL(root)
print_dll(head)  # forward: 2 1, backward: 1 2

## TC - 4
#   1
#  / \
# 2   3
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print('\n\nInorder traversal:', end=' ')
inorder(root)  # 2 1 3
head = Wrapper().BTtoDLL(root)
print_dll(head)  # forward: 2 1 3, backward: 3 1 2
