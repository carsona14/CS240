# Carson Adams 
# 4/21/2024
# CS240
# Data Structures HW 2: Stacks and Queues
# This programs uses stacks and queues from the linked list in HW1

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

class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
        else:
            print("Stack Overflow")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack Underflow")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None
# Example
stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)

print("Peek:", stack.peek())
print("Pop:", stack.pop()) # comment out to test Is Full
print("Is Full:", stack.is_full())
print("Is Empty:", stack.is_empty()) # comment out pushes to test If Empty

class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, item):
        self.queue.insert_end(item)

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.head.data
            self.queue.delete_beginning()
            return item
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return self.queue.head is None

    def is_full(self):
        # Doubly linked lists do not have a maximum capacity
        return False

    def peek(self):
        if not self.is_empty():
            return self.queue.head.data
        else:
            print("Queue is empty")
            return None

# Example 
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Is Empty:", queue.is_empty())

