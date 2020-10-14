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

    def remove_duplicates(self):
        if not (self.head and self.head.next):
            return

        prev = self.head
        curr = prev.next

        seen = set()
        seen.add(prev.k)

        while curr:
            if curr.k in seen:
                prev.next = curr.next
            else:
                seen.add(curr.k)
                prev = curr
            curr = curr.next


def main():
    L = LinkedList()

    L.insert_begin(5)
    L.insert_begin(5)
    for i in range(9, 0, -1):
        L.insert_begin(i)

    L.insert_begin(1)
    L.traverse()

    L.remove_duplicates()
    L.traverse()



if __name__ == '__main__':
    main()
