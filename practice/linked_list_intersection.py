class Node:
    def __init__(self, k):
        self.k = k
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, k):
        n = Node(k)
        if self.head is None:
            self.head = n
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = n

    def traverse(self):
        if self.head is None:
            return
        p = self.head
        while p:
            print(p.k, end=' ')
            p = p.next
        print()

    def length(self):
        p = self.head
        length = 0
        while p:
            length += 1
            p = p.next
        return length

    def intersection(self, l1, l2):
        len_1 = l1.length()
        len_2 = l2.length()

        if len_1 > len_2:
            longer = l1
            shorter = l2
        else:
            longer = l2
            shorter = l1

        p = longer.head
        for _ in range(abs(len_1 - len_2)):
            p = p.next

        q = shorter.head
        while p and q:
            if p is q:
                return p
            p = p.next
            q = q.next
        return None

def main():
    l1 = LinkedList()
    for i in '1234':
        l1.insert_end(i)
    l1.traverse()

    l2 = LinkedList()
    for i in '1234':
        l2.insert_end(i)
    l2.head = l1.head
    l2.traverse()

    node = LinkedList().intersection(l1, l2)
    if node:
        print(node.k, node)


if __name__ == '__main__':
    main()

