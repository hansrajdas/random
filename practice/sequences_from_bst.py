#!/usr/bin/python

# Date: 2020-10-24
#
# Description:
#
# Approach:
#
# Complexity:

class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def sequence_from_bst(root, seq):
    if root is None:
        return
    
    if len(seq) == 3:
        print(seq)
        seq = []

    seq.append(root.k)
    sequence_from_bst(root.left, seq)
    sequence_from_bst(root.right, seq)

    sequence_from_bst(root.right, seq)
    sequence_from_bst(root.left, seq)

def main():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)

    seq = []
    sequence_from_bst(root, seq)

main()
