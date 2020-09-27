def BTtoDLL(root, head):
    if root is None:
        return None
    BTtoDLL(root.right, head)
    root.right = head[0]
    if head[0]:
        head[0].left = root
    head[0] = root
    BTtoDLL(root.left, head)
