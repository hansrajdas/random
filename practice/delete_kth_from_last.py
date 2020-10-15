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

    def delete_kth_from_last(self, k):
        if k < 1:
            raise ValueError(f'{k} too small')
        p = self.head
        count = 0
        while count < k:
            if p is None:
                raise ValueError(f'{k} larger than size of linked list')
            p = p.next
            count += 1

        p1 = self.head
        while p and p.next:
            p1 = p1.next
            p = p.next

        p1.next = p1.next.next

def main():
    L = LinkedList()
    for i in range(9, 0, -1):
        L.insert_begin(i)
    L.traverse()

    L.delete_kth_from_last(3)
    L.traverse()

    L.delete_kth_from_last(1)
    L.traverse()

    L.delete_kth_from_last(7)
    L.traverse()

if __name__ == '__main__':
    main()
