# Carson Adams 
# 4/14/2024
# CS240
# Data Structures HW 1: Linked Lists
# This programs has single and double linked lists 

# Node class for both singly and doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # For double linked list

# Single Linked List implementation
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    # Insert value at beginning of list
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    # Insert value at end of list
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    # Checks position, inserts new nodes
    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.insert_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        prev = None
        while position > 0 and current:
            prev = current
            current = current.next
            position -= 1
        if not current:
            print("Invalid position")
            return
        new_node.next = current
        prev.next = new_node
    # Removes values at beginning
    def delete_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
    # Removes values at end
    def delete_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    # Checks position, removes new nodes
    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.delete_beginning()
            return
        current = self.head
        prev = None
        while position > 0 and current:
            prev = current
            current = current.next
            position -= 1
        if not current:
            print("Invalid position")
            return
        prev.next = current.next
    # Checks for values
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1
    # Goes through list and prints out data
    def read(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    # Sorts from biggest to smallest
    def insertion_sort(self):
        if not self.head:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head
    # Inserts sorted values into list
    def sorted_insert(self, sorted_head, new_node):
        if not sorted_head or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head

# Double linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.insert_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        prev = None
        while position > 0 and current:
            prev = current
            current = current.next
            position -= 1
        if not current:
            print("Invalid position")
            return
        new_node.next = current
        new_node.prev = prev
        prev.next = new_node
        if current:
            current.prev = new_node

    def delete_beginning(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None

    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.delete_beginning()
            return
        current = self.head
        prev = None
        while position > 0 and current:
            prev = current
            current = current.next
            position -= 1
        if not current:
            print("Invalid position")
            return
        prev.next = current.next
        if current.next:
            current.next.prev = prev

    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1

    def read(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def insertion_sort(self):
        if not self.head:
            return

        current = self.head.next

        while current:
            key = current.data
            prev_node = current.prev

            while prev_node and prev_node.data > key:
                prev_node.next.data = prev_node.data
                prev_node = prev_node.prev

            if prev_node is None:
                self.head.data = key
            else:
                prev_node.next.data = key

            current = current.next


with open("numbers-2.txt", "r") as file:
    data = file.readlines()

singly_linked_list = SinglyLinkedList()
doubly_linked_list = DoublyLinkedList()

for line in data:
    number = int(line.strip())  
    singly_linked_list.insert_end(number)
    doubly_linked_list.insert_end(number)

# Calling the sorting 
singly_linked_list.insertion_sort()
doubly_linked_list.insertion_sort()

print("Singly Linked List:")
singly_linked_list.read()

print("\nDoubly Linked List:")
doubly_linked_list.read()
