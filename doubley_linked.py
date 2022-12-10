class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    def print_list(self):
        if not self.head:
            print("The list is empty.")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.length += 1
    
    def insert(self, index, data):
        if index >= self.length:
            if index > self.length:
               print("Unavailable position, inserting at the end of the list. ")
            new_node = Node(data)
            print("appending")
            self.append(new_node)
        elif index == 0:
            new_node = Node(data)
            self.prepend(new_node)
            print("prepending")
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            new_node.previous = current_node
            new_node.next = current_node.next
            current_node.next = new_node
            new_node.next.previous = new_node
            self.length += 1
            print("inserting")

linked = DoublyLinkedList()

linked.append(3)
linked.append(5)
linked.append(8)
linked.print_list()
linked.prepend(1)
linked.print_list()
print("ll length: ", linked.length)
linked.insert(1, 2)
linked.print_list()