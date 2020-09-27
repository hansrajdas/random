class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class Solution:
    def kth_smallest(self, root, k):
        self.count = k
        def inorder(root):
            if root:
                n = inorder(root.left)
                if n is not None:
                    return n
                self.count -= 1
                if not self.count:
                    return root.key
                return inorder(root.right)
        return inorder(root)


def main():
  root = Node(10)
  root.left = Node(5)
  root.right = Node(20)

  root.left.left = Node(3)
  root.left.right = Node(7)

  for i in range(1, 10):
      a = Solution()
      print(a.kth_smallest(root, i))

main()
