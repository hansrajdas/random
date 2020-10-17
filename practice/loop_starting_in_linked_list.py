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

    def find_loop_begining(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                print('Loop is detected')
                break
        if fast is None:
            return None

        slow = self.head
        while fast:
            if slow is fast:
                return slow
            slow = slow.next
            fast = fast.next

def main():
  linked_list = LinkedList()
  loop_start = Node(4)

  linked_list.head = Node(1)
  linked_list.head.next = Node(2)
  linked_list.head.next.next = Node(3)
  linked_list.head.next.next.next = loop_start
  linked_list.head.next.next.next.next = Node(5)
  linked_list.head.next.next.next.next.next = Node(6)
  linked_list.head.next.next.next.next.next.next = Node(7)
  linked_list.head.next.next.next.next.next.next.next = Node(8)
  linked_list.head.next.next.next.next.next.next.next.next = Node(9)
  linked_list.head.next.next.next.next.next.next.next.next.next = Node(10)
  linked_list.head.next.next.next.next.next.next.next.next.next.next = Node(11)
  linked_list.head.next.next.next.next.next.next.next.next.next.next.next = loop_start


  loop_start = linked_list.find_loop_begining()
  if loop_start:
    print('Loop starting node: data[%d], id[%d]' % (
      loop_start.k, id(loop_start)))
  else:
    print('Loop not found in linked list')

if __name__ == '__main__':
    main()

