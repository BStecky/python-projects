class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0 

    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
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
            self.head = new_node
            self.length += 1

    def print_list(self):
        if not self.head:
            print("Empty")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()
    
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
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
            print("inserting")

    def reverse(self):
        if not self.head.next:
            return
        first_node = self.head
        self.tail = self.head
        second_node = first_node.next
        while second_node:
            temp_node = second_node.next
            second_node.next = first_node
            first_node = second_node
            second_node = temp_node
        self.head.next = None
        self.head = first_node


linked = LinkedList()
linked.append(3)
linked.append(5)
linked.append(8)
linked.print_list()
linked.prepend(1)
linked.print_list()
print("l length: ", linked.length)
linked.insert(1, 2)
linked.print_list()
linked.reverse()
linked.print_list()