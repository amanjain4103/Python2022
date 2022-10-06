# implement stack using singly linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, val):
        if self.head.data is None:
            self.head = Node(val)
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = Node(val)

    def remove_from_end(self):
        last_node = self.head
        while last_node.next is not None:
            prev = last_node
            last_node = last_node.next
        prev.next = None

    def last_element(self):
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        return last_node.data

    def __str__(self):
        current_node = self.head
        print_str = ''
        while current_node is not None:
            print_str = print_str + str(current_node.data) + '-->'
            current_node = current_node.next
        return print_str


class Stack:
    def __init__(self, max_len):
        self.top = -1
        self.max_len = max_len
        self.ll = LinkedList()

    def push(self, val):
        if self.top == self.max_len:
            print('Stack Overflow')
        else:
            self.ll.append(val)
            self.top = self.top + 1

    def pop(self):
        if self.top == -1:
            print('Stack Empty')
        else:
            self.ll.remove_from_end()
            self.top = self.top - 1

    def peek(self):
        print(self.ll.last_element())

    def __str__(self):
        return self.ll.__str__()


stk = Stack(10)
stk.push(10)
stk.push(20)
stk.push(30)
stk.peek()
print(stk)
stk.pop()
print(stk)
