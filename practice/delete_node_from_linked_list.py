class Node:
    def __init__(self, k):
        self.k = k
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, k):
        if self.head is None:
            self.head = Node(k)
            return
        n = Node(k)
        n.next = self.head
        self.head = n

    def traverse(self):
        if self.head is None:
            return
        p = self.head
        while p:
            print(p.k, end=' ')
            p = p.next
        print()

    def delete_node(self, node):
        if node is None:
            return
        node.k = node.next.k
        node.next = node.next.next

def main():
    L = LinkedList()
    for i in range(10, 0, -1):
        L.insert_begin(i)
    L.traverse()

    p = L.head
    while p.next:
        p = p.next
    print(p.k)
    L.delete_node(p)
    L.traverse()


if __name__ == '__main__':
    main()
