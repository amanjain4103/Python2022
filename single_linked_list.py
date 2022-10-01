# singly linked list

class Node:
    def __init__(self, data: int = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # at end
    def append(self, data: int):
        if self.head is None:
            self.head = Node(data)
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(data)

    def __str__(self):
        ele = self.head
        print_str = ''
        while ele is not None:
            print_str = print_str + str(ele.data) + '-->'
            ele = ele.next
        return print_str

    def insert(self, after_this_value: int, data: int):
        ele = self.head
        while ele is not None:
            if ele.data == after_this_value:
                new_node = Node(data)
                new_node.next = ele.next
                ele.next = new_node
                return
            ele = ele.next
        print('element not found, hence not inserted')

    def delete(self, value: int):
        iterr = self.head
        prev = self.head
        while iterr is not None:
            if iterr.data == value:
                if iterr.next is None and iterr.data == self.head.data:
                    self.head = None
                    return
                elif iterr.data == self.head.data:
                    self.head = iterr.next
                    return
                prev.next = iterr.next
                return
            prev = iterr
            iterr = iterr.next
        print('element not found')


ll = LinkedList()
ll.append(23)
ll.append(32)
ll.append(47)
ll.insert(32, 77)
print(ll)
ll.delete(47)
print(ll)
