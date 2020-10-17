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
        
    def insert_end(self, k):
        if self.head is None:
            self.head = Node(k)
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(k)  

    def add_nums(self, l1, l2):
        carry = 0
        while l1 or l2:
            s = carry
            if l1:
                s += l1.k
                l1 = l1.next
            if l2:
                s += l2.k
                l2 = l2.next
            d = s % 10
            carry = s // 10
            self.insert_end(d)

        if carry:
            self.insert_end(carry)

def main():
    # Case
    L = LinkedList()
    for i in [6, 1, 7]:
        L.insert_begin(i)
    L.traverse()

    R = LinkedList()
    for i in [2, 9, 5]:
        R.insert_begin(i)
    R.traverse()

    S = LinkedList()
    S.add_nums(L.head, R.head)
    S.traverse()

    # Case
    L = LinkedList()
    for i in [8, 9, 7]:
        L.insert_begin(i)
    L.traverse()

    R = LinkedList()
    for i in [5, 8, 6]:
        R.insert_begin(i)
    R.traverse()

    S = LinkedList()
    S.add_nums(L.head, R.head)
    S.traverse()

    # Case
    L = LinkedList()
    for i in [1, 2, 3]:
        L.insert_begin(i)
    L.traverse()

    R = LinkedList()
    for i in [4, 5, 6]:
        R.insert_begin(i)
    R.traverse()

    S = LinkedList()
    S.add_nums(L.head, R.head)
    S.traverse()

    # Case
    L = LinkedList()
    for i in [1, 2, 3]:
        L.insert_begin(i)
    L.traverse()

    R = LinkedList()
    for i in [4, 5]:
        R.insert_begin(i)
    R.traverse()

    S = LinkedList()
    S.add_nums(L.head, R.head)
    S.traverse()



if __name__ == '__main__':
    main()
