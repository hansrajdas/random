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

    def reverse(self):
        if not self.head:
            return
        first = None
        second = self.head
        third = second.next

        while third:
            second.next = first
            first = second
            second = third
            third = third.next
        second.next = first
        self.head = second


def main():
    L = LinkedList()
    for i in range(9, 7, -1):
        L.insert_begin(i)
    L.traverse()


    L.reverse()
    L.traverse()

if __name__ == '__main__':
    main()

