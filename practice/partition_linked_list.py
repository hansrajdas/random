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
    
    def partition(self, x):
        before = LinkedList()
        after = LinkedList()

        p = self.head
        while p:
            if p.k < x:
                before.insert_begin(p.k)
            else:
                after.insert_begin(p.k)
            p = p.next

        if before.head is None:
            return after
        elif after.head is None:
            return before
        p = before.head
        while p.next:
            p = p.next
        p.next = after.head
        return before

def main():
    L = LinkedList()
    for i in [3, 5, 8, 5, 10, 2, 1]:
        L.insert_begin(i)
    L.traverse()

    new = L.partition(5)
    new.traverse()

    new = L.partition(50)
    new.traverse()

    new = L.partition(-50)
    new.traverse()



if __name__ == '__main__':
    main()

