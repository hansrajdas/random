#!/usr/bin/python

# Date: 2020-10-25
#
# Description:
#
# Approach:
#
# Complexity:

import random

class Node:
    def __init__(self, d):
        self.d = d
        self.left = None
        self.right = None
        self.size = 1

    def insert(self, d):
        if d <= self.d:
            if self.left is None:
                self.left = Node(d)
            else:
                self.left.insert(d)
        else:
            if self.right is None:
                self.right = Node(d)
            else:
                self.right.insert(d)
        self.size += 1

    def delete(self, d):
        pass  # need to decrement size also

    def get_random(self):
        left_size = 0 if not self.left else self.left.size
        index = random.randrange(self.size)
        if index < left_size:
            return self.left.get_random()
        elif index == left_size:
            return self
        else:
            return self.right.get_random()

root = Node(10)
root.left = Node(5)
root.right = Node(20)
print(root.get_random().d)
