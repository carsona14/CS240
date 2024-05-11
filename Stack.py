class Stack:
    def __init__(self, max_size): # makes empty stack
        self.stack = []
        self.max_size = max_size

    def push(self, item): # adds element to stack
        if len(self.stack) < self.max_size:
            self.stack.append(item)
        else:
            print("Stack full")

    def pop(self): # removes element from stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack empty")
            return None

    def is_empty(self): # sees if stack is empty
        return len(self.stack) == 0

    def is_full(self): # sees if stack is full
        return len(self.stack) >= self.max_size

    def peek(self): # finds element at the top of the stack
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

# Example of full stack
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

# prints top of stack
print("Peek:", stack.peek())

# remove all elements from the stack
while not stack.is_empty():
    print("Pop:", stack.pop())

# prints true/false based on if full or empty
print("Is Full:", stack.is_full())
print("Is Empty:", stack.is_empty())

