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

    def is_palindrome(self):
        if not (self.head and self.head.next):
            return True
        slow = self.head
        fast = self.head

        stack = []
        while fast and fast.next:
            stack.append(slow.k)
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
        while slow:
            x = stack.pop()
            if slow.k != x:
                return False
            slow = slow.next
        return True

def main():
    print('# Case')
    L = LinkedList()
    for i in "123243454":
        L.insert_end(i)
    L.traverse()
    assert L.is_palindrome() == False

    print('# Case')
    L = LinkedList()
    for i in "1331":
        L.insert_end(i)
    L.traverse()
    assert L.is_palindrome() == True

    print('# Case')
    L = LinkedList()
    for i in "1":
        L.insert_end(i)
    L.traverse()
    assert L.is_palindrome() == True

    print('# Case')
    L = LinkedList()
    for i in "12":
        L.insert_end(i)
    L.traverse()
    assert L.is_palindrome() == False

    print('# Case')
    L = LinkedList()
    for i in "12344321":
        L.insert_end(i)
    L.traverse()
    assert L.is_palindrome() == True

    print('# Case')
    L = LinkedList()
    for i in "101":
        L.insert_end(i)
    L.traverse()
    assert L.is_palindrome() == True

if __name__ == '__main__':
    main()

