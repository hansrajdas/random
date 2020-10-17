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

    def add_nums_same_order(self, l1, l2):
        c1 = l1.length()
        c2 = l2.length()
        if c1 > c2:
            for _ in range(c1 - c2):
                l2.insert_begin(0)
        else:
            for _ in range(c2 - c1):
                l1.insert_begin(0)

        if self.add_nums_same_order_utils(l1.head, l2.head):
            self.insert_begin(1)

    def add_nums_same_order_utils(self, l1, l2):
        if not l1:
            return 0
        carry = self.add_nums_same_order_utils(l1.next, l2.next)
        s = carry + l1.k + l2.k
        self.insert_begin(s % 10)
        return s // 10
    
    def length(self):
        p = self.head
        c = 0
        while p:
            c += 1
            p = p.next
        return c

def main():
    print('# Case')
    L = LinkedList()
    for i in [6, 1, 7]:
        L.insert_end(i)
    L.traverse()

    R = LinkedList()
    for i in [2, 9, 5]:
        R.insert_end(i)
    R.traverse()

    S = LinkedList()
    S.add_nums_same_order(L, R)
    S.traverse()

    print('# Case')
    L = LinkedList()
    for i in [8, 9, 7]:
        L.insert_end(i)
    L.traverse()

    R = LinkedList()
    for i in [5, 8, 6]:
        R.insert_end(i)
    R.traverse()

    S = LinkedList()
    S.add_nums_same_order(L, R)
    S.traverse()

    print('# Case')
    L = LinkedList()
    for i in [1, 2, 3]:
        L.insert_end(i)
    L.traverse()

    R = LinkedList()
    for i in [4, 5, 6]:
        R.insert_end(i)
    R.traverse()

    S = LinkedList()
    S.add_nums_same_order(L, R)
    S.traverse()

    print('# Case')
    L = LinkedList()
    for i in [1, 2, 3]:
        L.insert_end(i)
    L.traverse()

    R = LinkedList()
    for i in [4, 5]:
        R.insert_end(i)
    R.traverse()

    S = LinkedList()
    S.add_nums_same_order(L, R)
    S.traverse()


if __name__ == '__main__':
    main()
